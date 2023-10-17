---
date: 2023-09-07T13:28:03-04:00
title: "pachctl delete project"
description: "Learn about the pachctl_delete_project command"
---

## pachctl delete project

Delete a project.

### Synopsis

This command deletes a project.

```
pachctl delete project <project> [flags]
```

### Examples

```
 pachctl delete project foo-project 
 pachctl delete project foo-project --force 

```

### Options

```
  -f, --force   Force delete the project regardless of errors; use with caution.
  -h, --help    help for project
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

