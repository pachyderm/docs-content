---
date: 2023-10-18T16:51:53-04:00
title: "pachctl update defaults"
description: "Learn about the pachctl update defaults command"
---

## pachctl update defaults

Update defaults.

### Synopsis

Update defaults.

```
pachctl update defaults [--cluster] [flags]
```

### Options

```
      --cluster       Update cluster defaults.
      --dry-run       Do not actually update defaults.
  -f, --file string   A JSON file containing cluster defaults.  "-" reads from stdin (the default behavior.) (default "-")
  -h, --help          help for defaults
      --regenerate    Regenerate pipeline specs from new defaults.
      --reprocess     Reprocess regenerated pipelines.  Implies --regenerate.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl update](../pachctl_update)	 - Change the properties of an existing Pachyderm resource.

