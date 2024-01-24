---
# metadata # 
title:  Set Project Defaults
description: Learn how to set project defaults for pipeline spec settings.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 1
---

You can set defaults for your project's pipelines from the Console UI that are passed down to all pipeline specs. These defaults provide a consistent experience for your data scientists and help manage your project.

## Before You Start

- You must have a running {{%productName%}} cluster and access to the Console UI, either locally our via [IdP](/{{%release%}}/get-started/connect-to-existing/)
- Read the [Global Config](/{{%release%}}/set-up/global-config) for information about Cluster Defaults

## How to Set Project Defaults

1. Log in to Console
2. Navigate to the Project Dashboard homepage.
3. Scroll to the project you wish to add defaults to and select **View Project**.
4. Select **Project Defaults** from the sidebar.
5. Input your desired default [Pipeline Specification (PPS)](/{{%release%}}/build-dags/pipeline-spec) settings in JSON format. 
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
6. Optionally select the **Prettify** button to make the JSON more readable.
7. Select **Continue**.
8. Choose from one of the following options:
    - **Save Project Defaults**
      - Only new and edited pipelines apply the new defaults 
      - No pipeline regeneration or datum reprocessing occurs
    - **Save Project Defaults and Regenerate Pipelines**
      - Only pipelines with impacted specs are regenerated 
      - Previously processed datums are not reprocessed
    - **Save Project Defaults, Regenerate Pipelines, and Reprocess Datums**
      - Only pipelines with impacted specs are regenerated
      - Previously processed datums are reprocessed
9. Select **Save**.

{{<youtube ZmXt6ao-JrM>}}


## How to View Project Defaults Applied to a Pipeline

In addition to viewing Project Defaults directly from the sidebar inside a project, you can also view them from a pipeline.

1. Log in to Console.
2. Scroll to a project you wish to inspect and select **View Project**.
3. Select a pipeline from the **DAG**.
4. Select the **Pipeline Actions**  dropdown and choose **Update Pipeline**
5. Select the **Project Defaults** tab.

{{%notice tip%}}
Project Defaults that have been overridden by user inputs have a user icon next to them in the **Effective Spec** view.
{{%/notice%}}
