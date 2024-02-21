---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth get repo"
description: "Learn about the pachctl auth get repo command"
---

## pachctl auth get repo

Get the role bindings for a repo.

### Synopsis

This command returns the role bindings for a given repo.

```
pachctl auth get repo <repo> [flags]
```

### Examples

```
 pachctl auth get repo foo pachctl auth get repo foo --project bar
```

### Options

```
  -h, --help             help for repo
      --project string   The project containing the repo. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth get](../pachctl_auth_get)	 - Get the role bindings for a resource

