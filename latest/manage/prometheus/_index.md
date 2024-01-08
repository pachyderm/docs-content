---
# metadata #
title: Monitor with Prometheus
description: Learn how to monitor a cluster using Prometheus.
date:
# taxonomy #
tags:
series:
seriesPart:
weight: 21
---

{{% notice note %}}
To monitor a {{%productName%}} cluster
with Prometheus, a ***Enterprise License*** is required.
{{% /notice %}}


{{%productName%}}'s deployment manifest exposes Prometheus metrics,
allowing an easy set up of the monitoring of your cluster.
Only available for self-managed deployments today.


{{% notice warning %}}
These installation steps are for **Informational Purposes** ONLY.
Please refer to your full Prometheus documentation for further installation details and any troubleshooting advice.
{{% /notice %}}

## Prometheus installation and Service Monitor creation
1. Helm install [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack#kube-prometheus-stack),
Prometheus' **Kubernetes cluster monitoring** using the Prometheus Operator:

    - Get Repo Info
    ```s
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    ```

    - Install the Prometheus-operator helm chart
    ```s
    helm install <a-release-name> prometheus-community/kube-prometheus-stack
    ```

1. Create a ServiceMonitor for {{%productName%}} in Kubernetes:
    - Create a myprometheusservice.yaml
        ```s
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          name: pachyderm-scraper
          labels:
            release: <a-release-name>
        spec:
            selector:
                matchLabels:
                  suite: pachyderm
            namespaceSelector:
                matchNames:
                - default
            endpoints:
            - port: prom-metrics
              interval: 30s
        ```
    - Create a ServiceMonitor looking to scrape metrics from `suite: pachyderm`:
        ```s
        kubectl create -f myprometheusservice.yaml
        ```
        The prometheus-operator will search for the pods based on the label selector `<a-release-name>`
        and creates a prometheus target so prometheus will scrape the metrics endpoint `prom-metrics`.

        In this case, it looks for anything with the label `suite: pachyderm` -
        which is by default associated with all {{%productName%}} resources.

{{% notice note %}}
   Our Service Monitor `pachyderm-scraper` above maps the endpoint port `prom-metrics`
       to a corresponding `prom-metrics` port described in {{%productName%}}'s deployment manifest.
       Let's take a quick look at this file:

   ```s
   kubectl -o json get service/pachd
   ```
   In the json file, find:

   ```json
      {
      "name": "prom-metrics",
      "port": 1656,
      "protocol": "TCP",
      "targetPort": "prom-metrics"
      }
   ```
   {{% /notice %}}

1.  Create a PodMonitor for {{%productName%}} in Kubernetes:
	- Create a mypodmonitor.yaml
		```s
		apiVersion: monitoring.coreos.com/v1
		kind: PodMonitor
		metadata:
		  name: worker-scraper
		  labels:
		    release: pach-prom
		spec:
		  selector:
		    matchLabels:
		      app: pipeline
		      component: worker
		  podMetricsEndpoints:
		  - port: metrics-storage
		```
		The prometheus-operator will search for worker pods and create
		a prometheus target so that prometheus will scrape the storage
		sidecar metrics endpoint `metrics-storage`.
## Port-Forward

Connect to Prometheus using the following command:

```s
  kubectl port-forward service/<release-name>-kube-prometheus-prometheus 9090
```
If you have an existing Prometheus deployment, please navigate to your Prometheus GUI.

## Browse
You can now browse your targets (http://localhost:9090/targets).
Run a pipeline of your choice. The `pachyderm-scraper` should be visible:

![pachyderm scraper target](/images/prometheus_target_pachyderm_scaper.png)

In the ClassicUI tab, you should be able to see the new {{% productName %}}metrics.
