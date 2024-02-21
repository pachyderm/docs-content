---
date: 2023-10-18T16:51:53-04:00
title: "pachctl auth set project"
description: "Learn about the pachctl auth set project command"
---

## pachctl auth set project

Set the roles that a subject has on a project 

### Synopsis

This command sets the roles that a given subject has on a given project (`projectViewer`, `projectWriter`, `projectOwner`, `projectCreator`).

```
pachctl auth set project <project> [role1,role2 | none ] <subject> [flags]
```

### Examples

```
 pachctl auth set project foo projectOwner user:alan.watts@domain.com pachctl auth set project foo projectWriter, projectReader robot:my-robot
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

* [pachctl auth set](../pachctl_auth_set)	 - Set the role bindings for a resource

