---
# metadata # 
title: Deactivate Authorization
description: Learn how to deactivate Authorization (User Access Management).
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 6
directory: true
---

When you deactivate authorization, all permissions granted to users on {{% productName %}} resources are removed. Everyone that can connect to {{% productName %}} is back to being a clusterAdmin (can access and modify all data in all repos).

## Before You Start 

- You must be logged in as a `clusterAdmin`.

## How to Deactivate Auth 

```s
pachctl auth deactivate
```
