---
# metadata #
title: Pipeline Specification
description: Learn about the concept of a pipeline specification, which is a declarative configuration file used to define the behavior of a pipeline.
date:
# taxonomy #
tags: 
series: ["glossary"]
seriesPart:
---
## About 

A pipeline specification is a declarative configuration file used to define the behavior of a {{% productName %}} [pipeline](/{{% release %}}/learn/glossary/pipeline). It is typically written in YAML or JSON format and contains information about the pipeline's input sources, output destinations, Docker image ([user code](/{{% release %}}/learn/glossary/user-code)), command, and other metadata.

In addition to simply transforming your data, you can also achieve more advanced techniques though the pipeline specification, such as:

- [Deferred professing](/{{% release %}}/learn/glossary/deferred-processing)
- [Distributed computing](/{{% release %}}/learn/glossary/distributed-computing)
