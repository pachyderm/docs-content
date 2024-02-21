---
date: 2024-02-13T16:12:03-05:00
title: "pachctl stop pipeline"
description: "Learn about the pachctl stop pipeline command"
---

## pachctl stop pipeline

Stop a running pipeline.

### Synopsis

This command stops a running pipeline.

```
pachctl stop pipeline <pipeline> [flags]
```

### Examples

```
 pachctl stop pipeline foo 
 pachctl stop pipeline foo --project bar 

```

### Options

```
  -h, --help             help for pipeline
      --project string   Project containing pipeline. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl stop](../pachctl_stop)	 - Cancel an ongoing task.

