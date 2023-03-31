---
# metadata # 
title:  Pachyderm Worker
description: Learn about the concept of a Pachyderm worker.
date: 
# taxonomy #
tags:  
series: ["glossary"]
seriesPart:
--- 

{{% productName %}} workers are kubernetes pods that run the docker image (your user code) specified in the pipeline specification. When you create a pipeline, {{% productName %}} spins up workers that continuously run in the cluster, waiting for new data to process. 

Each datum goes through the following processing phases inside a {{% productName %}}
worker pod:

| Phase       | Description |
| ----------- | ----------- |
| Downloading | The {{% productName %}} worker pod downloads the datum contents <br>into {{% productName %}}. |
| Processing  | The {{% productName %}} worker pod runs the contents of the datum <br>against your code. |
| Uploading   | The {{% productName %}} worker pod uploads the results of processing <br>into an output repository. |

![Distributed processing internals](/images/distributed-computing102.gif) 