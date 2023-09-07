---
date: 2023-09-07T13:28:03-04:00
title: "pachctl license add-cluster"
description: "Learn about the pachctl_license_add-cluster command"
---

## pachctl license add-cluster

Register a new cluster with the license server.

### Synopsis

Register a new cluster with the license server.

```
pachctl license add-cluster [flags]
```

### Options

```
      --address string   The host and port where the cluster can be reached
  -h, --help             help for add-cluster
      --id string        The id for the cluster to register
      --secret string    The shared secret to use to authenticate this cluster
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service

