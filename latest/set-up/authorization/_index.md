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

- You must be using [Enterprise](/{{%release%}}/set-up/enterprise) to set up [authentication](/{{%release%}}/set-up/connectors) and authorization. 

## Activate User Access Management

1. Activate authentication using the following command:

```s
pachctl auth activate 

# {{% productName %}} root token:
# 54778a770c554d0fb84563033c9cb808
```
2. Save the root token value in a secure place.

You can use this token in the future to log in to the initial root admin user by entering the following comand: 

```s
pachctl auth use-auth-token

# Please paste your {{% productName %}} auth token:
```

As a *Root User* (or initial admin), 
you can now configure {{% productName %}} to work with
the identity management provider (IdP) of your choice.

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
