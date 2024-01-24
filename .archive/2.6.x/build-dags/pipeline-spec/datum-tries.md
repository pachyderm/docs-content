---
# metadata # 
title:  Datum Tries PPS
description: Define the number of job attempts to run on a datum when a failure occurs.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: optional
weight: 1
---
## Spec 
This is a top-level attribute of the pipeline spec. 

```s

"datum_tries": int,

```

## Behavior 

The `datum_tries` attribute in a {{% productName %}} pipeline specifies the maximum number of times that Pachyderm will try to process a datum. When a datum fails to process, either because of an error in the processing logic or because it exceeds the [`datum_timeout`](/{{%release%}}/build-dags/pipeline-spec/datum-timeout) value, {{% productName %}} will automatically retry the datum until it is successful or the number of `datum_tries` has been reached.

Each retry of a datum is treated as a new attempt, and the datum is added back to the job queue for processing. The retry process is transparent to the user and happens automatically within the {{% productName %}} system.

Other considerations:

- `datum_tries` is set to `3`  by default if unspecified. 
- Setting to `1` attempts a datum once with no retries.
- If all tries have been exhausted and processing has not succeeded, the datum is marked as `Failed`.


## When to Use 

 You should consider setting a higher `datum_tries` count if your pipeline has a large number of datums that are prone to errors or timeouts, or if the datums you are working with have to be imported or fetched (via data ingress) from an external source.

