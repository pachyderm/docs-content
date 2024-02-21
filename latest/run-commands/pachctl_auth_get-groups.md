---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth get-groups"
description: "Learn about the pachctl auth get-groups command"
---

## pachctl auth get-groups

Get the list of groups a user belongs to

### Synopsis

This command returns the list of groups a user belongs to. If no user is specified, the current user's groups are listed.

```
pachctl auth get-groups [username] [flags]
```

### Examples

```
 pachctl auth get-groups pachctl auth get-groups alan.watts@domain.com pachctl auth get-groups alan.watts@domain.com --enterprise
```

### Options

```
      --enterprise   Get group membership info from the enterprise server.
  -h, --help         help for get-groups
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

