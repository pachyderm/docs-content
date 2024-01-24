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

{{% notice warning %}}

**We do not currently recommend upgrading to 2.6.x at this time.**  If you have questions, please reach out to us on Slack.

Upgrading to 2.6.5 from older versions involves a data migration. This migration can take a long time depending on the size of your cluster. If you are looking to upgrade a long-lived cluster, we recommend waiting for 2.7.0.  For a newer cluster, if you still wish to upgrade, we recommend that you:

- Backup your cluster before upgrading
- Upgrade to 2.6.5 during a time when your cluster is not in use
- Run the following check before upgrading: 
  
  ```s
  pachctl misc test-migrations postgres://USERNAME:PASSWORD@HOST:PORT/pachyderm
  ```
{{% /notice %}}

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