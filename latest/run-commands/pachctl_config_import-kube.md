---
date: 2023-10-18T16:51:53-04:00
title: "pachctl config import-kube"
description: "Learn about the pachctl config import-kube command"
---

## pachctl config import-kube

Import a Kubernetes context as a Pachyderm context, and set the active Pachyderm context.

### Synopsis

This command imports a Kubernetes context as a Pachyderm context. By default the current kubernetes context is used.

```
pachctl config import-kube <context> [flags]
```

### Examples

```
 pachctl config import-kube foo 
 pachctl config import-kube foo --overwrite
```

### Options

```
  -e, --enterprise          Configure an enterprise server context.
  -h, --help                help for import-kube
  -k, --kubernetes string   Specify the kubernetes context's values to import.
  -n, --namespace string    Specify a namespace where Pachyderm is deployed.
  -o, --overwrite           Overwrite a context if it already exists.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config](../pachctl_config)	 - Manages the pachyderm config.

