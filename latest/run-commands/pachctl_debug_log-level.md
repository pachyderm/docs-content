---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug log-level"
description: "Learn about the pachctl debug log-level command"
---

## pachctl debug log-level

Change the log level across Pachyderm.

### Synopsis

This command changes the log level across Pachyderm.

```
pachctl debug log-level <level> [flags]
```

### Examples

```
 pachctl debug log-level debug 
 pachctl debug log-level info --duration 5m 
 pachctl debug log-level info --grpc --duration 5m 
 pachctl debug log-level info --recursive false --duration 5m 

```

### Options

```
  -d, --duration duration   Specify a duration for how long to log at the non-default level. (default 5m0s)
  -g, --grpc                Set the grpc log level instead of the Pachyderm log level.
  -h, --help                help for log-level
  -r, --recursive           Set the log level on all Pachyderm pods; if false, only the pachd that handles this RPC (default true)
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

