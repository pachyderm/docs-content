---
# metadata # 
title: Commit
description: Learn about the concept of a commit, which is an atomic operation that snapshots and preserves the state of files/directories within a repository.
glossaryDefinition: An atomic operation that snapshots and preserves the state of files/directories within a repository.
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series: ["glossary"]
seriesPart:
--- 
## About 

In {{% productName %}}, commits snapshot and preserve the state of files and directories in a repository at a point in time.
Unlike Git, {{% productName %}} commits are centralized and transactional. You can create a commit with `pachctl start commit` and save it with `pachctl finish commit`. Once the commit is closed its contents are immutable. Commits may be chained together to represent a sequence of states. 

All commits have an alphanumeric ID, and you can reference a commit with `<repo>@<commitID>`. Each commit has an origin that indicates why it was produced (USER or AUTO).
### Global Commits 

A commit with global scope (global commit) represents the set of all provenance-dependent commits sharing the same ID.

### Sub-Commits

A commit with a more focused scope (sub-commit) represents the "Git-like" record of one commit in a single branch of a repository’s file system.

## Actions

- [List Commits](/{{%release%}}/build-dags/provenance-operations/list-globals)
<!-- - [Inspect Commit](/{{%release%}}/build-dags/provenance-operations/inspect-commit) -->
- [Squash Commit](/{{%release%}}/build-dags/provenance-operations/squash-nonhead)
- [Delete Commit](/{{%release%}}/build-dags/provenance-operations/delete-history)
- [Track Downstream Provenance](/{{%release%}}/build-dags/provenance-operations/track-downstream)