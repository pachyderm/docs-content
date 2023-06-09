---
# metadata # 
title: Activate Enterprise via Helm
description: Learn how to deploy the Enterprise edition using Helm.
date: 
# taxonomy #
tags: ["enterprise"]
series:
seriesPart:
directory: true 
---

## Before You Start 

- You must have a {{%productName%}} [Enterprise License Key](https://www.pachyderm.com/trial/).
- You must have pachctl and {{%productName%}} installed. 
- You must have the {{%productName%}} Helm repo downloaded.

## How to Activate Enterprise {{%productName%}} via Helm

{{<stack type="wizard">}}
{{% wizardRow id="Activation Method" %}}
{{% wizardButton  option="License" state="active" %}}
{{% wizardButton  option="License Secret" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="activation-method/license" %}}
1. Open your Helm `values.yml` file. 
2. Find the the `pachd.enterpriseLicenseKey` attribute.
3. Input your enterprise key.
4. Upgrade your cluster by running the following command:
```s
helm upgrade {{% productName %}}pachyderm/pachyderm -f values.yml
```
Once deployed, {{%productName%}} stores your provided Enterprise license as the platform secret `pachyderm-license` in the key `enterprise-license-key`.

{{% /wizardResult%}}
{{% wizardResult val1="activation-method/license-secret" %}}
1. [Create a secret](../../how-tos/advanced-data-operations/secrets/#create-and-manage-secrets-in-pachyderm) for your Enterprise license.
2. Open your Helm values.yml file. 
3. Find the the `pachd.enterpriseLicenseKeySecretName` attribute.
4. Input your license's secret name.
5. Upgrade your cluster by running the following command:
```s
helm upgrade {{% productName %}}pachyderm/pachyderm -f values.yml
```
{{% /wizardResult%}}
{{% /wizardResults %}}
{{</stack>}}