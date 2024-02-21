---
date: 2024-02-13T16:12:03-05:00
title: "pachctl idp create-client"
description: "Learn about the pachctl idp create-client command"
---

## pachctl idp create-client

Create a new OIDC client.

### Synopsis

This command creates a new OIDC client via a YAML configuration file or through stdin.

```
pachctl idp create-client [flags]
```

### Examples

```
pachctl idp create-client --config settings.yaml
```

### Options

```
      --config string   Set the file to read the YAML-encoded client configuration from, or use '-' for stdin. (default "-")
  -h, --help            help for create-client
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

