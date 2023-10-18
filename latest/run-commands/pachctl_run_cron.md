---
date: 2023-10-18T16:51:53-04:00
title: "pachctl run cron"
description: "Learn about the pachctl run cron command"
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
 pachctl run cron foo 
 pachctl run cron foo  --project bar 

```

### Options

```
  -h, --help             help for cron
      --project string   Specify the project (by name) containing the cron pipeline. (default "video-to-frame-traces")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl run](../pachctl_run)	 - Manually run a Pachyderm resource.

