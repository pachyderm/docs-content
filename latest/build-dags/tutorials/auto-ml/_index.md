---
# metadata # 
title: AutoML Pipeline
description: Learn how to build an automated machine learning pipeline 
date: 
# taxonomy #
tags: ["integrations", "automl", "mljar"]
series:
seriesPart:
weight: 2
beta: false 
---

You can use {{% productName %}} to build an automated machine learning pipeline that trains a model on a CSV file. This tutorial uses the [mljar-supervised](https://github.com/mljar/mljar-supervised) package to perform automated feature engineering, model selection, and hyperparameter tuning, making it easy to train high-quality machine learning models on structured data.


## Before You Start
- You must have {{% productName %}} installed and running on your cluster
- You should have already completed the [Standard ML Pipeline](/{{%release%}}/build-dags/tutorials/basic-ml) tutorial
- You must be familiar with jsonnet

## How to Build an AutoML Pipeline

1. Upload your CSV file to {{% productName %}} by creating a new data repository and committing your data: 

```bash
pachctl create repo csv-data
pachctl put file csv_data@master:housing-simplified.csv -f ../housing-prices-intermediate/data/housing-simplified-1.csv
```

2. Create the AutoML Pipeline:

```bash
pachctl update pipeline --jsonnet ./automl.jsonnet  \
    --arg name="regression" \
    --arg input="csv_data" \
    --arg target_col="MEDV" \
    --arg args="--mode Explain --random_state 42"
```
The model automatically starts training. Once complete, the trained model and evaluation metrics are output to the AutoML output repo.

3. Update the dataset; {{% productName %}} retrains the model automatically.

```bash
pachctl put file csv_data@master:housing-simplified.csv -f ../housing-prices-intermediate/data/housing-simplified-error.csv
```

You can update the dataset as many times as you want. Each time, {{% productName %}} automatically retrains the model and outputs the new model and evaluation metrics to the AutoML output repo. 