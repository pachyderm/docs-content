---
# metadata # 
title:  Deploy Target HCVs
description: Choose where you're deploying (Local, Cloud).
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
label: required
weight: 1
--- 

## About 

The Deploy Target section defines where you're deploying {{% productName %}}; this is typically located at the top of your values.yaml file.

## Values 

The following section contains a series of tabs for commonly used configurations for this section of your values.yml Helm chart. 

{{< stack type="wizard">}}

{{% wizardRow id="Options"%}}
{{% wizardButton option="Amazon" %}}
{{% wizardButton option="Custom" %}}
{{% wizardButton option="Google" %}}
{{% wizardButton option="Local" state="active" %}}
{{% wizardButton option="Microsoft" %}}
{{% wizardButton option="Minio" %}}

{{% /wizardRow %}}

{{% wizardResults  %}}
{{% wizardResult val1="options/amazon" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "AMAZON"
```
{{% /wizardResult %}}
{{% wizardResult val1="options/custom" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "CUSTOM"
```
{{% /wizardResult %}}
{{% wizardResult val1="options/google" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "GOOGLE"
```
{{% /wizardResult %}}
{{% wizardResult val1="options/local" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "LOCAL"
```
{{% /wizardResult %}}
{{% wizardResult val1="options/microsoft" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "MICROSOFT"
```
{{% /wizardResult %}}
{{% wizardResult val1="options/minio" %}}
```s
# Deploy Target configures the storage backend and cloud provider settings (storage classes, etc). 
# options:  GOOGLE, AMAZON, MINIO, MICROSOFT, CUSTOM or LOCAL.
deployTarget: "MINIO"
```
{{% /wizardResult %}}
{{% /wizardResults%}}


{{< /stack >}}

