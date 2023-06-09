---
# metadata # 
title: Branch
description: Learn about the concept of a branch, which is a pointer to a commit that moves along with new commits as they are submitted. 
glossaryDefinition: A pointer to a commit that moves along with new commits as they are submitted.
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series: ["glossary"]
seriesPart:
--- 

## About 
A {{% productName %}} branch is a pointer to a [commit](/{{%release%}}/learn/glossary/commit) that moves along with new commits. By default, {{% productName %}} does not create any branches when you create a repository. Most users create a `master` branch to initiate the first commit.

Branches allow collaboration between teams of data scientists. However, the `master` branch is sufficient for most users.

Each branch stores information about [provenance](/{{%release%}}/learn/glossary/provenance), including input and output branches. {{% productName %}} pipelines trigger a job when changes are detected in the `HEAD` of a branch.

You can create additional branches with `pachctl create branch` and view branches with `pachctl list branch`. Deleting a branch doesn't delete its commits, and all branches require a head commit.

## Example

```s
pachctl list branch images

# BRANCH HEAD
# master c32879ae0e6f4b629a43429b7ec10ccc
```