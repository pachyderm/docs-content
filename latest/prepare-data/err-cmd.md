---
# metadata # 
title: Skip Failed Datums
description: Learn how to skip failed datums to prevent jobs from fully failing.
date: 
# taxonomy #
tags: ["datums", "data-operations"]
series:
seriesPart:
directory: true 
---

{{% notice note%}}
The `errCmd` parameter enables you to fail a datum without failing the
whole job.
{{% /notice%}}

{{% notice tip %}}
Before you read this section, make sure that you understand such
concepts as [Datum](/{{%release%}}/learn/glossary/datum) and
[Pipeline](/{{%release%}}/learn/glossary/pipeline/).
{{% /notice %}}

When {{% productName %}} processes your data, it breaks it up into units of
computation called datums. Each datum is processed separately.
In a basic pipeline configuration, a failed datum results in a failed
job. However, in some cases, you might not need all datums
to consider a job successful. If your downstream pipelines can be run
on only the successful datums instead of needing all the datums to be
successful, {{% productName %}} can mark some datums as *recovered* which means
that they failed with a non-critical error, but the successful datums
will be processed.

To configure a condition under which you want your failed datums not
to fail the whole job, you can add your custom error code in
`errCmd` and `errStdin` fields in your pipeline specification.

For example, your DAG consists of two pipelines:

* The pipeline 1 cleans the data.
* The pipeline 2 trains your model by using the data from the first pipeline.

That means that the second pipeline takes the results of the first pipeline
from its output repository and uses that data to train a model. In some cases,
you might not need all the datums in the first pipeline to be successful
to run the second pipeline.

The following diagram describes how {{% productName %}} transformation and error
code work:

![err_cmd logic](/images/err_cmd_workflow.svg)

Here is what is happening in the diagram above:

1. {{% productName %}} executes the transformation code that you defined in
the `cmd` field against your datums.
1. If a datum is processed without errors, {{% productName %}} marks it as
`processed`.
1. If a datum fails, {{% productName %}} executes your
error code (`errCmd`) on that datum.
1. If the code in `errCmd` successfully runs on the *skipped* datum,
{{% productName %}} marks the skipped datum as `recovered`. The datum is in a
failed state and, therefore, the pipeline does not put it into the output
repository, but successful datums continue onto the next step in your DAG.
1. If the `errCmd` code fails on the skipped datum, the datum is marked
as failed, and, consequently, the job is marked as failed.

You can view the processed, skipped, and recovered datums in the `PROGRESS`
field in the output of the `pachctl list job -p <pipeline name>` command:

![Datums in progress](/images/datums_in_progress.png)

{{% productName %}} writes only processed datums of successful jobs to the output
commit so that these datums can be processed by downstream pipelines.
For example, in your first pipeline, {{% productName %}} processes three datums.
If one of the datums is marked as *recovered* and two others are
successfully processed, only these two successful datums are used in
the next pipeline.

If you want to let the job proceed with only the successful datums being
written to the output, set `"errCmd" : ["true"]`. The failed datums,
which are "recovered" by `errCmd` in this way, will be retried on
the next job, just as failed datums.

{{% notice note %}}
**See Also**: [Example errCmd pipeline](https://github.com/pachyderm/pachyderm/tree/{{% majorMinorVersion %}}/examples/err_cmd/)
{{%/notice%}}
