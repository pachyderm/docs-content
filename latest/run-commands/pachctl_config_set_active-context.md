---
date: 2024-02-13T16:12:03-05:00
title: "pachctl config set active-context"
description: "Learn about the pachctl config set active-context command"
---

## pachctl config set active-context

Sets the currently active context.

### Synopsis

This command sets the currently active context. This should be a combination of your `proxy.host` value and `proxy.server.http(s)Port number`. 
 To list all contexts, use `pachctl config list contexts`. 
 To view details, use `pachctl config get context <context>`. 
 To clean up your contexts, use `pachctl config delete context <context>`.

```
pachctl config set active-context <context> [flags]
```

### Examples

```
pachctl config set active-context grpc://localhost:80
```

### Options

```
  -h, --help   help for active-context
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config set](../pachctl_config_set)	 - Commands for setting pachyderm config values

