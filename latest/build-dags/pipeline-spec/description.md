---
# metadata # 
title:  Description PPS
description: Display meaningful information about your pipeline.
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
    "description": string,
    ...
}

```

## Behavior 

`description` is displayed in your pipeline details when viewed from pachCTL or console.

## When to Use

It's recommended to always provide meaningful descriptions to your {{% productName %}} resources.
