---
# metadata # 
title: Draw a Pipeline
description: Learn how to draw a pipeline using the PachCTL draw command or Console. 
date: 
# taxonomy #
tags: ["pipelines"]
series:
seriesPart:
---

Sometimes it's easier to share and reason about pipelines when you can see them drawn out. You can draw ASCII pipelines via PachCTL, or download highly detailed pipeline canvases (in the form of SVGs) from Console.

## How to Draw a Pipeline

{{<stack type="wizard">}}
{{% wizardRow id="Tool"%}}
{{% wizardButton option="PachCTL CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}

{{% wizardResults  %}}

{{% wizardResult val1="tool/pachctl-cli"%}}
```s
pachctl draw pipeline <pipeline-name>
```

Example output:

```s
       +-----------+
       |housing_d..|
       +-----------+
             |            
             |            
             |            
             |            
             |            
       +-----------+
       |regression |
       +-----------+
```
{{% /wizardResult %}}

{{% wizardResult val1="tool/console"%}}

1. Open the Console UI.
2. Navigate to the project containing the pipeline.
3. Select **Download Canvas**. 

An SVG version of your DAG will be saved to your computer.

![draw-pipeline-canvas](/images/console/download-canvas.gif)

{{% /wizardResult %}}
{{% /wizardResults %}}
{{</stack>}}

