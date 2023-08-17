---
# metadata # 
title:  IAM & RBAC
description: Learn how to manage access to resources using roles.
date: 
# taxonomy #
tags: ["permissions", "management", "roles", "RBAC"]
series:
seriesPart:
---

This page describes how {{% productName %}}'s Identity and Access Management (IAM) system works and how you can use it to manage access in {{% productName %}}. Use IAM to grant granular access to specific {{% productName %}} resources.


## How IAM Works 

IAM works by managing access for **users** (human or robot) through assigned **roles**. Roles contain a set of granular **permissions** (create, read, update, delete) for a given **resource**. In {{% productName %}}, resources include clusters, projects, and repositories. 

A user can have many roles, and some roles encompass the permissions of other roles. For example, if you have a `clusterAdmin`, all other permissions belonging to more restricted roles are included. 

---

{{% notice tip %}}
You can use the command `pachctl auth roles-for-permission <permission>` to look up which roles provide a given permission.
{{% /notice %}}

## Admin Roles

### clusterAdmin 

The `clusterAdmin` role includes all of the previous permissions, plus the following:
 
 | Permission |
|---|
| CLUSTER_MODIFY_BINDINGS |
| CLUSTER_GET_BINDINGS |
| CLUSTER_AUTH_ACTIVATE |
| CLUSTER_AUTH_DEACTIVATE |
| CLUSTER_AUTH_GET_CONFIG |
| CLUSTER_AUTH_SET_CONFIG |
| CLUSTER_AUTH_MODIFY_GROUP_MEMBERS |
| CLUSTER_AUTH_GET_GROUPS |
| CLUSTER_AUTH_GET_GROUP_USERS |
| CLUSTER_AUTH_EXTRACT_TOKENS |
| CLUSTER_AUTH_RESTORE_TOKEN |
| CLUSTER_AUTH_ROTATE_ROOT_TOKEN |
| CLUSTER_AUTH_DELETE_EXPIRED_TOKENS |
| CLUSTER_AUTH_GET_PERMISSIONS_FOR_PRINCIPAL |
| CLUSTER_AUTH_REVOKE_USER_TOKENS |
| CLUSTER_ENTERPRISE_ACTIVATE |
| CLUSTER_ENTERPRISE_HEARTBEAT |
| CLUSTER_ENTERPRISE_GET_CODE |
| CLUSTER_ENTERPRISE_DEACTIVATE |
| CLUSTER_DELETE_ALL |
| CLUSTER_ENTERPRISE_PAUSE |

### oidcAppAdmin 

| Permission |
|---|
| CLUSTER_IDENTITY_DELETE_OIDC_CLIENT |
| CLUSTER_IDENTITY_CREATE_OIDC_CLIENT |
| CLUSTER_IDENTITY_UPDATE_OIDC_CLIENT |
| CLUSTER_IDENTITY_LIST_OIDC_CLIENTS |
| CLUSTER_IDENTITY_GET_OIDC_CLIENT |


### idpAdmin 

| Permission |
|---|
| CLUSTER_IDENTITY_CREATE_IDP |
| CLUSTER_IDENTITY_UPDATE_IDP |
| CLUSTER_IDENTITY_LIST_IDPS |
| CLUSTER_IDENTITY_GET_IDP |
| CLUSTER_IDENTITY_DELETE_IDP |

### secretAdmin 

| Permission |
|---|
| CLUSTER_CREATE_SECRET |
| CLUSTER_LIST_SECRETS |
| SECRET_INSPECT |
| SECRET_DELETE |

### identityAdmin 

| Permission |
|---|
| CLUSTER_IDENTITY_SET_CONFIG |
| CLUSTER_IDENTITY_GET_CONFIG |

### licenseAdmin 

| Permission |
|---|
| CLUSTER_LICENSE_ACTIVATE |
| CLUSTER_LICENSE_GET_CODE |
| CLUSTER_LICENSE_ADD_CLUSTER |
| CLUSTER_LICENSE_UPDATE_CLUSTER |
| CLUSTER_LICENSE_DELETE_CLUSTER |
| CLUSTER_LICENSE_LIST_CLUSTERS |

---

## Project Roles 

All users have the `PROJECT_LIST_REPO` and `PROJECT_CREATE_REPO` permissions by default. 

{{% notice tip %}}
You can view your access level by running the command `pachctl list project` and checking the `ACCESS_LEVEL` column.
{{% /notice %}}

### projectViewer 

| Permission |
|---|
|PROJECT_LIST_REPO|

### projectWriter 

The `projectWriter` role includes all of the `projectViewer` permissions, plus the following:

| Permission |
|---|
|PROJECT_CREATE_REPO|

### projectOwner

<!-- The `ProjectOwnerRole` includes all of the `ProjectWriterRole`, `ProjectViewerRole`, and `RepoOwnerRole` permissions, plus the following: -->

| Permission |
|---|
|PROJECT_DELETE|
|PROJECT_MODIFY_BINDINGS|

### projectCreator

| Permission |
|---|
|PROJECT_CREATE|

---

## Repo Roles

### repoReader 

| Permission |
|---|
| REPO_READ |
| REPO_INSPECT_COMMIT |
| REPO_LIST_COMMIT |
| REPO_LIST_BRANCH |
| REPO_LIST_FILE |
| REPO_INSPECT_FILE |
| REPO_ADD_PIPELINE_READER |
| REPO_REMOVE_PIPELINE_READER |
| PIPELINE_LIST_JOB |

### RepoWriter

The `repoWriter` role includes all of the `repoReader` permissions, plus the following:

| Permission |
|---|
| REPO_WRITE |
| REPO_DELETE_COMMIT |
| REPO_CREATE_BRANCH |
| REPO_DELETE_BRANCH |
| REPO_ADD_PIPELINE_WRITER |

### RepoOwner

The `repoOwner` role includes all of the `repoWriter` and  `repoReader` permissions, plus the following:

| Permission |
|---|
| REPO_MODIFY_BINDINGS |
| REPO_DELETE |

---

## Misc Roles

### debugger

| Permission |
|---|
| CLUSTER_DEBUG_DUMP |
| CLUSTER_GET_PACHD_LOGS |

### robotUser

| Permission |
|---|
| CLUSTER_AUTH_GET_ROBOT_TOKEN |


### pachdLogReader

| Permission |
|---|
| CLUSTER_GET_PACHD_LOGS |

