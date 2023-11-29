---
date: 2023-10-18T16:51:53-04:00
title: "pachctl create repo"
description: "Learn about the pachctl create repo command"
---

## pachctl create repo

Create a new repo in your active project.

### Synopsis

This command creates a repo in the project that is set to your active context (initially the `default` project).

 To specify which project to create the repo in, use the `--project` flag 
 To add a description to the project, use the `--description` flag  


```
pachctl create repo <repo> [flags]
```

### Examples

```
 pachctl create repo foo ➔ /<active-project>/foo 
 pachctl create repo bar --description 'my new repo' ➔ /<active-project>/bar 
 pachctl create repo baz --project myproject ➔ /myproject/baz 

```

### Options

```
  -d, --description string   Set a repo description.
  -h, --help                 help for repo
      --project string       Specify an existing project (by name) for where the new repo will be located. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.

