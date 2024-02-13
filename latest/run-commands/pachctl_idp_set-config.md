---
date: 2024-02-13T16:12:03-05:00
title: "pachctl idp set-config"
description: "Learn about the pachctl idp set-config command"
---

## pachctl idp set-config

Set the identity server config

### Synopsis

This command sets the identity server config via a YAML configuration file or by using `-` for stdin; requires an active enterprise key and authentication to be enabled.

```
pachctl idp set-config [flags]
```

### Examples

```
pachctl idp set-config --config settings.yaml
```

### Options

```
      --config string   Set the file to read the YAML-encoded configuration from, or use '-' for stdin. (default "-")
  -h, --help            help for set-config
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

