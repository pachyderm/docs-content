---
# metadata # 
title:  Spec Commit PPS
description: This attribute is auto-generated and is not configurable.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: auto-generated
weight: 1
---

## Spec 
This is a top-level attribute of the pipeline spec. 

```s
{
  "pipeline": {...},
  "transform": {...},
  "spec_commit": {
    "option": false,
    "branch": {
      "option": false,
      "repo": {
        "option": false,
        "name": string,
        "type": string,
        "project":{
          "option": false,
          "name": string,
        },
      },
      "name": string
    },
    "id": string,
  },
  ...
}

```

## When to Use 

You do not need to ever configure this attribute; its details are auto-generated.
