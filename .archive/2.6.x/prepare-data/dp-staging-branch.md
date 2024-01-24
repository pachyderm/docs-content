---
# metadata # 
title: Defer Processing via Staging Branch
description: Learn how to defer processing of data by using a staging branch in an input repository.
date: 
# taxonomy #
tags: ["datums", "data-operations"]
series:
seriesPart:
directory: true 
---

When you want to load data into {{%productName%}} without triggering a pipeline, you can upload it to a staging branch and then submit accumulated changes in one batch by re-pointing the `HEAD` of your `master` branch to a commit in the staging branch. Let's see how this works.

## How to Use a Staging Branch 

1. Create a repository. For example, `data`.

   ```s
   pachctl create repo data
   ```

2. Create a `master` branch.

   ```s
   pachctl create branch data@master
   ```

3. View the created branch:

   ```s
   pachctl list commit data
   ```

   ```s
   REPO BRANCH COMMIT                           FINISHED           SIZE  ORIGIN DESCRIPTION
   data master 8090bfb4d4fe44158eac12199c37a591 About a minute ago   0B  AUTO
   ```

   {{%productName%}} automatically created an empty `HEAD` commit on the new branch, as you can see from the `0B` (zero-byte) size and `AUTO` commit origin. 

4. Commit a file to a staging branch:

   ```s
   pachctl put file data@staging -f <file>
   ```

   {{%productName%}} automatically creates the `staging` branch. Your repo now has 2 branches, `staging` and `master`. In this example, the `staging` name is used, but you can name the branch as you want -- and have as many staging branches as you need.

5. Verify that the branches were created:

   ```s
   pachctl list branch data
   ```

   ```s
   BRANCH  HEAD                              TRIGGER

   staging f3506f0fab6e483e8338754081109e69   -
   master  8090bfb4d4fe44158eac12199c37a591   -
   ```

   The `master` branch still has the same `HEAD` commit. No jobs have started to process the new file, because there are no pipelines that take `staging` as inputs. You can continue to commit to `staging` to add new data to the branch, and the pipeline will not process anything.

6. When you are ready to process the data, update the `master` branch to point it to the head of the staging branch:

   ```s
   pachctl create branch data@master --head staging
   ```

7. List your branches to verify that the master branch's `HEAD` commit has changed:

   ```s
   pachctl list branch data
   ```

   ```s
   staging f3506f0fab6e483e8338754081109e69
   master  f3506f0fab6e483e8338754081109e69
   ```

   The `master` and `staging` branches now have the same `HEAD` commit. This means that your pipeline has data to process.

8. Verify that the pipeline has new jobs:

   ```s
   pachctl list job data@f3506f0fab6e483e8338754081109e69

   ID                               PIPELINE STARTED        DURATION           RESTART PROGRESS  DL   UL  STATE
   f3506f0fab6e483e8338754081109e69 data     32 seconds ago Less than a second 0       6 + 0 / 6 108B 24B success
   ```

   You should see one job that {{%productName%}} created for all the changes you have submitted to the `staging` branch, with the same ID. While the commits to the `staging` branch are ancestors of the current `HEAD` in `master`, they were never the actual `HEAD` of `master` themselves, so they do not get processed. This behavior works for most of the use cases because commits in {{%productName%}} are generally additive, so processing the HEAD commit also processes data from previous commits.