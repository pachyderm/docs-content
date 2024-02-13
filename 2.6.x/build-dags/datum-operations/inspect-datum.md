---
# metadata # 
title: Inspect Datum
description: Learn how to inspect a datum using the pachctl inspect datum command. 
date: 
# taxonomy #
tags: ["datums"]
series:
seriesPart:
---

{{%productName%}} stores information about each datum that a pipeline processes, including timing information, size information,
and `/pfs` snapshots. You can view these statistics by running the `pachctl inspect datum` command (or its language client equivalents).

In particular, {{%productName%}} provides the following information for each datum processed by your pipelines:

- The amount of data that was uploaded and downloaded
- The time spend uploading and downloading data
- The total time spend processing
- Success/failure information, including any error encountered for failed datums
- The directory structure of input data that was seen by the job.

Use the `pachctl list datum <pipeline>@<job ID>` to retrieve the list of datums processed by a given job, and pick the datum ID you want to inspect. That information can be useful when troubleshooting a failed job.