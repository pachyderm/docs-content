---
date: 2023-09-07T13:28:03-04:00
title: "pachctl restart datum"
description: "Learn about the pachctl_restart_datum command"
---

## pachctl restart datum

Restart a stuck datum during a currently running job.

### Synopsis

This command restarts a stuck datum during a currently running job; it does not solve failed datums. 
 
You can configure a job to skip failed datums via the transform.err_cmd setting of your pipeline spec. 
 
 To specify the project where the parent pipeline lives, use the `--project` flag 


```
pachctl restart datum <pipeline>@<job> <datum-path1>,<datum-path2>,... [flags]
```

### Examples

```
 pachctl restart datum foo@5f93d03b65fa421996185e53f7f8b1e4 /logs/logs.txt 
 pachctl restart datum foo@5f93d03b65fa421996185e53f7f8b1e4 /logs/logs-a.txt, /logs/logs-b.txt 
 pachctl restart datum foo@5f93d03b65fa421996185e53f7f8b1e4 /logs/logs-a.txt, /logs/logs-b.txt --project bar 
```

### Options

```
  -h, --help             help for datum
      --project string   Specify the project (by name) containing parent pipeline for the datum's job (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl restart](../pachctl_restart)	 - Cancel and restart an ongoing task.

