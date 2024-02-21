---
title: Breast Cancer Detection
description: Learn how to use Pachyderm and the SDK to set up multiple pipelines that iterate on one another to detect breast cancer from pipeline specs
directory: true 
weight: 04 
---

{{%notice tip%}}
You can download this repo at `pachyderm/docs-content` and navigate to `latest/sdk/examples/breast_cancer_detection` to execute the following steps.
{{% /notice %}}

This is a reproduction of the [example](https://github.com/pachyderm/examples/tree/master/breast-cancer-detection) found in Pachyderm's examples repository. Rather than using `pachctl`, the repos and pipelines are created using their Python SDK analogues.

**Prerequisites:**
- A running [Pachyderm cluster](https://docs.pachyderm.com/latest/get-started/)
- Install the latest package of pachyderm-sdk

**To run:**
From within the latest/sdk/examples/breast_cancer_detection directory:
```shell
$ python breast_cancer_detection.py
```
