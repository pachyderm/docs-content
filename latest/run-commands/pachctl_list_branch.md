---
date: 2023-08-04T13:05:50-04:00
title: "pachctl list branch"
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
	- pachctl list branch foo@master 
	- pachctl list branch foo@master --project bar 
	- pachctl list branch foo@master --raw 
	- pachctl list branch foo@master --raw -o yaml 

```

### Options

```
  -h, --help             help for branch
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Specify the project (by name) containing branch's repo. (default "standard-ml-tutorial")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

