---
date: 2023-10-18T16:51:53-04:00
title: "pachctl delete pipeline"
description: "Learn about the pachctl delete pipeline command"
---

## pachctl delete pipeline

Delete a pipeline.

### Synopsis

This command deletes a pipeline.

```
pachctl delete pipeline (<pipeline>|--all) [flags]
```

### Examples

```
 pachctl delete pipeline foo 
 pachctl delete pipeline --all 
 pachctl delete pipeline foo --force 
 pachctl delete pipeline foo --keep-repo 
 pachctl delete pipeline foo --project bar --keep-repo
```

### Options

```
      --all              Delete all pipelines
  -A, --all-projects     Delete pipelines from all projects; only valid with --all
  -f, --force            Delete the pipeline regardless of errors; use with care
  -h, --help             help for pipeline
      --keep-repo        Specify that the pipeline's output repo should be saved after pipeline deletion; to reuse this pipeline's name, you'll also need to delete this output repo.
      --project string   Specify the project (by name) containing project (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.

