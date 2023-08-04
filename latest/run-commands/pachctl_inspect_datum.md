---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect datum"
slug: "Learn about the pachctl_inspect_datum command"
---

## pachctl inspect datum

Display detailed info about a single datum.

### Synopsis

This command displays detailed info about a single datum; requires the pipeline to have stats enabled.

```
pachctl inspect datum <pipeline>@<job> <datum> [flags]
```

### Examples

```
	- pachctl inspect datum foo@5f93d03b65fa421996185e53f7f8b1e4 7f3cd988429894000bdad549dfe2d09b5ca7bfc5083b79fec0e6bda3db8cc705 
	- pachctl inspect datum foo@5f93d03b65fa421996185e53f7f8b1e4 7f3cd988429894000bdad549dfe2d09b5ca7bfc5083b79fec0e6bda3db8cc705 --project foo
```

### Options

```
  -h, --help             help for datum
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Project containing the job (default "standard-ml-tutorial")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl inspect](/commands/pachctl_inspect/)	 - Show detailed information about a Pachyderm resource.

