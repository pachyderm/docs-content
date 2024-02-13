---
# metadata # 
title:  Console Setup
description: Learn how to deploy the Console UI from the cloud (AWS, GCP, Azure).
date: 
# taxonomy #
tags: ["console", "cloud-deploy"]
series:
seriesPart:
weight: 4
--- 

<!-- Todo: evaluate if this doc is really needed still -->

## Before You Start 

You must have {{% productName %}} installed using one of the following guides:
  - [AWS](/{{%release%}}/set-up/cloud-deploy/aws/)
  - [GCP](/{{%release%}}/set-up/cloud-deploy/gcp/)
  - [Azure](/{{%release%}}/set-up/cloud-deploy/azure/)

## Deploy 

1. Set up your [Proxy](/{{%release%}}/manage/helm-values/proxy) and DNS and point your browser to:  
   - `http://<external-IP-address-or-domain-name>:80` or,
   - `https://<external-IP-address-or-domain-name>:443` if TLS is enabled
2. Set up your IDP during deployment.
   {{% notice note %}}
   You can use the mock user (username:`admin`, password: `password`) to login to Console when authentication is enabled but no Identity provider was wired (Enterprise).
   {{%/notice %}}
3. Configure your Identity Provider
    - **As Part of Helm**: To configure your Identity Provider as a part of `helm install`, see examples for the `oidc.upstreamIDPs` value in the [helm chart values specification](https://github.com/pachyderm/pachyderm/blob/42462ba37f23452a5ea764543221bf8946cebf4f/etc/helm/pachyderm/values.yaml#L461) and read [our IDP Configuration page](/{{%release%}}/set-up/connectors) for a better understanding of each field. 
    - **Manually via Values.yaml:** You can manually update your values.yaml with `oidc.mockIDP = false`.
4. Connect.

{{< stack type="wizard">}}

{{% wizardRow id="Method" %}}
{{% wizardButton option="HTTP" state="active" %}}
{{% wizardButton option="HTTPS (TLS)" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="method/http" %}}
```s
pachctl connect http://pachyderm.<your-proxy.host-value>
```
{{% /wizardResult %}}
{{% wizardResult val1="method/https-tls" %}}
```s
pachctl connect https://pachyderm.<your-proxy.host-value>
```
{{% /wizardResult %}}
{{% /wizardResults%}}

{{</stack>}}

You are all set! 
You should land on the Projects page of Console.


### Enterprise + Helm

When Enterprise is enabled through Helm, Auth is automatically activated. This means that you do not need to run `pachctl auth activate`; a `pachyderm-auth` Kubernetes secret is created which contains a [rootToken](/{{%release%}}/set-up/enterprise/activate-via-pachctl) key. Use `{{"kubectl get secret pachyderm-auth -o go-template='{{.data.rootToken | base64decode }}'"}}` to retrieve it and save it where you see fit.


## Considerations 

- If you run `pachctl auth activate`, the secret is not updated. Instead, the rootToken is printed in your STDOUT for you to save; the same behavior applies if you activate enterprise manually (`pachctl license activate`) and then activate authentication (`pachctl auth activate`).
- You can set the helm value `pachd.activateAuth` to false to prevent the automatic bootstrap of auth on the cluster.


