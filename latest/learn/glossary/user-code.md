---
# metadata # 
title: User Code
description: Learn about the concept of User Code, which is custom code that users write to process their data in pipelines.
date: 
# taxonomy #
tags: 
series: ["glossary"]
seriesPart:
--- 

In {{% productName %}}, user code refers to the custom code that users write to process their data in [pipelines](/{{% release %}}/learn/glossary/pipeline). User code can be written in any language and can use any libraries or frameworks.

{{% productName %}} allows users to define their user code as a Docker image, which can be pushed to a registry and referenced using the [Transform](/{{%release%}}/build-dags/pipeline-spec/transform) attribute of the [pipeline's specification](/{{%release%}}/build-dags/pipeline-spec). The user code image contains the necessary dependencies and configuration for the code to run in {{% productName %}}'s distributed computing environment.

User code can be defined for each pipeline stage in {{% productName %}}, allowing users to chain together multiple processing steps and build complex data pipelines. {{% productName %}} also provides a Python library for building pipelines, which simplifies the process of defining user code and specifying pipeline stages.