---
date: 2023-10-18T16:51:53-04:00
title: "pachctl edit pipeline"
description: "Learn about the pachctl edit pipeline command"
---

## pachctl edit pipeline

Edit the manifest for a pipeline in your text editor.

### Synopsis

This command edits the manifest for a pipeline in your text editor.

```
pachctl edit pipeline <pipeline> [flags]
```

### Examples

```
 pachctl edit pipeline foo 
 pachctl edit pipeline foo --project bar 
 pachctl edit pipeline foo --project bar --editor vim 
 pachctl edit pipeline foo --project bar --editor vim --output yaml 
 pachctl edit pipeline foo --project bar --editor vim --reprocess 

```

### Options

```
      --editor string    Specify the editor to use for modifying the manifest.
  -h, --help             help for pipeline
  -o, --output string    Specify the output format: "json" or "yaml" (default "json")
      --project string   Specify the project (by name) containing pipeline to edit. (default "video-to-frame-traces")
      --reprocess        If true, reprocess datums that were already processed by previous version of the pipeline.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl edit](../pachctl_edit)	 - Edit the value of an existing Pachyderm resource.

