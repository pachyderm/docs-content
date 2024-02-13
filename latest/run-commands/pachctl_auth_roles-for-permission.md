---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth roles-for-permission"
description: "Learn about the pachctl auth roles-for-permission command"
---

## pachctl auth roles-for-permission

List roles that grant the given permission

### Synopsis

This command lists roles that grant the given permission.

```
pachctl auth roles-for-permission <permission> [flags]
```

### Examples

```
 pachctl auth roles-for-permission repoOwner pachctl auth roles-for-permission clusterAdmin
```

### Options

```
  -h, --help   help for roles-for-permission
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

