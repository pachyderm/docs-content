---
date: 2023-09-07T13:28:03-04:00
title: "pachctl auth get-groups"
description: "Learn about the pachctl_auth_get-groups command"
---

## pachctl auth get-groups

Get the list of groups a user belongs to

### Synopsis

Get the list of groups a user belongs to. If no user is specified, the current user's groups are listed.

```
pachctl auth get-groups [username] [flags]
```

### Options

```
      --enterprise   Get group membership info from the enterprise server
  -h, --help         help for get-groups
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

