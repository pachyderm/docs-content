---
date: 2023-10-18T16:51:53-04:00
title: "pachctl config get context"
description: "Learn about the pachctl config get context command"
---

## pachctl config get context

Gets a context.

### Synopsis

This command returns the config of a context by its name. This includes the pachd address, cluster deployment ID, and actively set project name.

```
pachctl config get context <context> [flags]
```

### Examples

```
pachctl config get context foo
```

### Options

```
  -h, --help   help for context
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config get](../pachctl_config_get)	 - Commands for getting pachyderm config values

