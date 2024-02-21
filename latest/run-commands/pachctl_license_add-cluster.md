---
date: 2024-02-13T16:12:03-05:00
title: "pachctl license add-cluster"
description: "Learn about the pachctl license add-cluster command"
---

## pachctl license add-cluster

Register a new cluster with the license server.

### Synopsis

This command registers a new cluster with Enterprise Server.

```
pachctl license add-cluster [flags]
```

### Examples

```
 pachctl license add-cluster --id=my-cluster --address=grpc://my-cluster:1653 --secret=secret

```

### Options

```
      --address string   Set the host and port where the cluster can be reached.
  -h, --help             help for add-cluster
      --id string        Set the ID for the cluster to register.
      --secret string    Set the shared secret to use to authenticate this cluster.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service

