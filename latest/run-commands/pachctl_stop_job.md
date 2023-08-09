---
date: 2023-08-04T13:05:50-04:00
title: "pachctl stop job"
---

## pachctl stop job

Stop a job.

### Synopsis

This command stops a job immediately.	

  - To specify the project where the parent pipeline lives, use the `--project` flag 


```
pachctl stop job <pipeline>@<job> [flags]
```

### Options

```
  -h, --help             help for job
      --project string   Specify the project (by name) containing the parent pipeline for the job. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

