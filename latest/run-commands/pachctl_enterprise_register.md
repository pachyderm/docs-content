---
date: 2024-02-13T16:12:03-05:00
title: "pachctl enterprise register"
description: "Learn about the pachctl enterprise register command"
---

## pachctl enterprise register

Register the cluster with an enterprise license server

### Synopsis

This command registers a given cluster with an enterprise license server. Enterprise servers also handle IdP authentication for the clusters registered to it.

```
pachctl enterprise register [flags]
```

### Examples

```
 pachctl enterprise register 
 pachctl enterprise register --id my-cluster-id 
 pachctl enterprise register --id my-cluster-id --pachd-address <pachd-ip>:650 
 pachctl enterprise register --id my-cluster-id --pachd-enterprise-server-address <pach-enterprise-IP>:650 

```

### Options

```
      --cluster-deployment-id string       Set the deployment id of the cluster being registered.
      --enterprise-server-address string   Set the address for the pachd to reach the enterprise server.
  -h, --help                               help for register
      --id string                          Set the ID for this cluster.
      --pachd-address string               Set the address for the enterprise server to reach this pachd.
      --pachd-user-address string          Set the address for a user to reach this pachd.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl enterprise](../pachctl_enterprise)	 - Enterprise commands enable Pachyderm Enterprise features

