---
# metadata # 
title:  Copy Files
description: Learn how to copy files between branches.
date: 
# taxonomy #
tags: ["deferred processing", "branches"]
series:
seriesPart:
weight: 
---

Sometimes you need to be able to copy files between branches. This can be especially useful if you want to commit data in an ad-hoc, disorganized manner to a staging branch and then organize it later. 

When you run `copy file`, {{%productName%}} only copies references to the files and does not move the actual data for the files around.

## How to Copy Files Between Branches

1. Start a commit:

   ```s
   pachctl start commit data@master
   ```

2. Copy files:

   ```s
   pachctl copy file data@staging:file1 data@master:file1
   pachctl copy file data@staging:file2 data@master:file2
   ...
   ```

3. Close the commit:

   ```s
   pachctl finish commit data@master
   ```

{{% notice note %}}
While the commit is open, you can run `pachctl delete file` if you want to remove something from
the parent commit or `pachctl put file` if you want to upload something that is not in a repo yet.

{{% /notice %}}