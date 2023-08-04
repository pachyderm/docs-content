---
date: 2023-08-04T13:05:50-04:00
title: "pachctl diff file"
slug: "Learn about the pachctl_diff_file command"
---

## pachctl diff file

Return a diff of two file trees stored in Pachyderm

### Synopsis

This command returns a diff of two file trees stored in Pachyderm. The file trees are specified by two files, one from the new tree and one from the old tree. 
	- To specify the project where the repos are located, use the `--project flag` 
	- To specify the project where the second older repo is located, use the `--old-project flag` 
	- To prevent descending into sub-directories, use the `--shallow flag`
	- To use an alternative (non-git) diff command, use the `--diff-command flag` 
	- To get only the names of changed files, use the `--name-only flag` 


```
pachctl diff file <new-repo>@<new-branch-or-commit>:<new-path> [<old-repo>@<old-branch-or-commit>:<old-path>] [flags]
```

### Examples

```
	- pachctl diff file foo@master:/logs/log.txt 
	- pachctl diff file foo@0001a0100b1c10d01111e001fg00h00i:log.txt 
	- pachctl diff file foo@master:path1 bar@master:path2
```

### Options

```
      --diff-command string   Set a git-alternative program to diff files.
      --full-timestamps       Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help                  help for file
      --name-only             Specify results should only return the names of changed files.
      --no-pager              Don't pipe output into a pager (i.e. less).
      --old-project string    Specify the project (by name) where the second, older repo is located.
      --project string        Specify the project (by name) where the first repo is located. (default "standard-ml-tutorial")
  -s, --shallow               Specify results should not to descend into sub directories.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl diff](/commands/pachctl_diff/)	 - Show the differences between two Pachyderm resources.

