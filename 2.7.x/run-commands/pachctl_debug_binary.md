---
date: 2023-09-07T13:28:03-04:00
title: "pachctl debug binary"
description: "Learn about the pachctl_debug_binary command"
---

## pachctl debug binary

Collect a set of binaries.

### Synopsis

Collect a set of binaries.

```
pachctl debug binary <file> [flags]
```

### Options

```
  -h, --help              help for binary
      --pachd             Only collect the binary from pachd.
  -p, --pipeline string   Only collect the binary from the worker pods for the given pipeline.
  -w, --worker string     Only collect the binary from the given worker pod.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

