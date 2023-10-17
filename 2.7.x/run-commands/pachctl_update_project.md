---
date: 2023-09-07T13:28:03-04:00
title: "pachctl update project"
description: "Learn about the pachctl_update_project command"
---

## pachctl update project

Update a project.

### Synopsis

This command updates a project's description.

```
pachctl update project <project> [flags]
```

### Examples

```
 pachctl update project foo-project --description 'This is a project for foo.' 

```

### Options

```
  -d, --description string   Set a new description of the updated project.
  -h, --help                 help for project
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl update](../pachctl_update)	 - Change the properties of an existing Pachyderm resource.

