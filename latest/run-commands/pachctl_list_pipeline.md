---
date: 2024-02-13T16:12:03-05:00
title: "pachctl list pipeline"
description: "Learn about the pachctl list pipeline command"
---

## pachctl list pipeline

Return info about all pipelines.

### Synopsis

This command returns information about all pipelines. 
 
 To return pipelines with a specific state, use the `--state` flag 
 To return pipelines as they existed at a specific commit, use the `--commit` flag 
 To return a history of pipeline revisions, use the `--history` flag 


```
pachctl list pipeline [<pipeline>] [flags]
```

### Examples

```
 pachctl list pipeline 
 pachctl list pipeline --spec --output yaml 
 pachctl list pipeline --commit 5f93d03b65fa421996185e53f7f8b1e4 
 pachctl list pipeline --state crashing 
 pachctl list pipeline --project foo 
 pachctl list pipeline --project foo --state restarting 

```

### Options

```
  -A, --all-projects        Show pipelines form all projects.
  -c, --commit string       List the pipelines as they existed at this commit.
      --full-timestamps     Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help                help for pipeline
      --history string      Specify results should include revision history for pipelines. (default "none")
  -o, --output string       Output format when --raw is set: "json" or "yaml" (default "json")
      --project string      Specify the project (by name) containing the pipelines. (default "video-to-frame-traces")
      --raw                 Disable pretty printing; serialize data structures to an encoding such as json or yaml
  -s, --spec                Output 'create pipeline' compatibility specs.
      --state stringArray   Specify results should include only pipelines with the specified state (starting, running, restarting, failure, paused, standby, crashing); can be repeated for multiple states.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.

