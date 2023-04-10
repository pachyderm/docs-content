---
# metadata #
title: Datum
description: Learn about datums, the smallest indivisible unit of computation within a job.
date:
# taxonomy #
tags: 
series: ["glossary"]
seriesPart:
---
## About 

A datum is **the smallest indivisible unit of computation within a job**. Datums are used to:
- Divide your input data
- Distribute processing workloads

A datum's scope can be as large as all of your data at once, a directory, a file, or a combination of multiple inputs. The shape and quantity of your datums is determined by a glob pattern defined in your pipeline specification. 

A job can have one, many, or no datums. Each datum is processed independently with a single execution of the user code on one of the pipeline worker pods. The individual output files produced by all of your datums are combined to create the final output commit.

If a job is successfully executed but has no matching files to transform, it is considered a zero-datum job.

## Datum Processing States

When a pipeline runs, it processes your datums. Some of them get processed successfully and some might be skipped or even fail. Generally, processed datums fall into either successful or failure state category.

### Successful States

| State      | Description |
| ---------- | ----------- |
| Success    | The datum has been successfully processed in this job. |
| Skipped    | The datum has been successfully processed in a previous job, has not changed since then, and therefore, it was skipped in the current job. |

### Failure States

| State      | Description |
| ---------- | ----------- |
| Failed     | The datum failed to be processed. Any failed datum in a job fails the whole job. |
| Recovered  | The datum failed, but was recovered by the user's error handling code. Although the datum is marked as *recovered*, {{%productName%}} does not process it in the downstream pipelines. A recovered datum does not fail the whole job. Just like failed datums, recovered datums are retried on the next run of the pipeline. |

You can view the information about datum processing states in the output of
the `pachctl list job <jobID>` command:

![datums in progress](/images/datums_in_progress.png)

{{% notice note %}}
Datums that failed are still included in the total, but not shown in the progress indicator.
{{%/notice%}}