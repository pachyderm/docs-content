---
date: 2023-10-18T16:51:53-04:00
title: "pachctl debug template"
description: "Learn about the pachctl debug template command"
---

## pachctl debug template

Print a yaml debugging template.

### Synopsis

This command outputs a customizable yaml template useful for debugging. This is often used by Customer Engineering to support your troubleshooting needs. 
Use the modified template with the `debug dump` command (e.g., `pachctl debug dump --template debug-template.yaml out.tgz`) 


```
pachctl debug template <file> [flags]
```

### Examples

```
 pachctl debug template 
 pachctl debug template > debug-template.yaml

```

### Options

```
  -h, --help   help for template
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.

