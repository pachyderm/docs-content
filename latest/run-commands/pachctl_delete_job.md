---
date: 2023-08-04T13:05:50-04:00
title: "pachctl delete job"
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
	- pachctl delete job 5f93d03b65fa421996185e53f7f8b1e4 
	- pachctl delete job 5f93d03b65fa421996185e53f7f8b1e4 --project foo
```

### Options

```
  -h, --help             help for job
      --project string   Specify the project (by name) containing the parent pipeline for this job. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

