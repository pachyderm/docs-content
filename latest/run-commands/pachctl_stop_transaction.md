---
date: 2023-10-18T16:51:53-04:00
title: "pachctl stop transaction"
description: "Learn about the pachctl stop transaction command"
---

## pachctl stop transaction

Stop modifying the current transaction.

### Synopsis

This command stops modifying the current transaction; to be used with `pachctl resume transaction`. This command is ideal for drafting a transaction in multiple steps.

```
pachctl stop transaction [flags]
```

### Options

```
  -h, --help   help for transaction
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl stop](../pachctl_stop)	 - Cancel an ongoing task.

