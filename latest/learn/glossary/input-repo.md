---
# metadata # 
title: Input Repository 
description: Learn about the concept of an input repository, which is a location where data resides that is used as input for a pipeline.
glossaryDefinition: 
date: 
# taxonomy #
tags:  
series: ["glossary"]
seriesPart:
--- 
## About 

In {{% productName %}}, an input repository is a location where data resides that is used as input for a {{% productName %}} [pipeline](/{{% release %}}/learn/glossary/pipeline). To define an input repository, you need to fill out the `input` attribute in [pipeline's specification](/{{%release%}}/build-dags/pipeline-spec) file.

There are several ways to structure the content of your input repos, such as:

- [Cross](/{{%release%}}/build-dags/pipeline-spec/input-cross)
- [Group](/{{%release%}}/build-dags/pipeline-spec/input-group)
- [PFS](/{{%release%}}/build-dags/pipeline-spec/input-pfs)
- [Join](/{{%release%}}/build-dags/pipeline-spec/input-join)

Once you have defined an input repository, you can use it as the input source for a {{% productName %}} pipeline. The pipeline will automatically subscribe to the branch of the input repository and process any new data that is added to the branch according to the pipeline configuration.