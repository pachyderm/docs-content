---
# metadata # 
title: Cron
description: Learn about the concept of a cron
glossaryDefinition: 
date: 
# taxonomy #
tags: ["concepts", "triggers", "data-operations", "pipeline"]
series: ["glossary"]
seriesPart:
--- 

## About 

A [cron](https://en.wikipedia.org/wiki/Cron), short for "chronograph," is a time-based job scheduler that allows users to schedule and automate the execution of recurring tasks or commands at specific intervals. These tasks, referred to as cron jobs, are typically scripts or commands that perform specific actions.

{{% productName %}} uses the concept of crons in two ways: a [cron pipeline spec](/{{%release%}}/learn/glossary/input-cron), and a [cron trigger](/{{%release%}}/build-dags/branch-operations/set-branch-triggers).

### Cron Pipelines vs Cron Triggers

Cron Pipelines trigger on their specified cron interval, *plus* each time a new input data is added. This enables you to create pipelines that trigger jobs *at least once* on a regular schedule. This could be useful if you periodically make changes to your user code, but have no reason to commit more data. When you do commit more data, the Cron Pipeline still triggers as a normal pipeline would.

Cron Triggers enable you to set up a scheduled reoccurring event on a repo branch that evaluates and fires the trigger. When a Cron Trigger fires, but no new data has been added, there are no new downstream commits or jobs.
