---
date: 2023-10-18T16:51:53-04:00
title: "pachctl delete commit"
description: "Learn about the pachctl delete commit command"
---

## pachctl delete commit

Delete the sub-commits of a commit.

### Synopsis

This command deletes the sub-commits of a commit; data in sub-commits will be lost, so use with caution. This operation is only supported if none of the sub-commits have children. 

```
pachctl delete commit <commit-id> [flags]
```

### Examples

```
 pachctl delete commit 0001a0100b1c10d01111e001fg00h00i
```

### Options

```
  -h, --help   help for commit
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

