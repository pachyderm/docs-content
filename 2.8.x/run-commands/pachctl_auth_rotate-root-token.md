---
date: 2023-10-18T16:51:53-04:00
title: "pachctl auth rotate-root-token"
description: "Learn about the pachctl auth rotate-root-token command"
---

## pachctl auth rotate-root-token

Rotate the root user's auth token

### Synopsis

This command rotates the root user's auth token; you can supply a token to rotate to, or one can be auto-generated.

```
pachctl auth rotate-root-token [flags]
```

### Examples

```
 pachctl auth rotate-root-token 
 pachctl auth rotate-root-token --supply-token <token>
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

