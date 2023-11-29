---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug profile"
description: "Learn about the pachctl debug profile command"
---

## pachctl debug profile

Collect a set of pprof profiles.

### Synopsis

This command collects a set of pprof profiles. Options include heap (memory), CPU, block, mutex, and goroutine profiles.

```
pachctl debug profile <profile> <file> [flags]
```

### Examples

```
 pachctl debug profile cpu cpu.tgz 
 pachctl debug profile heap heap.tgz 
 pachctl debug profile goroutine goroutine.tgz 
 pachctl debug profile goroutine --pachd goroutine.tgz 
 pachctl debug profile cpu --pachd -d 30s cpu.tgz 
 pachctl debug profile cpu --pipeline foo -d 30s foo-pipeline.tgz 
 pachctl debug profile cpu --worker foo-v1-r6pdq -d 30s worker.tgz 

```

### Options

```
  -d, --duration duration   Specify a duration for compiling a CPU profile. (default 1m0s)
  -h, --help                help for profile
      --pachd               Collect only pachd's profile.
  -p, --pipeline string     Collect only a specific pipeline's profile from the worker pods.
  -w, --worker string       Collect only the profile of a given worker pod.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

