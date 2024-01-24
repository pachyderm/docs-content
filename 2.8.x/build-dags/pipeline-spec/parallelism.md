---
# metadata # 
title:  Parallelism Spec PPS
description: Define the number of workers used in parallel. 
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: Optional
weight: 1
---

## Spec
This is a top-level attribute of the pipeline spec. 

```s
{
  "pipeline": {...},
  "transform": {...},
  "parallelismSpec": {
    "constant": int
  },
  ...
}

```

## Behavior 


{{% productName %}} starts the number of workers that you specify. For example, set
`"constant":10` to use 10 workers.

- The default value is `1`

## When to Use 

{{% notice warning  %}}
Because spouts and services are designed to be single instances, do not
modify the default `parallism_spec` value for these pipelines.

{{% /notice %}}