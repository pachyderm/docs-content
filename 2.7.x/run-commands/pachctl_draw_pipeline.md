---
date: 2023-09-07T13:28:03-04:00
title: "pachctl draw pipeline"
description: "Learn about the pachctl_draw_pipeline command"
---

## pachctl draw pipeline

Draw a DAG

### Synopsis

This command draws a DAG

```
pachctl draw pipeline [flags]
```

### Examples

```
 pachctl draw pipeline --commit 5f93d03b65fa421996185e53f7f8b1e4 pachctl draw pipeline --box-width 20 pachctl draw pipeline --edge-height 8 pachctl draw pipeline --project foo pachctl draw pipeline --box-width 20 --edge-height 8 --commit 5f93d03b65fa421996185e53f7f8b1e4
```

### Options

```
      --box-width int     Character width of each box in the DAG (default 11)
  -c, --commit string     Commit at which you would to draw the DAG
      --edge-height int   Number of vertical lines spanned by each edge (default 5)
  -h, --help              help for pipeline
      --project string    Project containing pipelines. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl draw](../pachctl_draw)	 - Draw an ASCII representation of an existing Pachyderm resource.

