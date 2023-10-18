---
date: 2023-10-18T16:51:53-04:00
title: "pachctl delete job"
description: "Learn about the pachctl delete job command"
---

## pachctl delete job

Delete a job.

### Synopsis

This command deletes a job.

```
pachctl delete job <pipeline>@<job> [flags]
```

### Examples

```
 pachctl delete job 5f93d03b65fa421996185e53f7f8b1e4 
 pachctl delete job 5f93d03b65fa421996185e53f7f8b1e4 --project foo
```

### Options

```
  -h, --help             help for job
      --project string   Specify the project (by name) containing the parent pipeline for this job. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

