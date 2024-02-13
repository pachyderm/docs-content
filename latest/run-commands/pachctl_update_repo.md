---
date: 2024-02-13T16:12:03-05:00
title: "pachctl update repo"
description: "Learn about the pachctl update repo command"
---

## pachctl update repo

Update a repo.

### Synopsis

This command enables you to update the description of an existing repo. 

 To specify which project to update the repo in, use the `--project` flag 
 To update the description of a repo, use the `--description` flag 

If you are looking to update the pipelines in your repo, see `pachctl update pipeline` instead.

```
pachctl update repo <repo> [flags]
```

### Examples

```
 pachctl update repo foo --description 'my updated repo description'
 pachctl update repo foo --project bar --description 'my updated repo description'

```

### Options

```
  -d, --description string   Set a repo description.
  -h, --help                 help for repo
      --project string       Specify the project (by name) where the repo is located. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl update](../pachctl_update)	 - Change the properties of an existing Pachyderm resource.

