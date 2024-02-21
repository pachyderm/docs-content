---
date: 2024-02-13T16:12:03-05:00
title: "pachctl delete defaults"
description: "Learn about the pachctl delete defaults command"
---

## pachctl delete defaults

Delete defaults.

### Synopsis

Delete cluster or project defaults.

```
pachctl delete defaults [--cluster | --project PROJECT] [flags]
```

### Options

```
      --cluster          Delete cluster defaults.
      --dry-run          Do not actually delete defaults.
  -h, --help             help for defaults
      --project string   Delete project defaults. (default "video-to-frame-traces")
      --regenerate       Regenerate pipeline specs deleted (i.e., empty) defaults.
      --reprocess        Reprocess regenerated pipelines.  Implies --regenerate
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

