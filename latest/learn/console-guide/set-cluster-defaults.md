---
# metadata # 
title:  Set Cluster Defaults
description: Learn how to set cluster defaults for pipeline spec settings.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 1
---

You can set global defaults for your cluster from the Console UI that are passed down to all pipeline specs. These defaults provide a consistent experience for your data scientists and help manage your cluster.

## Before You Start

- You must have a running {{%productName%}} cluster and access to the Console UI, either locally our via IdP
- Read the [Global Config](/{{%release%}}/set-up/global-config) setup guide for context on global defaults outside the scope of the Console UI.

## How to Set Cluster Defaults

1. Log in to Console
2. Navigate to the Project Dashboard homepage.
3. Select **Cluster Defaults**.
4. Input your desired default [Pipeline Specification (PPS)](/{{%release%}}/build-dags/pipeline-spec) settings in JSON format. 
    ```s
   {
     "createPipelineRequest": {
       "resourceRequests": {
         "cpu": 1,
         "memory": "256Mi",
         "disk": "1Gi"
       },
       "sidecarResourceRequests": {
         "cpu": 1,
         "memory": "256Mi",
         "disk": "10Gi"
       }
     }
   }
    ```
5. Optionally select the **Prettify** button to make the JSON more readable.
6. Select **Continue**.
7. Choose from one of the following options:
    - **Save Cluster Defaults**
      - Only new and edited pipelines apply the new defaults 
      - No pipeline regeneration or datum reprocessing occurs
    - **Save Cluster Defaults and Regenerate Pipelines**
      - Only pipelines with impacted specs are regenerated 
      - Previously processed datums are not reprocessed
    - **Save Cluster Defaults, Regenerate Pipelines, and Reprocess Datums**
      - Only pipelines with impacted specs are regenerated
      - Previously processed datums are reprocessed
8. Select **Save**.

## How to View Cluster Defaults Applied to a Pipeline

In addition to viewing Cluster Defaults from the Project Dashboard page, you can also view them from a pipeline.

1. Log in to Console.
2. Scroll to a project you wish to inspect and select **View Project**.
3. Select a pipeline from the **DAG**.
4. Select the **Update Pipeline**  pencil icon. 
5. Select the **Cluster Defaults** tab.

{{%notice tip%}}
Cluster Defaults that have been overridden by user inputs have a user icon next to them in the **Effective Spec** view.
{{%/notice%}}