---
date: 2024-02-13T16:12:03-05:00
title: "pachctl list datum"
description: "Learn about the pachctl list datum command"
---

## pachctl list datum

Return the datums in a job.

### Synopsis

This command returns the datums in a job. 
 
 To pass in a JSON pipeline spec instead of `pipeline@job`, use the `--file` flag 
  To specify the project where the parent pipeline lives, use the `--project` flag 


```
pachctl list datum <pipeline>@<job> [flags]
```

### Examples

```
 pachctl list datum foo@5f93d03b65fa421996185e53f7f8b1e4 
 pachctl list datum foo@5f93d03b65fa421996185e53f7f8b1e4 --project bar 
 pachctl list datum --file pipeline.json
```

### Options

```
  -f, --file string      Set the JSON file containing the pipeline to list datums from; the pipeline need not exist.
  -h, --help             help for datum
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Specify the project (by name) containing parent pipeline for the job. (default "video-to-frame-traces")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

