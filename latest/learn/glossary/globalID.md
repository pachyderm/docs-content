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

Global Identifiers provide a simple way to follow the [provenance](../provenance) or [subvenance](../subvenance) of a DAG. Commits and jobs sharing the same Global ID represent a logically-related set of objects.

When a new commit is made, {{% productName %}} creates an associated commit ID; all resulting downstream **commits** and **jobs** in your DAG will then share that same ID (the Global Identifier). 

## Actions

You can perform the following actions with a Global ID:

1. [List all global commits & jobs](../../../build-dags/provenance-operations/list-globals)
2. [List all sub-commits associated with a global ID](../../../build-dags/provenance-operations/list-sub-commits)
3. [Track provenance downstream, live](../../../build-dags/provenance-operations/track-downstream)
4. [Squash & delete commits](../../../prepare-data/removing-data)



