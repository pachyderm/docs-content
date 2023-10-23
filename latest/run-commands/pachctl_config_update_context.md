---
date: 2023-10-18T16:51:53-04:00
title: "pachctl config update context"
description: "Learn about the pachctl config update context command"
---

## pachctl config update context

Updates a context.

### Synopsis

This command updates an existing context config from a given name (or the currently-active context, if no name is given).

```
pachctl config update context [<context>] [flags]
```

### Examples

```
 pachctl config update context foo 
 pachctl config update context foo --pachd-address localhost:30650 
 pachctl config update context foo --cluster-name my-cluster 
 pachctl config update context foo --auth-info my-auth-info 
 pachctl config update context foo --server-cas /path/to/ca.crt 
 pachctl config update context foo --namespace my-namespace 
 pachctl config update context foo --project my-project 
 pachctl config update context foo --remove-cluster-deployment-id
```

### Options

```
      --auth-info string               Set a new k8s auth info.
      --cluster-name string            Set a new cluster name.
  -h, --help                           help for context
      --namespace string               Set a new namespace.
      --pachd-address string           Set a new name pachd address.
      --project string                 Set a new project.
      --remove-cluster-deployment-id   Remove the cluster deployment ID field, which will be repopulated on the next 'pachctl' call using this context.
      --server-cas string              Set new trusted CA certs.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config update](../pachctl_config_update)	 - Commands for updating pachyderm config values

