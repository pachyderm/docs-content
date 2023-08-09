---
date: 2023-08-04T13:05:50-04:00
title: "pachctl stop pipeline"
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
	- pachctl stop pipeline foo 
	- pachctl stop pipeline foo --project bar 

```

### Options

```
  -h, --help             help for pipeline
      --project string   Project containing pipeline. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

