---
date: 2023-08-04T13:05:50-04:00
title: "pachctl run cron"
slug: "Learn about the pachctl_run_cron command"
---

## pachctl run cron

Run an existing Pachyderm cron pipeline now

### Synopsis

This command runs an existing Pachyderm cron pipeline immediately.

```
pachctl run cron <pipeline> [flags]
```

### Examples

```
	- pachctl run cron foo 
	- pachctl run cron foo  --project bar 

```

### Options

```
  -h, --help             help for cron
      --project string   Specify the project (by name) containing the cron pipeline. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl run](/commands/pachctl_run/)	 - Manually run a Pachyderm resource.

