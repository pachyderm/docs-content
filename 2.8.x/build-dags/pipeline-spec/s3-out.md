---
# metadata # 
title:  s3 Out PPS
description:  Write results out to an S3 gateway endpoint.
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
    "s3Out": bool,
    ...
}

```

## Behavior 

`s3Out` allows your pipeline code to write results out to an S3 gateway
endpoint instead of the typical `pfs/out` directory. When this parameter
is set to `true`, {{% productName %}} includes a sidecar S3 gateway instance
container in the same pod as the pipeline container. The address of the
output repository will be `s3://<output_repo>`. 

If you want to expose an input repository through an S3 gateway, see
`input.pfs.s3` in [PFS Input](/{{%release%}}/build-dags/pipeline-spec/input-pfs). 

## When to Use 

You should use the s3 Out attribute when you'd like to access and store the results of your {{% productName %}} transformations externally. 

