---
date: 2023-08-04T13:05:50-04:00
title: "pachctl validate pipeline"
slug: "Learn about the pachctl_validate_pipeline command"
---

## pachctl validate pipeline

Validate pipeline spec.

### Synopsis

This command validates a pipeline spec.  Client-side only; does not check that repos, images, etc exist on the server.

```
pachctl validate pipeline [flags]
```

### Examples

```
	- pachctl validate pipeline --file spec.json
```

### Options

```
  -f, --file string   A JSON file (url or filepath) containing one or more pipelines. "-" reads from stdin (the default behavior). Exactly one of --file and --jsonnet must be set.
  -h, --help          help for pipeline
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

