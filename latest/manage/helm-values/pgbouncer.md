---
# metadata # 
title:  PGBouncer HCVs
description: Deploy a lightweight connection pooler for PostgreSQL.
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 9 
---

## About

The PGBouncer section configures a PGBouncer Postgres connection pooler.

## Values

```s
pgbouncer:
  service:
    type: ClusterIP
  annotations: {}
  priorityClassName: ""
  nodeSelector: {}
  tolerations: []
  image:
    repository: pachyderm/pgbouncer
    tag: 1.16.2
  resources:
    {}
    #limits:
    #  cpu: "1"
    #  memory: "2G"
    #requests:
    #  cpu: "1"
    #  memory: "2G"
  # maxConnections specifies the maximum number of concurrent connections into pgbouncer.
  maxConnections: 100000
  # defaultPoolSize specifies the maximum number of concurrent connections from pgbouncer to the postgresql database.
  defaultPoolSize: 80
```