---
# metadata # 
title: Distributed Computing
description: Learn about the concept of distributed computing. 
date: 
# taxonomy #
tags:  ["data-operations", "pipelines"]
series:
seriesPart:
--- 

Distributing your computations across multiple workers
is a fundamental part of any big data processing.
When you build production-scale pipelines, you need
to adjust the number of workers and resources that are
allocated to each job to optimize throughput.

A {{%productName%}} worker is an identical Kubernetes pod that runs
the Docker image that you specified in the
[pipeline spec](../../../reference/pipeline-spec/). Your analysis code
does not affect how {{%productName%}} distributes the workload among workers.
Instead, {{%productName%}} spreads out the data that needs to be processed
across the various workers and makes that data available for your code.

When you create a pipeline, {{%productName%}} spins up worker pods that
continuously run in the cluster waiting for new data to be available
for processing. You can change this behavior by setting `"autoscaling" :true`.
Therefore, you do not need to recreate and
schedule workers for every new job.

For each job, all the datums are queued up and then distributed
across the available workers. When a worker finishes processing
its datum, it grabs a new datum from the queue until all the datums
complete processing. If a worker pod crashes, its datums are
redistributed to other workers for maximum fault tolerance.

The following animation shows how distributed computing works:

![Distributed computing basics](/images/distributed-computing101.gif)

In the diagram above, you have three {{%productName%}} worker pods that
process your data. When a pod finishes processing a datum,
it automatically takes another datum from the queue to process it.
Datums might be different in size and, therefore, some of them might be
processed faster than others.

Each datum goes through the following processing phases inside a {{%productName%}}
worker pod:

| Phase       | Description |
| ----------- | ----------- |
| Downloading | The {{%productName%}} worker pod downloads the datum contents <br>into {{%productName%}}. |
| Processing  | The {{%productName%}} worker pod runs the contents of the datum <br>against your code. |
| Uploading   | The {{%productName%}} worker pod uploads the results of processing <br>into an output repository. |

When a datum completes a phase, the {{%productName%}} worker moves it to the next
one while another datum from the queue takes its place in the
processing sequence.

The following animation displays what happens inside a pod during
the datum processing:

![Distributed processing internals](/images/distributed-computing102.gif)

## Parallelism

You can control the number of worker pods that {{%productName%}} runs in a
pipeline by defining the `parallelism` parameter in the
[pipeline specification](../../../reference/pipeline-spec/).

### example
```json
"parallelism_spec": {
    // Exactly one of these two fields should be set
    "constant": int
```

{{%productName%}} has the following parallelism strategies that you
can set in the pipeline spec:

| Strategy    | Description        |
| ----------- | ------------------ |
| constant    | {{%productName%}} starts the specified number of workers. For example, <br> if you set `"constant":10`, {{%productName%}} spreads the computation workload among ten workers. |

By default, {{%productName%}} sets `parallelism` to `“constant": 1`, which means
that it spawns one worker per Kubernetes node for this pipeline.

## Autoscaling 

Pipelines that will not have a constant flow of data to process should use the `autoscaling` feature by setting `"autoscaling": true` in the pipeline spec. 

Doing so will cause the pipeline **to go into standby when there is nothing for the workers to do**. In standby a pipeline will have no workers and will consume no resources; it will just wait for data to come in for it to process.

When data does come in, the pipeline will exit its standby status and spin up workers to process the new data. Initially, a single worker will spin up and layout a distributed processing plan for the job. Then it will start working on the job, and if there is more work that could happen in parallel, it will spin up more workers to run in parallel, up to the limit defined by the `parallelism_spec`.

Multiple jobs can run in parallel and cause new workers to spin up. For example, if a job comes in with a single datum, it will cause a single worker to spin up. If another job with a single datum comes in while the first job is still running, another worker will spin up to work on the second job. Again this is bounded by the limit defined in the `parallelism_spec`.

One limitation of autoscaling is that **it cannot dynamically scale down**. Suppose a job with many datums is near completion, only one worker is still working while the others are idle. {{%productName%}} does not yet have a way for the idle workers to steal work, and there are a few issues that prevent us from spinning down the idle workers. Kubernetes does not have a good way to scale down a controller and specify which pods should be killed, so scaling down may kill the worker pod that is still doing work. This means another worker will have to restart that work from scratch, and the job will take longer. Additionally, we want to keep the workers around to participate in the **distributed merge process** at the end of the job.

{{% notice note %}}
See Also:
* [Glob Pattern](../../pipeline-concepts/datum/glob-pattern/)
* [Pipeline Specification](../../../reference/pipeline-spec/)
{{% /notice %}}