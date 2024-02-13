---
date: 2024-02-13T16:12:03-05:00
title: "pachctl list job"
description: "Learn about the pachctl list job command"
---

## pachctl list job

Return info about jobs.

### Synopsis

This command returns info about a list of jobs. You can pass in the command with or without a job ID. 
 
Without an ID, this command returns a global list of top-level job sets which contain their own sub-jobs; With an ID, it returns a list of sub-jobs within the specified job set. 
 
 To return a list of sub-jobs across all job sets, use the `--expand` flag without passing an ID 
 To return only the sub-jobs from the most recent version of a pipeline, use the `--pipeline` flag 
 To return all sub-jobs from all versions of a pipeline, use the `--history` flag 
 To return all sub-jobs whose input commits include data from a particular repo branch/commit, use the `--input` flag 
 To turn only sub-jobs with a particular state, use the `--state` flag; options: CREATED, STARTING, UNRUNNABLE, RUNNING, EGRESS, FINISHING, FAILURE, KILLED, SUCCESS

```
pachctl list job [<job-id>] [flags]
```

### Examples

```
 pachctl list job 
 pachctl list job --state starting 
 pachctl list job --pipeline foo 
 pachctl list job --expand 
 pachctl list job --expand --pipeline foo 
 pachctl list job --expand --pipeline foo  --state failure --state unrunnable 
 pachctl list job 5f93d03b65fa421996185e53f7f8b1e4 
 pachctl list job 5f93d03b65fa421996185e53f7f8b1e4 --state running
 pachctl list job --input foo-repo@staging 
 pachctl list job --input foo-repo@5f93d03b65fa421996185e53f7f8b1e4 
 pachctl list job --pipeline foo --input bar-repo@staging 
 pachctl list job --pipeline foo --input bar-repo@5f93d03b65fa421996185e53f7f8b1e4 

```

### Options

```
  -A, --all-projects        Specify results should return jobs from all projects.
  -x, --expand              Specify results return as one line for each sub-job and include more columns; not needed if ID is passed.
      --full-timestamps     Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help                help for job
      --history string      Specify results returned include jobs from historical versions of pipelines. (default "none")
  -i, --input strings       Specify results should only return jobs with a specific set of input commits; format: <repo>@<branch-or-commit>
      --no-pager            Don't pipe output into a pager (i.e. less).
  -o, --output string       Output format when --raw is set: "json" or "yaml" (default "json")
  -p, --pipeline string     Specify results should only return jobs created by a given pipeline.
      --project string      Specify the project (by name) containing the parent pipeline for returned jobs. (default "video-to-frame-traces")
      --raw                 Disable pretty printing; serialize data structures to an encoding such as json or yaml
      --state stringArray   Specify results return only sub-jobs with the specified state; can be repeated to include multiple states.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

