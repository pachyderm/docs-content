---
date: 2024-02-13T16:12:03-05:00
title: "pachctl squash commitV2"
description: "Learn about the pachctl squash commitV2 command"
---

## pachctl squash commitV2

Squash a commit.

### Synopsis

Squashes the provided commit into its children. The recursive flag must be used if the squashed commit has subvenance.

```
pachctl squash commitV2 <repo>@<branch-or-commit> [flags]
```

### Options

```
  -h, --help        help for commitV2
  -r, --recursive   Recursively squash all subvenant commits
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl squash](../pachctl_squash)	 - Squash an existing Pachyderm resource.

