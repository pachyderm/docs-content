---
date: 2024-02-13T16:12:03-05:00
title: "pachctl debug local"
description: "Learn about the pachctl debug local command"
---

## pachctl debug local

Collect debugging information without connecting to a Pachyderm server.

### Synopsis

This command collects debugging information based on a special template provided by Pachyderm Support.

It works in cases where Pachyderm isn't already installed.

```
pachctl debug local <template> [flags]
```

### Examples

```
 pachctl debug local template.yaml 

```

### Options

```
  -h, --help   help for local
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

