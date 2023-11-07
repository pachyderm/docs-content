---
# metadata # 
title:  Set Branch Triggers
description: Learn how to use branch triggers to automate deferred processing.
date: 
# taxonomy #
tags: ["deferred processing", "branches"]
series:
seriesPart:
weight: 
mermaid: true
---

You can automate re-pointing from one branch to another by using **branch triggers**. A branch trigger is a relationship between two branches, such as `master` and `staging`. When the head commit of `staging` meets a certain condition, it triggers `master` to update its head to that same commit. In other words, it does `pachctl create branch data@master --head staging` automatically when the trigger condition is met.

You can set branch triggers to fire when:

- A certain amount of time has passed (`--trigger-cron`)
- A specific number of commits have been made (`--trigger-size`)
- The amount of unprocessed data reaches a certain size (`--trigger-commits`)

When more than one is specified, a branch repoint will be triggered when any of
the conditions is met. To guarantee that they all must be met, add
`--trigger-all`.


## How to Automate Deferred Processing via Branch Triggers

Let's make the `master` branch automatically trigger when there's 1 Megabyte of new data on the `staging` branch.

1. Create a repo.
```s
pachctl create repo data
```
2. Create the staging branch. This is the **target** branch that will trigger the master branch to update its head; as of 2.8.0, it must be created first.

```s
pachctl create branch data@staging
```

3. Create a master branch with trigger settings (see [pachctl create branch options](/{{%release%}}/run-commands/pachctl_create_branch#options)).

```s
pachctl create branch data@master --trigger staging --trigger-size 1MB
```
4. View your branches.

```s 
pachctl list branch data 
```
```s
BRANCH  HEAD                             TRIGGER              
staging f35c5e5d6b4c499eaae0ab0c733ad7a6 -                    
master  383c2acb298e4d6aa8327ea49aaeede6 staging on Size(1MB) 
```

{{% notice tip %}}
You can test your trigger using a command similar to the following: 

```s
dd if=/dev/urandom bs=1M count=1 | pachctl put file data@staging:/file
pachctl list branch data
```

```s
BRANCH  HEAD                             TRIGGER              
staging 5e27464aab4c4857bfd5d402afe043c6 -                    
master  5e27464aab4c4857bfd5d402afe043c6 staging on Size(1MB) 
```

{{% /notice %}}

## How to Manually Trigger Master

Triggers automate deferred processing, but they don't prevent manually updating the head of a branch. If you ever want to trigger `master` even though the trigger condition hasn't been met, you can run:

```s
pachctl create branch data@master --head staging
```

Notice that you don't need to re-specify the trigger when you call `create branch` to change the head. If you do want to clear the trigger delete the branch and recreate it.

To experiment further, see the full [triggers example](https://github.com/pachyderm/examples/tree/master/deferred_processing/triggers).