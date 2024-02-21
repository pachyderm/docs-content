---
date: 2024-02-13T16:12:03-05:00
title: "pachctl create secret"
description: "Learn about the pachctl create secret command"
---

## pachctl create secret

Create a secret on the cluster.

### Synopsis

This command creates a secret on the cluster.

```
pachctl create secret [flags]
```

### Examples

```
 pachctl create secret --file my-secret.json
```

### Options

```
  -f, --file string   File containing Kubernetes secret.
  -h, --help          help for secret
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.

