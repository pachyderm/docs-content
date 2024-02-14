---
# metadata # 
title:  On-Prem Deploy 
description: Learn how to install on your premises. 
date: 
# taxonomy #
tags:  ["deployment"]
series:
seriesPart: 
weight: 1
---
## Before you start 

Before you can deploy {{% productName %}}, you will need to perform the following actions:

1. [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
2. [Install Helm](https://helm.sh/docs/intro/install/)
3. [Deploy Kubernetes on-premises](https://kubernetes.io/docs/setup/).
4. [Deploy two Kubernetes persistent volumes for {{% productName %}} metadata storage](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1). 
5. Deploy an on-premises object store using a storage provider like [MinIO](https://min.io), [EMC's ECS](https://www.delltechnologies.com/en-us/storage/ecs/index.htm), or [SwiftStack](https://www.swiftstack.com/) to provide S3-compatible access to your data storage.
6. Install [PachCTL](/{{%release%}}/get-started/first-time-setup) and [PachCTL Auto-completion](/{{%release%}}/set-up/pachctl-autocomplete).

   
## How to Deploy {{% productName %}} On-Premises

### 1. Install {{% productName %}} via Helm

```s
helm repo add pachyderm https://helm.pachyderm.com
helm repo update
```

### 2. Configure Helm Values

View and copy a full helm chart from [GitHub](https://github.com/pachyderm/pachyderm/blob/{{%majorMinorVersion%}}/etc/helm/pachyderm/values.yaml) or [ArtifactHub](https://artifacthub.io/packages/helm/pachyderm/pachyderm) for reference when configuring your Helm values file. You can quickly explore the options for different sections of the Helm chart from our [Helm series](/series/helm) documentation.

#### Add Storage classes to Helm Values

Update your Helm values file to include the storage classes you are going to use:

```yaml
etcd:
  storageClass: MyStorageClass
  size: 10Gi

postgresql:
  persistence:
    storageClass: MyStorageClass
    size: 10Gi
```

#### Size & Configure Object Store

1. Determine the endpoint of your object store, for example `minio-server:9000`.
2. Choose a unique name for the bucket you will dedicate to {{% productName %}}.
3. Create a new access key ID and secret key for {{% productName %}} to use when accessing the object store.
4. Update the {{% productName %}} Helm values file with the endpoint, bucket name, access key ID, and secret key.

```s
pachd:
  storage:
    backend: minio
    minio:
      endpoint: minio-server:9000
      bucket: pachyderm-bucket
      id: pachyderm-access-key
      secret: pachyderm-secret-key
      secure: false

```

#### Configure Authentication & Authorization

To set up [Authentication](/{{%release%}}/set-up/connectors/), you must use the Enterprise version of {{%productName%}} and provide a valid license key. 

We recommend that you [create a secret](/{{%release%}}/manage/secrets/#secrets-create-a-secret) and provide it on the Helm chart as the value to the attribute `pachd.enterpriseLicenseKeySecretName`. Once deployed, Pachyderm stores your provided Enterprise license as the platform secret `pachyderm-license` in the key `enterprise-license-key`.


{{%notice note%}}
After deploying {{%productName%}}, you can [log in as the root user](/{{%release%}}/set-up/authorization/#authorization-activate-user-access-management) and begin to add users to certain resource types such as Projects and Repos. 

```s
pachctl auth set project <project-name> <role-name> user:<username@email.com>
```

For more information on user permissions, see the [Authorization](/{{%release%}}/set-up/authorization/) section. 
{{%/notice%}}
### 3. Deploy 

```s
helm install pachyderm -f values.yaml pachyderm/pachyderm --version <your_chart_version>
```

{{% notice tip %}}
You can update your Helm values file using the following command:

```s
helm upgrade pachyderm pachyderm/pachyderm -f values.yml
```
{{% /notice %}}

