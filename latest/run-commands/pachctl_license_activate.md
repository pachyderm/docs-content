---
date: 2023-10-18T16:51:53-04:00
title: "pachctl license activate"
description: "Learn about the pachctl license activate command"
---

## pachctl license activate

Activate the license server with an activation code

### Synopsis

This command activates Enterprise Server with an activation code.

```
pachctl license activate [flags]
```

### Examples

```
 pachctl license activate
 pachctl license activate --no-register

```

### Options

```
  -h, --help          help for activate
      --no-register   Activate auth on the active enterprise context
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service

