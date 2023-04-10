---
# metadata # 
title: Commit Set
description: Learn about the concept of a commit set, which is an immutable set of all the commits that resulted from a modification to the system.
glossaryDefinition:  
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series: ["glossary"]
seriesPart:
--- 

## About 

A Commit Set is an immutable set of all the [commits](/{{%release%}}/learn/glossary/commit) that resulted from a modification to the system. The commits within a commit set share a name (i.e. [Global ID](/{{%release%}}/learn/glossary/globalid)). This naming scheme enables you to reference data related to a commit anywhere in their provenance graph by simply naming it.
