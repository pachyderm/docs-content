---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug binary"
description: "Learn about the pachctl debug binary command"
---

## pachctl debug binary

Collect a set of binaries.

### Synopsis

This command collects a set of binaries.

```
pachctl debug binary <file> [flags]
```

### Examples

```
 pachctl debug binary binaries.tgz 
 pachctl debug binary --pachd pachd-binary.tgz 
 pachctl debug binary --worker foo-v1-r6pdq foo-pod-binary.tgz 
 pachctl debug binary --pipeline foo foo-binary.tgz 

```

### Options

```
  -h, --help              help for binary
      --pachd             Collect only pachd's binary.
  -p, --pipeline string   Collect only the binary from a given pipeline.
  -w, --worker string     Collect only the binary from a given worker pod.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

