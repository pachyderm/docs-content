---
# metadata # 
title: Inspect a Pipeline
description: Learn how to inspect a pipeline using the pachctl inspect command or console. 
date: 
# taxonomy #
tags: ["pipelines"]
series:
seriesPart:
---

You can inspect a [pipeline](/{{%release%}}/learn/glossary/pipeline) via PachCTL or the Console. When you inspect a pipeline, you can see key details such as its input configuration, output configuration, and transformation image/command details.

## How to Inspect a Pipeline

{{<stack type="wizard">}}
{{% wizardRow id="Tool"%}}
{{% wizardButton option="PachCTL CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}

{{% wizardResults  %}}

{{% wizardResult val1="tool/pachctl-cli"%}}
```s
pachctl inspect pipeline <pipeline-name>
```

Example output:

```json
Name: regression
Description: A pipeline that trains produces a regression model for housing prices.
Created: 4 weeks ago 
State: running
Reason: 
Workers Available: 1/1
Stopped: false
Parallelism Spec: <nil>


Datum Timeout: (duration: nil Duration)
Job Timeout: (duration: nil Duration)
Input:
{
  "pfs": {
    "project": "standard-ml-tutorial",
    "name": "housing_data",
    "repo": "housing_data",
    "repoType": "user",
    "branch": "master",
    "glob": "/*"
  }
}

Output Branch: master
Transform:
{
  "image": "lbliii/housing-prices:latest",
  "cmd": [
    "python",
    "regression.py",
    "--input",
    "/pfs/housing_data/",
    "--target-col",
    "MEDV",
    "--output",
    "/pfs/out/"
  ],
  "datumBatching": true
}
```
{{% /wizardResult %}}

{{% wizardResult val1="tool/console"%}}

1. Open the Console UI.
2. Navigate to the project containing the pipeline.
3. From the DAG view, select the pipeline name. A slideout panel appears with three tabs you can inspect: **Job Overview**, **Pipeline Info**, and **Spec**.

![inspect pipelines in console](/images/console/inspect-pipeline.gif)

{{% /wizardResult %}}
{{% /wizardResults %}}
{{</stack>}}