---
date: 2024-02-13T16:12:03-05:00
title: "pachctl idp create-connector"
description: "Learn about the pachctl idp create-connector command"
---

## pachctl idp create-connector

Create a new identity provider connector.

### Synopsis

This command creates a new identity provider connector via a YAML configuration file or through stdin.

```
pachctl idp create-connector [flags]
```

### Examples

```
pachctl idp create-connector --config settings.yaml
```

### Options

```
      --config string   Set the file to read the YAML-encoded connector configuration from, or use '-' for stdin. (default "-")
  -h, --help            help for create-connector
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

