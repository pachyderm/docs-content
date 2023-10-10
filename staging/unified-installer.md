---
# metadata # 
title: Unified Deployment 
description: Learn how to deploy Pachyderm and Determined together.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 2
directory: true
---

{{% notice warning %}}
The Unified Deployment experience is in Beta and has not officially been released, so these instructions are subject to change.
{{%/notice%}}

In this guide, we'll show you how to update your cluster configuration to support a unified installation and deployment of {{%productName%}} + Determined.

## Before You Start 

This guide assumes that you have already completed all of the following: 

1.  Deployed {{%productName%}} using one of the cloud deployment guides ([AWS](/{{%release%}}/set-up/cloud-deploy/aws), [GCP](/{{%release%}}/set-up/cloud-deploy/gcp), or [Azure](/{{%release%}}/set-up/cloud-deploy/azure)).
2.  Added an active [Enterprise License Key](/{{%release%}}/set-up/enterprise/activate-via-helm/).
3. Set up [TLS (SSL, HTTPS)](/{{%release%}}/set-up/tls/) for your {{%productName%}} cluster and already have a TLS secret.
4.  Set up an [OIDC connector](/{{%release%}}/set-up/connectors/) for your {{%productName%}} cluster.

## How to Configure a Unified Setup 

### 1. Create Necessary Secrets

You will need to create two [secrets](/{{%release%}}/manage/secrets) for Determined:
   1. A Determined Enterprise docker image credentials secret (e.g., `det-image`)

        ```s
        kubectl create secret docker-registry det-image \
        --docker-server=https://index.docker.io/v1/ \
        --docker-username=<username> \
        --docker-password=<password> \
        --docker-email=<email> \
        --output=json > det-image-secret.json
        ```

   2. A Determined Enterprise admin credentials secret (e.g., `det-creds`)

        ```s
        kubectl create secret generic det-creds \
        --from-literal=determined-username=admin \
        --from-literal=determined-password="" \
        --output=json > det-creds-secret.json
        ```

### 2. Update the {{%productName%}} Helm Chart


1. Open your `values.yaml` file or generate a local copy using the following command:
 ```s
 helm get values pachyderm > values.yaml
 ```

2. Add the following `determined` section to your `values.yaml` file and fill in the appropriate values:

```yaml
determined:
  detVersion: 0.24.0 
  enabled: true
  enterpriseEdition: true
  imagePullSecretName: det-image 
  maxSlotsPerPod: 1
  oidc:
    clientID: determined
    enabled: true
    idpRecipientUrl: # https://<proxy.host.value.com>:8080 
    idpSsoUrl: # https://<proxy.host.value.com>/dex
    provider: # your oidc.upstreamIDPs.config.id; e.g., Auth0 or Okta
  tlsSecret: # your tls secret name
```

3. Update the `pachd` section of your `values.yaml` file to include the full endpoint address and the name of the Determined admin credentials secret:

```yaml
pachd:
  determined:
    apiEndpoint: # https://determined-master-service-internal-<HELM RELEASE NAME>:8082
    credentialsSecretName: det-creds 
  activateEnterprise: true
```

### 3. Provision Determined Users

Currently, {{%productName%}} does not automatically provision users for Determined. You will need to manually provision users for Determined using the following command:

1. Invoke Determine's Auth/Login API as the default admin user: 
```s
curl --location 'https://<proxy.host.value.com>:8080/api/v1/auth/login' \
--header 'Content-Type: application/json' \
--data '{
"username": "admin",
"password": "",
"isHashed": true
}'
```
2. Invoke Determine's User API and create a new user matching a registered IDP user:
```s
curl --location 'https://<proxy.host.value.com>:8080/api/v1/users' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <TOKEN FROM PREVIOUS RESPONSE>' \
--data-raw '{
  "user": {
    "id": 0,
    "username": "<USER FROM IDP>",
    "admin": true,
    "active": true,
    "agentUserGroup": {
      "agentUid": 0,
      "agentGid": 0,
      "agentUser": "string",
      "agentGroup": "string"
    },
    "displayName": "<ANY NAME>",
    "modifiedAt": "2023-06-21T14:36:49.980Z",
    "remote": true
  },
  "password": "",
  "isHashed": true
}'
```

--- 

## Adding Users to Pipelines

You can add a `determined` section to your [pipeline specification](/{{%release%}}/build-dags/pipeline-spec/) file and make use of a user via the `$DET_USER` and `$DET_PASS` environment variables. This can be used by the user code that run determined work to talk back to {{%productName%}} and can be used with the Pachyderm SDK. 

```json
{
    "pipeline": {
      "name": "<PIPELINE NAME>"
    },
    "description": "<PIPELINE DESCRIPTION>",
    "input": {
      "pfs": {
        "name": "data",
        "repo": "input",
        "branch": "master",
        "glob": "/",
        "empty_files": true
      }
    },
    "transform": {
      "cmd": ["/bin/sh"],
      "stdin": ["pip install determined && echo $DET_PASS | det user login $DET_USER && det model list -w WORKSPACE-NAME  > /pfs/out/WORKSPACE-NAME.txt"],
      "image": "python:3.8"
    },
    "determined": {
      "workspaces": ["WORKSPACE-NAME"]
    }
  }

```

{{%notice note%}}

These tokens life cycles are scoped to the jobs and are revoked after the job ends.

{{%/notice%}}