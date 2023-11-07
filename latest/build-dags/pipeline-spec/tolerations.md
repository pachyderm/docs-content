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

Pipeline tolerations enable you to run a pipeline on a node that has a taint.

- You can have as many tolerations as you'd like, or none at all. 
- Taints behave almost exactly like the Kuberentes API, with the exception of some enums such as `Exists` and `DoesNotExist` being replaced with Golang equivalents like `EXISTS` and `DOES_NOT_EXIST`. 

### Example of Tainting a Node

```s
kubectl taint node example dedicated:NoSchedule
```

