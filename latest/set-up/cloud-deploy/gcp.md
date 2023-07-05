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
- You have access to a Google Cloud account linked to an active billing account `gcloud alpha billing accounts list`

### Configure Variables

Configure these variables and set in a `.env` file and source them with `source .env` before starting the installation guide.

```s
PROJECT_ID="pachyderm-001"
PROJECT_NAME="pachyderm-gcp-example"
NAME="fuzzy-alpaca"
SQL_ADMIN_PASSWORD="batteryhorsestaple"
BILLING_ACCOUNT_ID="000000-000000-000000"

# This group of variables can be changed, but are sane defaults
GCP_REGION="us-central1"
GCP_ZONE="us-central1-a"
K8S_NAMESPACE="default"
CLUSTER_MACHINE_TYPE="n2-standard-2"
SQL_CPU="2"
SQL_MEM="7680MB"

# The following variables probably shouldn't be changed
CLUSTER_NAME="${NAME}-gke"
BUCKET_NAME="${NAME}-gcs"
LOKI_BUCKET_NAME="${NAME}-logs-gcs"
CLOUDSQL_INSTANCE_NAME="${NAME}-sql"
GSA_NAME="${NAME}-gsa"
LOKI_GSA_NAME="${NAME}-loki-gsa"
STATIC_IP_NAME="${NAME}-ip"

ROLE1="roles/cloudsql.client"
ROLE2="roles/storage.admin"

SERVICE_ACCOUNT="${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
LOKI_SERVICE_ACCOUNT="${LOKI_GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
PACH_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/pachyderm]"
SIDECAR_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/pachyderm-worker]"
CLOUDSQLAUTHPROXY_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/k8s-cloudsql-auth-proxy]"
```

---

## 1. Create a New Project 

1. Create a new project (e.g.,`pachyderm-quickstart-project`). You can pre-define the project id using a between 6-30 characters, starting with a lowercase letter. This ID will be used to set up the cluster and will be referenced throughout this guide.
   
   ```s
   gcloud projects create ${PROJECT_ID} --name=${PROJECT_NAME} --set-as-default
   gcloud alpha billing projects link ${PROJECT_ID} --billing-account=${BILLING_ACCOUNT_ID}
   ```
2. Enable the following APIs:

   ```s
   gcloud services enable container.googleapis.com
   gcloud services enable sqladmin.googleapis.com
   ```


## 2. Create a Static IP Address

1. Create the static IP Address:

```s
gcloud compute addresses create ${STATIC_IP_NAME} --region=${GCP_REGION} 
```
2. Get the static IP address:

```s
STATIC_IP_ADDR=$(gcloud compute addresses describe ${STATIC_IP_NAME} --region=${GCP_REGION}--flatten=address)
```

## 3. Create a GKE Cluster 

Make sure to replace the values in the following commands to suit your needs.

1. Create a GKE cluster with the following command:

   ```s
   gcloud container clusters create ${CLUSTER_NAME} \
     --region=${GCP_REGION} \
     --machine-type=${CLUSTER_MACHINE_TYPE} \
     --workload-pool=${PROJECT_ID}.svc.id.goog \
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
   gcloud container clusters get-credentials ${CLUSTER_NAME}
   ```

## 4. Create Storage Buckets

```s
gsutil mb -l ${GCP_REGION} gs://${BUCKET_NAME}
gsutil mb -l ${GCP_REGION} gs://${LOKI_BUCKET_NAME}
```

## 5. Create a Cloud SQL Instance

Make sure to replace the values in the following commands to suit your needs.


1. Create a Cloud SQL instance with the following command:

```s
gcloud sql instances create ${CLOUDSQL_INSTANCE_NAME} \
  --database-version=POSTGRES_13 \
  --cpu=${SQL_CPU} \
  --memory=${SQL_MEM} \
  --zone=${GCP_ZONE} \
  --availability-type=ZONAL \
  --storage-size=50GB \
  --storage-type=SSD \
  --storage-auto-increase \
  --root-password=${SQL_ADMIN_PASSWORD}
```
2. Create a databases for {{%productName%}} and Dex:
```s
gcloud sql databases create pachyderm -i ${CLOUDSQL_INSTANCE_NAME}
gcloud sql databases create dex -i ${CLOUDSQL_INSTANCE_NAME}
```
3. Get the Cloud SQL connection name:
```s
CLOUDSQL_CONNECTION_NAME=$(gcloud sql instances describe ${CLOUDSQL_INSTANCE_NAME} --flatten="connectionName")
```

## 6. Create a Service Accounts 

Create a service account for {{%productName%}} and Loki. 

```s
gcloud iam service-accounts create ${GSA_NAME}

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="${ROLE1}"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="${ROLE2}"

gcloud iam service-accounts add-iam-policy-binding ${SERVICE_ACCOUNT} \
    --role roles/iam.workloadIdentityUser \
    --member "${PACH_WI}"

gcloud iam service-accounts add-iam-policy-binding ${SERVICE_ACCOUNT} \
    --role roles/iam.workloadIdentityUser \
    --member "${SIDECAR_WI}"

gcloud iam service-accounts add-iam-policy-binding ${SERVICE_ACCOUNT} \
    --role roles/iam.workloadIdentityUser \
    --member "${CLOUDSQLAUTHPROXY_WI}"

gcloud iam service-accounts create ${LOKI_GSA_NAME}

gcloud iam service-accounts keys create "${LOKI_GSA_NAME}-key.json" --iam-account="${LOKI_SERVICE_ACCOUNT}"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${LOKI_SERVICE_ACCOUNT}" \
    --role="${ROLE2}"
```

## 7. Create Loki a Secret

```s
kubectl create secret generic loki-service-account --from-file="${LOKI_GSA_NAME}-key.json"
```

## 8. Build a Helm Values File

1. Create file.
```s
cat <<EOF > ${NAME}.values.yaml
deployTarget: "GOOGLE"

pachd:
  enabled: true
  externalService:
    enabled: true
    aPIGrpcport: 31400
    loadBalancerIP: ${STATIC_IP_ADDR}
  image:
    tag: "2.6.5"
  lokiDeploy: true
  lokiLogging: true
  storage:
    google:
      bucket: "${BUCKET_NAME}"
  serviceAccount:
    additionalAnnotations:
      iam.gke.io/gcp-service-account: "${SERVICE_ACCOUNT}"
    create: true
    name: "pachyderm"
  worker:
    serviceAccount:
      additionalAnnotations:
        iam.gke.io/gcp-service-account: "${SERVICE_ACCOUNT}"
      create: true
      name: "pachyderm-worker"

cloudsqlAuthProxy:
  enabled: true
  connectionName: ${CLOUDSQL_CONNECTION_NAME}
  serviceAccount: "${SERVICE_ACCOUNT}"
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
    postgresqlPassword: "${SQL_ADMIN_PASSWORD}"

loki-stack:
  loki:
    env:
      - name: GOOGLE_APPLICATION_CREDENTIALS
        value: /etc/secrets/${LOKI_GSA_NAME}-key.json
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
          bucket_name: "${LOKI_BUCKET_NAME}"
  grafana:
    enabled: false
EOF
```
2. Install using the following command:
```s
helm repo add pachyderm https://helm.pachyderm.com
helm repo update
helm install pachyderm -f ./${NAME}.values.yaml pachyderm/pachyderm

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

