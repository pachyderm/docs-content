---
date: 2024-02-13T16:12:03-05:00
title: "pachctl start commit"
description: "Learn about the pachctl start commit command"
---

## pachctl start commit

Start a new commit.

### Synopsis

This command starts a new commit with parent-commit as the parent on the given branch; if the branch does not exist, it will be created. 

 To specify a parent commit, use the `--parent` flag 
 To add a message to the commit, use the `--message` or `--description` flag 
 To specify which project the repo is in, use the `--project` flag 


```
pachctl start commit <repo>@<branch> [flags]
```

### Examples

```
 pachctl start commit foo@master 
 pachctl start commit foo@master -p 0001a0100b1c10d01111e001fg00h00i 
 pachctl start commit foo@master --message 'my commit message' 
 pachctl start commit foo@master --description 'my commit description' 
 pachctl start commit foo@master --project bar
```

### Options

```
      --description string   Set a description of this commit's contents (synonym for --message). (default "d")
  -h, --help                 help for commit
  -m, --message string       Set a description for the commit's contents (synonym for --description).
  -p, --parent string        Set the parent (by id) of the new commit; only needed when branch is not specified using the @ syntax.
      --project string       Specify the project (by name) where the repo for this commit is located. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl start](../pachctl_start)	 - Start a Pachyderm resource.

