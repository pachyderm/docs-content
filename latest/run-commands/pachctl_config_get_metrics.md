---
date: 2023-10-18T16:51:53-04:00
title: "pachctl config get metrics"
description: "Learn about the pachctl config get metrics command"
---

## pachctl config get metrics

Gets whether metrics are enabled.

### Synopsis

This command returns the status of metric enablement (`pachd.metrics.enabled`).

```
pachctl config get metrics [flags]
```

### Examples

```
pachctl config get metrics
```

### Options

```
  -h, --help   help for metrics
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl config get](../pachctl_config_get)	 - Commands for getting pachyderm config values

