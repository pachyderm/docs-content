---
# metadata # 
title: NLP Pipeline
description: Learn how to create a NLP (Natural Language Processing) pipeline.
date: 
# taxonomy #
tags: ["integrations", "nlp"]
series:
seriesPart:
weight: 6
beta: false 
---

In this tutorial, we'll build an [NLP](/{{% release %}}/learn/glossary/nlp) (Natural Language Processing) pipeline to classify the sentiment of financial news articles. This tutorial shows how to combine inputs from separate sources, incorporates data labeling, model training, and data visualization.

## Before You Start 

- You must have {{% productName %}} installed and running on your cluster
- You should have already completed the [Standard ML Pipeline](/{{%release%}}/build-dags/tutorials/basic-ml) tutorial
- You should have completed the [Label Studio](/{{%release%}}/integrate/label-studio) integration guide
- This tutorial assumes your active context is `localhost:80`

## Tutorial 

Our Docker image's [user code](/{{%release%}}/learn/glossary/user-code) for this tutorial is built on top of the [pytorch/pytorch](https://github.com/civisanalytics/datascience-python) base image, which includes necessary dependencies. This image also uses the [FinBERT](https://huggingface.co/ProsusAI/finbert) pre-trained NLP model for sentiment analysis.

### 1. Create Your Repos
1. Make sure your `tutorials` project we created in the [Standard ML Pipeline](/{{%release%}}/build-dags/tutorials/basic-ml) tutorial is set to your active context. (This would only change if you have updated your active context since completing the first tutorial.)

   ```s
   pachctl config get context localhost:80

   # {
   #   "pachd_address": "grpc://localhost:80",
   #   "cluster_deployment_id": "KhpCZx7c8prdB268SnmXjELG27JDCaji",
   #   "project": "Tutorials"
   # }
   ```
2. Create the following repos:
   ```s
   pachctl create repo financial_phrase_bank
   pachctl create repo language_model
   pachctl create repo labeled_data
   pachctl create repo sentiment_words
   ```

### 2. Create Your Pipelines

1. Create the following pipelines:
   ```s
   pachctl create pipeline -f pachyderm/dataset.json
   pachctl create pipeline -f pachyderm/train_model.json
   pachctl create pipeline -f pachyderm/visualizations.json
   pachctl create pipeline -f pachyderm/query_es.json
   ```


---
## User Code Assets 






## TLDR;
```bash
# Upload the Financial Phrase Bank data
pachctl create repo financial_phrase_bank
pachctl put file financial_phrase_bank@master:/Sentences_50Agree.txt -f data/FinancialPhraseBank-v1.0/Sentences_50Agree.txt

# Download the pre-trained BERT language model
./download_model.sh

# Upload the language model to Pachyderm
pachctl create repo language_model
cd models/finbertTCR2/; pachctl put file -r language_model@master -f ./; cd ../../

# Set up labeled_data repo for labeling production data later
pachctl create repo labeled_data
pachctl start commit labeled_data@master; pachctl finish commit labeled_data@master

# Deploy the dataset creation pipeline
pachctl create pipeline -f pachyderm/dataset.json

# Deploy the training pipeline
pachctl create pipeline -f pachyderm/train_model.json

# (Optional) Use a sentiment word list to visualize the current dataset
pachctl create repo sentiment_words
pachctl put file sentiment_words@master:/LoughranMcDonald_SentimentWordLists_2018.csv -f resources/LoughranMcDonald_SentimentWordLists_2018.csv
pachctl create pipeline -f pachyderm/visualizations.json

# Tag our current dataset as branch v1 (easy to referr to later on)
pachctl create branch financial_phrase_bank@v1 --head master

# Modify the version of Financial Phrase Bank dataset used
pachctl start commit financial_phrase_bank@master
pachctl delete file financial_phrase_bank@master:/Sentences_50Agree.txt
pachctl put file financial_phrase_bank@master:/Sentences_AllAgree.txt -f data/FinancialPhraseBank-v1.0/Sentences_AllAgree.txt
pachctl finish commit financial_phrase_bank@master

# Version our new dataset
pachctl create branch financial_phrase_bank@v2 --head master

# Show the diff between the datasets
pachctl diff file financial_phrase_bank@v2 financial_phrase_bank@v1

# Inspect everything impacted by v1 of our dataset
pachctl wait commit financial_phrase_bank@v1 --raw

# Download the trained model
pachctl get file -r train_model@master:/ -o trained_model/

# Deploy the model (See Seldon or Algorithmia examples)

# Run Label Studio locally to labeling production data
pachctl create pipeline -f pachyderm/query_es.json
docker run -it -p 8080:8080 -v `pwd`/mydata:/label-studio/data jimmywhitaker/labelstudio:v1.0.1
# Note: see the Label Studio integration to learn how to connect with the Pachyderm Cluster

# As data is labeled, our model_train pipeline automatically retrains on the new data
```

## Labeling
Most production machine learning models rely on supervised learning, however incorporating new, labeled data into a model is often a manual process. Pachyderm helps us avoid that by versioning our data and automatically running pipelines when our data changes.

In this example, we integrate [Label Studio](https://labelstud.io/) to facilitate human interaction while providing training and deployment automation.

For more details on creating a sentiment analysis labeling project, see our [example integration](https://github.com/pachyderm/examples/tree/master/label-studio). 

## Dataset Creation

The dataset creation step will combine the Financial Phrase Bank dataset with newly labeled data into a single dataset. It is a simple script that takes the Union of the `financial_phrase_bank` and `labeled_data` repositories to generate a single dataset. 

## Model Training
Our model training pipeline uses the BERT fine-tuning script from [FinBERT](https://huggingface.co/ProsusAI/finbert). It relies on two input repositories. 
1. The language model - our pre-trained financial language model that will be tuned to our new task. 
2. The dataset - sentiment analysis data that will be used to train our model.

The model_train pipeline is GPU enabled, but if you do not have access to a GPU in your cluster, then you can remove the resource requirements in `pachyderm/train_model.json`. It will function, but run much slower. 

## Visualization (Optional)
The `visualization` pipeline provides exploration and understanding of our dataset and includes the following.  
1. Correlation matrix showing the relationship between the sentiment words and the assigned label. 
2. Histogram of frequent words in the training set. 
3. Word cloud of the training data. 

## Deploy Model
Once we have a tuned model trained, we can deploy it as a REST endpoint for inference. We currently support the following integrations to deploy this model: 

- [Seldon Deploy Integration](../seldon/)
- [Algorithmia Integration](../algorithmia/)
