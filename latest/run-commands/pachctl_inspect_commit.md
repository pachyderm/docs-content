---
date: 2023-09-07T13:28:03-04:00
title: "pachctl inspect commit"
description: "Learn about the pachctl_inspect_commit command"
---

## pachctl inspect commit

Return info about a commit.

### Synopsis

This command returns information about the commit, such as the commit location (`branch@commit-id`), originating branch, start/finish times, and size. 

 To view the raw details of the commit in JSON format, use the `--raw` flag 
 To specify which project the repo is in, use the `--project` flag 


```
pachctl inspect commit <repo>@<branch-or-commit> [flags]
```

### Examples

```
 pachctl inspect commit foo@master 
 pachctl inspect commit foo@master --project bar 
 pachctl inspect commit foo@master --raw 
 pachctl inspect commit foo@0001a0100b1c10d01111e001fg00h00i --project bar --raw 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for commit
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) where the repo for this commit is located. (default "video-to-frame-traces")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl inspect](../pachctl_inspect)	 - Show detailed information about a Pachyderm resource.

