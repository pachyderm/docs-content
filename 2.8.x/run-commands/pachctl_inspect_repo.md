---
date: 2023-10-18T16:51:53-04:00
title: "pachctl inspect repo"
description: "Learn about the pachctl inspect repo command"
---

## pachctl inspect repo

Return info about a repo.

### Synopsis

This command returns details of the repo such as: `Name`, `Description`, `Created`, and `Size of HEAD on Master`. By default, PachCTL checks for a matching repo in the project that is set to your active context (initially the `default` project).

 To specify the project containing the repo you want to inspect, use the `--project` flag 


```
pachctl inspect repo <repo> [flags]
```

### Examples

```
 pachctl inspect repo foo  
 pachctl inspect repo foo --project myproject
```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for repo
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) where the repo is located. (default "video-to-frame-traces")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl inspect](../pachctl_inspect)	 - Show detailed information about a Pachyderm resource.

