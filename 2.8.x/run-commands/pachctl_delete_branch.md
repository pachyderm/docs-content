---
date: 2023-10-18T16:51:53-04:00
title: "pachctl delete branch"
description: "Learn about the pachctl delete branch command"
---

## pachctl delete branch

Delete a branch

### Synopsis

This command deletes a branch while leaving its commits intact. 

 To delete a branch from a repo in another project, use the `--project` flag 
 To delete a branch regardless of errors, use the `--force` flag 


```
pachctl delete branch <repo>@<branch> [flags]
```

### Examples

```
 pachctl delete branch foo@master 
 pachctl delete branch foo@master --project bar 
 pachctl delete branch foo@master --force 
 pachctl delete branch foo@master --project bar --force 

```

### Options

```
  -f, --force            Force branch deletion regardless of errors; use with caution.
  -h, --help             help for branch
      --project string   Specify the project (by name) containing branch's repo. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

