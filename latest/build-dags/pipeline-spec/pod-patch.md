---
# metadata # 
title:  Pod Patch PPS
description: Patch a Pod Spec.
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
    "podPatch": string,
    ...
}

```

## Behavior 

`podPatch` is similar to `podSpec` but is applied as a [JSON
Patch](https://tools.ietf.org/html/rfc6902). Note, this means that the
process outlined above of modifying an existing pod spec and then manually
blanking unchanged fields won't work, you'll need to create a correctly
formatted patch by diffing the two pod specs.

