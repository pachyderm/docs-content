---
date: 2023-08-04T13:05:50-04:00
title: "pachctl run pps-load-test"
slug: "Learn about the pachctl_run_pps-load-test command"
---

## pachctl run pps-load-test

Run a PPS load test.

### Synopsis

This command runs a PPS load test for a specified pipeline specification file. 
	- To run a load test with a specific seed, use the `--seed` flag 
	- To run a load test with a specific parallelism count, use the `--parallelism` flag 
	- To run a load test with a specific pod patch, use the `--pod-patch` flag

```
pachctl run pps-load-test <spec-file>  [flags]
```

### Examples

```
	- pachctl run pps-load-test --dag myspec.json 
	- pachctl run pps-load-test --dag myspec.json --seed 1 
	- pachctl run pps-load-test --dag myspec.json  --parallelism 3 
	- pachctl run pps-load-test --dag myspec.json  --pod-patch patch.json 
	- pachctl run pps-load-test --dag myspec.json --state-id xyz

```

### Options

```
  -d, --dag string         Provide DAG specification file to use for the load test
  -h, --help               help for pps-load-test
  -p, --parallelism int    Set the parallelism count to use for the pipelines.
      --pod-patch string   Provide pod patch file to use for the pipelines.
  -s, --seed int           Specify the seed to use for generating the load.
      --state-id string    Provide the ID of the base state to use for the load.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl run](/commands/pachctl_run/)	 - Manually run a Pachyderm resource.

