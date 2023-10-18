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

You should be familiar with the [Pachyderm Pipeline Specification (PPS)](/{{%release%}}/build-dags/pipeline-spec).

## Set Global Config Defaults for Your Cluster

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

{{% notice note %}}
Setting global defaults does not trigger existing pipelines to regenerate automatically unless the pipeline's resources have been affected (e.g., if `cpu` was doubled.) 
{{% /notice %}}

## View Global Config Defaults for Your Cluster

1. Open a terminal window.
2. Input the following command:
   ```s
   pachctl inspect defaults --cluster | jq
   ```
## Override Global Config Defaults for a Pipeline 

Users can override global defaults in their pipeline specs when necessary. For example, let's say that you set a global default for [resource requests](/{{%release%}}/build-dags/pipeline-spec/resource-request/) to look like the following:

```s
{
  "resource_requests": {
    "cpu": 1,
    "memory": "256Mi",
    "disk": "1Gi",
  },
}
```

A user could disable needing any CPU by setting the following in their pipeline spec:

```s
{
  "resource_requests": {
    "cpu": null,
  },
}
```

Any keys not specified in the pipeline spec will use the global defaults. 