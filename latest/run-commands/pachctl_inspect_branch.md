---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect branch"
slug: "Learn about the pachctl_inspect_branch command"
---

## pachctl inspect branch

Return info about a branch.

### Synopsis

This command returns info about a branch, such as its `Name`, `Head Commit`, and `Trigger`. 

	- To inspect a branch from a repo in another project, use the `--project` flag 
	- To get additional details about the branch, use the `--raw` flag 


```
pachctl inspect branch  <repo>@<branch> [flags]
```

### Examples

```
	- pachctl inspect branch foo@master  
	- pachctl inspect branch foo@master --project bar 
	- pachctl inspect branch foo@master --raw 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for branch
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) containing branch's repo. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl inspect](/commands/pachctl_inspect/)	 - Show detailed information about a Pachyderm resource.

