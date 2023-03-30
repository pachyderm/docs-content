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

In {{% productName %}}, an input repository is a location where data resides that is used as input for a {{% productName %}} [pipeline](TBD). To define an input repository, you need to fill out the `input` attribute in [pipeline's specification](TBD) file.

There are several ways to structure the content of your input repos, such as:

- [Cross](TBD)
- [Group](TBD)
- [PFS](TBD)
- [Join](TBD)

Once you have defined an input repository, you can use it as the input source for a {{% productName %}} pipeline. The pipeline will automatically subscribe to the branch of the input repository and process any new data that is added to the branch according to the pipeline configuration.