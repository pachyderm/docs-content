---
date: 2024-02-13T16:12:03-05:00
title: "pachctl license update-cluster"
description: "Learn about the pachctl license update-cluster command"
---

## pachctl license update-cluster

Update an existing cluster registered with the license server.

### Synopsis

This command updates an existing cluster registered with Enterprise Server.

```
pachctl license update-cluster [flags]
```

### Examples

```
 pachctl license update-cluster --id=my-cluster --address=grpc://my-cluster:1653 
 pachctl license update-cluster --id=my-cluster --user-address=grpc://my-cluster:1653
 pachctl license update-cluster --id=my-cluster --cluster-deployment-id=1234

```

### Options

```
      --address string                 Set the host and port where the cluster can be reached by the enterprise server.
      --cluster-deployment-id string   Set the deployment ID of the updated cluster.
  -h, --help                           help for update-cluster
      --id string                      Set the ID for the cluster to update.
      --user-address string            Set the host and port where the cluster can be reached by a user.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service

