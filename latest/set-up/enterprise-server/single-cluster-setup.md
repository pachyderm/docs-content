---
# metadata # 
title: Activate ES for Single-Cluster
description: Learn how to set up a Enterprise server for a single-cluster environment embedded in pachd.
date: 
# taxonomy #
tags: ["enterprise", "deployment", "helm"]
series:
seriesPart:
---

You can register an existing single-cluster {{% productName %}} instance to the embedded [Enterprise Server](/{{%release%}}/set-up/enterprise-server) that comes included with `pachd` using the steps in this guide. Doing so enables you to also activate [authentication](/{{%release%}}/set-up/connectors) and set up [IdP connectors](/{{%release%}}/set-up/connectors). 

## Before You Start

- You must have an Enterprise license key
- You must have an active {{% productName %}} cluster

##  How to Activate Enterprise Server 

1. Open your terminal.
2. Activate Enterprise Server:
```s
echo <enterprise-license-key-value> | pachctl license activate
```
3. Activate Authentication:
```s
pachctl auth activate --enterprise
```
4. [Set up your Identity Provider (IdP)](/{{%release%}}/set-up/connectors/).
