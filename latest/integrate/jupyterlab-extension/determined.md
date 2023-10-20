---
# metadata # 
title: Run in Determined
description: Learn how to run the JupyterLab Mount Extension inside of Determined.
date: 
# taxonomy #
tags: ["integrations", "jupyterlab", "notebooks", "docker", "determined"]
series:
seriesPart:
weight: 1
beta: true 
hidden: false 
---

You can run the {{%productName%}} Jupyterlab Extension inside of [Determined](https://docs.determined.ai/latest/). 

## Before You Start 

- You must have Determined `0.23.4` or greater installed 
- You must have {{%productName%}} JupyterLab Extension `2.7.0` or greater installed


## How to Run the Extension in Determined

1. Open Determined.
2. Navigate to the Notebook Launcher.
3. Click **Show Full Config**.
4. Replace the `podSpec` section with the following:
   ```s
   podSpec:
       spec:
         containers:
         - name: determined-container
           securityContext:
             privileged: true
   ``` 
5. Update the `cpu` image to the following: `pachderm/notebooks-user:v{{%latestPatchNumber%}}`

## Limitations 

- GPUs are not yet supported