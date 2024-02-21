---
date: 2024-02-13T16:12:03-05:00
title: "pachctl create defaults"
description: "Learn about the pachctl create defaults command"
---

## pachctl create defaults

Set cluster defaults.

### Synopsis

Set cluster or project defaults.

```
pachctl create defaults [--cluster | --project PROJECT] [flags]
```

### Options

```
      --cluster          Create cluster defaults.
      --dry-run          Do not actually create defaults.
  -f, --file string      A JSON file containing cluster defaults.  "-" reads from stdin (the default behavior.) (default "-")
  -h, --help             help for defaults
      --project string   Create project defaults. (default "video-to-frame-traces")
      --regenerate       Regenerate pipeline specs from new defaults.
      --reprocess        Reprocess regenerated pipelines.  Implies --regenerate
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.

