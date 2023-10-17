---
date: 2023-09-07T13:28:03-04:00
title: "pachctl list branch"
description: "Learn about the pachctl_list_branch command"
---

## pachctl list branch

Return all branches on a repo.

### Synopsis

This command returns all branches on a repo. 

- To list branches from a repo in another project, use the `--project` flag 
- To get additional details about the branches, use the `--raw` flag 


```
pachctl list branch <repo> [flags]
```

### Examples

```
 pachctl list branch foo@master 
 pachctl list branch foo@master --project bar 
 pachctl list branch foo@master --raw 
 pachctl list branch foo@master --raw -o yaml 

```

### Options

```
  -h, --help             help for branch
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Specify the project (by name) containing branch's repo. (default "video-to-frame-traces")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

