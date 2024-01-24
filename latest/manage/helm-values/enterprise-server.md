---
# metadata # 
title:  Enterprise Server HCVs
description: Configure the Enterprise Server for production deployments.
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 4
label: Optional
--- 

## About

[Enterprise Server](/{{%release%}}/set-up/enterprise-server) is a production management layer that centralizes  the licensing registration of multiple {{% productName %}} clusters for Enterprise use and the setup of user authorization/authentication via [OIDC](/{{%release%}}/manage/helm-values/oidc).

## Values 

```yaml
enterpriseServer:
  enabled: false
  affinity: {}
  annotations: {}
  tolerations: []
  priorityClassName: ""
  nodeSelector: {}
  service:
    type: ClusterIP
    apiGRPCPort: 31650
    prometheusPort: 31656
    oidcPort: 31657
    identityPort: 31658
    s3GatewayPort: 31600
  # There are three options for TLS:
  # 1. Disabled
  # 2. Enabled, existingSecret, specify secret name
  # 3. Enabled, newSecret, must specify cert, key and name
  tls:
    enabled: false
    secretName: ""
    newSecret:
      create: false
      crt: ""
      key: ""
  resources:
    {}
    #limits:
    #  cpu: "1"
    #  memory: "2G"
    #requests:
    #  cpu: "1"
    #  memory: "2G"
  # podLabels specifies labels to add to the pachd pod.
  podLabels: {}
  clusterDeploymentID: ""
  image:
    repository: "pachyderm/pachd"
    pullPolicy: "IfNotPresent"
    # tag defaults to the chart’s specified appVersion.
    tag: ""
```

