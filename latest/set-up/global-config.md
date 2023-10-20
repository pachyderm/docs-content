---
# metadata # 
title:  Global Config
description: Learn how to set global defaults for your cluster, projects (coming soon), and pipelines.
date: 
# taxonomy #
tags: ["cluster", "projects", "pipelines"]
series:
seriesPart:
directory: true
weight: 
--- 
You can set global defaults for your cluster that are passed down to all pipeline specs. These defaults provide a consistent experience for your data scientists and help manage your cluster. 

## Before You Start

- You must have a running {{%productName%}} cluster
- You should be familiar with the [Pachyderm Pipeline Specification (PPS)](/{{%release%}}/build-dags/pipeline-spec)

## Cluster Defaults 

### Set Global Cluster Defaults


{{< stack type="wizard" >}}
{{% wizardRow id="Tool" %}}
{{% wizardButton option="CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}
{{% wizardResults %}}
{{% wizardResult val1="tool/cli" %}}

```s
pachctl update defaults --cluster <<EOF
{
  "createPipelineRequest": {
    "resourceRequests": {
      "cpu": 1,
      "memory": "256Mi",
      "disk": "1Gi"
    },
    "resourceLimits": {
      "cpu": 1,
      "memory": "256Mi",
      "disk": "1Gi"
    }
  }
}
EOF
```

{{% /wizardResult%}}
{{% wizardResult val1="tool/console" %}}

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

{{% /wizardResult%}}
{{% /wizardResults%}}
{{</stack>}}
 

{{% notice note %}}
Setting global defaults does not trigger existing pipelines to regenerate automatically unless the `--regenerate` flag is set.
{{% /notice %}}

### View Global Cluster Defaults

1. Open a terminal window.
2. Input the following command:
   ```s
   pachctl inspect defaults --cluster | jq
   ```
  
### Override Global Cluster Defaults

Users can override global defaults in their pipeline specs when necessary. For example, let's say that you set a global default for [resource requests](/{{%release%}}/build-dags/pipeline-spec/resource-request/) to look like the following:

```s
{
  "resourceRequests": {
    "cpu": 1,
    "memory": "256Mi",
    "disk": "1Gi",
  },
}
```

A user could disable needing any CPU by setting the following in their pipeline spec:

```s
{
  "resourceRequests": {
    "cpu": null,
  },
}
```

Any keys not specified in the pipeline spec will use the global defaults. 