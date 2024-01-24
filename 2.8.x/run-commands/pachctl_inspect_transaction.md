---
date: 2023-10-18T16:51:53-04:00
title: "pachctl inspect transaction"
description: "Learn about the pachctl inspect transaction command"
---

## pachctl inspect transaction

Print information about an open transaction.

### Synopsis

This command prints information about an open transaction.

```
pachctl inspect transaction [<transaction>] [flags]
```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for transaction
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl inspect](../pachctl_inspect)	 - Show detailed information about a Pachyderm resource.

