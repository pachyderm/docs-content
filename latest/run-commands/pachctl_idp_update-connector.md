---
date: 2023-10-18T16:51:53-04:00
title: "pachctl idp update-connector"
description: "Learn about the pachctl idp update-connector command"
---

## pachctl idp update-connector

Update an existing identity provider connector.

### Synopsis

This command updates an existing identity provider connector. Only fields which are specified are updated.

```
pachctl idp update-connector [flags]
```

### Examples

```
pachctl idp update-connector --config settings.yaml
```

### Options

```
      --config string   Set the file to read the YAML-encoded connector configuration from, or use '-' for stdin. (default "-")
  -h, --help            help for update-connector
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

