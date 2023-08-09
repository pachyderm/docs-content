---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect project"
slug: "Learn about the pachctl_inspect_project command"
---

## pachctl inspect project

Inspect a project.

### Synopsis

This command inspects a project and returns information like its `Name` and `Created at` time. 

	- To return additional details, use the `--raw` flag 


```
pachctl inspect project <project> [flags]
```

### Examples

```
	- pachctl inspect project foo-project 
	- pachctl inspect project foo-project --raw 
	- pachctl inspect project foo-project --output=yaml 

```

### Options

```
  -h, --help            help for project
  -o, --output string   Output format when --raw is set: "json" or "yaml" (default "json")
      --raw             Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

