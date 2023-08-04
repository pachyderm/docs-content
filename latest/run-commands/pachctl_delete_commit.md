---
date: 2023-08-04T13:05:50-04:00
title: "pachctl delete commit"
slug: "Learn about the pachctl_delete_commit command"
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
	- pachctl delete commit 0001a0100b1c10d01111e001fg00h00i
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

* [pachctl delete](/commands/pachctl_delete/)	 - Delete an existing Pachyderm resource.

