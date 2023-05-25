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

- Check the [release notes](https://github.com/pachyderm/pachyderm/blob/master/CHANGELOG.md) before upgrading
- [Back up your cluster](/{{%release%}}/manage/backup-restore/) 
- Update your Helm chart values if applicable

## How to Upgrade {{% productName %}} 

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