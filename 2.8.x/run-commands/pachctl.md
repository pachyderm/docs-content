---
date: 2023-10-18T16:51:53-04:00
title: "pachctl"
description: "Learn about the pachctl command"
---

## pachctl



### Synopsis

Access the Pachyderm API.

PachCTL Environment Variables:
 PACH_CONFIG=<path> | (Req) PachCTL config location. 
 PACH_TRACE={true,false} | (Opt) Attach Jaeger trace to outgoing RPCs; JAEGER_ENDPOINT must be specified. 
		[req. PACH_TRACE={true}]: 
	 JAEGER_ENDPOINT=<host>:<port>  | Jaeger server to connect to. 
	 PACH_TRACE_DURATION=<duration> | Duration to trace pipelines after 'pachctl create-pipeline'. 
 
Documentation: https://docs.pachyderm.com/latest/

### Options

```
  -h, --help       help for pachctl
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster
* [pachctl buildinfo](../pachctl_buildinfo)	 - Print go buildinfo.
* [pachctl completion](../pachctl_completion)	 - Print or install terminal completion code.
* [pachctl config](../pachctl_config)	 - Manages the pachyderm config.
* [pachctl connect](../pachctl_connect)	 - Connect to a Pachyderm Cluster
* [pachctl copy](../pachctl_copy)	 - Copy a Pachyderm resource.
* [pachctl create](../pachctl_create)	 - Create a new instance of a Pachyderm resource.
* [pachctl debug](../pachctl_debug)	 - Debug commands for analyzing a running cluster.
* [pachctl delete](../pachctl_delete)	 - Delete an existing Pachyderm resource.
* [pachctl diff](../pachctl_diff)	 - Show the differences between two Pachyderm resources.
* [pachctl draw](../pachctl_draw)	 - Draw an ASCII representation of an existing Pachyderm resource.
* [pachctl edit](../pachctl_edit)	 - Edit the value of an existing Pachyderm resource.
* [pachctl enterprise](../pachctl_enterprise)	 - Enterprise commands enable Pachyderm Enterprise features
* [pachctl exit](../pachctl_exit)	 - Exit the pachctl shell.
* [pachctl find](../pachctl_find)	 - Find a file addition, modification, or deletion in a commit.
* [pachctl finish](../pachctl_finish)	 - Finish a Pachyderm resource.
* [pachctl fsck](../pachctl_fsck)	 - Run a file system consistency check on PFS.
* [pachctl get](../pachctl_get)	 - Get the raw data represented by a Pachyderm resource.
* [pachctl glob](../pachctl_glob)	 - Print a list of Pachyderm resources matching a glob pattern.
* [pachctl idp](../pachctl_idp)	 - Commands to manage identity provider integrations
* [pachctl inspect](../pachctl_inspect)	 - Show detailed information about a Pachyderm resource.
* [pachctl kube-events](../pachctl_kube-events)	 - Return the kubernetes events.
* [pachctl license](../pachctl_license)	 - License commmands manage the Enterprise License service
* [pachctl list](../pachctl_list)	 - Print a list of Pachyderm resources of a specific type.
* [pachctl logs](../pachctl_logs)	 - Return logs from a job.
* [pachctl loki](../pachctl_loki)	 - Query the loki logs.
* [pachctl mount](../pachctl_mount)	 - Mount pfs locally. This command blocks.
* [pachctl port-forward](../pachctl_port-forward)	 - Forward a port on the local machine to pachd. This command blocks.
* [pachctl put](../pachctl_put)	 - Insert data into Pachyderm.
* [pachctl rerun](../pachctl_rerun)	 - Manually rerun a Pachyderm resource.
* [pachctl restart](../pachctl_restart)	 - Cancel and restart an ongoing task.
* [pachctl resume](../pachctl_resume)	 - Resume a stopped task.
* [pachctl run](../pachctl_run)	 - Manually run a Pachyderm resource.
* [pachctl shell](../pachctl_shell)	 - Run the pachyderm shell.
* [pachctl squash](../pachctl_squash)	 - Squash an existing Pachyderm resource.
* [pachctl start](../pachctl_start)	 - Start a Pachyderm resource.
* [pachctl stop](../pachctl_stop)	 - Cancel an ongoing task.
* [pachctl subscribe](../pachctl_subscribe)	 - Wait for notifications of changes to a Pachyderm resource.
* [pachctl unmount](../pachctl_unmount)	 - Unmount pfs.
* [pachctl update](../pachctl_update)	 - Change the properties of an existing Pachyderm resource.
* [pachctl validate](../pachctl_validate)	 - Validate the specification of a Pachyderm resource.
* [pachctl version](../pachctl_version)	 - Print Pachyderm version information.
* [pachctl wait](../pachctl_wait)	 - Wait for the side-effects of a Pachyderm resource to propagate.

