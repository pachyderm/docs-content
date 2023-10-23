---
# metadata # 
title: MockIDP
description: Learn how to authenticate with MockIDP for testing and development purposes.
date: 
# taxonomy #
tags:  ["identity-providers", "permissions", "management", "mockidp"]
series:
seriesPart:
weight: 01
---

MockIDP is used for **testing** and **development** so that you can run {{% productName %}} and experiment with [permissions](/latest/set-up/authorization/permissions/) locally without having to set up an external identity provider.

{{% notice warning %}}

**Do not use mockIDP for clusters that will be deployed into production.**  If you do upgrade a cluster with mockIDP enabled, you must revoke the default mockIDP admin user by running the following command:

```s
pachctl auth revoke --user kilgore@kilgore.trout
```
{{% /notice %}}

## Before You Start 

- You must have [Enterprise](/latest/set-up/enterprise/activate-via-helm/) enabled on your cluster

## How to Activate MockIDP 

The following steps assume that you are deploying locally and wish to have Console enabled. 

1. Obtain your current user-input helm values:
    ```s
    helm get values pachyderm  > values.yaml
    ```
2. Add [Console configuration](/latest/manage/helm-values/console/):
   ```yaml
   console:
     disableTelemetry: true
     config:
       oauthRedirectURI: http://localhost/oauth/callback/?inline=true
       oauthClientSecret: '123'
   ```
3. Add [OIDC configuration](/latest/manage/helm-values/oidc/):
    ```yaml
    oidc:
     issuerURI: "http://pachd:30658/dex"
     userAccessibleOauthIssuerHost: http://localhost
    ```
    A minimal `values.yaml` file should look like this:
   ```yaml
   deployTarget: LOCAL
   pachd:
     enterpriseLicenseKeySecretName: pachyderm-enterprise-key
   proxy:
     enabled: true
     host: localhost
     service:
       type: LoadBalancer
   console:
    disableTelemetry: true
    config:
      oauthRedirectURI: http://localhost/oauth/callback/?inline=true
      oauthClientSecret: '123'
   oidc:
    issuerURI: "http://pachd:30658/dex"
    userAccessibleOauthIssuerHost: http://localhost
   ```

4. Upgrade your cluster:
    ```s
    helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
    ```
5. Connect:
   ```s
   pachctl connect grpc://localhost:80
   ```
6. Log in via the [browser](http://localhost) at `localhost` or via the CLI:
   ```s
   pachctl auth login
   ```
    - user: `admin`
    - password: `password`
  
7. Verify that you are logged in:
   ```s
   pachctl auth whoami
   ```

   ```
   You are "user:kilgore@kilgore.trout"
    session expires: 21 Sep 23 18:07 UTC
   ```
8. List your [projects](/latest/build-dags/project-operations/) to view your permissions/access level:
    ```s
    pachctl list projects
    ```
    ```
    ACTIVE PROJECT           ACCESS_LEVEL                 CREATED           DESCRIPTION
    default                 [clusterAdmin projectWriter]    3 days ago        -
    * batch-inference-1     [clusterAdmin projectOwner]     About an hour ago -
    ```

You can now test and develop locally with MockIDP and Console enabled.