---
date: 2023-09-07T13:28:03-04:00
title: "pachctl enterprise register"
description: "Learn about the pachctl_enterprise_register command"
---

## pachctl enterprise register

Register the cluster with an enterprise license server

### Synopsis

Register the cluster with an enterprise license server

```
pachctl enterprise register [flags]
```

### Options

```
      --cluster-deployment-id string       the deployment id of the cluster being registered
      --enterprise-server-address string   the address for the pachd to reach the enterprise server
  -h, --help                               help for register
      --id string                          the id for this cluster
      --pachd-address string               the address for the enterprise server to reach this pachd
      --pachd-user-address string          the address for a user to reach this pachd
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl enterprise](../pachctl_enterprise)	 - Enterprise commands enable Pachyderm Enterprise features

