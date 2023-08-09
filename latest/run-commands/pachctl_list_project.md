---
date: 2023-08-04T13:05:50-04:00
title: "pachctl list project"
slug: "Learn about the pachctl_list_project command"
---

## pachctl list project

Return all projects.

### Synopsis

This command returns all projects.

```
pachctl list project <repo> [flags]
```

### Examples

```
	- pachctl list project 
	- pachctl list project --raw 

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

