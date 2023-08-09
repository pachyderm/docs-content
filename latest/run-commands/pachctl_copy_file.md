---
date: 2023-08-04T13:05:50-04:00
title: "pachctl copy file"
---

## pachctl copy file

Copy files between pfs paths.

### Synopsis

This command copies files between pfs paths. While using this command, take special note of which project is set to your active context by running `pachctl list projects` and checking for the `*` in the ACTIVE column. 

	- To append to an existing file, use the --append flag.
	- To specify the project where both the source and destination repos are located, use the --project flag. This is only necessary if the project in question is not set to your active context.
	- To copy a file from one project to another, use the --src-project and --dest-project flags. Needing to use one (or both) depends on whether or not either project is set to your active context.


```
pachctl copy file <src-repo>@<src-branch-or-commit>:<src-path> <dst-repo>@<dst-branch-or-commit>:<dst-path> [flags]
```

### Examples

```
	- pachctl copy file foo@master:/file bar@master:/file 
	- pachctl copy file foo@0001a0100b1c10d01111e001fg00h00i:/file bar@master:/file 
	- pachctl copy file foo@master:/file bar@master:/file --project ProjectContainingFooAndBar 
	- pachctl copy file foo@master:/file bar@master:/file --dest-project ProjectContainingBar 
	- pachctl copy file foo@master:/file bar@master:/file --src-project ProjectContainingFoo 
	- pachctl copy file foo@master:/file bar@master:/file --src-project ProjectContainingFoo --dest-project ProjectContainingBar
```

### Options

```
  -a, --append                Append to the existing content of the file, either from previous commits or previous calls to 'put file' within this commit.
      --dest-project string   Specify the project (by name) where the destination repo is located; this overrides --project.
  -h, --help                  help for file
      --project string        Specify the project (by name) where both source and destination repos are located. (default "standard-ml-tutorial")
      --src-project string    Specify the project (by name) where the source repo is located; this overrides --project.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```