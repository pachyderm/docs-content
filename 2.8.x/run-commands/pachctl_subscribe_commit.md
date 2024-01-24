---
date: 2023-10-18T16:51:53-04:00
title: "pachctl subscribe commit"
description: "Learn about the pachctl subscribe commit command"
---

## pachctl subscribe commit

Print commits as they are created (finished).

### Synopsis

This command prints commits as they are created in the specified repo and branch. By default, all existing commits on the specified branch are returned first.  A commit is only considered created when it's been finished.
 To only see commits created after a certain commit, use the `--from` flag. 
 To only see new commits created from now on, use the `--new` flag. 
 To see all commit types, use the `--all` flag.
 To only see commits of a specific type, use the `--origin` flag. 


```
pachctl subscribe commit <repo>[@<branch>] [flags]
```

### Examples

```
 pachctl subscribe commit foo@master ➔ subscribe to commits in the foo repo on the master branch 
 pachctl subscribe commit foo@bar --from 0001a0100b1c10d01111e001fg00h00i ➔ starting at <commit-id>, subscribe to commits in the foo repo on the master branch 
 pachctl subscribe commit foo@bar --new ➔ subscribe to commits in the foo repo on the master branch, but only for new commits created from now on 

```

### Options

```
      --all               Specify results should return all types of commits (AUTO, FSCK, USER)
      --from string       Subscribe to and return all commits since the specified commit.
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for commit
      --new               Subscribe to and return only new commits created from now on.
      --origin string     Specify results should only return commits of a specific type; options include AUTO, FSCK, & USER.
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

* [pachctl subscribe](../pachctl_subscribe)	 - Wait for notifications of changes to a Pachyderm resource.

