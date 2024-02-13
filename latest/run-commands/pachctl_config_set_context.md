---
date: 2024-02-13T16:12:03-05:00
title: "pachctl config set context"
description: "Learn about the pachctl config set context command"
---

## pachctl config set context

Set a context.

### Synopsis

This command sets a context config from a given name and a JSON configuration file on stdin

```
pachctl config set context <context> [flags]
```

### Examples

```
 pachctl config set context foo pachctl config set context foo --overwrite
```

### Options

```
  -h, --help        help for context
      --overwrite   Overwrite a context if it already exists.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config set](../pachctl_config_set)	 - Commands for setting pachyderm config values

