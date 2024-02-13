---
# metadata #
title:  Track Downstream
description: Learn how to track downstream commits and jobs.
date:
# taxonomy #
tags: ["provenance"]
series:
seriesPart:

weight: 3
---

## Track Provenance Downstream

{{%productName%}} provides the `wait commit <commitID>` command that enables you
to **track your commits downstream as they are produced**. 

Unlike the `list commit <commitID>`, each line is printed as soon as a new (sub) commit of your global commit finishes.

Change `commit` in `job` to list the jobs related to your global job as they finish processing a commit.

<!-- todo: elaborate on this -->