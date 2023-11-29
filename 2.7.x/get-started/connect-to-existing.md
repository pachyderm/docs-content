---
# metadata # 
title:  Connect to Existing Instance
description: Learn how to connect to your organization's existing instance. 
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 3
directory: true
---

## Before You Start

- This guide assumes you have already [installed {{% productName %}}](/{{%release%}}/get-started/first-time-setup).
- You should know the URL of your organization's {{%productName%}} instance, located in your Helm Chart at [proxy.host](/{{%release%}}/manage/helm-values/proxy/#values).

## How to Log in to a Cluster via IdP

1. Open a terminal.
2. Connect to your organization's instance.
   {{< stack type="wizard">}}

   {{% wizardRow id="Method" %}}
   {{% wizardButton option="HTTP" %}}
   {{% wizardButton option="HTTPS (TLS)" state="active" %}}
   {{% /wizardRow %}}

   {{% wizardResults %}}
   {{% wizardResult val1="method/http" %}}
   ```s
   pachctl connect http://pachyderm.<your-proxy.host-value>
   ```
   {{% /wizardResult %}}
   {{% wizardResult val1="method/https-tls" %}}
   ```s
   pachctl connect https://<your-proxy.host-value>
   ```
   {{% /wizardResult %}}
   {{% /wizardResults%}}

   {{</stack>}}
3. Input the following command:
   ```s
   pachctl auth login
   ```
4. Select the connector you wish to use.
5. Provide your credentials.