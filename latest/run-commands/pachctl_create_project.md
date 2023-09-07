---
date: 2023-09-07T13:28:03-04:00
title: "pachctl create project"
description: "Learn about the pachctl_create_project command"
---

## pachctl create project

Create a new project.

### Synopsis

This command creates a new project. 

 To set a description for the project, use the `--description` flag 


```
pachctl create project <project> [flags]
```

### Examples

```
 pachctl create project foo-project 
 pachctl create project foo-project --description 'This is a project for foo.' 

```

### Options

```
  -d, --description string   Set a description for the newly-created project.
  -h, --help                 help for project
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.

