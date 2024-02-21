---
date: 2024-02-13T16:12:03-05:00
title: "pachctl idp get-client"
description: "Learn about the pachctl idp get-client command"
---

## pachctl idp get-client

Get an OIDC client.

### Synopsis

This command returns an OIDC client's settings, such as its name, ID, redirect URIs, secrets, and trusted peers. You can get a list of IDs by running `pachctl idp list-client`.

```
pachctl idp get-client <client ID> [flags]
```

### Options

```
  -h, --help   help for get-client
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

