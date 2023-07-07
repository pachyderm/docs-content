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
-  You have already tried [{{%productName%}} locally](/{{%release%}}/set-up/local-deploy/) and have some familiarity with [Kubectl](https://kubernetes.io/docs/tasks/tools/), [Helm](https://helm.sh/docs/intro/install/), [Google Cloud SDK](https://cloud.google.com/sdk/) and [jq](https://stedolan.github.io/jq/download/)
- You have access to a Google Cloud account linked to an active billing account (`gcloud alpha billing accounts list`)

### Configure Variables

Configure these variables and set in a `.env` file and source them by inputting `source .env` into the terminal before starting the installation guide.

```s
PROJECT_NAME="pachyderm-0001"
SQL_ADMIN_PASSWORD="batteryhorsestaple"
BILLING_ACCOUNT_ID="000000-000000-000000" # see `gcloud alpha billing accounts list`

# This group of variables can be changed, but are sane defaults
GCP_REGION="us-central1"
GCP_ZONE="us-central1-a"
K8S_NAMESPACE="default"
CLUSTER_MACHINE_TYPE="n2-standard-2"
SQL_CPU="2"
SQL_MEM="7680MB"
LOGGING="SYSTEM"
PROJECT_ID=$(echo "pach-$(openssl rand -base64 32 | tr -dc 'a-z0-9-' | fold -w 2-26 | head -n 1)")

## optional name generator, useful if you are creating multiple clusters or testing.
adjective=("happy" "silly" "brave" "witty" "elegant" "fierce" "gentle" "clever" "vibrant" "charming")
color=("red" "blue" "green" "yellow" "purple" "orange" "pink" "black" "white" "gray")
animal=("cat" "dog" "elephant" "lion" "tiger" "panda" "giraffe" "zebra" "monkey" "bear")
NAME="${adjective[$RANDOM % ${#adjective[@]}]}-${color[$RANDOM % ${#color[@]}]}-${animal[$RANDOM % ${#animal[@]}]}"

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
ROLE3="roles/storage.objectCreator"

SERVICE_ACCOUNT="${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
LOKI_SERVICE_ACCOUNT="${LOKI_GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
PACH_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/pachyderm]"
SIDECAR_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/pachyderm-worker]"
CLOUDSQLAUTHPROXY_WI="serviceAccount:${PROJECT_ID}.svc.id.goog[${K8S_NAMESPACE}/k8s-cloudsql-auth-proxy]"

```
---

The following steps use a template to create a GKE cluster, a Cloud SQL instance, and a static IP address. The template also creates a service account for {{%productName%}} and Loki, and grants the service account the necessary permissions to access the Cloud SQL instance and storage buckets. You do not have to this template, but it's a good outline for understanding how to create your own set up.

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
   gcloud services enable compute.googleapis.com
   ```


## 2. Create a Static IP Address

1. Create the static IP Address:

```s
gcloud compute addresses create ${STATIC_IP_NAME} --region=${GCP_REGION} 
```
2. Get the static IP address:

```s
STATIC_IP_ADDR=$(gcloud compute addresses describe ${STATIC_IP_NAME} --region=${GCP_REGION} --format="json" --flatten="address" | jq -r '.[]')
```

## 3. Create a GKE Cluster 

1. Create a GKE cluster with the following command:

   ```s
   gcloud container clusters create ${CLUSTER_NAME} \
     --region=${GCP_REGION} \
     --machine-type=${CLUSTER_MACHINE_TYPE} \
     --workload-pool=${PROJECT_ID}.svc.id.goog \
     --enable-ip-alias \
     --create-subnetwork="" \
     --logging=${LOGGING} \
     --enable-dataplane-v2 \
     --enable-shielded-nodes \
     --release-channel="regular" \
     --workload-metadata="GKE_METADATA" \
     --enable-autorepair \
     --enable-autoupgrade \
     --disk-type="pd-ssd" \
     --image-type="COS_CONTAINERD"

   ```
2. Grant your user account the privileges needed for the `helm install` to work properly:
   ```s
   # By default, GKE clusters have RBAC enabled. To allow the 'helm install' to give the 'pachyderm' service account
   # the requisite privileges via clusterrolebindings, you will need to grant *your user account* the privileges
   # needed to create those clusterrolebindings.
   #
   # Note that this command is simple and concise, but gives your user account more privileges than necessary. See
   # https://docs.pachyderm.io/en/latest/deploy-manage/deploy/rbac/ for the complete list of privileges that the
   # Pachydermserviceaccount needs.
   kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)
   ```
3. Connect to the cluster:

   ```s
   gcloud container clusters get-credentials ${CLUSTER_NAME} --region=${GCP_REGION}
   ```

## 4. Create Storage Buckets

```s
gsutil mb -l ${GCP_REGION} gs://${BUCKET_NAME}
gsutil mb -l ${GCP_REGION} gs://${LOKI_BUCKET_NAME}
```

## 5. Create a Cloud SQL Instance

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
CLOUDSQL_CONNECTION_NAME=$(gcloud sql instances describe ${CLOUDSQL_INSTANCE_NAME} --format=json | jq ."connectionName")
```

## 6. Create Service Accounts 

Create a service account for {{%productName%}} and Loki. 

```s
gcloud iam service-accounts create ${GSA_NAME}

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="${ROLE1}"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="${ROLE2}"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member=serviceAccount:${SERVICE_ACCOUNT} 
    --role="${ROLE3}"

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

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${LOKI_SERVICE_ACCOUNT}" \
    --role="${ROLE3}"
```

## 7. Create a Loki Secret

```s
kubectl create secret generic loki-service-account --from-file="${LOKI_GSA_NAME}-key.json"
```
## 8. Build a Helm Values File

1. Create a values.yaml file, inserting the variables we've created in the previous steps:
```s
cat <<EOF > ${NAME}.values.yaml
deployTarget: "GOOGLE"

pachd:
  enabled: true
  externalService:
    enabled: false
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
  connectionName: ${CLOUDSQL_CONNECTION_NAME}
  serviceAccount: "${SERVICE_ACCOUNT}"
  enabled: true
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

proxy:
  enabled: true
  service:  
    type: LoadBalancer
    loadBalancerIP: ${STATIC_IP_ADDR} 
    httpPort: 80  
    httpsPort: 443 
  tls: 
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
   pachctl connect grpc://<your-proxy.host-value>:80
   ```
   {{% /wizardResult %}}
   {{% wizardResult val1="method/https-tls" %}}
   ```s
   pachctl connect grpcs://<your-proxy.host-value>:443
   ```
   {{% /wizardResult %}}
   {{% /wizardResults%}}

   {{</stack>}}
3. You can optionally run `port-forward` to connect to console in your dashboard at `http://localhost:4000/`.