---
# metadata # 
title: Job Metrics
description: Learn about the job metrics available. 
date: 
# taxonomy #
tags: 
series:
seriesPart:
hidden: true
--- 

The following job metrics are available for {{%productName%}}.

| Metric                                     | Description                                 |
|--------------------------------------------|---------------------------------------------|
| pachyderm_worker_datum_count               | A counter tracking the number of datums processed by a pipeline      |
| pachyderm_worker_datum_proc_time| A histogram tracking the time spent in user code for datums processed by a pipeline |
| pachyderm_worker_datum_proc_seconds_count| A counter tracking the total time spent in user code by a pipeline |
| pachyderm_worker_datum_download_time | A histogram tracking the time spent downloading input data by a pipeline |
| pachyderm_worker_datum_download_seconds_count| A counter tracking the total time spent downloading input data by a pipeline|
| pachyderm_worker_datum_upload_time| A histogram tracking the time spent uploading output data by a pipeline|
| pachyderm_worker_datum_upload_seconds_count| A counter tracking the total time spent uploading output data by a pipeline|
| pachyderm_worker_datum_download_size| A histogram tracking the size of input data downloaded by a pipeline|
| pachyderm_worker_datum_download_bytes_count| A counter tracking the total size of input data downloaded by a pipeline|
| pachyderm_worker_datum_upload_size| A histogram tracking the size of output data uploaded by a pipeline|
| pachyderm_worker_datum_upload_bytes_count| A counter tracking the total size of output data uploaded by a pipeline|


