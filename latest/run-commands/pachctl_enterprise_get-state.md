---
date: 2023-10-18T16:51:53-04:00
title: "pachctl enterprise get-state"
description: "Learn about the pachctl enterprise get-state command"
---

## pachctl enterprise get-state

Check whether the Pachyderm cluster has an active enterprise license.

### Synopsis

This command checks whether the Pachyderm cluster has an active enterprise license; If so, it also returns the expiration date of the license.

```
pachctl enterprise get-state [flags]
```

### Options

```
      --enterprise   Activate auth on the active enterprise context
  -h, --help         help for get-state
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl enterprise](../pachctl_enterprise)	 - Enterprise commands enable Pachyderm Enterprise features

