---
date: 2024-02-13T16:12:03-05:00
title: "pachctl delete commitV2"
description: "Learn about the pachctl delete commitV2 command"
---

## pachctl delete commitV2

Delete a commit.

### Synopsis

Deletes the provided commit. The recursive flag must be used if the deleted commit has subvenance.

```
pachctl delete commitV2 <repo>@<branch-or-commit> [flags]
```

### Options

```
  -h, --help        help for commitV2
  -r, --recursive   Recursively delete all subvenant commits
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

