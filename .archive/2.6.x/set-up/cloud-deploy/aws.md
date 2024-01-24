---
# metadata # 
title:  AWS Deployment
description: Learn how to deploy to the cloud with AWS.
date: 
# taxonomy #
tags: ["aws", "cloud-deploy"]
series:
seriesPart:
weight: 1
---

## Before You Start 

This guide assumes that you have already tried [{{% productName %}} locally](/{{%release%}}/set-up/local-deploy/) and have all of the following installed:

- [Kubectl](https://kubernetes.io/docs/tasks/tools/) 
- Pachctl 
- [Helm](https://helm.sh/docs/intro/install/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html)

---

## 1. Create an EKS Cluster 

1. Use the eksctl tool to deploy an EKS Cluster:
```s
eksctl create cluster --name pachyderm-cluster --region <region> -profile <your named profile>
```
2. Verify deployment: 
```s
kubectl get all
```

## 2. Create an S3 Bucket

1. Run the following command:
```s
aws s3api create-bucket --bucket ${BUCKET_NAME} --region ${AWS_REGION}
```
2. Verify. 
```s
aws s3 ls
```

## 3. Enable Persistent Volumes Creation 

1. Create an [IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html). 
2. [Install the Amazon EBS Container Storage Interface (CSI)](https://docs.aws.amazon.com/eks/latest/userguide/managing-ebs-csi.html) driver on your cluster.
3. [Create a gp3 storage class](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html) manifest file (e.g., `gp3-storageclass.yaml`)
   ```s
   kind: StorageClass
   apiVersion: storage.k8s.io/v1
   metadata:
     name: gp3
     annotations:
       storageclass.kubernetes.io/is-default-class: "true"
   provisioner: kubernetes.io/aws-ebs
   parameters:
     type: gp3
     fsType: ext4

   ```
4. [Set gp3 to your default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/). 
   ```s
   kubectl apply -f gp3-storageclass.yaml
   ```
5. Verify that it has been set as your default.
   ```s
   kubectl get storageclass
   ```

## 4. Set up an RDS PostgreSQL Instance

By default, {{%productName%}} runs with a bundled version of PostgreSQL. 
For production environments, it is **strongly recommended that you disable the bundled version and use an RDS PostgreSQL instance**. 

{{% notice warning %}}
[Aurora Serverless PostgreSQL](https://aws.amazon.com/rds/aurora/serverless/) is not supported.
{{% /notice %}}
 
1. In the RDS console, create a database **in the region matching your {{%productName%}} cluster**. 
2. Choose the **PostgreSQL** engine.
3. Select a PostgreSQL version >= 13.3.
4. Configure your DB instance as follows:

| SETTING | Recommended value|
|:----------------|:--------------------------------------------------------|
| *DB instance identifier* | Fill in with a unique name across all of your DB instances in the current region.|
| *Master username* | Choose your Admin username.|
| *Master password* | Choose your Admin password.|
| *DB instance class* | The standard default should work. You can change the instance type later on to optimize your performances and costs. |
| *Storage type* and *Allocated storage*| If you select **io1**, keep the 100 GiB default size. <br> Read more [information on Storage for RDS on Amazon's website](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html). |
| *Storage autoscaling* | If your workload is cyclical or unpredictable, enable storage autoscaling to allow RDS to scale up your storage when needed. |
| *Standby instance* | We highly recommend creating a standby instance for production environments.|
| *VPC* | **Select the VPC of your Kubernetes cluster**. Attention: After a database is created, you can't change its VPC. <br> Read more on [VPCs and RDS on Amazon documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html).| 
| *Subnet group* | Pick a Subnet group or Create a new one. <br> Read more about [DB Subnet Groups on Amazon documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets). |
| *Public access* | Set the Public access to `No` for production environments. |
| *VPC security group* | Create a new VPC security group and open the postgreSQL port or use an existing one. |
| *Password authentication* or *Password and IAM database authentication* | Choose one or the other. |
| *Database name* | In the *Database options* section, enter {{%productName%}}'s Database name (We are using `{{% productName %}}`in this example.) and click *Create database* to create your PostgreSQL service. Your instance is running. <br>Warning: If you do not specify a database name, Amazon RDS does not create a database.|

   {{% notice info %}}
  **Standalone Clusters**

   If you are deploying a standalone cluster, you must create a second database named `dex` in your RDS instance for {{%productName%}}'s authentication service. Read more about [dex on PostgreSQL in Dex's documentation](https://dexidp.io/docs/storage/#postgres). 
   
   Multi-cluster setups use [Enterprise Server](/{{%release%}}/set-up/enterprise-server) to handle authentication, so you do not need to create a `dex` database.
   {{% /notice %}}
   
1. Create a new user account and **grant it full CRUD permissions to both `{{% productName %}}`and (when applicable) `dex` databases**. Read about managing PostgreSQL users and roles in this [blog](https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/). {{%productName%}} will use the same username to connect to `{{% productName %}}`as well as to `dex`. 

## 5. Create a Values.yaml

{{< stack type="wizard" >}}
{{% wizardRow id="version" %}}
{{% wizardButton option="Community Edition" state="active" %}}
{{% wizardButton option="Enterprise" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="version/community-edition" %}}
```yaml
global:
  postgresql:
    postgresqlAuthType: "scram-sha-256" # use "md5" if using postgresql < 14
    postgresqlUsername: "username"
    postgresqlPassword: "password" 
    # The name of the database should be {{%productName%}}'s ("pachyderm" in the example above), not "dex" 
    # See also 
    # postgresqlExistingSecretName: "<yoursecretname>"
    postgresqlDatabase: "databasename"
    # The postgresql database host to connect to. Defaults to postgres service in subchart
    postgresqlHost: "RDS CNAME"
    # The postgresql database port to connect to. Defaults to postgres server in subchart
    postgresqlPort: "5432"

postgresql:
  # turns off the install of the bundled postgres.
  # If not using the built in Postgres, you must specify a Postgresql
  # database server to connect to in global.postgresql
  enabled: false

deployTarget: "AMAZON"

proxy:
  enabled: true
  service:
    type: LoadBalancer

pachd:
  storage:
    amazon:
      bucket: "bucket_name"      
      # this is an example access key ID taken from https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html (AWS Credentials)
      id: "AKIAIOSFODNN7EXAMPLE"                
      # this is an example secret access key taken from https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html  (AWS Credentials)          
      secret: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      region: "us-east-2"
  externalService:
    enabled: true

 console:
   enabled: true
```
{{% /wizardResult %}}
{{% wizardResult val1="version/enterprise" %}}
```yaml
global:
  postgresql:
    postgresqlAuthType: "scram-sha-256" # use "md5" if using postgresql < 14
    postgresqlUsername: "username"
    postgresqlPassword: "password" 
    # The name of the database should be {{%productName%}}'s ("pachyderm" in the example above), not "dex" 
    # See also 
    # postgresqlExistingSecretName: "<yoursecretname>"
    postgresqlDatabase: "databasename"
    # The postgresql database host to connect to. Defaults to postgres service in subchart
    postgresqlHost: "RDS CNAME"
    # The postgresql database port to connect to. Defaults to postgres server in subchart
    postgresqlPort: "5432"

postgresql:
  # turns off the install of the bundled postgres.
  # If not using the built in Postgres, you must specify a Postgresql
  # database server to connect to in global.postgresql
  enabled: false

deployTarget: "AMAZON"

proxy:
  enabled: true
  service:
    type: LoadBalancer
  
pachd:
  storage:
    amazon:
      bucket: "bucket_name"                
      # this is an example access key ID taken from https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html (AWS Credentials)
      id: "AKIAIOSFODNN7EXAMPLE"                
      # this is an example secret access key taken from https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html  (AWS Credentials)          
      secret: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      region: "us-east-2"
# Enterprise key 
  enterpriseLicenseKey: "YOUR_ENTERPRISE_TOKEN"
console:
  enabled: true
```
{{% /wizardResult %}}
{{% /wizardResults %}}
{{< /stack>}}

## 6. Configure Helm

Run the following to add the {{% productName %}} repo to Helm:
```s
helm repo add pachyderm https://helm.pachyderm.com
helm repo update
helm install pachyderm pachyderm/pachyderm -f my_pachyderm_values.yaml 
```
## 7. Verify Installation 

1. In a new terminal, run the following command to check the status of your pods:
 ```s
 kubectl get pods
 ```
 ```
 NAME                                           READY   STATUS      RESTARTS   AGE
pod/console-5b67678df6-s4d8c                   1/1     Running     0          2m8s
pod/etcd-0                                     1/1     Running     0          2m8s
pod/pachd-c5848b5c7-zwb8p                      1/1     Running     0          2m8s
pod/pg-bouncer-7b855cb797-jqqpx                1/1     Running     0          2m8s
pod/postgres-0                                 1/1     Running     0          2m8s
 ```
2. Re-run this command after a few minutes if `pachd` is not ready.

## 8. Connect to Cluster

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


{{% notice note %}}
If the connection commands did not work together, run each separately.
{{%/notice %}}

Optionally open your browser and navigate to the [Console UI](http://localhost:4000).

{{% notice tip %}}
You can check your {{% productName %}} version and connection to `pachd` at any time with the following command:
   ```s
   pachctl version
   ```
   ```
   COMPONENT           VERSION  

   pachctl             {{% latestPatchNumber %}}  
   pachd               {{% latestPatchNumber %}}  
   ```
{{% /notice %}}
