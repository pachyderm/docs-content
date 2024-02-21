---
date: 2023-10-18T16:51:53-04:00
title: "pachctl delete defaults"
description: "Learn about the pachctl delete defaults command"
---

## pachctl delete defaults

Delete defaults.

### Synopsis

Delete defaults.

```
pachctl delete defaults [--cluster] [flags]
```

### Options

```
      --cluster      Delete cluster defaults.
      --dry-run      Do not actually delete defaults.
  -h, --help         help for defaults
      --regenerate   Regenerate pipeline specs deleted (i.e., empty) defaults.
      --reprocess    Reprocess regenerated pipelines.  Implies --regenerate
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

