---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth set repo"
description: "Learn about the pachctl auth set repo command"
---

## pachctl auth set repo

Set the roles that a subject has on repo

### Synopsis

This command sets the roles (`repoReader`, `repoWriter`, `repoOwner`) that a subject (user, robot) has on a given repo.

```
pachctl auth set repo <repo> [role1,role2 | none ] <subject> [flags]
```

### Examples

```
 pachctl auth set repo foo repoOwner user:alan.watts@domain.com pachctl auth set repo foo repoWriter, repoReader robot:my-robot pachctl auth set repo foo none robot:my-robot --project foobar
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

* [pachctl auth set](../pachctl_auth_set)	 - Set the role bindings for a resource

