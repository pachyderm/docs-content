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

Provenance in {{% productName %}} refers to the tracking of the dependencies and relationships between datasets, as well as the ability to go back in time and see the state of a dataset or repository at a particular moment. It allows users to track all revisions of their data and understand the connection between the data stored in one repository and the results in the other repository. {{% productName %}} automatically maintains a complete audit trail, allowing all results to be fully reproducible.

{{% productName %}} provides the `pachctl inspect` command to track the direct provenance of [commits](../commit) and learn where the data in the repository originates. By running this command, users can view provenance information, including the origin kind, direct provenance, and size of the data.

{{% productName %}}'s DAG structure makes it easy to traverse the provenance and [subvenance](../subvenance) in any commit. All related steps in a DAG share the same [global identifier](../globalID), making it possible to run `pachctl list commit <commitID>` to get the full list of all the [branches](../branch) with commits created due to provenance relationships. 