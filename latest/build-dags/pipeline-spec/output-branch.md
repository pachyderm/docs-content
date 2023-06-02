---
# metadata # 
title:  Output Branch PPS
description: Define the branch where the pipeline outputs new commits.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: optional
---

## Spec
This is a top-level attribute of the pipeline spec. 

```s
{
    "pipeline": {...},
    "transform": {...},
    "output_branch": string,
    ...
}

```

## Behavior 

-  Set to `master` by default. 

## When to Use

Use this setting to output commits to `dev` or `testing` branches. 