---
# metadata # 
title: Uninstall {{%productName%}}
description: Learn how to uninstall {{%productName%}}.
date: 
# taxonomy #
tags: 
series:
seriesPart:
---

## Uninstall {{%productName%}}

```s
helm uninstall pachd 
kubectl delete pvc -l suite=pachyderm 
```

## Uninstall Pachctl 

```s
brew uninstall @<major>.<minor>
```