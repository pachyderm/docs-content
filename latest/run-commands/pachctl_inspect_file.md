---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect file"
---

## pachctl inspect file

Return info about a file.

### Synopsis

This command returns info about a file.While using this command, take special note of how you can use ancestry syntax (e.g., appending`^2` or `.-1` to `repo@branch`) to inspect the contents of a file from a previous commit. 
	- To specify the project where the repo is located, use the --project flag 


```
pachctl inspect file <repo>@<branch-or-commit>:<path/in/pfs> [flags]
```

### Examples

```
	- pachctl inspect file repo@master:/logs/log.txt 
	- pachctl inspect file repo@0001a0100b1c10d01111e001fg00h00i:/logs/log.txt 
	- pachctl inspect file repo@master:/logs/log.txt^2 
	- pachctl inspect file repo@master:/logs/log.txt.-1 
	- pachctl inspect file repo@master:/logs/log.txt^2  --project foo 

```

### Options

```
  -h, --help             help for file
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Specify the project (by name) where the file's repo is located. (default "standard-ml-tutorial")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

