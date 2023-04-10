---
# metadata #
title:  List Global ID Sub Commits 
description: Learn how to list global commits and jobs.
date:
# taxonomy #
tags: ["provenance"]
series:
seriesPart:

weight: 2
---

## How to List Commits via Global ID

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

## How to List Jobs via Global ID

Tto list all (sub) jobs linked to your global job ID:
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

