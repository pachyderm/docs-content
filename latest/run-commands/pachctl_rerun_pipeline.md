---
date: 2023-10-18T16:51:53-04:00
title: "pachctl rerun pipeline"
description: "Learn about the pachctl rerun pipeline command"
---

## pachctl rerun pipeline

Rerun a pipeline.

### Synopsis

This command is used to rerun an existing pipeline.

```
pachctl rerun pipeline <pipeline> [flags]
```

### Examples

```
 pachctl rerun pipeline foo 
 pachctl rerun pipeline foo --reprocess
 pachctl rerun pipeline foo --project bar

```

### Options

```
  -h, --help             help for pipeline
      --project string   Specify the project (by name) containing project (default "video-to-frame-traces")
      --reprocess        If true, reprocess datums that were already processed by previous version of the pipeline.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl rerun](../pachctl_rerun)	 - Manually rerun a Pachyderm resource.

