---
date: 2023-08-04T13:05:50-04:00
title: "pachctl update project"
slug: "Learn about the pachctl_update_project command"
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
	- pachctl update project foo-project --description 'This is a project for foo.' 

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

