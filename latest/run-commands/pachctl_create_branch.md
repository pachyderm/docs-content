---
date: 2023-08-04T13:05:50-04:00
title: "pachctl create branch"
slug: "Learn about the pachctl_create_branch command"
---

## pachctl create branch

Create a new branch, or update an existing branch, on a repo.

### Synopsis

This command creates or updates a branch on a repo. 

	- To create a branch for a repo in a particular project, use the `--project` flag; this requires the repo to already exist in that project 
	- To attach an existing commit as the head commit of the new branch, use the `--head` flag 
	- To set a trigger, use the `--trigger` flag, pass in the branch (from same repo, without `repo@`), and set conditions using any of the `--trigger` options 
	- To require all defined triggering conditions to be met, use the `--trigger-all` flag; otherwise, each condition can execute the trigger 
	- To attach provenance to the new branch, use the `--provenance` flag. You can inspect provenance using `pachctl inspect branch foo@bar` 

Note: Starting a commit on the branch also creates it, so there's often no need to call this.

```
pachctl create branch <repo>@<branch> [flags]
```

### Examples

```
	- pachctl create branch foo@master 
	- pachctl create branch foo@master --project bar 
	- pachctl create branch foo@master --head 0001a0100b1c10d01111e001fg00h00i 
	- pachctl create branch foo@master=0001a0100b1c10d01111e001fg00h00i 
	- pachctl create branch foo@master --provenance=foo@branch1,foo@branch2 
	- pachctl create branch foo@master --trigger staging 
	- pachctl create branch foo@master --trigger staging --trigger-size=100M 
	- pachctl create branch foo@master --trigger staging --trigger-cron='@every 1h' 
	- pachctl create branch foo@master --trigger staging --trigger-commits=10' 
	- pachctl create branch foo@master --trigger staging --trigger-size=100M --trigger-cron='@every 1h --trigger-commits=10 --trigger-all 

```

### Options

```
      --head string           Set the head of the newly created branch using <branch-or-commit> or <repo>@<branch>=<id>
  -h, --help                  help for branch
      --project string        Specify the project (by name) where the repo for this branch is located. (default "standard-ml-tutorial")
  -p, --provenance []string   Set the provenance for the branch. format: <repo>@<branch> (default [])
  -t, --trigger string        Specify the branch name that triggers this branch.
      --trigger-all           Specify that all set conditions must be met for the trigger.
      --trigger-commits int   Set the number of commits as a condition for the trigger.
      --trigger-cron string   Set a cron spec interval as a condition for the trigger.
      --trigger-size string   Set data size as a condition for the trigger.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl create](/commands/pachctl_create/)	 - Create a new instance of a Pachyderm resource.

