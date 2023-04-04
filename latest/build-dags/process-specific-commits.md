---
# metadata # 
title:  Process Specific Commits
description: Learn how to process specific commits in a branch.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 
---
{{% productName %}} enables you to process specific commits in a branch that are not the `HEAD` commit, which can be useful in many scenarios. For example, you can use this feature for:

- **Testing and debugging**: By processing specific intermediary commits, you can identify issues, test changes, or debug the pipeline at different stages of the data processing flow. This helps you ensure the quality and correctness of your data processing tasks.

- **Selective processing**: In some cases, you might want to process only specific subsets of data instead of the entire dataset. By targeting specific commits, you can selectively process the data as needed.

- **Historical data reprocessing**: If your pipeline has been updated or you need to re-process data with new parameters, you can target specific commits to re-run the pipeline on previously processed data.

- **Resource utilization**: By processing only the necessary commits, you can optimize the use of resources and reduce the overall time and cost of data processing.

## How to Process Specific Commits

To do process a specific commit, you need to set the `master` branch of your repo to have your specified commit as `HEAD`.

For example, if you submitted ten commits in the `staging` branch and you want to process the seventh, third, and most recent commits, you need to run the following commands respectively:

```s
pachctl create branch data@master --head staging^7
pachctl create branch data@master --head staging^3
pachctl create branch data@master --head staging
```

When you run the commands above, {{%productName%}} creates a job for each of the commands one after another. Therefore, when one job is completed, {{%productName%}} starts the next one. To verify that {{%productName%}} created jobs for these commands, run `pachctl list job -p <pipeline_name> --history all`.

### Change the HEAD of your Branch

You can move backward to previous commits as easily as advancing to the latest commits. For example, if you want to change the final output to be the result of processing `staging^1`, you can _roll back_ your HEAD commit by running the following command:

```s
pachctl create branch data@master --head staging^1
```

This command starts a new job to process `staging^1`. The `HEAD` commit on your output repo will be the result of processing `staging^1` instead of `staging`.