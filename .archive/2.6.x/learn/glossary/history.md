---
# metadata # 
title: History
description: Learn about the concept of history (version control), which is a record of the changes made to data over time.
glossaryDefinition: The collective record of version-controlled commits for pipelines and jobs.
date: 
# taxonomy #
tags:  
series: ["glossary"]
seriesPart:
--- 
## About 

History in {{% productName %}} is a record of the changes made to data over time, stored as a series of immutable snapshots ([commits](/{{%release%}}/learn/glossary/commit)) that can be accessed using [ancestry syntax](/{{%release%}}/learn/glossary/ancestry-syntax) and [branch](/{{%release%}}/learn/glossary/branch) pointers. Each commit has a parentage structure, where new commits inherit content from their parents, creating a chain of commits that represents the full history of changes to the data. 
