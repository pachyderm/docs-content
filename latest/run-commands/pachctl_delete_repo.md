---
date: 2023-08-04T13:05:50-04:00
title: "pachctl delete repo"
slug: "Learn about the pachctl_delete_repo command"
---

## pachctl delete repo

Delete a repo.

### Synopsis

This command deletes a repo. If this is a shared resource, it will be deleted for other users as well. 

	- To force delete a repo, use the `--force` flag; use with caution 
	- To delete all repos across all projects, use the `--all` flag 
	- To delete a repo of a specific type, use the `--type` flag; options include `USER`, `META`, & `SPEC` 
	- To delete all repos of a specific type across all projects, use the `--all` and `--type` flags 
	- To delete all repos of a specific type in a specific project, use the `--all`, `--type`, and `--project` flags 



```
pachctl delete repo <repo> [flags]
```

### Examples

```
	- pachctl delete repo foo 
	- pachctl delete repo foo --force 
	- pachctl delete repo --type user 
	- pachctl delete repo --all 
	- pachctl delete repo --all --type user 
	- pachctl delete repo --all --type user --project default
```

### Options

```
      --all              remove all repos
  -A, --all-projects     Delete repo(s) across all projects; only valid with --all.
  -f, --force            Force repo deletion, regardless of errors; use with caution.
  -h, --help             help for repo
      --project string   Specify the project (by name) where the to-be-deleted repo is located. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

