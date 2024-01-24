---
date: 2023-10-18T16:51:53-04:00
title: "pachctl idp update-client"
description: "Learn about the pachctl idp update-client command"
---

## pachctl idp update-client

Update an OIDC client.

### Synopsis

This command updates an OIDC client's settings via a YAML configuration file or stdin input.

```
pachctl idp update-client [flags]
```

### Examples

```
pachctl idp update-client --config settings.yaml
```

### Options

```
      --config string   Set the file to read the YAML-encoded client configuration from, or use '-' for stdin. (default "-")
  -h, --help            help for update-client
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

