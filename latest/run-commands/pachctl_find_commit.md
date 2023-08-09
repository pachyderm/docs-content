---
date: 2023-08-04T13:05:50-04:00
title: "pachctl find commit"
slug: "Learn about the pachctl_find_commit command"
---

## pachctl find commit

Find commits with reference to <filePath> within a branch starting from <repo@commitID>

### Synopsis

This command returns a list of commits using a reference to their `file/path` within a branch, starting from `repo@<commitID>`. 

	- To find commits from a repo in another project, use the `--project` flag 
	- To set a limit on the number of returned commits, use the `--limits` flag 
	- To set a timeout for your commit search, use the `--timeout` flag 
	- To print the results as json, use the `--json` flag 


```
pachctl find commit <repo>@<branch-or-commit>:<path/in/pfs> [flags]
```

### Examples

```
	- pachctl find commit foo@master:file 
	- pachctl find commit foo@master:file --project bar 
	- pachctl find commit foo@master:file --limit 10 
	- pachctl find commit foo@master:file --timeout 10s 
	- pachctl find commit foo@master:file --json 
	- pachctl find commit foo@master:file --project bar --json --limit 100 --timeout 20s 

```

### Options

```
  -h, --help               help for commit
      --json               Print the response in json.
      --limit uint32       Set the number of matching commits to return.
      --project string     Specify the project (by name) in which commits are located. (default "standard-ml-tutorial")
      --timeout duration   Set the search duration timeout.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

