---
# metadata # 
title:  Input Cron PPS
description: Trigger pipelines based on time.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: Required for Cron Inputs
---

## Spec 
This is a top-level attribute of the pipeline spec. 

```s
{
  "pipeline": {...},
  "transform": {...},
  "input": {
    "cron": {
      {
          "name": string,
          "spec": string,
          "repo": string,
          "start": time,
          "overwrite": bool
      }
    }
  },
  ...
}

```

## Attributes 

| Attribute |Required?| Description |
|-|-|-|
| `name`      |Yes|The name of the cron job, which should be unique within the {{% productName %}} cluster.                                                     |
| `spec`      |Yes|The cron schedule for the job, specified using the standard cron format or macros. [**See schedule macros**](https://en.wikipedia.org/wiki/Cron) for examples. {{% productName %}} also supports non-standard schedules, such as `"@daily"`.  |
| `repo`      | No |The name of the input repository that the cron job should read data from; default:`<pipeline-name>_<input-name>` |
| `start`     |No |Specifies the start time for the cron job. This is useful for running the job on a specific date in the future. If not specified, starts immediately.  Specifying a time enables you to run on matching times from the past or skip times from the present and only start running on matching times in the future. Format the time value according to [**RFC3339**](https://www.ietf.org/rfc/rfc3339.txt). |
| `overwrite` |No |Defines whether you want the timestamp file to be overwritten on each tick; defaults to simply writing new files on each tick. By default, when `"overwrite"` is disabled, ticks accumulate in the cron input repo. When `"overwrite"` is enabled, {{% productName %}} erases the old ticks and adds new ticks with each commit. If you do not add any manual ticks or run `pachctl run cron`, only one tick file per commit (for the latest tick) is added to the input repo. |


## Behavior 
The `input` field in a {{% productName %}} Pipeline Spec is used to specify the inputs to the pipeline, which are the {{% productName %}} repositories that the pipeline should read data from. The `input` field can include both static and dynamic inputs.

The `cron` field within the input field is used to specify a dynamic input that is based on a cron schedule. This is useful for pipelines that need to process data on a regular schedule, such as daily or hourly. 

A repo is created for each cron input. When a Cron input triggers, `pachd` commits a single file, named by the current [RFC3339 timestamp](https://www.ietf.org/rfc/rfc3339.txt) to the repo which contains the time which satisfied the spec.

## Callouts 

- Avoid using intervals faster than `1-5` minutes
- You can use `never` during development and manually trigger the pipeline
- If using jsonnet, you can pass arguments like: `--arg cronSpec="@every 5m"`
- You **cannot update a cron pipeline** after it has been created; instead, you must delete the pipeline and build a new one.

## When to Use

You should use a `cron` input in a {{% productName %}} Pipeline Spec when you need to process data on a regular schedule, such as hourly or daily. A `cron` input allows you to specify a schedule for the pipeline to run, and {{% productName %}} will automatically trigger the pipeline at the specified times.

Example scenarios:

- **Batch processing**: If you have a large volume of data that needs to be processed on a regular schedule, a cron input can be used to trigger the processing automatically, without the need for manual intervention.

- **Data aggregation**: If you need to collect data from different sources and process it on a regular schedule, a cron input can be used to automate the data collection and processing.

- **Report generation**: If you need to generate reports on a regular schedule, a cron input can be used to trigger the report generation process automatically.

## Examples

{{< stack type="wizard">}}

{{% wizardRow id="Examples"%}}
{{% wizardButton option="Every 60s" state="active" %}}
{{% wizardButton option="Daily With Overwrites" %}}
{{% wizardButton option="SQL Ingest" %}}
{{% /wizardRow %}}

{{% wizardResults  %}}
{{% wizardResult val1="examples/every-60s"%}}
```json
  "input": {
    "cron": {
      "name": "tick",
      "spec": "@every 60s"
    }
  }
```
{{% /wizardResult %}}
{{% wizardResult val1="examples/daily-with-overwrites"%}}
```json
  "input": {
    "cron": {
      "name": "tick",
      "spec": "@daily",
      "overwrite": true
    }
  }
```
{{% /wizardResult %}}
{{% wizardResult val1="examples/sql-ingest"%}}
```json
pachctl update pipeline --jsonnet https://raw.githubusercontent.com/pachyderm/pachyderm/{{% majorMinorVersion %}}/src/templates/sql_ingest_cron.jsonnet \
  --arg name=myingest \
  --arg url="mysql://root@mysql:3306/test_db" \
  --arg query="SELECT * FROM test_data" \
  --arg hasHeader=false \
  --arg cronSpec="@every 60s" \
  --arg secretName="mysql-creds" \
  --arg format=json 
```
{{% /wizardResult %}}
{{% /wizardResults %}}

{{< /stack >}}
