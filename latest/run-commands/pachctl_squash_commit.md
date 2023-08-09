---
date: 2023-08-04T13:05:50-04:00
title: "pachctl squash commit"
slug: "Learn about the pachctl_squash_commit command"
---

## pachctl squash commit

Squash the sub-commits of a commit.

### Synopsis

This command squashes the sub-commits of a commit.  The data in the sub-commits will remain in their child commits. The squash will fail if it includes a commit with no children

```
pachctl squash commit <commit-id> [flags]
```

### Examples

```
	- pachctl squash commit 0001a0100b1c10d01111e001fg00h00i 

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

