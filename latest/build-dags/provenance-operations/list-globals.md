---
# metadata #
title:  List Global Commits & Jobs
description: Learn how to list global commits and jobs.
date:
# taxonomy #
tags: ["provenance"]
series:
seriesPart:

weight: 
---

You can list all global commits by running the following command: 

```s
pachctl list commit
```
Each global commit displays how many (sub) commits it is made of.
```s
ID                               SUBCOMMITS PROGRESS CREATED        MODIFIED
1035715e796f45caae7a1d3ffd1f93ca 7          ▇▇▇▇▇▇▇▇ 7 seconds ago  7 seconds ago
28363be08a8f4786b6dd0d3b142edd56 6          ▇▇▇▇▇▇▇▇ 24 seconds ago 24 seconds ago
e050771b5c6f4082aed48a059e1ac203 4          ▇▇▇▇▇▇▇▇ 24 seconds ago 24 seconds ago
```
Similarly, if you run the equivalent command for global jobs:
```s
pachctl list job
```
you will notice that the job IDs are shared with the global commit IDs.

```s
ID                               SUBJOBS PROGRESS CREATED            MODIFIED
1035715e796f45caae7a1d3ffd1f93ca 2       ▇▇▇▇▇▇▇▇ 55 seconds ago     55 seconds ago
28363be08a8f4786b6dd0d3b142edd56 1       ▇▇▇▇▇▇▇▇ About a minute ago About a minute ago
e050771b5c6f4082aed48a059e1ac203 1       ▇▇▇▇▇▇▇▇ About a minute ago About a minute ago
```
For example, in this example, 7 commits and 2 jobs are involved in the changes occured
in the global commit ID `1035715e796f45caae7a1d3ffd1f93ca`.

{{% notice note %}}

The progress bar is equally divided to the number of steps, or pipelines, you have in your DAG. In the example above,`1035715e796f45caae7a1d3ffd1f93ca` is two steps.
If one of the sub-jobs fails, you will see the progress bar turn red for that pipeline step. To troubleshoot, look into that particular pipeline execution.
{{% /notice %}}
