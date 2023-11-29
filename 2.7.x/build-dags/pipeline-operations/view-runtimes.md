---
# metadata # 
title: View Pipeline Jobs & Runtimes
description: Learn how to view pipeline runtimes from Console
date: 
# taxonomy #
tags: ["pipelines"]
series:
seriesPart:
---

You can easily view and compare pipeline jobs and job runtimes from within Console. This can be a great way to measure and compare performance across different job sizes and pipeline versions.

## How to View Pipeline Jobs

This view is great for quickly understanding how many datums were processed, if the job required restarts, and how much data was downloaded/uploaded.

1. Log in to Console.
2. Navigate to a project.
3. Select **Pipelines**.
4. Find and select the pipeline(s) you wish to list jobs for.

![list jobs from Console](/images/console/list-jobs.gif)

{{%notice tip%}}

You can achieve a similar output from the terminal by using the follwing PachCTL command:
```s
pachctl list jobs --project <project-name> --pipeline <pipeline-name>
```
{{%/notice%}}


## How to View Pipeline Runtimes

This view is great for visually comparing processing times between jobs.

1. Log in to Console.
2. Navigate to a project.
3. Select **Pipelines**.
4. Find and select the pipeline(s) you wish to view runtimes for.
5. Select the **Runtimes** tab.

![view pipeline runtimes from Console](/images/console/view-pipeline-runtimes.gif)