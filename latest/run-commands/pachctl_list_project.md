---
date: 2024-02-13T16:12:03-05:00
title: "pachctl list project"
description: "Learn about the pachctl list project command"
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
 pachctl list project 
 pachctl list project --raw 

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

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

