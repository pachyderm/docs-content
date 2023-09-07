---
date: 2023-09-07T13:28:03-04:00
title: "pachctl list commit"
description: "Learn about the pachctl_list_commit command"
---

## pachctl list commit

Return a list of commits.

### Synopsis

This command returns a list of commits, either across the entire pachyderm cluster or restricted to a single repo. 

 To specify which project the repo is in, use the `--project` flag 
 To specify the number of commits to return, use the `--number` flag 
 To list all commits that have come after a certain commit, use the `--from` flag 
 To specify the origin of the commit, use the `--origin` flag; options include `AUTO`, `FSCK`, & `USER`. Requires at least repo name in command 
 To expand the commit to include all of its sub-commits, use the `--expand` flag 


```
pachctl list commit [<commit-id>|<repo>[@<branch-or-commit>]] [flags]
```

### Examples

```
 pachctl list commit foo ➔ returns all commits in repo foo 
 pachctl list commit foo@master ➔ returns all commits in repo foo on branch master 
 pachctl list commit foo@master --number 10 ➔ returns the last 10 commits in repo foo on branch master 
 pachctl list commit foo@master --from 0001a0100b1c10d01111e001fg00h00i ➔ returns all commits in repo foo on branch master since <commit> 
 pachctl list commit foo@master --origin user ➔ returns all commits in repo foo on branch master originating from 
 pachctl list commit 0001a0100b1c10d01111e001fg00h00i ➔ returns all commits with ID <commit-id> 
 pachctl list commit 0001a0100b1c10d01111e001fg00h00i --expand ➔ returns all sub-commits on new lines, along with columns of more information 
 pachctl list commit foo@master --raw -o yaml ➔ returns all commits in repo foo on branch master in YAML format 

```

### Options

```
      --all               Specify all types of commits (AUTO, FSCK, USER) should be returned; default only includes USER.
  -x, --expand            Specify results should return one line for each sub-commit and include more columns.
  -f, --from string       Set the starting point of the commit range to list.
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for commit
  -n, --number int        Set the limit of returned results; if zero, list all commits.
      --origin string     Specify the type of commit to scope returned results by; options include AUTO, FSCK, & USER.
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) containing the commit. (default "video-to-frame-traces")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

