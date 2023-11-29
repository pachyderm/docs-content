---
# metadata # 
title:  View Dashboard
description: Learn how to view the status of your projects and their jobs from a single dashboard in the Console UI.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 1
---

You can quickly tab between projects to get a high-level view of the status of its jobs from Console's main dashboard.

# How to View Project Statuses From the Dashboard

1. Open Console. 
2. Select the project you want to view. 
3. View the **Project Preview** column to get an update on the last 10 jobs that ran in the project. 
4. Select a Job to view a breakdown of its subjobs, which includes details like:
   - **ID**: Subjob ID
   - **Pipeline**: The pipeline name and version number 
   - **Datums Processed**: The number of datums processed and skipped
   - **Started**: When the job started
   - **Duration**: How long the job ran in seconds
   - **D/L**: The total amount of data downloaded 
   - **U/L**: The total amount of data uploaded
   - **Restarts**: The number of times the job restarted

![project dashboard](/images/console/project-dashboard.gif)