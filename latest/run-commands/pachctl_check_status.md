---
date: 2024-02-13T16:12:03-05:00
title: "pachctl check status"
description: "Learn about the pachctl check status command"
---

## pachctl check status

Check the status of pipelines within a project.

### Synopsis

Check the status of pipelines within a project.

```
pachctl check status [flags]
```

### Examples

```
 pachctl check status 
 pachctl check status --project bar 

```

### Options

```
  -A, --all-projects     Show pipeline status form all projects.
  -h, --help             help for status
      --project string   Specify the project (by name) containing the pipeline. (default "video-to-frame-traces")
      --raw              Specify results should only return log messages verbatim from server.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl check](../pachctl_check)	 - Check the status of pipelines within a project.

