---
# metadata # 
title: Enterprise Server Backup
description: Learn how to back-up and restore the state of a production Enterprise Server.
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

## Backup A Standalone Enterprise Server

Backing up and restoring an Enterprise Server is similar to the backing up and restoring of a regular [cluster](../cluster), with three slight variations:

1. The name of its Kubernetes deployment is `pach-enterprise` versus `pachd` in the case of a regular cluster.
2. The Enterprise Server does not use an Object Store.
3. An Enterprise server only requires a `dex` database.


{{% notice warning %}}
Make sure that `pachctl` and `kubectl` are pointing to the right cluster. Check your Enterprise Server context: `pachctl config get active-enterprise-context`, or `pachctl config set active-enterprise-context <my-enterprise-context-name> --overwrite` to set it.
{{% /notice%}}

- Pause the Enterprise Server like you would pause a regular cluster by running `pachctl enterprise pause` (Enterprise users), or using `kubectl`.

  {{% notice note %}} 
  **kubectl users**:
   There is a difference with the pause of a regular cluster. The deployment of the enterprise server is named `pach-enterprise`; therefore, the first command should be:

   ```s
   kubectl scale deployment pach-enterprise --replicas 0 
   ``` 

   There is no need to pause all the {{% productName %}} clusters registered to the Enterprise Server to backup the enterprise server; however, pausing the Enterprise server will result in your clusters becoming unavailable.
  {{% /notice %}}

- As a reminder, the Enterprise Server does not use any object-store. Therefore, the backup of the Enterprise Server only consists in backing up the database `dex`.

- Resume the operations on your Enterprise Server by running `pachctl enterprise unpause`  (Enterprise users) to scale the `pach-enterprise` deployment back up. Alternatively, if you used `kubectl`, run:

    ```s
    kubectl scale deployment pach-enterprise --replicas 1
    ```

### Restore An Enterprise Server

- [Follow the cluster restoration steps](../cluster) while skipping all tasks related to creating and populating a new object-store.

- Once your cluster is up and running, check that all [your clusters are automatically registered with your new Enterprise Server](../../../set-up/enterprise-server/).