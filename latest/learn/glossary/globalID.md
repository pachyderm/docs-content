---
# metadata # 
title: Global Identifier
description: Learn about the concept of a global identifier, which is a unique identifier for a DAG.
date: 
# taxonomy #
tags:  ["data-operations", "pipelines"]
series: ["glossary"]
seriesPart:
--- 
## About 

Global Identifiers provide a simple way to follow the [provenance](/{{% release %}}/learn/glossary/provenance) or [subvenance](/{{% release %}}/learn/glossary/subvenance) of a DAG. Commits and jobs sharing the same Global ID represent a logically-related set of objects.

When a new commit is made, {{% productName %}} creates an associated commit ID; all resulting downstream **commits** and **jobs** in your DAG will then share that same ID (the Global Identifier). 

The following diagram illustrates the global commit and its various components:
![global_commit_after_putfile](/images/global_commit_after_putfile.png)

## Actions

1. [List all global commits & jobs](/{{%release%}}/build-dags/provenance-operations/list-globals)
2. [List all sub-commits associated with a global ID](/{{%release%}}/build-dags/provenance-operations/list-sub-commits)
3. [Track provenance downstream, live](/{{%release%}}/build-dags/provenance-operations/track-downstream)
4. [Squash & delete commits](/{{%release%}}/prepare-data/removing-data)



