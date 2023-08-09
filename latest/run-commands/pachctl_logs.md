---
date: 2023-08-04T13:05:50-04:00
title: "pachctl logs"
slug: "Learn about the pachctl_logs command"
---

## pachctl logs

Return logs from a job.

### Synopsis

This command returns logs from a job. 
	- To filter your logs by pipeline, use the `--pipeline` flag 
	- To filter your logs by job, use the `--job` flag 
	- To filter your logs by datum, use the `--datum` flag 
	- To filter your logs by the master process, use the `--master` flag  with the `--pipeline` flag 
	- To filter your logs by the worker process, use the `--worker` flag 
	- To follow the logs as more are created, use the `--follow` flag 
	- To set the number of lines to return, use the `--tail` flag 
	- To return results starting from a certain amount of time before now, use the `--since` flag 


```
pachctl logs [--pipeline=<pipeline>|--job=<pipeline>@<job>] [--datum=<datum>] [flags]
```

### Examples

```
	- pachctl logs --pipeline foo 
	- pachctl logs --job foo@5f93d03b65fa421996185e53f7f8b1e4 
	- pachctl logs --job foo@5f93d03b65fa421996185e53f7f8b1e4 --tail 10 
	- pachctl logs --job foo@5f93d03b65fa421996185e53f7f8b1e4 --follow 
	- pachctl logs --job foo@5f93d03b65fa421996185e53f7f8b1e4 --datum 7f3c[...] 
	- pachctl logs --pipeline foo --datum 7f3c[...] --master 
	- pachctl logs --pipeline foo --datum 7f3c[...] --worker  
	- pachctl logs --pipeline foo --datum 7f3c[...] --master --tail 10  
	- pachctl logs --pipeline foo --datum 7f3c[...] --worker --follow 

```

### Options

```
      --datum string      Specify results should only return logs for a given datum ID.
  -f, --follow            Follow logs as more are created.
  -h, --help              help for logs
      --inputs string     Filter for log lines generated while processing these files (accepts PFS paths or file hashes)
  -j, --job string        Specify results should only return logs for a given job ID.
      --master            Specify results should only return logs from the master process; --pipeline must be set.
  -p, --pipeline string   Specify results should only return logs for a given pipeline.
      --project string    Specify the project (by name) containing parent pipeline for the job. (default "standard-ml-tutorial")
      --raw               Specify results should only return log messages verbatim from server.
      --since string      Specify results should return log messages more recent than "since". (default "24h")
  -t, --tail int          Set the number of lines to return of the most recent logs.
      --worker            Specify results should only return logs from the worker process.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

