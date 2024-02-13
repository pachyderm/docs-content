---
# metadata # 
title: Docker Image + User Code
description: Learn how to build a Docker image that contains your user code and all required dependencies.
date: 
# taxonomy #
tags: ["tutorials"]
series:
seriesPart:
weight: 0
beta: false 
---

In this tutorial, you'll learn how to build a Docker image that contains your user code and all required dependencies. You'll then learn how to reference this Docker image in a [pipeline spec](/{{%release%}}/build-dags/pipeline-spec).


## Before You Start 

- You must have [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- You should be familiar with the {{%productName%}} [pipeline specification](/{{%release%}}/build-dags/pipeline-spec).
- You should be comfortable in a programming language of your choice (Python is most common).

## Tutorial 

Pipelines in {{%productName%}} use Docker images to execute user code. When you specify an image in a pipeline spec, {{%productName%}}  deploys the image to the cluster. During pipeline execution, Pachyderm pulls the image from the registry and creates containers from it to process data in the pipeline.

None of our tutorials require that you build your own Docker images. But eventually, you'll want to build your own Docker images so that you can precisely control how your data is transformed. We recommend that you read through this tutorial for context on how pipelines use Docker images to transform your data, but you don't need to follow along with the steps until you are ready to build your first custom pipeline/DAG. 

To jump into a hands-on tutorial that uses a pre-built Docker image, check out our other tutorials in this section, starting with the [Standard ML Pipeline](/{{%release%}}/build-dags/tutorials/basic-ml) tutorial.

### 1. Create a Working Directory

Create a working directory for your all the files we'll need to create a Docker image with your code.

```bash
mkdir -p ~/{{%productName%}}/tutorials/my-first-image
cd ~/{{%productName%}}/tutorials/my-first-image
```

### 2. Create a Dockerfile

To create a Docker image with your user code, you'll need to first create a Dockerfile. The Dockerfile defines the environment and dependencies needed to run your code using the files located inside of your working directory. The following is an example of a simple working directory with a Dockerfile.

```s
.
├── Dockerfile
├── app.py
└── requirements.txt
```


1. Create a file named `Dockerfile` in your working directory.
2. Add a base image to your Dockerfile. The base image is the starting point for your Docker image. You can use any image that has the dependencies you need to run your code. 
3. Add a `WORKDIR` command to your Dockerfile. The `WORKDIR` command sets the working directory for your Docker image. This is the directory where your code will be run.
4. Add a `COPY` command to your Dockerfile. The `COPY` command copies the contents of your working directory into the Docker image. This is where you'll copy your code and any other files needed to run your code.
5. Add a `RUN` command to your Dockerfile. The `RUN` command executes a command in your Docker image. This is where you'll install any dependencies needed to run your code.
6. Add a `CMD` command to your Dockerfile. The `CMD` command defines the command that will be run when the Docker image is run. This is where you'll define the command to run your actual user code.

**Python Example:**

```dockerfile
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 3. Add Your Code

1. Create a file named `app.py` in your working directory.
2. Write your desired transformation code in the `app.py` file.
3. Create a file named `requirements.txt` in your working directory.
4. List all of the dependencies needed to run your code in the `requirements.txt` file.

### 4. Build the Docker Image

1. Open the terminal and navigate to your working directory.
2. Run the following command.
   ```s
   docker build -t <image-name>:<tag> .
   ```

### 4. Register the Docker Image

In order to make your Docker image available to your {{%productName%}} cluster, you'll need to push it to a Docker registry. In this tutorial, we'll be using Docker Hub.

1. Create a Docker Hub account.
2. Run the following command to log into Docker Hub.
    ```s
    docker login
    ```
3. Run the following commands to tag and push your Docker image to Docker Hub.
    ```s
    docker tag <image-name>:<tag> <docker-hub-username>/<image-name>:<tag>
    docker push <docker-hub-username>/<image-name>:<tag>
    ```
4. Run the following command to verify that your Docker image was pushed to Docker Hub.
    ```s
    docker images
    ```
5. Run the following command to verify that your Docker image is available on Docker Hub.
    ```s
    docker pull <docker-hub-username>/<image-name>:<tag>
    ```

### 5. Use Your Docker Image

Now that you have a Docker image with your code, you can reference it in a [pipeline spec](/{{%release%}}/build-dags/pipeline-spec). The following is an example of a pipeline spec that references a Docker image with user code.

1. Create a file named `my-pipeline.json` in your working directory.
2. Define the pipeline spec using the options found in the [pipeline specification ](/{{%release%}}/build-dags/pipeline-spec) docs.

   ```s
   {
     "pipeline": {
       "name": "my-pipeline"
     },
     "transform": {
       "image": "<dockerhub-username>/<image-name>:<tag>",
       "cmd": ["python", "app.py"],
       "stdin": ["input"],
       "stdout": ["output"]
     },
     "input": {
       "pfs": {
         "repo": "input-repo",
         "glob": "/*"
       }
     }
   }

   ```
3. Create a pipeline using the `my-pipeline.json` file.
   ```s
   pachctl create pipeline -f my-pipeline.json
   ```
4. Inspect your pipeline to verify that it was created successfully.
   ```s
   pachctl inspect pipeline my-pipeline
   ```