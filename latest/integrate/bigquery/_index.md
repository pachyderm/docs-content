---
# metadata # 
title: Google BigQuery Connector
description: Learn how to use the Google BigQuery connector to ingest data.
date: 
# taxonomy #
tags: ["integrations", "bigquery", "google"]
series:
seriesPart:
weight: 
beta: true 
---

This connector ingests the result of a BigQuery query into Pachyderm. With this connector, you can easily create pipelines that read data from BigQuery and process it using Pachyderm's powerful data parallelism and versioning capabilities. It uses python and the python-bigquery-pandas library built by Google. 


## Before You Start

- You must have a Google Cloud Platform account with a project that has BigQuery enabled.
- You must download the following files.

[dockerfile](./Dockerfile)

{{< githubCodeSnippet repo="pachyderm/examples" file="bigquery/Dockerfile" lines="1-30" >}}

{{< githubCodeSnippet repo="pachyderm/examples" file="bigquery/gbq_ingest.jsonnet" lines="1-30" lang="json">}}



## 1. Create a Dataset & Service Account
Before using this connector, you will need to create a BigQuery dataset and a service account with the necessary permissions.

1. Go to the BigQuery web UI and create a new dataset.
2. In the GCP Console, go to the IAM & admin section and create a new [service account](https://console.cloud.google.com/iam-admin/serviceaccounts/).
3. Grant the service account the BigQuery Data Viewer and BigQuery Data Editor roles for the dataset you created in step 1.
4. Download the private key file for the service account, give it a descriptive name (e.g., `gbq-pachyderm-creds.json`), and save it to a secure location.

Once you have completed these steps, you can use the connector by simply specifying your service account key file and the name of your BigQuery query in the jsonnet pipeline spec for your pipeline.

## 2. Create a Pachyderm Secret

Create the secret (be sure to add the namespace if your cluster is deployed in one).

{{< stack type="wizard">}}
{{% wizardRow id="Namespaced" %}}
{{% wizardButton option="Yes" state="active" %}}
{{% wizardButton option="No" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="namespaced/yes" %}}
```bash
kubectl create secret generic gbqsecret --from-file=gbq-pachyderm-creds.json -n mynamespace
```
{{% /wizardResult %}}
{{% wizardResult val1="namespaced/no" %}}
```bash
kubectl create secret generic gbqsecret --from-file=gbq-pachyderm-creds.json
```
{{% /wizardResult %}}
{{% /wizardResults %}}
{{< /stack >}}


## 3. Create the Jsonnet Pipeline 

Run the pipeline template with jsonnet. Note, this pipeline will not run immediately, but rather will wait until the next cron tick. E.g. if you have it set to `5m`, you will wait 5 minutes until the first run of the pipeline. 

```bash
$ pachctl update pipeline --jsonnet gbq_ingest.jsonnet \
--arg inputQuery="SELECT country_name, alpha_2_code FROM bigquery-public-data.utility_us.country_code_iso WHERE alpha_2_code LIKE 'A%'" \
--arg outFile="gbq_output.parquet" \
--arg project="<gcp_project_name>" \
--arg cronSpec="@every 5m"
--arg credsFile="gbq-pachyderm-creds.json"
```

## Additional Details
### Cron Spec 
In some cases, you may not want your cron pipeline to run every 5 minutes as shown in the example above. For example, when testing a large ingestion, you may want to run the pipeline manually. To do this, you can use a cron specification that never triggers, such as `--arg cronSpec="* * 31 2 *"`. This value will never trigger the cron pipeline (it refers to a nonexistent date - 31st of Feb). 

To manually trigger the cron pipeline, run the following command:
```bash
pachctl run cron gbq_ingest 
```

For more information on using cron with Pachyderm pipelines, see the [cron documentation](https://docs.pachyderm.com/2.4.x/concepts/pipeline-concepts/pipeline/cron/). 

### Configuring your own pipeline spec
You can configure your own pipeline spec with the secret by using these parameters in the pipeline spec. 

```json
"secrets": [ {
    "name": "gbqsecret",
    "mount_path": "/kubesecret/"}]
```
and
```json
    "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/kubesecret/gbq-pachyderm-creds.json"
    },
```

### Links to Relevant Documentation
- [Pachyderm documentation](https://docs.pachyderm.com/)
- [Pachyderm cron spec documentation](https://docs.pachyderm.com/2.4.x/concepts/pipeline-concepts/pipeline/cron/)
- [Google Cloud Platform documentation](https://cloud.google.com/docs)
- [BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/)
- [Troubleshooting tips for the BigQuery API](https://cloud.google.com/bigquery/troubleshooting-errors)