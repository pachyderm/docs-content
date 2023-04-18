---
# metadata # 
title: Superb AI
description: Learn how to use the Superb AI connector to ingest data.
date: 
# taxonomy #
tags: ["integrations", "superb-ai"]
series:
seriesPart:
weight: 
beta: false 
---

Connect your [Superb.ai](https://www.superb-ai.com/) project to {{% productName %}} to automatically version and save data you've labeled in Superb AI to use in downstream machine learning workflows. 

This integration ingests the data into {{% productName %}} on a [cron schedule](https://docs.pachyderm.com/latest/concepts/pipeline-concepts/pipeline/cron/). Once your data is ingested into {{% productName %}}, you can perform data tests, train a model, or any other type of data automation you may want to do, all while having full end-to-end reproducibility. 

![diagram](/images/superb-ai/diagram.png)


## Before You Start 
* You must have a [Superb.AI account](https://suite.superb-ai.com/auth/create?from=homepage)
* You must have a {{% productName %}} cluster


## How to Use the Superb AI Connector


1. Generate an Access API Key in SuperbAI. 
![](/images/superb-ai/SuperbAI_api_key.png)
2. Put the key and your user name in the [`secrets.json`](secrets.json) file. 
3. Create the Pachyderm secret

```bash
pachctl create secret -f secrets.json
```

4. Create the cron pipeline to synchronize your `Sample project` from SuperbAI to {{% productName %}}. This pipeline will run every minute to check for new data (you can configure it to run more or less often in the cron spec in `sample_project.yml`).

```bash
pachctl create pipeline -f sample_project.yml
```

5. {{% productName %}} will automatically kick off the pipeline and import the data from your sample project. 
![](/images/superb-ai/pachyderm_preview.jpeg)