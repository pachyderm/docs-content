---
# metadata # 
title: Uninstall
description: Learn how to uninstall our platform.
date: 
# taxonomy #
tags: 
series:
seriesPart:
directory: true
weight: 21
---

## Uninstall {{% productName %}}

```s
helm uninstall pachd 
kubectl delete pvc -l suite=pachyderm 
```

## Uninstall Pachctl 

```s
brew uninstall @<major>.<minor>
```