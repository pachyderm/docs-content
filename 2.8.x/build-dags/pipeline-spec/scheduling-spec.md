---
# metadata # 
title:  Scheduling Spec PPS
description:  Define how the pipeline pods should be scheduled.
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
    "schedulingSpec": {
        "nodeSelector": {string: string},
        "priorityClassName": string
    },
    ...
}

```

## Attributes 

|Attribute| Description|
|-|-|
|`nodeSelector`|Allows you to select which nodes your pipeline will run on. Refer to the [Kubernetes docs](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) on node selectors for more information about how this works.|
|`priorityClassName`|Allows you to select the priority class for the pipeline, which is how Kubernetes chooses to schedule and de-schedule the pipeline. Refer to the [Kubernetes docs](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) on priority and preemption for more information about how this works.|

## Behavior 

- When you include a `nodeSelector` in the `schedulingSpec`, it tells Kubernetes to schedule the pipeline's Pods on nodes that match the specified key-value pairs. For example, if you specify `{"gpu": "true"}` in the `nodeSelector`, Kubernetes will only schedule the pipeline's Pods on nodes that have a label `gpu=true`. This is useful when you have specific hardware or other node-specific requirements for your pipeline.

- When you specify a `priorityClassName` in the `schedulingSpec`, it tells Kubernetes to assign the specified priority class to the pipeline's Pods. The priority class determines the priority of the Pods relative to other Pods in the cluster, and can affect the order in which Pods are scheduled and the resources they are allocated. For example, if you have a high-priority pipeline that needs to complete as quickly as possible, you can assign it a higher priority class than other Pods in the cluster to ensure that it gets scheduled and allocated resources first.

## When to Use

You should use the `schedulingSpec` field in a {{% productName %}} Pipeline Spec when you have specific requirements for where and when your pipeline runs. This can include requirements related to hardware, node labels, scheduling priority, and other factors.

Example requirements:

- **Hardware requirements**: If your pipeline requires specific hardware, such as GPUs, you can use the nodeSelector field to ensure that your pipeline runs on nodes that have the necessary hardware.

- **Node labels**: If you have specific requirements for node labels, such as data locality, you can use the nodeSelector field to schedule your pipeline on nodes with the appropriate labels.

- **Priority**: If you have a high-priority pipeline that needs to complete as quickly as possible, you can use the priorityClassName field to assign a higher priority class to your pipeline's Pods.

- **Resource constraints**: If your pipeline requires a large amount of resources, such as CPU or memory, you can use the nodeSelector field to ensure that your pipeline runs on nodes with sufficient resources.