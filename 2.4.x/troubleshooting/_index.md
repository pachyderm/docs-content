---
# metadata # 
title:  Troubleshooting Guides
description: Learn how to resolve issues with deploying, configuring, or running our platform.
date: 
# taxonomy #
tags: 
series:
seriesPart:
# other # 
author: Lawrence Lane
weight: 7
---

This section describe troubleshooting guidelines that should
help you in troubleshooting your deployment and pipelines.

{{%productName%}} has a built-in logging system that collects
information about events in your {{%productName%}} environment at
pipeline, datum, and job level. See [pachctl logs](../reference/pachctl/pachctl_logs).

To troubleshoot the cluster itself, use the `kubectl` tool
troubleshooting tips. A few basic commands that you can use
include the following:

* Get the list of all Kubernetes objects:

  ```s
  kubectl get all
  ```

* Get the information about a pod:

  ```s
  kubectl describe pod <podname>
  ```
 