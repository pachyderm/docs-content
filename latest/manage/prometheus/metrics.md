---
# metadata # 
title: Metrics
description: Learn about the job metrics available. 
date: 
# taxonomy #
tags: 
series:
seriesPart:
aliases: ["job-metrics", "pachd-metrics"]
--- 

| Metric | Type | Description |
|---|---|---|
| pachyderm_worker_datum_count | Counter | Counts the number of datums processed by a pipeline. |
| pachyderm_worker_datum_proc_time | Histogram | Tracks the time spent in user code for datums processed by a pipeline. |
| pachyderm_worker_datum_proc_seconds_count | Counter | Counts the total time spent in user code by a pipeline. |
| pachyderm_worker_datum_download_time | Histogram | Tracks the time spent downloading input data by a pipeline. |
| pachyderm_worker_datum_download_seconds_count | Counter | Counts the total time spent downloading input data by a pipeline. |
| pachyderm_worker_datum_upload_time | Histogram | Tracks the time spent uploading output data by a pipeline. |
| pachyderm_worker_datum_upload_seconds_count | Counter | Counts the total time spent uploading output data by a pipeline. |
| pachyderm_worker_datum_download_size | Histogram | Tracks the size of input data downloaded by a pipeline. |
| pachyderm_worker_datum_download_bytes_count | Counter | Counts the total size of input data downloaded by a pipeline. |
| pachyderm_worker_datum_upload_size | Histogram | Tracks the size of output data uploaded by a pipeline. |
| pachyderm_worker_datum_upload_bytes_count | Counter | Counts the total size of output data uploaded by a pipeline. |
| pachyderm_auth_dex_approval_errors_total | Counter | Counts the number of HTTP requests to /approval that ended in error. |
| pachyderm_auth_dex_http_requests_duration_seconds | Histogram | Histogram of time spent processing Dex requests, by response status code and HTTP method. |
| pachyderm_auth_dex_http_requests_in_flight | Gauge | Tracks the number of requests currently being handled by Dex. |
| pachyderm_auth_dex_http_requests_total | Counter | Counts the number of HTTP requests handled by Dex, by response status code and HTTP method. |
| pachyderm_auth_dex_startup_errors_total | Counter | Counts the number of HTTP requests that were rejected because the server can't start. |
| pachyderm_pachd_admin_v2_inspect_cluster_seconds | Histogram | Tracks the run time of InspectCluster. |
| pachyderm_pachd_auth_v2_who_am_i_seconds | Histogram | Tracks the run time of WhoAmI. |
| pachyderm_pachd_enterprise_v2_get_state_seconds | Histogram | Tracks the run time of GetState. |
| pachyderm_pachd_grpc_check_seconds | Histogram | Tracks the run time of Check. |
| pachyderm_pachd_pfs_v2_list_repo_seconds | Histogram | Tracks the run time of ListRepo. |
| pachyderm_pachd_pps_v2_list_pipeline_seconds | Histogram | Tracks the run time of ListPipeline. |
| pachyderm_pachd_report_metric | Gauge | Tracks the gauge of the number of calls to reportDuration(). |
| pachyderm_pfs_object_storage_cache_evictions_total | Counter | Counts the number of objects evicted from the LRU cache. |
| pachyderm_pfs_object_storage_cache_hits_total | Counter | Counts the number of object storage gets served from cache. |
| pachyderm_pfs_object_storage_cache_misses_total | Counter | Counts the number of object storage gets that were not served from cache. |
| pachyderm_pfs_object_storage_operation_count_total | Counter | Counts the number of object storage operations, by storage type and operation name. |
| pachyderm_pfs_object_storage_read_bytes_total | Counter | Counts the number of bytes read from object storage, by storage type. |
| pachyderm_pfs_object_storage_written_bytes_total | Counter | Counts the number of bytes written to object storage, by storage type. |
| pachyderm_postgres_tx_start_count | Counter | Counts the number of transactions that have been started. |
| pachyderm_postgres_tx_underlying_start_count | Counter | Counts the number of underlying database transactions that have been started. |