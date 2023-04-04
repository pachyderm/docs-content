---
# metadata #
title:  List Global ID Sub Commits 
description: Learn how to list global commits and jobs.
date:
# taxonomy #
tags: ["provenance"]
series:
seriesPart:

weight: 
---

List All Commits And Jobs With A Global ID

To list all (sub) commits involved in a global commit:
```s
pachctl list commit 1035715e796f45caae7a1d3ffd1f93ca
```
```s
REPO         BRANCH COMMIT                           FINISHED      SIZE        ORIGIN DESCRIPTION
images       master 1035715e796f45caae7a1d3ffd1f93ca 5 minutes ago 238.3KiB    USER
edges.spec   master 1035715e796f45caae7a1d3ffd1f93ca 5 minutes ago 244B        ALIAS
montage.spec master 1035715e796f45caae7a1d3ffd1f93ca 5 minutes ago 405B        ALIAS
montage.meta master 1035715e796f45caae7a1d3ffd1f93ca 4 minutes ago 1.656MiB    AUTO
edges        master 1035715e796f45caae7a1d3ffd1f93ca 5 minutes ago 133.6KiB    AUTO
edges.meta   master 1035715e796f45caae7a1d3ffd1f93ca 5 minutes ago 373.9KiB    AUTO
montage      master 1035715e796f45caae7a1d3ffd1f93ca 4 minutes ago 1.292MiB    AUTO
```

Similarly, change `commit` in `job` to list all (sub) jobs linked to your global job ID.
```s
pachctl list job 1035715e796f45caae7a1d3ffd1f93ca
```
```s
ID                               PIPELINE STARTED       DURATION  RESTART PROGRESS  DL       UL       STATE
1035715e796f45caae7a1d3ffd1f93ca montage  5 minutes ago 4 seconds 0       1 + 0 / 1 79.49KiB 381.1KiB success
1035715e796f45caae7a1d3ffd1f93ca edges    5 minutes ago 2 seconds 0       1 + 0 / 1 57.27KiB 22.22KiB success
```
For each pipeline execution (sub job) within this global job, {{%productName%}} shows the time since each sub job started and its duration, the number of datums in the PROGRESS section,  and other information.
The format of the progress column is `DATUMS PROCESSED + DATUMS SKIPPED / TOTAL DATUMS`.

For more information, see [Datum Processing States](../../../concepts/pipeline-concepts/datum/datum-processing-states/).

{{% notice note %}}
The global commit and global job above are the result of
a `pachctl put file images@master -i images.txt` in the images repo of [the open cv example](../../../getting-started/beginner-tutorial/).
{{% /notice %}}

The following diagram illustrates the global commit and its various components:
![global_commit_after_putfile](/images/global_commit_after_putfile.png)

Let's take a look at the origin of each commit.

{{% notice note %}}
Check the list of [all commit origins](../../data-concepts/commit) in the `Commit` page.
{{% /notice %}}


1. Inspect the commit ID `1035715e796f45caae7a1d3ffd1f93ca` in the `images` repo,  the repo in which our change (`put file`) has originated:

    ```s
    pachctl inspect commit images@1035715e796f45caae7a1d3ffd1f93ca --raw
    ```
    Note that this original commit is of `USER` origin (i.e., the result of a user change).

    ```json
    "origin": {
    "kind": "USER"
        },
    ```

2. Inspect the following commit 1035715e796f45caae7a1d3ffd1f93ca produced in the output repos of the edges pipeline:
    ```s
    pachctl inspect commit edges@1035715e796f45caae7a1d3ffd1f93ca --raw
    ```
    ```json
    {
        "commit": {
            "branch": {
            "repo": {
                "name": "edges",
                "type": "user"
            },
            "name": "master"
            },
            "id": "1035715e796f45caae7a1d3ffd1f93ca"
        },
        "origin": {
            "kind": "AUTO"
        },
        "parent_commit": {
            "branch": {
            "repo": {
                "name": "edges",
                "type": "user"
            },
            "name": "master"
            },
            "id": "28363be08a8f4786b6dd0d3b142edd56"
        },
        "started": "2021-07-07T13:52:34.140584032Z",
        "finished": "2021-07-07T13:52:36.507625440Z",
        "direct_provenance": [
            {
            "repo": {
                "name": "edges",
                "type": "spec"
            },
            "name": "master"
            },
            {
            "repo": {
                "name": "images",
                "type": "user"
            },
            "name": "master"
            }
        ],
        "details": {
            "size_bytes": "22754"
        }
    }

    ```
    Note that the origin of the commit is of kind **`AUTO`** as it has been trigerred by the arrival of a commit in the upstream repo `images`.
    ```json
        "origin": {
            "kind": "AUTO"
        },
    ```

    The same origin (`AUTO` ) applies to the commits sharing that same ID in the `montage` output repo as well as `edges.meta` and `montage.meta` system repos. 

 {{% notice info %}}
 Check the list of [all types of repos](../../data-concepts/repo) in the `Repo` page.
 {{% /notice %}}

- Besides  the `USER` and `AUTO` commits, notice a set of `ALIAS` commits in `edges.spec` and `montage.spec`:
```s
pachctl inspect commit edges.spec@336f02bdbbbb446e91ba27d2d2b516c6 --raw
```
The version of each pipeline within their respective `.spec` repos are neither the result of a user change, nor of an automatic change.
They have, however, contributed to the creation of the previous `AUTO` commits. 
To make sure that we have a complete view of all the data and pipeline versions involved in all the commits resulting from the initial 
`put file`, their version is kept as `ALIAS` commits under the same global ID.

For a full view of GlobalID in action, take a look at our [GlobalID illustration](https://github.com/pachyderm/pachyderm/tree/{{% majorMinorVersion %}}/examples/globalID).