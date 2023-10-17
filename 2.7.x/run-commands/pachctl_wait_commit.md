---
date: 2023-09-07T13:28:03-04:00
title: "pachctl wait commit"
description: "Learn about the pachctl_wait_commit command"
---

## pachctl wait commit

Wait for the specified commit to finish and return it.

### Synopsis

This command waits for the specified commit to finish before returning it, allowing you to track your commits downstream as they are produced. Each line is printed as soon as a new (sub) commit of your global commit finishes.

```
pachctl wait commit <repo>@<branch-or-commit> [flags]
```

### Examples

```
 pachctl wait commit foo@0001a0100b1c10d01111e001fg00h00i 
 pachctl wait commit foo@0001a0100b1c10d01111e001fg00h00i --project bar 
 pachctl wait commit foo@0001a0100b1c10d01111e001fg00h00i --project bar --raw -o yaml 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for commit
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

* [pachctl wait](../pachctl_wait)	 - Wait for the side-effects of a Pachyderm resource to propagate.

