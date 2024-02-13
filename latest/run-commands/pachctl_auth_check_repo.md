---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth check repo"
description: "Learn about the pachctl auth check repo command"
---

## pachctl auth check repo

Check the permissions a user has on a repo

### Synopsis

This command checks the permissions a given subject (user, robot) has on a given repo.

```
pachctl auth check repo <repo> [<user>] [flags]
```

### Examples

```
 pachctl auth check repo foo user:alan.watts@domain.com pachctl auth check repo foo user:alan.watts@domain.com --project bar pachctl auth check repo foo robot:my-robot
```

### Options

```
  -h, --help             help for repo
      --project string   Define the project containing the repo. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth check](../pachctl_auth_check)	 - Check whether a subject has a permission on a resource

