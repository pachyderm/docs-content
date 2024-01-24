---
date: 2023-10-18T16:51:53-04:00
title: "pachctl auth get-robot-token"
description: "Learn about the pachctl auth get-robot-token command"
---

## pachctl auth get-robot-token

Get an auth token for a robot user with the specified name.

### Synopsis

This command returns an auth token for a robot user with the specified name. You can assign roles to a robot user with `pachctl auth <resource> set robot:<robot-name>.` 

```
pachctl auth get-robot-token [username] [flags]
```

### Examples

```
 pachctl auth get-robot-token my-robot pachctl auth get-robot-token my-robot --ttl 1h pachctl auth get-robot-token my-robot --quiet pachctl auth get-robot-token my-robot --quiet --ttl 1h pachctl auth get-robot-token my-robot --enterprise
```

### Options

```
      --enterprise   Get a robot token for the enterprise context.
  -h, --help         help for get-robot-token
  -q, --quiet        if set, only print the resulting token (if successful). This is useful for scripting, as the output can be piped to use-auth-token.
      --ttl string   if set, the resulting auth token will have the given lifetime. If not set, the token does not expire. This flag should be a golang duration (e.g. "30s" or "1h2m3s").
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

