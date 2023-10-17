---
date: 2023-09-07T13:28:03-04:00
title: "pachctl debug analyze"
description: "Learn about the pachctl_debug_analyze command"
---

## pachctl debug analyze

Start a local pachd server to analyze a debug dump.

### Synopsis

Start a local pachd server to analyze a debug dump.

```
pachctl debug analyze <file> [flags]
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

