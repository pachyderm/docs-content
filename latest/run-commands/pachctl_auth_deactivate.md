---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth deactivate"
description: "Learn about the pachctl auth deactivate command"
---

## pachctl auth deactivate

Delete all ACLs, tokens, admins, IDP integrations and OIDC clients, and deactivate Pachyderm auth

### Synopsis

This command deactivates Pachyderm's auth and identity systems, which exposes data to everyone on the network. Use with caution. 

```
pachctl auth deactivate [flags]
```

### Examples

```
 pachctl auth deactivate pachctl auth deactivate --enterprise
```

### Options

```
      --enterprise   Deactivate auth on the active enterprise context.
  -h, --help         help for deactivate
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

