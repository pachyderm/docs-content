---
date: 2023-10-18T16:51:53-04:00
title: "pachctl idp get-connector"
description: "Learn about the pachctl idp get-connector command"
---

## pachctl idp get-connector

Get the config for an identity provider connector.

### Synopsis

This command returns the config for an identity provider connector by passing the connector's ID. You can get a list of IDs by running `pachctl idp list-connector`.

```
pachctl idp get-connector <connector id> [flags]
```

### Options

```
  -h, --help   help for get-connector
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

