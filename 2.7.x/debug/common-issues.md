---
# metadata # 
title:  Common Issues
description: Learn how to troubleshoot common issues.
date: 
# taxonomy #
tags: 
series:
seriesPart:
directory: true 
---

## Cannot Connect via PachCTL

### Context Deadline Exceeded

#### Symptom

You may be using the pachd address config value or environment variable to specify how `pachctl` talks to your {{%productName%}} cluster, or you may be forwarding the {{% productName %}}port.  In any event, you might see something similar to:

```s
pachctl version
COMPONENT           VERSION                                          
pachctl             {{% latestPatchNumber %}}  
context deadline exceeded
```

Also, you might get this message if `pachd` is not running.

#### Recourse

It's possible that the connection is just taking a while. Occasionally this can happen if your cluster is far away (deployed in a region across the country). Check your internet connection.

It's also possible that you haven't poked a hole in the firewall to access the node on this port. Usually to do that you adjust a security rule (in AWS parlance a security group). For example, on AWS, if you find your node in the web console and click on it, you should see a link to the associated security group. Inspect that group. There should be a way to "add a rule" to the group. You'll want to enable TCP access (ingress) on port 30650. You'll usually be asked which incoming IPs should be whitelisted. You can choose to use your own, or enable it for everyone (0.0.0.0/0).

### Could not get Cluster ID + Could Not Inspect Project

#### Symptom

You are trying to connect to a {{%productName%}} cluster using `pachctl` and you see the following error:

```s
could not get cluster ID: failed to inspect cluster: rpc error: code = NotFound desc = could not inspect project "foo": error getting project "foo": project "foo" not found
```

##### Recourse

1. Check your `./pachyderm/config.json` file to see if an entry for your active context has an existing conflicting contexts with other details, such as a `cluster_deployment_id` saved. This can happen if you have reinstalled {{%productName%}} and left the old configurations in place. Uninstalling {{%productName%}} does not remove these old configurations.
   
   {{%notice tip %}}

   The following example is an output for a `./pachyderm/config.json` file with duplicate entries for the same context.

   ```s
   {
     "user_id": "7b2f2427f72f418ea4a14287c76e63ea",
     "v2": {
       "active_context": "http://localhost:80",
       "contexts": {
           "grpc://localhost:80": {
               "pachd_address": "grpc://localhost:80",
               "cluster_deployment_id": "oO29fP0PC1Q3O39MSDgpVRgdpXraLJfw",
               "project": "foo"
           },
           "http://localhost:80": {
               "pachd_address": "grpc://localhost:80",
               "session_token": "672e166adf994b7ebdd7f32bffa44375",
               "cluster_deployment_id": "GaM2j0EknVSQIcfEHzNof25Z525QAf7S",
               "project": "standard-ml-tutorial"
           },
           "https://localhost:80": {
               "pachd_address": "grpcs://localhost:80"
           },
       }
     }
   }
   ```
   {{% /notice%}}

2. Delete the conflicting contexts from the `./pachyderm/config.json` file. When you run `pachctl connect`, a new context will be created.
3. Reset your default project if the conflicting contexts had an old project set as the default. 
   
   ```s 
   pachctl config update context --project default
   ```
4. Run `pachctl connect` again to connect to your {{%productName%}} cluster.
5. Run `pachctl version` to verify that you are connected to your {{%productName%}} cluster.



## Certificate Error When Using Kubectl

### Symptom

This can happen on any request using `kubectl` (e.g. `kubectl get all`). In particular you'll see:

```s
kubectl version
Client Version: version.Info{Major:"1", Minor:"6", GitVersion:"v1.6.4", GitCommit:"d6f433224538d4f9ca2f7ae19b252e6fcb66a3ae", GitTreeState:"clean", BuildDate:"2017-05-19T20:41:24Z", GoVersion:"go1.8.1", Compiler:"gc", Platform:"darwin/amd64"}
Unable to connect to the server: x509: certificate signed by unknown authority
```

### Recourse

Check if you're on any sort of VPN or other egress proxy that would break SSL.  Also, there is a possibility that your credentials have expired. In the case where you're using GKE and gcloud, renew your credentials via:

```s
kubectl get all
Unable to connect to the server: x509: certificate signed by unknown authority
```

```s
gcloud container clusters get-credentials my-cluster-name-dev
Fetching cluster endpoint and auth data.
kubeconfig entry generated for my-cluster-name-dev.
```

```s
kubectl config current-context
gke_my-org_us-east1-b_my-cluster-name-dev
```

## Uploads and Downloads are Slow

### Symptom

Any `pachctl put file` or `pachctl get file` commands are slow.

### Recourse

If you do not explicitly set the pachd address config value, `pachctl` will default to using port forwarding, which throttles traffic to ~1MB/s. If you need to do large downloads/uploads you should consider using pachd address config value. You'll also want to make sure you've allowed ingress access through any firewalls to your k8s cluster.

## Naming a Repo with an Unsupported Symbol

### Symptom

A {{%productName%}} repo was accidentally named starting with a dash (`-`) and the repository
is treated as a command flag instead of a repository.

### Recourse

{{%productName%}} supports standard `bash` utilities that you can
use to resolve this and similar problems. For example, in this case,
you can specify double dashes (`--`) to delete the repository. Double dashes
signify the end of options and tell the shell to process the
rest arguments as filenames and objects.

For more information, see `man bash`.

## Failed Uploads

### Symptom

A file upload, particularly a recursive one of many files, fails. You may see log messages containing the following in either pipeline logs, pachd logs, or from the pachctl command locally:
- pachctl errror: ``an error occurred forwarding XXXXX -> 650: error forwarding port 650``
- pachctl error: ``EOF``
- pachd or worker: ``all SubConns are in TransientFailure, latest connection error: connection error: desc = \"transport: Error while dialing dial tcp  127.0.0.1:653: connect: connection refused\"; retrying in XXXX.XXXXXs"}``

### Recourse

Either ``pachd`` or your pipeline's worker sidecar may be getting OOM killed as it grows while getting data from object storage. 

You can give the storage container more resources by increasing the ``cache_size`` parameter in your pipeline spec. Increase it to what you can afford; its default is 64M.(If you’re using a release prior to 1.10.0 and you have cluster-wide or namepace policies on resource limits, you may need to manually edit the pipeline RC.)

If it still gets OOM killed by k8s, there are a couple of environment variables you can set in your pachd deployment to limit the amount of memory the sidecar and pachd use.

- ``STORAGE_UPLOAD_CONCURRENCY_LIMIT`` limits the parallelism to put files into the storage backend. Default is 100.
- ``STORAGE_PUT_FILE_CONCURRENCY_LIMIT`` limits the number of parallel downloads pachd will initiate. Default is also 100.

You may use a binary search technique to hone in on a value appropriate for a production pipeline:

for ``cache_size``, max it out. If it works, halve it. If its OOM killed, increase the value by 50%. and so on
for the ``CONCURRENCY_LIMITS``, halve and increase by 50% until you get a value that works.
