---
# metadata # 
title: Weights and Biases
description: Learn how to use the Weights and Biases connector to track your data science experiments.
date: 
# taxonomy #
tags: ["integrations", "weights-and-biases"]
series:
seriesPart:
weight: 
beta: false 
---

Connect {{% productName %}} to [Weights and Biases](https://wandb.ai/) to track your data science experiments. Using {{% productName %}} as our execution platform, we can version our executions, code, data, and models while still tracking everything in W&B. 

![](/images/weights-and-biases/wandb_screenshot.png)


Here we'll use Pachyderm to manage our data and train our model. 

![](/images/weights-and-biases/pachyderm_mnist_screenshot.png)

## Before You Start

* You must have a [W&B account](https://wandb.ai/authorize)
* You must have a {{% productName %}} cluster
* Download the [example code](Example.zip) and unzip it. (or download this repo. `gh repo clone pachyderm/docs-content` and navigate to `docs-content/docs/latest/integrate/weights-and-biases`)



## How to Use the Weights and Biases Connector

1. Create a {{% productName %}} cluster.
2. Create a [W&B Account](https://wandb.ai/) 
3. Copy your [W&B API Key](https://wandb.ai/authorize) into the `secrets.json` file. We'll use this file to make a [{{% productName %}} secret](/{{%release%}}/manage/secrets/). This keeps our access keys from being built into our container or put in plaintext somewhere.
4. Create the secret with `pachctl create secret -f secrets.json`
5. Run `make all` to create a data repository and the pipeline. 


{{% notice tip %}}
Downloading the data locally and then pushing it to a remote cluster seems like an extra step, especially when dealing with a standard dataset like MNIST. However, if we think about a real-world use case where multiple teams may be manipulating the data (removing examples, adding classes, etc.) then having a history for each of these models can be very useful. In most production settings with supervised learning, the [labeling environment can be directly connected to the data repository](https://towardsdatascience.com/versioning-and-labeling-better-together-2dd7d4fe8bd9), automating this step.

{{% /notice %}}

## About the MNIST example

- Creates a project in W&B with the name of the {{% productName %}} pipeline. 
- Trains an MNIST classifier in a {{% productName %}} Job.
- Logs training info from training to W&B.
- If the Data or {{% productName %}} Pipeline changes, it kicks off a new training process.
