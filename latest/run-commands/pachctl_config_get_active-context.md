---
date: 2024-02-13T16:12:03-05:00
title: "pachctl config get active-context"
description: "Learn about the pachctl config get active-context command"
---

## pachctl config get active-context

Gets the currently active context.

### Synopsis

This command returns the currently active context. 
 To list all contexts, use `pachctl config list contexts`. 
 To view details, use `pachctl config get context <context>`. 
 To clean up your contexts, use `pachctl config delete context <context>`. 
 To set a different context as active, use `pachctl config set active-context <context>`. 


```
pachctl config get active-context [flags]
```

### Examples

```
pachctl config get active-context}
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

* [pachctl config get](../pachctl_config_get)	 - Commands for getting pachyderm config values

