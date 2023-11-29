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

## How to Install Pachyderm with MockIDP Activated

1. Run the following command with your Enterprise License Key provided to enable MockIDP:

   ```s
   helm install pach pachyderm/pachyderm \
     --set deployTarget=LOCAL \
     --set proxy.enabled=true \
     --set proxy.service.type=LoadBalancer \
     --set pachd.enterpriseLicenseKey=<yourkey> \
     --set proxy.host=localhost \
     --set oidc.issuerURI=http://pachd:30658/dex \
     --set oidc.userAccessibleOauthIssuerHost=http://localhost/dex
   ```
2. Connect:
   ```s
   pachctl connect grpc://localhost:80
   ```
3. Log in via the [browser](http://localhost) at `localhost` or via the CLI:
   ```s
   pachctl auth login
   ```
    - user: `admin`
    - password: `password`
  
4. Verify that you are logged in:
   ```s
   pachctl auth whoami
   ```

   ```
   You are "user:kilgore@kilgore.trout"
    session expires: 21 Sep 23 18:07 UTC
   ```
5. List your [projects](/latest/build-dags/project-operations/) to view your permissions/access level:
    ```s
    pachctl list projects
    ```
    ```
    ACTIVE PROJECT           ACCESS_LEVEL                 CREATED           DESCRIPTION
    default                 [clusterAdmin projectWriter]    3 days ago        -
    * batch-inference-1     [clusterAdmin projectOwner]     About an hour ago -
    ```

You can now test and develop locally with MockIDP and Console enabled.

## Troubleshooting

### Error: No Authentication Providers are Configured

If you are seeing the error `no authentication providers are configured`, it's likely that you activated enterprise via pachCTL instead of having your license details in your `values.yaml` file. 