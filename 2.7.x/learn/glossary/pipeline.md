---
# metadata #
title: Pipeline
description: Learn about the concept of a pipeline, which is a primitive responsible for reading data from a specified source, transforming it according to the pipeline specification, and writing the result to an output repo.
date:
# taxonomy #
tags: 
series: ["glossary"]
seriesPart:
---
## About 

A pipeline is a {{% productName %}} primitive responsible for reading data from a specified source, such as a {{% productName %}} repo, transforming it according to the [pipeline specification](/{{%release%}}/learn/glossary/pipeline-specification), and writing the result to an output repo. 

Pipelines subscribe to a branch in one or more input repositories, and every time the branch has a new [commit](/{{%release%}}/learn/glossary/commit), the pipeline executes a job that runs [user code](/{{%release%}}/learn/glossary/user-code) to completion and writes the results to a commit in the output repository.

Pipelines are defined declaratively using a JSON or YAML file (the pipeline specification), which must include the `name`, `input`, and `transform` parameters at a minimum. Pipelines can be chained together to create a directed acyclic graph (DAG).