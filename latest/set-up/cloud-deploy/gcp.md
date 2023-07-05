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
-  You have already tried [{{%productName%}} locally](/{{%release%}}/set-up/local-deploy/) and have some familiarity with [Kubectl](https://kubernetes.io/docs/tasks/tools/), [Helm](https://helm.sh/docs/intro/install/), [Google Cloud SDK](https://cloud.google.com/sdk/) and [jq](https://stedolan.github.io/jq/download/).
- You have access to a Google Cloud account linked to an active billing account.
---

## 1. Create a New Project 

1. Create a new project (e.g.,`pachyderm-quickstart-project`).
   ```s
   gcloud projects create PROJECT_ID --name="Your Project Name" --set-as-default
   gcloud alpha billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
   ```
2. Enable the following APIs:

   ```s
   gcloud services enable container.googleapis.com
   gcloud services enable sqladmin.googleapis.com
   ```

## 2. Create a Static IP Address

```s
gcloud compute addresses create STATIC_IP_NAME --region=GCP_REGION

STATIC_IP_ADDR=$(gcloud compute addresses describe STATIC_IP_NAME --region=GCP_REGION --format="json" --flatten="address" | jq .[])
```
## 3. Create a GKE Cluster 

Make sure to replace the values in the following commands to suit your needs.

1. Create a GKE cluster with the following command:

   ```s
   gcloud container clusters create CLUSTER_NAME \
     --machine-type=CLUSTER_MACHINE_TYPE \ # e.g., n1-standard-4 or n2-standard-2
     --workload-pool=PROJECT_ID.svc.id.goog \
     --enable-ip-alias \
     --create-subnetwork="" \
     --enable-dataplane-v2 \
     --enable-shielded-nodes \
     --release-channel="regular" \
     --workload-metadata="GKE_METADATA" \
     --enable-autorepair \
     --enable-autoupgrade \
     --disk-type="pd-ssd" \
     --image-type="COS_CONTAINERD"
   ```
2. Connect to the cluster:

   ```s
   gcloud container clusters get-credentials CLUSTER_NAME
   ```

## 4. Create Storage Buckets

```s
gsutil mb -l GCP_REGION gs://BUCKET_NAME
gsutil mb -l GCP_REGION gs://LOKI_BUCKET_NAME
```

## 5. Create a Cloud SQL Instance

Make sure to replace the values in the following commands to suit your needs.


1. Create a Cloud SQL instance with the following command:

```s
gcloud sql instances create CLOUDSQL_INSTANCE_NAME \
  --database-version=POSTGRES_13 \
  --cpu=SQL_CPU \
  --memory=SQL_MEM \
  --zone=GCP_ZONE \
  --availability-type=ZONAL \
  --storage-size=50GB \
  --storage-type=SSD \
  --storage-auto-increase \
  --root-password=SQL_ADMIN_PASSWORD
```
2. Create a databases for {{%productName%}} and Dex:
```s
gcloud sql databases create pachyderm -i CLOUDSQL_INSTANCE_NAME
gcloud sql databases create dex -i CLOUDSQL_INSTANCE_NAME
```
3. Get the Cloud SQL connection name:
```s
CLOUDSQL_CONNECTION_NAME=$(gcloud sql instances describe CLOUDSQL_INSTANCE_NAME --format="json" | jq .connectionName)
```

## 6. Create a Service Accounts 

Create a service account for {{%productName%}} and Loki. 

```s
gcloud iam service-accounts create GSA_NAME
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_ACCOUNT" \
  --role="roles/cloudsql.client"
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_ACCOUNT" \
  --role="roles/storage.admin"
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/pachyderm"
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/pachyderm-worker]"
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/k8s-cloudsql-auth-proxy]"

gcloud iam service-accounts create LOKI_GSA_NAME
gcloud iam service-accounts keys create "LOKI_GSA_NAME-key.json" --iam-account="LOKI_SERVICE_ACCOUNT"
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:LOKI_SERVICE_ACCOUNT" \
  --role="roles/storage.admin"
```

## 7. Create Loki a Secret

```s
kubectl create secret generic loki-service-account --from-file="LOKI_GSA_NAME-key.json"
```

## 8. Build a Helm Values File

1. Create file.
```s
cat <<EOF > NAME.values.yaml
deployTarget: "GOOGLE"

pachd:
  enabled: true
  externalService:
    enabled: true
    aPIGrpcport: 31400
    loadBalancerIP: STATIC_IP_ADDR
  image:
    tag: "2.6.5"
  lokiDeploy: true
  lokiLogging: true
  storage:
    google:
      bucket: "BUCKET_NAME"
  serviceAccount:
    create: true
    name: "pachyderm"
  worker:
    serviceAccount:
      create: true
      name: "pachyderm-worker"

cloudsqlAuthProxy:
  enabled: true
  connectionName: CLOUDSQL_CONNECTION_NAME
  resources:
    requests:
      memory: "500Mi"
      cpu: "250m"

postgresql:
  enabled: false

global:
  postgresql:
    postgresqlHost: "cloudsql-auth-proxy.default.svc.cluster.local."
    postgresqlPort: "5432"
    postgresqlSSL: "disable"
    postgresqlUsername: "postgres"
    postgresqlPassword: "SQL_ADMIN_PASSWORD"

loki-stack:
  loki:
    env:
      - name: GOOGLE_APPLICATION_CREDENTIALS
        value: /etc/secrets/loki-service-account
    extraVolumes:
      - name: loki-service-account
        secret:
          secretName: loki-service-account
    extraVolumeMounts:
      - name: loki-service-account
        mountPath: /etc/secrets
    config:
      schema_config:
        configs:
          - from: 1989-11-09
            object_store: gcs
            store: boltdb
            schema: v11
            index:
              prefix: loki_index_
            chunks:
              prefix: loki_chunks_
      storage_config:
        gcs:
          bucket_name: "LOKI_BUCKET_NAME"
  grafana:
    enabled: false
EOF
```
2. Install using the following command:
```s
helm repo add pachyderm https://helm.pachyderm.com
helm repo update
helm install pachyderm -f ./NAME.values.yaml pachyderm/pachyderm

```

## 9. Connect to Cluster

You'll need your organization's cluster URL ([proxy.host](/{{%release%}}/manage/helm-values/proxy)) value to connect. 

1. Run the following command to get your cluster URL:
```s
kubectl get services | grep pachd-lb | awk '{print $4}'
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

