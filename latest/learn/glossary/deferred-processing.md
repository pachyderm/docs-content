---
# metadata #
title: Deferred Processing
description: Learn about the concept of deferred processing, which allows you to commit data more frequently than you process it.
date:
# taxonomy #
tags: ["data-operations", "datums", "branch triggers", "trigger"]
series: ["glossary"]
seriesPart:
---

Deferred Processing is a technique that allows you to commit data more frequently than you process it. By default, {{% productName %}} automatically processes any newly committed data added to its input branch. For example, you may want to commit data hourly, but retrain your ML model daily. 

There are several ways to leverage deferred processing with {{% productName %}}:

1. [Defer processing via a staging branch](../../../prepare-data/dp-staging-branch)
2. [Process specific commits](../../../build-dags/branch-operations/process-specific-commits)
3. [Set branch triggers](../../../build-dags/branch-operations/set-branch-triggers)
4. [Set a custom output branch](../../../build-dags/branch-operations/set-output-branch)