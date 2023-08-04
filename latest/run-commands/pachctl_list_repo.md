---
date: 2023-08-04T13:05:50-04:00
title: "pachctl list repo"
slug: "Learn about the pachctl_list_repo command"
---

## pachctl list repo

Return a list of repos.

### Synopsis

This command returns a list of repos that you have permissions to view. By default, it does not show system repos like pipeline metadata. 

	- To view all input repos across projects, use `-A` flag 
	- To view all repos in a specific project, including system repos, use the `--all` flag 
	- To view repos of a specific type, use the `--type` flag; options include `USER`, `META`, & `SPEC` 
	- To view repos of a specific type across projects, use the `--type` and `-A` flags 
	- To view repos of a specific type in a specific project, use the `--type` and `--project` flags 

For information on roles and permissions, see the documentation: https://docs.pachyderm.com/latest/set-up/authorization/permissions/

```
pachctl list repo [flags]
```

### Examples

```
	- pachctl list repos 
	- pachctl list repo -A 
	- pachctl list repo --all 
	- pachctl list repo --type user 
	- pachctl list repo --type user --all 
	- pachctl list repo --type user --all --project default 
	- pachctl list repo --type user --all --project default --raw
```

### Options

```
      --all               Specify all repo types should be returned, including hidden system repos.
  -A, --all-projects      Specify all repos across all projects should be returned.
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for repo
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) where the repos are located. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
      --type string       Set a repo type for scoped results. (default "user")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](/commands/pachctl_list/)	 - Print a list of Pachyderm resources of a specific type.

