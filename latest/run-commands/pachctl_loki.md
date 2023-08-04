---
date: 2023-08-04T13:05:50-04:00
title: "pachctl loki"
slug: "Learn about the pachctl_loki command"
---

## pachctl loki

Query the loki logs.

### Synopsis

This command queries the loki logs.

```
pachctl loki <query> [flags]
```

### Examples

```
	- pachctl loki <query> --since 100s 
	- pachctl loki <query> --since 1h
```

### Options

```
  -h, --help           help for loki
      --since string   Specify results should return log messages more recent than "since". (default "0")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl](/commands/pachctl/)	 - 

