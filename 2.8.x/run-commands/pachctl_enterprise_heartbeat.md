---
date: 2023-10-18T16:51:53-04:00
title: "pachctl enterprise heartbeat"
description: "Learn about the pachctl enterprise heartbeat command"
---

## pachctl enterprise heartbeat

Sync the enterprise state with the license server immediately.

### Synopsis

This command syncs the enterprise state with the license server immediately. 

This means that if there is an active enterprise license associated with the enterprise server, the cluster will also have access to enterprise features.

```
pachctl enterprise heartbeat [flags]
```

### Options

```
      --enterprise   Make the enterprise server refresh its state
  -h, --help         help for heartbeat
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl enterprise](../pachctl_enterprise)	 - Enterprise commands enable Pachyderm Enterprise features

