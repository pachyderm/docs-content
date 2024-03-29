---
# metadata # 
title: Add Roles to Group via PachCTL
description: Learn how to grant and modify permissions on given resources for a group of users.
date: 
# taxonomy #
tags: ["permissions", "management"]
series:
seriesPart:
weight: 03
---

## Before You Start 

- You must have an active Enterprise key 
- You must have an [Authentication Provider (IdP)](/{{%release%}}/set-up/connectors) set up that supports groups
    - [Auth0](/{{%release%}}/set-up/connectors/auth0)
    - [Okta](/{{%release%}}/set-up/connectors/okta)
- Review the [Access Control (RBAC) Roles & Permissions](/{{%release%}}/set-up/authorization/permissions).
- Confirm you have the right role(s) to grant a user access to a given resource (e.g., you have the `projectOwner` role on a given project you wish to add other users to)
## How to Assign Roles to a Group 

This guide uses Auth0 and assumes resources (projects, repositories) have already been created in your cluster.

1. Enable group management in your [IdP of choice](https://dexidp.io/docs/connectors/) .
2. Update your connector config to include the [appropriate attributes](https://dexidp.io/docs/connectors/oidc/). 
   
{{< stack type="wizard" >}}
{{% wizardRow id="Syntax" %}}
{{% wizardButton option="JSON" state="active" %}}
{{% wizardButton option="YAML" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="syntax/json" %}}
```json
{
    "type": "oidc",
    "id": "auth0",
    "name": "Auth0",
    "version": 1,
    "config":{
    "issuer": "https://dev-k34x5yjn.us.auth0.com/",
    "clientID": "hegmOc5rTotLPu5ByRDXOvBAzgs3wuw5",
    "clientSecret": "7xk8O71Uhp5T-bJp_aP2Squwlh4zZTJs65URPma-2UT7n1iigDaMUD9ArhUR-2aL",
    "redirectURI": "http(s)://<insert-external-ip-or-dns-name>/dex/callback",
    "scopes": ["groups", "email", "profile"],
    "claimMapping":{
        "groups": "http://pachyderm.com/groups"
    },
    "insecureEnableGroups": true
    }
}
```
{{% /wizardResult %}}

{{% wizardResult val1="syntax/yaml" %}}
``` yaml
type: oidc
id: auth0
name: Auth0
version: 1
config:
    issuer: https://dev-k34x5yjn.us.auth0.com/
    clientID: hegmOc5rTotLPu5ByRDXOvBAzgs3wuw5
    clientSecret: 7xk8O71Uhp5T-bJp_aP2Squwlh4zZTJs65URPma-2UT7n1iigDaMUD9ArhUR-2aL
    redirectURI: http(s)://<insert-external-ip-or-dns-name>/dex/callback
    scopes: 
    - groups
    - email
    - profile
    claimMapping:
        groups: http://pachyderm.com/groups
    insecureEnableGroups: true
```
{{% /wizardResult %}}

{{% /wizardResults %}}
{{</stack >}}

3. Update the config by running the following command:
```s
pachctl idp update-connector <connector-id> --version 2
```
4. Grant the group roles by running the following command:
```s
pachctl auth set <resource-type>  <resource-name> <role-name> group:<group-name>
```
5. Confirm the group's roles were updated for the given resource:
   
{{< stack type="wizard" >}}
{{% wizardRow id="Resource Type" %}}
{{% wizardButton option="Project" state="active" %}}
{{% wizardButton option="Repo" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="resource-type/project" %}}
```s
pachctl auth get project <project-name>
```
{{% /wizardResult %}}

{{% wizardResult val1="resource-type/repo" %}}
```s
pachctl auth get repo <repo-name>
```
{{% /wizardResult %}}

{{% /wizardResults %}}
{{</stack >}}

{{% notice tip %}}
The command `pachctl auth get-groups` lists the groups that have been defined on your cluster.
{{%/notice %}}