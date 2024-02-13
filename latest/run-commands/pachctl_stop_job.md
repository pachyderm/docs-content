---
date: 2024-02-13T16:12:03-05:00
title: "pachctl stop job"
description: "Learn about the pachctl stop job command"
---

## pachctl stop job

Stop a job.

### Synopsis

This command stops a job immediately. To specify the project where the parent pipeline lives, use the `--project` flag 


```
pachctl stop job <pipeline>@<job> [flags]
```

### Options

```
  -h, --help             help for job
      --project string   Specify the project (by name) containing the parent pipeline for the job. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl stop](../pachctl_stop)	 - Cancel an ongoing task.

