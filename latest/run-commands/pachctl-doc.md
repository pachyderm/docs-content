---
date: 2023-08-04T13:05:50-04:00
title: "pachctl"
slug: "Learn about the pachctl command"
---

## pachctl



### Synopsis

Access the Pachyderm API.

PachCTL Environment Variables:
	- PACH_CONFIG=<path> | (Req) PachCTL config location. 
	- PACH_TRACE={true,false} | (Opt) Attach Jaeger trace to outgoing RPCs; JAEGER_ENDPOINT must be specified. 
		[req. PACH_TRACE={true}]: 
		- JAEGER_ENDPOINT=<host>:<port>  | Jaeger server to connect to. 
		- PACH_TRACE_DURATION=<duration> | Duration to trace pipelines after 'pachctl create-pipeline'. 
 
Documentation: https://docs.pachyderm.com/latest/

### Options

```
  -h, --help       help for pachctl
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](/commands/pachctl_auth/)	 - Auth commands manage access to data in a Pachyderm cluster
* [pachctl buildinfo](/commands/pachctl_buildinfo/)	 - Print go buildinfo.
* [pachctl completion](/commands/pachctl_completion/)	 - Print or install terminal completion code.
* [pachctl config](/commands/pachctl_config/)	 - Manages the pachyderm config.
* [pachctl connect](/commands/pachctl_connect/)	 - Connect to a Pachyderm Cluster
* [pachctl copy](/commands/pachctl_copy/)	 - Copy a Pachyderm resource.
* [pachctl create](/commands/pachctl_create/)	 - Create a new instance of a Pachyderm resource.
* [pachctl debug](/commands/pachctl_debug/)	 - Debug commands for analyzing a running cluster.
* [pachctl delete](/commands/pachctl_delete/)	 - Delete an existing Pachyderm resource.
* [pachctl diff](/commands/pachctl_diff/)	 - Show the differences between two Pachyderm resources.
* [pachctl draw](/commands/pachctl_draw/)	 - Draw an ASCII representation of an existing Pachyderm resource.
* [pachctl edit](/commands/pachctl_edit/)	 - Edit the value of an existing Pachyderm resource.
* [pachctl enterprise](/commands/pachctl_enterprise/)	 - Enterprise commands enable Pachyderm Enterprise features
* [pachctl exit](/commands/pachctl_exit/)	 - Exit the pachctl shell.
* [pachctl find](/commands/pachctl_find/)	 - Find a file addition, modification, or deletion in a commit.
* [pachctl finish](/commands/pachctl_finish/)	 - Finish a Pachyderm resource.
* [pachctl fsck](/commands/pachctl_fsck/)	 - Run a file system consistency check on PFS.
* [pachctl get](/commands/pachctl_get/)	 - Get the raw data represented by a Pachyderm resource.
* [pachctl glob](/commands/pachctl_glob/)	 - Print a list of Pachyderm resources matching a glob pattern.
* [pachctl idp](/commands/pachctl_idp/)	 - Commands to manage identity provider integrations
* [pachctl inspect](/commands/pachctl_inspect/)	 - Show detailed information about a Pachyderm resource.
* [pachctl kube-events](/commands/pachctl_kube-events/)	 - Return the kubernetes events.
* [pachctl license](/commands/pachctl_license/)	 - License commmands manage the Enterprise License service
* [pachctl list](/commands/pachctl_list/)	 - Print a list of Pachyderm resources of a specific type.
* [pachctl logs](/commands/pachctl_logs/)	 - Return logs from a job.
* [pachctl loki](/commands/pachctl_loki/)	 - Query the loki logs.
* [pachctl mount](/commands/pachctl_mount/)	 - Mount pfs locally. This command blocks.
* [pachctl port-forward](/commands/pachctl_port-forward/)	 - Forward a port on the local machine to pachd. This command blocks.
* [pachctl put](/commands/pachctl_put/)	 - Insert data into Pachyderm.
* [pachctl restart](/commands/pachctl_restart/)	 - Cancel and restart an ongoing task.
* [pachctl resume](/commands/pachctl_resume/)	 - Resume a stopped task.
* [pachctl run](/commands/pachctl_run/)	 - Manually run a Pachyderm resource.
* [pachctl shell](/commands/pachctl_shell/)	 - Run the pachyderm shell.
* [pachctl squash](/commands/pachctl_squash/)	 - Squash an existing Pachyderm resource.
* [pachctl start](/commands/pachctl_start/)	 - Start a Pachyderm resource.
* [pachctl stop](/commands/pachctl_stop/)	 - Cancel an ongoing task.
* [pachctl subscribe](/commands/pachctl_subscribe/)	 - Wait for notifications of changes to a Pachyderm resource.
* [pachctl unmount](/commands/pachctl_unmount/)	 - Unmount pfs.
* [pachctl update](/commands/pachctl_update/)	 - Change the properties of an existing Pachyderm resource.
* [pachctl validate](/commands/pachctl_validate/)	 - Validate the specification of a Pachyderm resource.
* [pachctl version](/commands/pachctl_version/)	 - Print Pachyderm version information.
* [pachctl wait](/commands/pachctl_wait/)	 - Wait for the side-effects of a Pachyderm resource to propagate.

