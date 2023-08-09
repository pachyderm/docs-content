---
date: 2023-08-04T13:05:50-04:00
title: "pachctl create secret"
slug: "Learn about the pachctl_create_secret command"
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
	- pachctl create secret --file my-secret.json
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

