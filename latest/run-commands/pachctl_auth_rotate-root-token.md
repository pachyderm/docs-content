---
date: 2023-09-07T13:28:03-04:00
title: "pachctl auth rotate-root-token"
description: "Learn about the pachctl_auth_rotate-root-token command"
---

## pachctl auth rotate-root-token

Rotate the root user's auth token

### Synopsis

Rotate the root user's auth token

```
pachctl auth rotate-root-token [flags]
```

### Options

```
  -h, --help                  help for rotate-root-token
      --supply-token string   An auth token to rotate to. If left blank, one will be auto-generated.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

