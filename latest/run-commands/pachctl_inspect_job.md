---
date: 2023-08-04T13:05:50-04:00
title: "pachctl inspect job"
slug: "Learn about the pachctl_inspect_job command"
---

## pachctl inspect job

Return info about a job.

### Synopsis

This command returns detailed info about a job, including processing stats, inputs, and transformation configuration (the image and commands used). 
 
If you pass in a job set ID (without the `pipeline@`), it will defer you to using the `pachctl list job <id>` command. See examples for proper use. 
 
	- To specify the project where the parent pipeline lives, use the `--project` flag 
	- To specify the output should be raw JSON or YAML, use the `--raw` flag along with `--output`

```
pachctl inspect job <pipeline>@<job> [flags]
```

### Examples

```
	- pachctl inspect job foo@e0f68a2fcda7458880c9e2e2dae9e678 
	- pachctl inspect job foo@e0f68a2fcda7458880c9e2e2dae9e678 --project bar 
	- pachctl inspect job foo@e0f68a2fcda7458880c9e2e2dae9e678 --project bar --raw --output yaml 

```

### Options

```
      --full-timestamps   Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help              help for job
  -o, --output string     Output format when --raw is set: "json" or "yaml" (default "json")
      --project string    Specify the project (by name) containing the parent pipeline for this job. (default "standard-ml-tutorial")
      --raw               Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

