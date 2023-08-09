---
date: 2023-08-04T13:05:50-04:00
title: "pachctl fsck"
---

## pachctl fsck

Run a file system consistency check on PFS.

### Synopsis

This command runs a file system consistency check on the Pachyderm file system, ensuring the correct provenance relationships are satisfied.

```
pachctl fsck [flags]
```

### Examples

```
	- pachctl fsck 
	- pachctl fsck --fix 
	- pachctl fsck --zombie-all 
	- pachctl fsck --zombie foo@bar 
	- pachctl fsck --zombie foo@bar --project projectContainingFoo 

```

### Options

```
  -f, --fix              Attempt to fix as many issues as possible.
  -h, --help             help for fsck
      --project string   Specify the project (by name) where the repo of the branch/commit is located. (default "standard-ml-tutorial")
      --zombie string    Set a single commit (by id) to check for zombie files
      --zombie-all       Check all pipelines for zombie files: files corresponding to old inputs that were not properly deleted.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

