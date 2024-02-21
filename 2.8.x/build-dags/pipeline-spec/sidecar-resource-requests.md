---
# metadata # 
title:  Sidecar Resource Requests PPS
description: Set the minimum amount of resources that the storage container will reserve.
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
  "sidecarResourceRequests": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
      }
    "disk": string,
  },
  ...
}

```
## Attributes

| Attribute | Description   |
| - | - |
| `cpu`       | The minimum number of CPU cores that the storage container will reserve.                                                     |
| `memory`    | The minimum amount of memory that the storage container will reserve. This can be specified in bytes, or with a unit such as "Mi" or "Gi". |
| `gpu`       | An optional field that specifies the number and type of GPUs that the storage container will reserve.                          |
| `type`      | The type of GPU to use, such as "nvidia" or "amd".                                                                        |
| `number`    | The number of GPUs that the storage container will reserve.                                                                    |
| `disk`      | The minimum amount of disk space that the storage container will reserve. This can be specified in bytes, or with a unit such as "Mi" or "Gi". |


## Behavior 
The `sidecarResourceRequests` field in a {{% productName %}} Pipeline Spec is used to specify the resource requests for the storage container that runs alongside the user container.

In a {{% productName %}} Pipeline, the storage container is used to perform additional tasks alongside the user pipeline container, such as logging, monitoring, or handling external dependencies. By specifying resource requests for this sidecar container, you can ensure that the storage container has enough resources reserved as to not impact the performance of the user container.
