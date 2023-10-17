---
date: 2023-09-07T13:28:03-04:00
title: "pachctl auth set repo"
description: "Learn about the pachctl_auth_set_repo command"
---

## pachctl auth set repo

Set the roles that 'subject' has on 'repo'

### Synopsis

Set the roles that 'subject' has on 'repo'

```
pachctl auth set repo <repo> [role1,role2 | none ] <subject> [flags]
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

