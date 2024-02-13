---
# metadata # 
title: Delete Branch Head
description: Learn how to delete the HEAD of a branch.
date: 
# taxonomy #
tags: ["data-operations"]
series:
seriesPart:
weight: 4
---


To fix a broken HEAD, run the following command:

```s
pachctl delete commit <commit-ID>
```

When you delete a HEAD commit, {{% productName %}} performs the following actions:

- Changes HEADs of all the branches that had the bad commit as their
  HEAD to their bad commit's parent and deletes the commit. 
  **The data in the deleted commit is lost**.
  If the bad commit does not have
  a parent, {{% productName %}} sets the branch's HEAD to a new empty commit. 
- Interrupts all running jobs, including not only the
  jobs that use the bad commit as a direct input but also the ones farther
  downstream in your DAG.
- Deletes the output commits from the deleted jobs. All the actions listed above are applied to those commits as well.

{{% notice warning %}}
This command will **only succeed if the HEAD commit has no children on any branch**. `pachctl delete commit` will error when attempting to delete a HEAD commit with children. 
{{% /notice %}}

{{% notice note %}} 
Are you wondering how a HEAD commit can have children?

A commit can be the head of a branch and still have children. 
For instance, given a `master` branch in a repository named `repo`, if you branch `master` by running `pachctl create branch repo@staging --head repo@master`, the `master`'s HEAD will have an alias child on `staging`. 
{{% /notice %}}