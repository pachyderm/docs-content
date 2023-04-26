---
# metadata # 
title: Provenance
description: Learn about the concept of provenance, which is the recorded data lineage that tracks the dependencies and relationships between datasets.
glossaryDefinition: The recorded data lineage that tracks the dependencies and relationships between datasets. 
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series: ["glossary"]
seriesPart:
mermaid: true
--- 
## About 

Provenance in {{% productName %}} refers to the tracking of the dependencies and relationships between datasets, as well as the ability to go back in time and see the state of a dataset or repository at a particular moment. {{% productName %}} models both [commit](/{{%release%}}/learn/glossary/commit) provenance and [branch](/{{%release%}}/learn/glossary/branch) provenance to represent the dependencies between data in the pipeline.

### Commit Provenance
Commit provenance refers to the relationship between commits in different repositories. If a commit in a repository is derived from a commit in another repository, the derived commit is provenant on the source commit. Capturing this relationship supports queries regarding how data in a commit was derived.

### Branch Provenance
Branch provenance represents a more general relationship between data. It asserts that future commits in the downstream branch will be derived from the head commit of the upstream branch.

## Traversing Provenance

{{% productName %}} automatically maintains a complete audit trail, allowing all results to be fully reproducible. To track the direct provenance of commits and learn where the data in the repository originates, you can use the `pachctl inspect command` to view provenance information, including the origin kind, direct provenance, and size of the data.

{{% productName %}}'s DAG structure makes it easy to traverse the provenance and subvenance in any commit. All related steps in a DAG share the same [global identifier](/{{%release%}}/learn/glossary/globalid), making it possible to run `pachctl list commit <commitID>` to get the full list of all the branches with commits created due to provenance relationships.
