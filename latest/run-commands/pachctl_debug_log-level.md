---
date: 2023-08-04T13:05:50-04:00
title: "pachctl debug log-level"
slug: "Learn about the pachctl_debug_log-level command"
---

## pachctl debug log-level

Change the log level across Pachyderm.

### Synopsis

Change the log level across Pachyderm.

```
pachctl debug log-level <level> [flags]
```

### Options

```
  -d, --duration duration   how long to log at the non-default level (default 5m0s)
  -g, --grpc                adjust the grpc log level instead of the pachyderm log level
  -h, --help                help for log-level
  -r, --recursive           set the log level on all pachyderm pods; if false, only the pachd that handles this RPC (default true)
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](/commands/pachctl_debug/)	 - Debug commands for analyzing a running cluster.

