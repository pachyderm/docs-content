---
# metadata # 
title: CloudSQL Auth Proxy HCVs
description: Deploy on GCP with CloudSQL.
date: 
# taxonomy #
tags: ["helm", "gcp" ]
series: ["helm"]
seriesPart: 
weight: 11
label: Required for GCP
--- 
## About

The CloudSQL Auth Proxy section configures the [CloudSQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/connect-auth-proxy) for deploying {{% productName %}} on GCP with CloudSQL.


## Values 

The following section contains a series of tabs for commonly used configurations for this section of your values.yml Helm chart. 

```yaml
cloudsqlAuthProxy:
  # connectionName may be found by running `gcloud sql instances describe INSTANCE_NAME --project PROJECT_ID`
  connectionName: ""
  serviceAccount: ""
  iamLogin: false
  port: 5432
  enabled: false
  image:
    # repository is the image repo to pull from; together with tag it
    # replicates the --dash-image & --registry arguments to pachctl
    # deploy.
    repository: "gcr.io/cloudsql-docker/gce-proxy"
    pullPolicy: "IfNotPresent"
    # tag is the image repo to pull from; together with repository it
    # replicates the --dash-image argument to pachctl deploy.
    tag: "1.23.0"
  priorityClassName: ""
  nodeSelector: {}
  tolerations: []
  # podLabels specifies labels to add to the dash pod.
  podLabels: {}
  # resources specifies the resource request and limits.
  resources: {}
  #  requests:
  #    # The proxy's memory use scales linearly with the number of active
  #    # connections. Fewer open connections will use less memory. Adjust
  #    # this value based on your application's requirements.
  #    memory: ""
  #    # The proxy's CPU use scales linearly with the amount of IO between
  #    # the database and the application. Adjust this value based on your
  #    # application's requirements.
  #    cpu: ""
  service:
    # labels specifies labels to add to the cloudsql auth proxy service.
    labels: {}
    # type specifies the Kubernetes type of the cloudsql auth proxy service.
    type: ClusterIP
```