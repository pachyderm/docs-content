---
# metadata # 
title:  Set Output Branch
description: Learn how to use an output branch to defer processing.
date: 
# taxonomy #
tags: ["deferred processing", "branches"]
series:
seriesPart:
weight: 
---

You can defer processing operations for data in output repositories by configuring an [output branch](/{{%release%}}/build-dags/pipeline-spec/output-branch) field in your [pipeline specification](/{{%release%}}/build-dags/pipeline-spec). This allows you to accumulate data in an output branch before processing it. 

## How to Defer Processing in an Output Branch


1. In the pipeline specification, add the `output_branch` field with
   the name of the branch in which you want to accumulate your data
   before processing:

   ```s
   "output_branch": "staging"
   ```

2. When you want to process data, run:

   ```s
   pachctl create branch pipeline@master --head staging
   ```