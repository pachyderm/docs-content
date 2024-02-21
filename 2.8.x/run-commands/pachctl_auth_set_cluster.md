---
date: 2023-10-18T16:51:53-04:00
title: "pachctl auth set cluster"
description: "Learn about the pachctl auth set cluster command"
---

## pachctl auth set cluster

Set the roles that a subject has on the cluster

### Synopsis

This command sets the roles that a given subject has on the cluster.

```
pachctl auth set cluster [role1,role2 | none ] subject [flags]
```

### Examples

```
 pachctl auth set cluster clusterOwner user:alan.watts@domain.com 
 pachctl auth set cluster clusterWriter, clusterReader robot:my-robot
```

### Options

```
  -h, --help   help for cluster
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth set](../pachctl_auth_set)	 - Set the role bindings for a resource

