---
date: 2023-08-04T13:05:50-04:00
title: "pachctl start pipeline"
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
	- pachctl start pipeline foo 
	- pachctl start pipeline foo --project bar 

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

