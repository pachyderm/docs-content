---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug analyze"
description: "Learn about the pachctl debug analyze command"
---

## pachctl debug analyze

Start a local pachd server to analyze a debug dump.

### Synopsis

This command starts a local pachd server to analyze a debug dump.

```
pachctl debug analyze <file> [flags]
```

### Examples

```
 pachctl debug analyze dump.tgz 
 pachctl debug analyze dump.tgz --port 1650 

```

### Options

```
  -h, --help       help for analyze
  -p, --port int   launch a debug server on the given port. If unset, choose a free port automatically
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

