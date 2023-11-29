---
date: 2023-09-07T13:28:03-04:00
title: "pachctl start pipeline"
description: "Learn about the pachctl_start_pipeline command"
---

## pachctl start pipeline

Restart a stopped pipeline.

### Synopsis

This command restarts a stopped pipeline.

```
pachctl start pipeline <pipeline> [flags]
```

### Examples

```
 pachctl start pipeline foo 
 pachctl start pipeline foo --project bar 

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

* [pachctl start](../pachctl_start)	 - Start a Pachyderm resource.

