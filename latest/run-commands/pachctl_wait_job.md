---
date: 2024-02-13T16:12:03-05:00
title: "pachctl wait job"
description: "Learn about the pachctl wait job command"
---

## pachctl wait job

Wait for a job to finish then return info about the job.

### Synopsis

This command waits for a job to finish then return info about the job.

```
pachctl wait job <job>|<pipeline>@<job> [flags]
```

### Examples

```
 pachctl wait job e0f68a2fcda7458880c9e2e2dae9e678 
 pachctl wait job foo@e0f68a2fcda7458880c9e2e2dae9e678 
 pachctl wait job foo@e0f68a2fcda7458880c9e2e2dae9e678 --project bar 
 pachctl wait job foo@e0f68a2fcda7458880c9e2e2dae9e678 --project bar --raw --output yaml 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for job
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) containing the parent pipeline for this job. (default "video-to-frame-traces")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl wait](../pachctl_wait)	 - Wait for the side-effects of a Pachyderm resource to propagate.

