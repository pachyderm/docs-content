---
# metadata # 
title:  Authorization (Roles & Groups)
description: Learn how to set up and manage Role-Based Access Control (RBAC).
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 4
---

You can use {{% productName %}}'s Role-Based Access Control (RBAC) model to configure authorization for your users. Users can be assigned roles that grant certain permissions for interacting with {{% productName %}}'s resources. 

## Authorization Model

## Users Types 

|User Type| Prefix | Description|
|-|-|-|
|clusterAdmin|user| |
|IdP User|user| Any user or group of users authenticated by your Identity Provider to access {{% productName %}}.|
|Robot User|robot|A Service account used for third party applications/systems integrating with {{% productName %}} APIs/Clients.|
|Pipeline User|pipeline|An internal Service Account used for Pipelines when interacting with {{% productName %}} resources.|
|All Cluster Users||A general subject that represents **everyone who has logged in to a cluster**.|

## Resource Types

|Resource Type| Description|
|-|-|
|Cluster| A set of nodes for running containerized applications. Containers allow users to run repeatable and standardized code. |
|Project| A project is a container of 1 or more DAGs that allows for users to organize their repos. Projects allow multiple teams to work in a cluster.|
|Repo| A repository is where data is stored and contains both files and folders. Repos tracks all changes to the data and creates a history of data changes.|

## Role Types 

|Role Type| Description|
|-|-|
|Cluster Roles| Granted at the cluster level.|
|Project Roles| Granted at the project level.|
|Repo Roles|  Granted at the repo level or at the cluster level.|


## License Expiration 
When an Enterprise License expires, a
{{% productName %}} cluster with enabled User Access Management goes into an
`admin-only` state. In this state, only `ClusterAdmins` have
access to the data stored in {{% productName %}}. This safety measure keeps sensitive data protected, even when an enterprise subscription becomes stale. To return the cluster to its previous state, run `pachctl license activate` and submit your new code.