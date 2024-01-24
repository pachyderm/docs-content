---
# metadata # 
title:  Transform PPS
description: Set the name of the Docker image that your jobs use.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: required 
weight: 1
---

## Spec 
This is a top-level attribute of the pipeline spec. 

```s
{
    "pipeline": {...},
    "transform": {
        "image": string,
        "cmd": [ string ],
        "datumBatching": bool,
        "errCmd": [ string ],
        "env": {
            string: string
        },

        "secrets": [ {
            "name": string,
            "mountPath": string
        },
        {
            "name": string,
            "envVar": string,
            "key": string
        } ],
        "imagePullSecrets": [ string ],
        "stdin": [ string ],
        "errStdin": [ string ],
        "acceptReturnCode": [ int ],
        "debug": bool,
        "user": string,
        "workingDir": string,
        "dockerfile": string,
        "memoryVolume": bool,
    },
    ...
}

```

## Attributes

|Attribute|Description|
|-|-|
|cmd| Passes a command to the Docker run invocation.|
|datumBatching|Enables you to call your user code once for a batch of datums versus calling it per each datum.|
|stdin| Passes an array of lines to your command on `stdin`.|
|errCmd| Passes a command executed on failed datums.|
|errStdin| Passes an array of lines to your error command on `stdin`.|
|env| Enables a key-value map of [environment variables](/{{%release%}}/set-up/environment-variables/) that {{% productName %}} injects into the container. |
|secrets| Passes an array of secrets to embed sensitive data. |
|imagePullSecrets| Passes an array of secrets that are mounted before the containers are created.|
|acceptReturnCode| Passes an array of return codes that are considered acceptable when your Docker command exits.|
|debug| Enables debug logging for the pipeline|
|user| Sets the user that your code runs as.|
|workingDir| Sets the directory that your command runs from.|
|memoryVolume| Sets pachyderm-worker's `emptyDir.Medium` to `Memory`, allowing Kubernetes to mount a memory-backed volume (`tmpfs`).|


## Behavior 

- `cmd` is not run inside a shell which means that wildcard globbing (`*`), pipes (`|`), and file redirects (`>` and `>>`) do not work. To specify these settings, you can set `cmd` to be a shell of your choice, such as `sh` and pass a shell script to `stdin`.
-  `errCmd` can be used to ignore failed datums while still writing successful datums to the output repo, instead of failing the whole job when some datums fail. The `transform.errCmd` command has the same limitations as `transform.cmd`.
-  `stdin` lines do not have to end in newline characters.
-  The following environment variables are automatically injected into the container:
   * `PACH_JOB_ID` – the ID of the current job.
   * `PACH_OUTPUT_COMMIT_ID` – the ID of the commit in the output repo for 
   the current job.
   * `<input>_COMMIT` - the ID of the input commit. For example, if your
   input is the `images` repo, this will be `images_COMMIT`.
- `secrets` reference Kubernetes secrets by name and specify a path to map the secrets or
an environment variable (`envVar`) that the value should be bound to.
-  `0` is always considered a successful exit code.
-  `tmpfs` is cleared on node reboot and any files you write count against your container's memory limit. This may be useful for workloads that are IO heavy or use memory caches.

{{%notice tip%}}
**Using a private registry? **

You can use `imagePullSecrets` to mount a secret that contains your registry credentials.

```s
{
  "pipeline": {
    "name": "pipeline-a"
  },
  "description": "...",
  "transform": {
    "cmd": [ "python3", "/example.py" ],
    "image": "<private container registry>/image:1.0",
    "imagePullSecrets": [ "k8s-secret-with-creds" ]
  },
  ...
}
```
{{%/notice%}}


## When to Use 

You must always use the transform attribute when making a pipeline. 