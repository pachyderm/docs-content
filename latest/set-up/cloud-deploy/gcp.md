---
# metadata # 
title:  GCP Deployment
description: Learn how to deploy to the cloud with GCP.
date: 
# taxonomy #
tags: ["gcp", "cloud-deploy"]
series:
seriesPart:
weight: 3
---
## Before You Start 

This guide assumes that:
-  You have already tried [{{% productName %}} locally](/{{%release%}}/set-up/local-deploy/) and have some familiarity with [Kubectl](https://kubernetes.io/docs/tasks/tools/), [Helm](https://helm.sh/docs/intro/install/), [Google Cloud SDK](https://cloud.google.com/sdk/) and [jq](https://stedolan.github.io/jq/download/).
- You have access to a Google Cloud account linked to an active billing account.
---

## 1. Create a New Project 

1. Log in to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (e.g.,`pachyderm-quickstart-project`).
3. Enable the Compute Engine API.

You are now ready to create a GKE Cluster.

## 2. Run Setup Script

You can run [this setup script](https://github.com/pachyderm/pachyderm/blob/master/etc/deploy/gcp/gcp-doco-script.sh) either through the **Cloud Shell** or in a local terminal via the `gcloud` cli. Running this script creates all of the following:

- One GKE cluster
- Workload identity service accounts
- Permissions
- A static IP address 
- The cloud SQL instance and databases
- One cloud storage bucket
- One file called `${NAME}.values.yaml` in the current directory

It also installs {{% productName %}} into the cluster.

## 3. Connect to Cluster

You'll need your organization's cluster URL ([proxy.host](/{{%release%}}/manage/helm-values/proxy)) value to connect. 

1. Run the following command to get your cluster URL:
```s
kubectl get services | grep pachyderm-proxy | awk '{print $4}'
```
2. Connect to your cluster:
   
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

{{% notice tip %}}

You can also connect to Console via Google's Cloud Shell: 

![console-in-browser](/images/gcp/console-in-browser.gif)

{{% /notice %}}