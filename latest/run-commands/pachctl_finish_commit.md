---
date: 2023-08-04T13:05:50-04:00
title: "pachctl finish commit"
slug: "Learn about the pachctl_finish_commit command"
---

## pachctl finish commit

Finish a started commit.

### Synopsis

This command finishes a started commit. 

	- To force finish a commit, use the `--force` flag 
	- To add a message to the commit, use the `--message` or `--description` flag 
	- To specify which project the repo is in, use the `--project` flag 


```
pachctl finish commit <repo>@<branch-or-commit> [flags]
```

### Examples

```
	- pachctl finish commit foo@master 
	- pachctl finish commit foo@master --force 
	- pachctl finish commit foo@master --project bar	- pachctl finish commit foo@master --message 'my commit message' 
	- pachctl finish commit foo@master --description 'my commit description' --project bar 

```

### Options

```
      --description string   Set a description of this commit's contents; overwrites existing commit description (synonym for --message).
  -f, --force                Force finish commit, even if it has provenance, which could break jobs; prefer 'pachctl stop stop job'
  -h, --help                 help for commit
  -m, --message string       Set a description of this commit's contents; overwrites existing commit description (synonym for --description).
      --project string       Specify the project (by name) where the repo for this commit is located. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl finish](/commands/pachctl_finish/)	 - Finish a Pachyderm resource.

