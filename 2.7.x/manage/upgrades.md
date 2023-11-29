---
# metadata # 
title: Upgrade
description: Learn how to upgrade PachCTLand & PachD. 
date: 
# taxonomy #
tags: ["management", "upgrades", "pachctl","pachd"]
series:
seriesPart:
directory: true
weight: 3
---

Learn how to upgrade {{% productName %}} to access new features and performance enhancements.

## Before You Start 

- Check the [release notes](/changelog) before upgrading
- [Back up your cluster](/{{%release%}}/manage/backup-restore/) 
- Update your Helm chart values if applicable

## How to Upgrade {{% productName %}} 

### 1. Run a Preflight Check

PachD has a preflight check mode that you can enable in your Helm chart by setting `pachd.preflightchecks.enabled` to `true`. Preflight checks run as a Kubernetes job, and can use a different version of {{%productName%}} than the rest of the chart. In this case, you will set it to the version you are upgrading to (for example, the latest version is **{{%latestPatchNumber%}}**).

Example configuration:

```yaml
preflightCheckJob:
    enabled: true
    image:
        tag: "{{%latestPatchNumber%}}"
```

You'll see a pod named `pachyderm-preflight-check` was created to perform the preflight checks. 

- If its status says `completed`, you are ready to continue with the upgrade.
- If its status does not say `completed`, reach out to the {{%productName%}} team for assistance with your upgrade.

```s
kubectl get pods
NAME                                         READY   STATUS      RESTARTS   AGE
console-76f5fd8c58-zwvj5                     1/1     Running     0          13m
default-edges-v1-bl6cf                       2/2     Running     0          12m
default-montage-v1-tbj6p                     2/2     Running     0          12m
etcd-0                                       1/1     Running     0          13m
minio-0                                      1/1     Running     0          14m
pachd-6c99fc7448-vsjbn                       1/1     Running     0          13m
pachyderm-kube-event-tail-5957785f5d-4557j   1/1     Running     0          13m
pachyderm-loki-0                             1/1     Running     0          13m
pachyderm-preflight-check-rh9rp              0/1     Completed   0          13m
pachyderm-promtail-h29zv                     1/1     Running     0          13m
pachyderm-proxy-7956c766bd-drndd             1/1     Running     0          13m
pg-bouncer-686db6477c-rjwgl                  1/1     Running     0          13m
postgres-0                                   1/1     Running     0          13m
```

### 2. Upgrade

1. Run the following brew command or [download & install the latest release assets](https://github.com/pachyderm/pachyderm/releases/latest):
```s  
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@{{% majorMinorNumber %}}  
```  
2. Upgrade Helm.

{{< stack type="wizard" >}}
{{% wizardRow id="Deploy Method"%}}
{{% wizardButton option="Production" state="active" %}}
{{% wizardButton option="Local (Personal Machine)" %}} 
{{% /wizardRow %}}

{{% wizardResults %}} 
{{% wizardResult val1="deploy-method/production"%}}
Note that the repo name input (`pachd`) must match the name you provided upon first install.
You can also pass in a specific version (e.g., `--version x.x.0-rc.1`) if you are testing a pre-released version of {{%productName%}}.

```s
helm repo update
helm upgrade pachyderm pachyderm/pachyderm -f my_pachyderm_values.yaml  --set proxy.enabled=true --set proxy.service.type=LoadBalancer 
```
{{% /wizardResult %}}

{{% wizardResult val1="deploy-method/local-personal-machine"%}}
Note that the repo name input (`pachd`) must match the name you provided upon first install. You can also pass in a specific version (e.g., `--version x.x.0-rc.1`) if you are testing a pre-released version of {{%productName%}}.

```s
helm repo update
helm upgrade pachyderm pachyderm/pachyderm --set deployTarget=LOCAL --set proxy.enabled=true --set proxy.service.type=LoadBalancer 
```
{{% /wizardResult %}} 
{{% /wizardResults %}} 
{{< /stack >}}

1. Verify that the installation was successful by running `pachctl version`:  
  
```s  
pachctl version 

# COMPONENT           VERSION  
# pachctl             {{% latestPatchNumber %}} 
# pachd               {{% latestPatchNumber %}} 
```  