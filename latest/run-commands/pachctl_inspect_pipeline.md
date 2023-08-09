---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect pipeline"
slug: "Learn about the pachctl_inspect_pipeline command"
---

## pachctl inspect pipeline

Return info about a pipeline.

### Synopsis

This command returns info about a pipeline.

```
pachctl inspect pipeline <pipeline> [flags]
```

### Examples

```
	- pachctl inspect pipeline foo 
	- pachctl inspect pipeline foo --project bar 
	- pachctl inspect pipeline foo --project bar --raw -o yaml 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for pipeline
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) containing the inspected pipeline. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

