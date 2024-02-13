---
date: 2024-02-13T16:12:03-05:00
title: "pachctl license delete-cluster"
description: "Learn about the pachctl license delete-cluster command"
---

## pachctl license delete-cluster

Delete a cluster registered with the license server.

### Synopsis

This command deletes a cluster registered with Enterprise Server.

```
pachctl license delete-cluster [flags]
```

### Examples

```
 pachctl license delete-cluster --id=my-cluster

```

### Options

```
  -h, --help        help for delete-cluster
      --id string   Set the ID for the cluster to delete.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service

