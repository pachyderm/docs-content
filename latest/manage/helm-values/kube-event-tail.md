---
# metadata # 
title:  Kube Event Tail HCVs
description: Deploy lightweight logging for Kubernetes events.
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 8
label: optional
--- 


## About

Kube Event Tail deploys a lightweight app that watches Kubernetes events and echoes them into logs. 

## Values

```yaml
kubeEventTail:
  # Deploys a lightweight app that watches kubernetes events and echos them to logs.
  enabled: true
  # clusterScope determines whether kube-event-tail should watch all events or just events in its namespace.
  clusterScope: false
  image:
    repository: pachyderm/kube-event-tail
    pullPolicy: "IfNotPresent"
    tag: "v0.0.7"
  resources:
    limits:
      cpu: "1"
      memory: 100Mi
    requests:
      cpu: 100m
      memory: 45Mi
```

