---
# metadata # 
title: JupyterLab Extension
description: Learn how to install and use the JupyterLab Extension.
date: 
# taxonomy #
tags: ["integrations", "jupyterlab", "notebooks"]
series:
seriesPart:
weight: 
beta: true 
---

Use our [JupyterLab extension](https://pypi.org/project/jupyterlab-pachyderm/) ("JupyterLab-{{%productName%}}") to:

- Connect your Notebook to a {{%productName%}} cluster
- Browse, open, and analyze data stored in {{%productName%}} directly from your Notebook
- Run and test out your pipeline code before creating a Docker image

![Mount extension in action](/images/mount-extension.gif)

---

## Try it Out

To try JupyterLab-{{%productName%}} right away, run our [JupyterLab Docker image](./docker-install), which contains JupyterLab and JupyterLab-{{%productName%}} pre-installed. If you have a running {{%productName%}} cluster, you can run the image, connect it to your cluster and explore your {{%productName%}} data in a notebook.

---

## Install the Extension 

If you have your own Jupyter notebook runner (such as JupyterHub or Kubeflow), or you're simply running JupyterLab on your local machine, check out our [JupyterLab-{{%productName%}} walkthrough](./extension-walkthrough) to learn about the components of JupyterLab-{{%productName%}} and how to get the pieces installed, running, and connected.

---

## Examples 

Make sure to check our [data science notebook examples](https://github.com/pachyderm/examples) running on {{%productName%}}, from a market sentiment NLP implementation using a FinBERT model to pipelines training a regression model on the Boston Housing Dataset. You will also find integration examples with open-source products, such as labeling or model serving applications. 

---
