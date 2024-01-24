---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug dump"
description: "Learn about the pachctl debug dump command"
---

## pachctl debug dump

Collect a standard set of debugging information.

### Synopsis

This command collects a standard set of debugging information related to the version, database, source repos, helm, profiles, binaries, loki-logs, pipelines, describes, and logs. 
 
You can customize this output by passing in a customized template (made from `pachctl debug template` via the `--template` flag.

```
pachctl debug dump <file> [flags]
```

### Examples

```
 pachctl debug dump dump.tgz 
 pachctl debug dump -t template.yaml out.tgz

```

### Options

```
  -h, --help              help for dump
  -t, --template string   Download a template to customize the output of the debug dump operation.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

