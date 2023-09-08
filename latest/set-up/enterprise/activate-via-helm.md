---
# metadata # 
title: Activate Enterprise via Helm
description: Learn how to deploy the Enterprise edition using Helm.
date: 
# taxonomy #
tags: ["enterprise", "setup", "activate", "enterprise key", "license"]
series:
seriesPart:
---

## Before You Start 

- You must have a {{% productName %}} [Enterprise License Key](https://www.pachyderm.com/trial/).
- You must have pachctl and {{% productName %}} installed. 
- You must have the {{% productName %}} Helm repo downloaded.

## How to Activate Enterprise {{% productName %}} via Helm

{{<stack type="wizard">}}
{{% wizardRow id="Activation Method" %}}
{{% wizardButton  option="License" %}}
{{% wizardButton  option="License Secret" state="active" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="activation-method/license" %}}
1. Open your Helm `values.yml` file. 
2. Find the the `pachd.enterpriseLicenseKey` attribute.
3. Input your enterprise key.
4. Upgrade your cluster by running the following command:
```s
helm upgrade pachyderm pachyderm/pachyderm -f values.yml
```
Once deployed, {{% productName %}} stores your provided Enterprise license as the platform secret `pachyderm-license` in the key `enterprise-license-key`.

{{% /wizardResult%}}
{{% wizardResult val1="activation-method/license-secret" %}}
1. [Create a secret](/{{%release%}}/manage/secrets) for your Enterprise license.
   ```s
   kubectl create secret generic pachyderm-enterprise-key \
   --from-literal=enterprise-license-key='<replace-with-key>'\
   --output=json > pachyderm-enterprise-key.json
   ```
2. Upload the secret to your cluster.
   ```s
   pachctl create secret -f pachyderm-enterprise-key.json
   ```
   {{%notice note %}}
   You may have to rename the `metadata.name` in `pachyderm-enterprise-key.json` if pachctl says the secret already exists.
   {{%/notice%}}
3. Obtain your current user-input helm values:
    ```s
    helm get values pachyderm > values.yaml
    ```
4. Find the the `pachd.enterpriseLicenseKeySecretName` attribute.
5. Input your license's secret name found in `meta.name` of `pachyderm-enterprise-key.json` (e.g., `pachyderm-enterprise-key-secret`).
6. Upgrade your cluster by running the following command:
```s
helm upgrade pachyderm pachyderm/pachyderm -f values.yml
```
{{% /wizardResult%}}
{{% /wizardResults %}}
{{</stack>}}