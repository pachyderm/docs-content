---
# metadata # 
title: AutoML Pipeline
description: Learn how to build an automated machine learning pipeline.
date: 
# taxonomy #
tags: ["integrations", "automl", "mljar"]
series:
seriesPart:
weight: 2
beta: false 
---

You can use {{% productName %}} to build an automated machine learning pipeline that trains a model on a CSV file.  


## Before You Start
- You must have {{% productName %}} installed and running on your cluster
- You should have already completed the [Standard ML Pipeline](/{{%release%}}/build-dags/tutorials/basic-ml) tutorial
- You must be familiar with jsonnet
- This tutorial assumes your active context is `localhost:80`

## Tutorial
Our Docker image's [user code](/{{%release%}}/learn/glossary/user-code) for this tutorial is built on top of the [python:3.7-slim-buster](https://hub.docker.com/_/python) base image. It also uses the [mljar-supervised](https://github.com/mljar/mljar-supervised) package to perform automated feature engineering, model selection, and hyperparameter tuning, making it easy to train high-quality machine learning models on structured data.

### 1. Create a Project & Input Repo

{{<stack type="wizard">}}
{{% wizardRow id="Tool"%}}
{{% wizardButton option="Pachctl CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}
{{% wizardResults %}}
{{% wizardResult val1="tool/pachctl-cli"%}}

1. Create a project named `automl-tutorial`. 
   ```s
   pachctl create project automl-tutorial
   ```
2. Set the project as current. 
   ```s
   pachctl config update context --project automl-tutorial
   ```
3. Create a new `csv-data` repo.
   ```s
   pachctl create repo csv-data
   ```
4. Upload the [housing-simplified-1.csv](housing-simplified-1.csv) file to the repo.
   ```s
   pachctl put file csv_data@master:housing-simplified.csv -f /path/to/housing-simplified-1.csv
   ```

{{% /wizardResult %}}

{{% wizardResult val1="tool/console"%}}
1. Navigate to Console. 
2. Select **Create Project**.
3. Provide a project **Name** and **Description**.
    - **Name**: `automl-tutorial`
    - **Description**: `My second project tutorial.`
4. Select **Create**.
5. Scroll to the project's row and select **View Project**.
6. Select **Create Your First Repo**.
7. Provide a repo **Name** and **Description**.
    - **Name**: `housing_data`
    - **Description**: `Repo for initial housing data`
8. Select **Create**.

{{% /wizardResult %}}
{{% /wizardResults  %}}
{{</stack>}}



### 2. Create a Jsonnet Pipeline

{{<stack type="wizard">}}
{{% wizardRow id="Tool"%}}
{{% wizardButton option="Pachctl CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}
{{% wizardResults %}}
{{% wizardResult val1="tool/pachctl-cli"%}}

1. Download or save our [automl.jsonnet](automl.jsonnet) template. 
   ```s
   ////
   // Template arguments:
   //
   // name : The name of this pipeline, for disambiguation when 
   //          multiple instances are created.
   // input : the repo from which this pipeline will read the csv file to which
   //       it applies automl.
   // target_col : the column of the csv to be used as the target
   // args : additional parameters to pass to the automl regressor (e.g. "--random_state 42")
   ////
   function(name='regression', input, target_col, args='')
   {
     pipeline: { name: name},
     input: {
       pfs: {
         glob: "/",
         repo: input
       }
     },
     transform: {
       cmd: [ "python","/workdir/automl.py","--input","/pfs/"+input+"/", "--target-col", target_col, "--output","/pfs/out/"]+ std.split(args, ' '),
       image: "jimmywhitaker/automl:dev0.02"
     }
   }
   ```
2. Create the AutoML pipeline by referencing and filling out the template's arguments:

   ```bash
   pachctl update pipeline --jsonnet /path/to/automl.jsonnet  \
       --arg name="regression" \
       --arg input="csv_data" \
       --arg target_col="MEDV" \
       --arg args="--mode Explain --random_state 42"
   ```

{{% /wizardResult %}}

{{% wizardResult val1="tool/console"%}}

This part must be done through the CLI due to the pipeline's use of Jsonnet.

{{% /wizardResult %}}
{{% /wizardResults  %}}
{{</stack>}}


The model automatically starts training. Once complete, the trained model and evaluation metrics are output to the AutoML output repo.

### 3. Upload the Dataset

{{<stack type="wizard">}}
{{% wizardRow id="Tool"%}}
{{% wizardButton option="Pachctl CLI" state="active" %}}
{{% wizardButton option="Console" %}}
{{% /wizardRow %}}
{{% wizardResults %}}
{{% wizardResult val1="tool/pachctl-cli"%}}

Update the dataset using [housing-simplified-2.csv](housing-simplified-2.csv); {{% productName %}} retrains the model automatically.

```bash
pachctl put file csv_data@master:housing-simplified.csv -f /path/to/housing-simplified-2.csv
```
{{% /wizardResult %}}

{{% wizardResult val1="tool/console"%}}

1. Download the data set, [housing-simplified-2.csv](housing-simplified-2.csv). 
2. Select the **regression** repo > **Upload Files**.
3. Select **Browse Files**.
4. Choose the `housing-simplified-1.csv` file.
5. Select **Upload**.
{{% /wizardResult %}}
{{% /wizardResults  %}}
{{</stack>}}

Repeat the previous step as many times as you want. Each time, {{% productName %}} automatically retrains the model and outputs the new model and evaluation metrics to the AutoML output repo. 


---

## User Code Assets 

The [Docker image](/{{%release%}}/build-dags/tutorials/user-code) used in this tutorial was built with the following assets:

{{< stack type="wizard" >}}

{{% wizardRow id ="assets" %}}
{{% wizardButton option="Dockerfile" state="active" %}}
{{% wizardButton option="Automl.py" %}}
{{% wizardButton option="Requirements.txt" %}}
{{% /wizardRow %}}

{{% wizardResults  %}}
{{% wizardResult val1="assets/dockerfile"%}}
```s
FROM python:3.7-slim-buster
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3-pip python3-dev
RUN pip3 -q install pip --upgrade

WORKDIR /workdir/

COPY requirements.txt /workdir/
RUN pip3 install -r requirements.txt

COPY *.py /workdir/
```
{{% /wizardResult %}}

{{% wizardResult val1="assets/automl.py"%}}
```s
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from supervised.automl import AutoML

import argparse
import os

parser = argparse.ArgumentParser(description="Structured data regression")
parser.add_argument("--input",
                    type=str,
                    help="csv file with all examples")
parser.add_argument("--target-col",
                    type=str,
                    help="column with target values")
parser.add_argument("--mode",
                    type=str,
                    default='Explain',
                    help="mode")
parser.add_argument("--random_state",
                    type=int,
                    default=42,
                    help="random seed")
parser.add_argument("--output",
                    metavar="DIR",
                    default='./output',
                    help="output directory")

def load_data(input_csv, target_col):
    # Load the data
    data = pd.read_csv(input_csv, header=0)
    targets = data[target_col]
    features = data.drop(target_col, axis = 1)
    
    # Create data splits
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        targets,
        test_size=0.25,
        random_state=123,
    )
    return X_train, X_test, y_train, y_test


def main():
    args = parser.parse_args()
    if os.path.isfile(args.input):
        input_files = [args.input]
    else:  # Directory
        for dirpath, dirs, files in os.walk(args.input):  
            input_files = [ os.path.join(dirpath, filename) for filename in files if filename.endswith('.csv') ]
    print("Datasets: {}".format(input_files))
    os.makedirs(args.output, exist_ok=True)

    for filename in input_files:

        experiment_name = os.path.basename(os.path.splitext(filename)[0])
        # Data loading and Exploration
        X_train, X_test, y_train, y_test = load_data(filename, args.target_col)
       
        # Fit model
        automl = AutoML(total_time_limit=60*60, results_path=args.output) # 1 hour
        automl.fit(X_train, y_train)
        
        # compute the MSE on test data
        predictions = automl.predict_all(X_test)
        print("Test MSE:", mean_squared_error(y_test, predictions))


if __name__ == "__main__":
    main()
```
{{% /wizardResult %}}
{{% wizardResult val1="assets/requirements.txt"%}}
```s
 mljar-supervised
```
{{% /wizardResult %}} 
{{% /wizardResults %}}

{{< /stack>}}
