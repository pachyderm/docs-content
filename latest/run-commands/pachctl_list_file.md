---
date: 2023-08-04T13:05:50-04:00
title: "pachctl list file"
slug: "Learn about the pachctl_list_file command"
---

## pachctl list file

Return the files in a directory.

### Synopsis

This command returns the files in a directory. While using this command, take special note of how you can use ancestry syntax (e.g., appending`^2` or `.-1` to `repo@branch`) to inspect the contents of a file from a previous commit. 
	- To specify the project where the repo is located, use the --project flag 


```
pachctl list file <repo>@<branch-or-commit>[:<path/in/pfs>] [flags]
```

### Examples

```
	- pachctl list file foo@master 
	- pachctl list file foo@master:dir 
	- pachctl list file foo@master^ 
	- pachctl list file foo@master^2 
	- pachctl list file repo@master.-2  --project foo 
	- pachctl list file 'foo@master:dir\[1\]'

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for file
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) where repo is located. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](/commands/pachctl_list/)	 - Print a list of Pachyderm resources of a specific type.

