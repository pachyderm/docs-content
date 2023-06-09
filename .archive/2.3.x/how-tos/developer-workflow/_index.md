---
# metadata # 
title:  Developer Workflow
description: Learn how to manage and process data in your CI workflow.
date: 
# taxonomy #
tags: 
series:
seriesPart:
---

In general, the developer workflow for {{%productName%}} involves adding  data to versioned data repositories, creating pipelines to read from those repositories, executing the pipeline's code, and writing the pipeline's output to other data repositories.
Both the data and pipeline can be iterated on independently with {{%productName%}}
handling the code execution according to the pipeline specfication.
The workflow steps are shown below.

![Developer workflow](../../assets/images/d_steps_analysis_pipeline.svg)

## Data Workflow

Adding data to {{%productName%}} is the first step towards building data-driven pipelines. There are multiple ways to add data to a {{%productName%}} repository:

* By using the `pachctl put file` command
* By using a special type of pipeline, such as a [spout](../../concepts/pipeline-concepts/pipeline/spout/) or [cron](../../concepts/pipeline-concepts/pipeline/cron/) 
* By using one of the {{%productName%}}'s [language clients](../../reference/clients/)
* By using a compatible S3 client

For more information, see [Load Your Data Into {{%productName%}}](../basic-data-operations/load-data-into-pachyderm/).

## Pipeline Workflow

The fundamental concepts of {{%productName%}} are very powerful, but the manual build steps mentioned in the [pipeline workflow](./working-with-pipelines) can become cumbersome during rapid-iteration development cycles. We've created a few helpful developer workflows and tools to automate steps that are error-prone or repetitive:

* The [push images flag](./push-images-flag) or `--push-images` is a optional flag that can be passed to the `create` or `update` pipeline command. This option is most useful when you need to customize your Docker image or are iterating on the Docker image and code together, since it tags and pushes the image before updating the pipeline. 
* [CI/CD Integration](./ci-cd-integration) provides a way to incorporate {{%productName%}} functions into the CI process. This is most useful when working with a complex project or for code collaboration. 

