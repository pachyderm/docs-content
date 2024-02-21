---
date: 2023-10-18T16:51:53-04:00
title: "pachctl list transaction"
description: "Learn about the pachctl list transaction command"
---

## pachctl list transaction

List transactions.

### Synopsis

This command lists transactions.

```
pachctl list transaction [flags]
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

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

