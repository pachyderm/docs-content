---
# metadata # 
title: Cluster Backup
description: Learn how to back-up and restore the state of a production cluster.
date: 
# taxonomy #
tags: ["management", "backups"]
series:
seriesPart:
directory: true
---

This page will walk you through the main steps required to manually back up and restore the state of a {{% productName %}} cluster in production. Details on how to perform those steps might vary depending on your infrastructure and cloud provider / on-premises setup. Refer to your provider's documentation.

## Overview

{{% productName %}} state is stored in two main places:

- An **object-store** holding {{% productName %}}'s data.
- A PostgreSQL instance made up of **one or two databases**: `pachyderm` holding {{% productName %}}'s metadata and `dex` holding authentication data. 

Backing up a {{% productName %}} cluster involves snapshotting both the object store and the PostgreSQL database(s), in a consistent state, at a given point in time.

Restoring it involves re-populating the database(s) and the object store using those backups, then recreating a {{% productName %}} cluster.

{{% notice note %}}
- Make sure that you have a bucket for backup use, separate from the object store used by your cluster.
- Depending on the reasons behind your cluster recovery, you might choose to use an existing vs. a new instance of PostgreSQL and/or the object store.
{{% /notice %}}

## Manual Back Up Of A {{% productName %}} Cluster

Before any manual backup:

- Make sure to retain a copy of the Helm values used to deploy your cluster.
- Then, suspend any state-mutating operations.

{{% notice note %}}
- **Backups incur downtime** until operations are resumed.
- Operational best practices include notifying {{% productName %}} users of the outage and providing an estimated time when downtime will cease.  
- Downtime duration is a function of the size of the data be to backed up and the networks involved; Testing before going into production and monitoring backup times on an ongoing basis might help make accurate predictions.
{{% /notice %}}

### Suspend Operations

- **Pause any external automated process ingressing data to {{% productName %}} input repos**, or queue/divert those as they will fail to connect to the cluster while the backup occurs.

- **Suspend all mutation of state by scaling `pachd` and the worker pods down**:

  {{% notice warning %}}
  Before starting, make sure that your context points to the server you want to pause by running `pachctl config get active-context`.
  {{% /notice%}}

  To pause {{% productName %}}:

  - If you are an [**Enterprise**](/{{%release%}}/set-up/enterprise/) user: **Run the `pachctl enterprise pause` command**. 

  - Alternatively, you can use `kubectl`:

      Before starting, make sure that `kubectl` [points to the right cluster](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).

      Run `kubectl config get-contexts` to list all available clusters and contexts (the current context is marked with a `*`), then `kubectl config use-context <your-context-name>` to set the proper active context.

      ```s 
      kubectl scale deployment pachd --replicas 0 
      kubectl scale rc --replicas 0 -l suite=pachyderm,component=worker
      ```

      Note that it takes some time for scaling down to take effect;

      Run the `watch` command to monitor the state of `pachd` and worker pods terminating:

      ```s
      watch -n 5 kubectl get pods
      ```

### Back Up The Databases And The Object Store

This step is specific to your database and object store hosting. 

- If your PostgreSQL instance is solely dedicated to {{% productName %}}, you can use PostgreSQL's tools, like `pg_dumpall`, to dump your entire PostgreSQL state.  

    Alternatively, you can use targeted `pg_dump` commands to dump the `pachyderm` and `dex` databases, or use your Cloud Provider's backup product. In any case, make sure to use TLS. Note that if you are using a cloud provider, you might choose to use the provider’s method of making PostgreSQL backups.
    
  {{% notice warning %}}
  A production setting of {{% productName %}} implies that you are running a managed PostgreSQL instance.
  {{% /notice %}}

  {{% notice info%}}

   - [PostgreSQL on AWS RDS backup](https://aws.amazon.com/backup/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
   - [GCP Cloud SQL backup](https://cloud.google.com/sql/docs/postgres/backup-recovery/backing-up)
   - [Azure Database for PostgreSQL backup](https://docs.microsoft.com/en-us/azure/backup/backup-azure-database-postgresql)

   For on-premises Kubernetes deployments, check the vendor documentation
   for your on-premises PostgreSQL for details on backing up and restoring your databases.
  {{% /notice%}}

- To back up the object store, you can either download all objects or
use the object store provider’s backup method.  
    The latter is preferable since it will typically not incur egress costs.

  {{% notice info %}}

  - [AWS backup for S3](https://aws.amazon.com/backup/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
  - [GCP Cloud storage bucket backup](https://cloud.google.com/storage-transfer/docs/overview)
  - [Azure blob backup](https://docs.microsoft.com/en-us/azure/backup/blob-backup-configure-manage)

  For on-premises Kubernetes deployments, check the vendor documentation
  for your on-premises object store for details on backing up and
  restoring a bucket.
  {{% /notice %}}

### Resuming operations

Once your backup is completed, resume your normal operations by scaling `pachd` back up. It will take care of restoring the worker pods:

- Enterprise users: **run `pachctl enterprise unpause`**. 

- Alternatively, if you used `kubectl`:

    ```s
    kubectl scale deployment pachd --replicas 1
    ```

## Restore {{% productName %}}

There are two primary use cases for restoring a cluster:

1. Your data have been corrupted, preventing your cluster from functioning correctly. You want the same version of {{% productName %}} re-installed on the latest uncorrupted data set. 
1. You have upgraded a cluster and are encountering problems. You decide to uninstall the current version and restore the latest backup of a previous version of {{% productName %}}.

Depending on your scenario, pick all or a subset of the following steps:

- Populate new `pachyderm` and `dex` (if required) databases on your PostgreSQL instance
- Populate a new bucket or use the backed-up object-store (note that, in that case, it will no longer be a backup)
- Create a new empty Kubernetes cluster and give it access to your databases and bucket
- Deploy {{% productName %}} into your new cluster

### Restore The Databases And Objects

- Restore PostgreSQL backups into your new databases using the appropriate
method (this is most straightforward when using a cloud provider).
- Copy the objects from the backed-up object store to your new bucket or re-use your backup.

### Deploy {{% productName %}} Into The New Cluster

Finally, update the copy of your original Helm values to point {{% productName %}} to the new databases and the new object store, then use Helm to install
{{% productName %}} into the new cluster.

### Connect 'pachctl' To Your Restored Cluster

And check that your cluster is up and running.
