---
# metadata # 
title:  Tolerations PPS
description: Learn how to use tolerations in PPS to allow node taints.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: optional
weight: 1
---

## Spec 
This is a top-level attribute of the pipeline spec. 

```s
{
    "pipeline": {...},
    "transform": {...},
    "tolerations": [
    {
      "key": "dedicated",
      "operator": "EXISTS",
      "effect": "NO_SCHEDULE"
    }
  ],
    ...
}

```

## Behavior

Tolerations are used to allow a node to be tainted. This is useful for running a pipeline on a node that has a taint.

```s
kubectl taint node example dedicated:NoSchedule
```

- You can have as many tolerations as you'd like, including 0. 
- Behaves almost exactly like the Kuberentes API, with the exception of some enums such as `Exists` and `DoesNotExist` being replaced with Golang equivalents like `EXISTS` and `DOES_NOT_EXIST`. 


## When to Use 

Use tolerations when you want to run a pipeline on a node that has a taint. 