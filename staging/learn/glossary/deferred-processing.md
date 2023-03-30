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

1. [Input repo staging branches](TBD)
2. [Commit-specific processing](TBD)
3. [Branch triggers](TBD)
4. [Pipeline Specification triggers](TBD)
5. [Kubernetes apps that use {{% productName %}} APIs](TBD)

<!-- Todo: create guides for each method -->

 