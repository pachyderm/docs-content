---
date: 2024-02-13T16:12:03-05:00
title: "pachctl idp delete-client"
description: "Learn about the pachctl idp delete-client command"
---

## pachctl idp delete-client

Delete an OIDC client.

### Synopsis

This command deletes an OIDC client by passing the clients's ID. You can get a list of IDs by running `pachctl idp list-client`.

```
pachctl idp delete-client <client ID> [flags]
```

### Options

```
  -h, --help   help for delete-client
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

