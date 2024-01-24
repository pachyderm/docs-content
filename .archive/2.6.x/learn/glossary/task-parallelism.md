---
# metadata # 
title: Task Parallelism
description: Learn about the concept of task parallelism.
glossaryDefinition: 
date: 
# taxonomy #
tags: ["concepts", "parallelism"]
series: ["glossary"]
seriesPart:
mermaid: true
--- 

## About 

Task parallelism refers to a parallel computing technique where multiple tasks within a directed acyclic graph (DAG) or pipeline are executed simultaneously on different computing resources. In task parallelism, the focus is on executing different tasks in parallel rather than parallelizing a single task. This means that each task in the DAG/pipeline is executed independently of other tasks, allowing for efficient use of resources and faster completion of the overall DAG/pipeline. Task parallelism is often used in data processing pipelines or workflows where tasks can be executed in parallel without any dependency on each other.