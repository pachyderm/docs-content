---
# metadata # 
title: Output Repository
description: Learn about the concept of an output repo, which is a repository where the results of a pipeline's processing are stored after being transformed by the provided user code.
date: 
# taxonomy #
tags:  
series: ["glossary"]
seriesPart:
--- 

## About 

In {{% productName %}}, an output repo is a repository where the results of a pipeline's processing are stored after being transformed by the provided [user code](/{{% release %}}/learn/glossary/user-code). Every pipeline automatically creates an output repository with the same name as the pipeline.

When a pipeline runs, it creates a new [commit](/{{% release %}}/learn/glossary/commit) in the output repository with the results of the processing. The commit contains a set of files that represent the output of the pipeline. Each commit in the output repository corresponds to a [job](/{{% release %}}/learn/glossary/job) that was run to generate that output.

An output repository can be created or deleted using a pachctl CLI command or the {{% productName %}} API. 