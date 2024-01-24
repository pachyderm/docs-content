---
date: 2023-10-18T16:51:53-04:00
title: "pachctl idp delete-connector"
description: "Learn about the pachctl idp delete-connector command"
---

## pachctl idp delete-connector

Delete an identity provider connector

### Synopsis

This command deletes an identity provider connector by passing the connector's ID. You can get a list of IDs by running `pachctl idp list-connector`. 

```
pachctl idp delete-connector <connector id> [flags]
```

### Options

```
  -h, --help   help for delete-connector
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations

