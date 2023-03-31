---
# metadata #
title: Pipeline Inputs
description: Learn about the concept of a pipeline input, which is the source of the data that the pipeline reads and processes.
date:
# taxonomy #
tags: 
series: ["glossary"]
seriesPart:
---

In {{% productName %}}, pipeline inputs are defined as the source of the data that the [pipeline](../pipeline) reads and processes. The input for a pipeline can be a {{% productName %}} repository ([input repo](../input-repo)) or an external data source, such as a file in a cloud storage service.

To define a pipeline input, you need to specify the source of the data and how the data is organized. This is done in the `input` section of the [pipeline specification](../../../build-dags/pipeline-spec) file, which is a YAML or JSON file that defines the configuration of the pipeline.

The input section can contain one or more input sources, each specified as a separate block. There are several types of pipeline inputs available, such as:

- [PFS](../../../build-dags/pipeline-spec/input-pfs)
- [Cron](../../../build-dags/pipeline-spec/input-cron)
- [Egress (DB)](../../../build-dags/pipeline-spec/egress)
- [Egress (Storage)](../../../build-dags/pipeline-spec/egress)
- [Service](../../../build-dags/pipeline-spec/service)
- [Spout](../../../build-dags/pipeline-spec/spout)
- [S3](../../../build-dags/pipeline-spec/s3-out)