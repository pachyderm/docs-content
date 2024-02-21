---
date: 2023-10-18T16:51:53-04:00
title: "pachctl create defaults"
description: "Learn about the pachctl create defaults command"
---

## pachctl create defaults

Set cluster defaults.

### Synopsis

Set cluster defaults.

```
pachctl create defaults [--cluster] [flags]
```

### Options

```
      --cluster       Create cluster defaults.
      --dry-run       Do not actually delete defaults.
  -f, --file string   A JSON file containing cluster defaults.  "-" reads from stdin (the default behavior.) (default "-")
  -h, --help          help for defaults
      --regenerate    Regenerate pipeline specs from new defaults.
      --reprocess     Reprocess regenerated pipelines.  Implies --regenerate
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.

