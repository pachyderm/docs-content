---
# metadata # 
title: Authentication & IdP Connectors
description: Learn how to enable users to access a cluster using their preferred identity provider. 
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 4
directory: true
---
{{%productName%}} has an embedded Open ID Connect based on Dex, allowing for vendor-neutral authentication using your existing credentials from various back-ends. You can enable users to authenticate to a {{% productName %}} cluster using their favorite Identity Providers by following the articles in this section. 

When you enable authentication, you gain access to {{%productName%}}'s [authorization features](/{{%release%}}/set-up/authorization). You can use {{%productName%}}'s Role-Based Access Control (RBAC) model to configure authorization for your users and assign roles that grant certain permissions for interacting with {{%productName%}}'s resources.

## Useful Auth PachCTL Commands

- `pachctl auth login`:  Logs in to the cluster
- `pachctl auth logout`: Logs out of the cluster
- `pachctl auth whoami`: Returns the current user's username
- `pachctl auth get-groups`: Returns the current user's groups
- `pachctl auth get-config`: Returns the instance's current auth configuration
- `pachctl auth get cluster`: Returns the role bindings for the cluster
- `pachctl auth get project <project-name>`: Returns the role bindings for a project
- `pachctl auth get repo <repo-name>`: Returns the role bindings for a repo


## Before You Start 

- You must be using [Enterprise](/{{%release%}}/set-up/enterprise) to set up authentication