---
# metadata # 
title:  Authorization
description: Learn how to set up and manage Role-Based Access Control (RBAC).
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 4
---

You can use {{% productName %}}'s Role-Based Access Control (RBAC) model to configure authorization for your users. Users can be assigned roles that grant certain permissions for interacting with {{% productName %}}'s resources. 

## Before You Start 

You must set up a DNS address used for {{%productName%}}; this can be a URL or an IP address, but it must be accessible from the internet.

## Enable Authorization

The following steps will enable authorization for your {{%productName%}} cluster and use the **mockIDP connector**. By default, the mockIDP connector comes with a default root user `admin` with the password `password`. To use additional connectors, complete these steps and then see the [Connectors](/{{%release%}}/set-up/connectors) page.

1. Obtain an [Enterprise license](/{{%release%}}/set-up/enterprise).
2. Create a [secret](/{{%release%}}/manage/secrets) for your license.
 ```s
 kubectl create secret generic enterprise-license \
   --from-literal=enterprise-license-key=<your license key>
 ```
3. Add the secret name to it to your values.yaml file at `pachd.enterpriseLicenseKeySecretName`.
4. Update the `proxy.host` field in your values.yaml file with your DNS address.
  {{% notice warning %}}
   If `proxy.host` is not set, {{%productName%}} will not be able to redirect users to the login page. `localhost` is not a valid value for `proxy.host` when using the mockIDP connector.
  {{% /notice %}}
5. Run the `helm upgrade` command (or `helm install` if you are installing {{%productName%}} for the first time).
   ```s
   helm install pachyderm/pachyderm -f values.yaml
   ```
6. Connect using `pachctl connect <host>`, where `<host>` is the value of `proxy.host` in your values.yaml file.
7. Log via the browser or by using `pachctl auth login`. You will be redirected to the login page.



## License Expiration 
When an Enterprise License expires, a
{{% productName %}} cluster with enabled User Access Management goes into an
`admin-only` state. In this state, only `ClusterAdmins` have
access to the data stored in {{% productName %}}. This safety measure keeps sensitive data protected, even when an enterprise subscription becomes stale. To return the cluster to its previous state, run `pachctl license activate` and submit your new code.


## Users Types
{{% productName %}} has 5 user types:

|User Type| Description|
|-|-|
|clusterAdmin| |
|IdP User| Any user or group of users authenticated by your Identity Provider to access {{% productName %}}.|
|Robot User|A Service account used for third party applications/systems integrating with {{% productName %}} APIs/Clients.|
|Pipeline User| An internal Service Account used for Pipelines when interacting with {{% productName %}} resources.|
|All Cluster Users|A general subject that represents **everyone who has logged in to a cluster**.|

  {{% productName %}} defines 4 prefixes depending on the type of user:

  - robot
  - user
  - group
  - pipeline (as mentioned above, this prefix will not be used in the context of granting privileges to users. However, it does exist. We are listing it here to give an exhauxtive list of all prefixes.)

  Aditionnally, the "everyone" user `allClusterUsers` has no specific prefix. See the example below to learn how to assign repoReader access to `allClusterUsers` on a repo.

## Resource Types
{{% productName %}} has 3 resource types:

|Resource Type| Description|
|-|-|
|Cluster| A set of nodes for running containerized applications. Containers allow users to run repeatable and standardized code. |
|Project| A project is a container of 1 or more DAGs that allows for users to organize their repos. Projects allow multiple teams to work in a cluster.|
|Repo| A repository is where data is stored and contains both files and folders. Repos tracks all changes to the data and creates a history of data changes.|

## Role Types 
{{% productName %}} has 3 role  types:

|Role Type| Description|
|-|-|
|Cluster Roles| Granted at the cluster level.|
|Project Roles| Granted at the project level.|
|Repo Roles|  Granted at the repo level or at the cluster level.|
