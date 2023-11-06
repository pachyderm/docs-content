---
# metadata # 
title: VS Code Intellisense
description: Learn how to add intellisense to VS Code for Pachyderm pipelines.
date: 
# taxonomy #
tags: ["integrations", "intellisense", "VS Code"]
series:
seriesPart:
weight: 
beta: false 
directory: true
---

You can draft [Pipeline Specifications (PPS)](/{{%release%}}/build-dags/pipeline-spec/) in JSON or YAML in VS Code with the help of intelligent code completion. This guide will show you how to add intellisense to VS Code for Pachyderm pipelines. 

Once installed, add `.pipeline.json` or `.pipeline.yaml` to the end of your file name and you will have access to intellisense.

## Before You Start

- You must have VS Code installed on your local machine.

## How to Add Intellisense to VS Code

### JSON 

1. Open VS Code.
2. Navigate to Code > Profiles (Default) > Show Profile Contents.
3. Open the `settings.json` file.
4. Add the following to your configuration:
    ```json
    "json.schemas": [
    {
      "fileMatch": ["*.pipeline.json"],
      "url": "https://raw.githubusercontent.com/pachyderm/pachyderm/master/src/internal/jsonschema/pps_v2/CreatePipelineRequest.schema.json"
    }
   ]
    ```
    {{<youtube zSt0lIeYrtY>}}

Now all files with the `.pipeline.json` extension will have access to intellisense.

### YAML

1. Install the [Red Hat YAML Extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml).
2. Navigate to Code > Profiles (Default) > Show Profile Contents.
3. Open the `settings.json` file.
4. Add the following to your configuration:
    ```json
    "yaml.schemas": {
    "https://raw.githubusercontent.com/pachyderm/pachyderm/master/src/internal/jsonschema/pps_v2/CreatePipelineRequest.schema.json": "/**/*.pipeline.yaml"
    }
    ```

Now all files with the `.pipeline.yaml` extension will have access to intellisense.