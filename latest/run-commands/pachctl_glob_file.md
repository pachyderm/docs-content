---
date: 2023-08-04T13:05:50-04:00
title: "pachctl glob file"
---

## pachctl glob file

Return files that match a glob pattern in a commit.

### Synopsis

This command returns files that match a glob pattern in a commit (that is, match a glob pattern in a repo at the state represented by a commit). Glob patterns are documented [here](https://golang.org/pkg/path/filepath/#Match). 

	- To specify the project where the repo is located, use the `--project flag` 


```
pachctl glob file "<repo>@<branch-or-commit>:<pattern>" [flags]
```

### Examples

```
	- pachctl glob file "foo@master:A*"
	- pachctl glob file "foo@0001a0100b1c10d01111e001fg00h00i:data/*"
	- pachctl glob file "foo@master:data/*"
```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for file
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) where the repo with potential matching file(s) is located. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

