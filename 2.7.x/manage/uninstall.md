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
helm uninstall pachyderm 
kubectl delete pvc -l suite=pachyderm 
```

{{%notice note%}}
The name of the Helm release is `pachyderm` by default. If you used a different name, replace `pachyderm` with the name of your Helm release (e.g., `pachd`)
{{%/notice %}}

## Uninstall Pachctl 

```s
brew uninstall @<major>.<minor>
```