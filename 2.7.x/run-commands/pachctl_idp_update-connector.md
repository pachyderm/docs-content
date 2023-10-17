---
date: 2023-09-07T13:28:03-04:00
title: "pachctl idp update-connector"
description: "Learn about the pachctl_idp_update-connector command"
---

## pachctl idp update-connector

Update an existing identity provider connector.

### Synopsis

Update an existing identity provider connector. Only fields which are specified are updated.

```
pachctl idp update-connector [flags]
```

### Options

```
      --config string   The file to read the YAML-encoded connector configuration from, or '-' for stdin. (default "-")
  -h, --help            help for update-connector
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

