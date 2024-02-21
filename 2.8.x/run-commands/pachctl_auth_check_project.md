---
date: 2023-10-18T16:51:53-04:00
title: "pachctl auth check project"
description: "Learn about the pachctl auth check project command"
---

## pachctl auth check project

Check the permissions a user has on a project

### Synopsis

This command checks the permissions a user has on a given project.

```
pachctl auth check project <project> [user] [flags]
```

### Examples

```
 pachctl auth check project foo user:alan.watts@domain.com
```

### Options

```
  -h, --help   help for project
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth check](../pachctl_auth_check)	 - Check whether a subject has a permission on a resource

