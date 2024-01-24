---
# metadata # 
title:  PachW HCVs
description:  Create a pool of pachd instances that dynamically scale storage task handling. 
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 7
label: optional
--- 
## About

PachW enables fine-grained control of where compaction and object-storage interaction occur by running storage tasks in a dedicated Kubernetes deployment. Users can configure PachW's min and max replicas as well as define nodeSelectors, tolerations, and resource requests. Using PachW allows power users to save on costs by claiming fewer resources and running storage tasks on less expensive nodes.



{{% notice warning %}}
If you are upgrading to **2.5.0+** for the first time and you wish to use PachW, you must calculate how many maxReplicas you need. By default, PachW is set to `maxReplicas:1`  --- however, that is not sufficient for production runs.
{{% /notice %}}


### maxReplicas
You should set the `maxReplicas` value to **at least match the number of pipeline replicas that you have**. For high performance, we suggest taking the following approach:

> `number of pipelines * highest parallelism spec * 1.5 = maxReplicas`

Let's say you have 6 pipelines. One of these pipelines has a [parallelism spec](/{{%release%}}/build-dags/pipeline-spec/parallelism) value of 6, and the rest are 5 or fewer. 

> `6 * 6 * 1.5 = 54`

### minReplicas

Workloads that constantly process storage and compaction tasks because they are committing rapidly may want to increase minReplicas to have instances on standby.

### nodeSelectors

Workloads that utilize GPUs and other expensive resources may want to add a node selector to scope PachW instances to less expensive nodes.

## Values 

```yaml
pachw:
  # When set to true, inheritFromPachd defaults below configuration options like 'resources' and 'tolerations' to
  # values from pachd. These values can be overridden by defining the corresponding pachw values below.
  # When set to false, a nil value will be used by default instead. Some configuration variables will always use their
  # corresponding pachd value, regardless of whether 'inheritFromPachd' is true, such as 'serviceAccountName'
  inheritFromPachd: true
  # When set to true, inSidecars also processes storage related tasks in pipeline storage sidecars like version 2.4 or less.
  # when enabled, pachw instances can still run in their own dedicated kubernetes deployment if maxReplicas is greater than 0.
  # For more control of where pachw instances run, 'inSidecars' should be disabled.
  inSidecars: false
  # maxReplicas should be tuned based on the number of pipelines on a user-per-user basis.
  maxReplicas: 1
  # minReplicas: 0
  # We recommend defining resources when running pachw with a high value of maxReplicas.
  #resources:
  #  limits:
  #    cpu: "1"
  #    memory: "2G"
  #  requests:
  #    cpu: "1"
  #  memory: "2G"
  #
  #tolerations: []
  #affinity: {}
  #nodeSelector: {}
```
