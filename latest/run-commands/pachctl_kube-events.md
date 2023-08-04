---
date: 2023-08-04T13:05:50-04:00
title: "pachctl kube-events"
slug: "Learn about the pachctl_kube-events command"
---

## pachctl kube-events

Return the kubernetes events.

### Synopsis

This command returns the kubernetes events. 
	- To return results starting from a certain amount of time before now, use the `--since` flag 
	- To return the raw events, use the `--raw` flag 


```
pachctl kube-events [flags]
```

### Examples

```
	- pachctl kube-events --raw 
	- pachctl kube-events --since 100s 
	- pachctl kube-events --raw --since 1h 

```

### Options

```
  -h, --help           help for kube-events
      --raw            Specify results should return log messages verbatim from server.
      --since string   Specify results should return log messages more recent than "since". (default "0")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl](/commands/pachctl/)	 - 

