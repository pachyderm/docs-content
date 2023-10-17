---
# metadata # 
title: Get Metadata
description: Learn how to view additional datum metadata using the pachctl get file command. 
date: 
# taxonomy #
tags: ["datums"]
series:
seriesPart:
---

Once a pipeline has finished a job, **you can access additional execution metadata about the datums processed** in the associated meta system repo. Note that all the `inspect datum` information above is stored in this meta repo, along with a couple more. For example, you can find the `reason` in `meta/<datumID>/meta`: the error message when the datum failed.

See the detail of the meta repo structure below.

{{% notice info %}}
A meta repo contains 2 directories:

- `/meta/`: The `meta` directory holds datums' statistics
- `/pfs`: The `pfs` directory holds the input data of datums, and their resulting output data

```s
pachctl list file edges.meta@master
```

**System response:**

```s
NAME   TAG TYPE SIZE
/meta/     dir  1.956KiB
/pfs/      dir  371.9KiB
```
{{% /notice %}}


### Meta directory
The **meta directory holds each datum's JSON metadata**, and can be accessed using a `get file`:

#### Example 

```s
pachctl get file edges.meta@master:/meta/002f991aa9db9f0c44a92a30dff8ab22e788f86cc851bec80d5a74e05ad12868/meta | jq
```

**System response:**

```s
{
  "job": {
    "pipeline": {
      "name": "edges"
    },
    "id": "efca9595bdde4c0ba46a444a5877fdfe"
  },
  "inputs": [
    {
      "fileInfo": {
        ...
    }
  ],
  "hash": "28e6675faba53383ac84b899d853bb0781c6b13a90686758ce5b3644af28cb62f763",
  "stats": {
    "downloadTime": "0.103591200s",
    "processTime": "0.374824700s",
    "uploadTime": "0.001807800s",
    "downloadBytes": "80588",
    "uploadBytes": "38046"
  },
  "index": "1"
}
```

Use`pachctl list file edges.meta@master:/meta/` to list the files in the meta directory.

### Pfs Directory
The pfs directory has both the **input files** of datums, and the resulting **output files** that were committed to the output repo:

#### Example 

```s
pachctl list file montage.meta@master:/pfs/47be06d9e614700397d8d56272a1a5e039df82bf931e8e3c9d34bccbfbc8b349/
```

**System response:**

```s
NAME                                                                          TAG TYPE SIZE
/pfs/47be06d9e614700397d8d56272a1a5e039df82bf931e8e3c9d34bccbfbc8b349/edges/      dir  133.6KiB
/pfs/47be06d9e614700397d8d56272a1a5e039df82bf931e8e3c9d34bccbfbc8b349/images/     dir  238.3KiB
/pfs/47be06d9e614700397d8d56272a1a5e039df82bf931e8e3c9d34bccbfbc8b349/out/        dir  1.292MiB
```

Use `pachctl list file montage.meta@master:/pfs/` to list the files in the pfs directory.
