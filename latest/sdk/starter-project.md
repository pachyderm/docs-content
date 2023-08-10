---
title: First Project
description: Learn how to create your first project, including repos and branches, using the SDK.
directory: true 
---

This tutorial is based on the [Standard ML Pipeline Tutorial](/latest/build-dags/tutorials/basic-ml/) found in the [Build Pipelines & DAGs](/latest/build-dags) section of the documentation. The end result is a simple machine learning pipeline that trains a regression model on housing market data to predict the value of homes in Boston.


## 1. Import the dependencies

```python
from pachyderm_sdk import Client 
from pachyderm_sdk import pfs, pps 
```

The imports you'll need for future projects depend on the setup of your instance and the operations you want to perform; see the [API submodules](/sdk/api/) reference documentation for more information. 

## 2. Initiate the Client

```python
client = Client(host="localhost", port="80")
version = client.get_version()

print("Pachyderm Version:", version)
```

See the [Client reference documentation](/sdk/#pachyderm_sdk.Client) for more information on how to configure and initiate the client in other ways, such as from a [PachD Address](/sdk/#pachyderm_sdk.Client.from_pachd_address) and from a [Config File](/sdk/#pachyderm_sdk.Client.from_config).

## 3. Create a Project, Repo, & Branch

```python
project = pfs.Project(name="sdk-standard-pipeline")
repo = pfs.Repo(name="housing_data", project=project)
branch = pfs.Branch.from_uri(f"{repo}@main")

try:
    client.pfs.create_project(project=project, description='standard ml pipeline via sdk')
    client.pfs.create_repo(repo=repo, description="my first sdk-created repo")
    print("Project and Repo creation successful.")
except Exception as e:
    print("Error creating project or repo:", e)
    exit(1)
```

You'll first need to create a class instance for each resource you want to create. In this case, you'll create a [project](/sdk/api/pfs/#pachyderm_sdk.api.pfs.Project), [repo](/sdk/api/pfs/#pachyderm_sdk.api.pfs.Repo), and [branch](/sdk/api/pfs/#pachyderm_sdk.api.pfs.Branch). You'll then use the [create_project](/sdk/api/pfs/#pachyderm_sdk.api.pfs.ApiStub.create_project) and [create_repo](/sdk/api/pfs/#pachyderm_sdk.api.pfs.ApiStub.create_repo) methods to create the resources in your cluster.

## 4. Commit Files 

```python
try:
    with client.pfs.commit(branch=branch) as commit:
        with open("../build-dags/tutorials/basic-ml/housing-simplified-1.csv", "rb") as source:
            commit.put_file_from_file(path="/housing-simplified-1.csv", file=source)
    print("Data loaded into the repo as a commit.")
except Exception as e:
    print("Error loading data into the repo:", e)
    exit(1)
```

You'll use the [commit](/sdk/api/pfs/#pachyderm_sdk.api.pfs.Commit) class to create a commit in your repo. While the commit is open, you can access the [OpenCommit subclass](/sdk/api/pfs/extension.html#pachyderm_sdk.api.pfs.extension.OpenCommit) to perform file operations (put, copy, delete).  In this example, the [put_from_file](/sdk/api/pfs/extension.html#pachyderm_sdk.api.pfs.extension.OpenCommit.put_file_from_file) method is used.

### Alternative Commit Methods

The following are just examples with mock filenames.

#### Commit As Raw Data 

```python
with client.pfs.commit(branch=branch) as commit:
    file = commit.put_file_from_bytes(path=f"/directory-a/filename-a.md", data=b"## raw data here \n this is a **markdown** sentence.")
    file = commit.put_file_from_bytes(path=f"/directory-b/filename-b.md", data=b"## raw data here \n this is a **markdown** sentence.")
```

See the OpenCommit's [put_file_from_bytes](/sdk/api/pfs/extension.html#pachyderm_sdk.api.pfs.extension.OpenCommit.put_file_from_bytes) method for more details.

#### Commit From URL 

```python
with client.pfs.commit(branch=branch) as commit:

    file = commit.put_file_from_url(path="/directory-c/locations.csv", url="https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv")
```
See the OpenCommit's [put_file_from_url](/sdk/api/pfs/extension.html#pachyderm_sdk.api.pfs.extension.OpenCommit.put_file_from_url) method for more details.

## 5. Create a Pipeline

```python
try:
    input = pps.Input(pfs=pps.PfsInput(project=project.name, branch="main", repo=repo.name, glob="/*"))
    transform = pps.Transform(
        image="lbliii/housing-prices:latest", 
        cmd=["python", "regression.py",
            "--input", "/pfs/housing_data/",
            "--target-col", "MEDV",
            "--output", "/pfs/out/"],
        datum_batching=True)

    pipeline = pps.Pipeline(name="pipeline-001", project=project)

    client.pps.create_pipeline(pipeline=pipeline, input=input, transform=transform)
    print("Pipeline created successfully.")
except Exception as e:
    print("Error creating the pipeline:", e)
    exit(1)
```

Up until this point, you have been working with the [`pfs` (Pachyderm File System)](/sdk/api/pfs/) submodule. Now you'll use the [`pps` (Pachyderm Pipeline System)](/sdk/api/pps/) submodule to create a pipeline.

A  basic pipeline requires at least an [input](/sdk/api/pps/#pachyderm_sdk.api.pps.Input), [transform](/sdk/api/pps/#pachyderm_sdk.api.pps.Transform), and [pipeline](/sdk/api/pps/#pachyderm_sdk.api.pps.Pipeline) class instance. Once those classes have been defined, you can finally create the pipeline by using the [create_pipeline](/sdk/api/pps/#pachyderm_sdk.api.pps.ApiStub.create_pipeline) method.

At this point, you can check the Console UI or use the `pachctl list pipelines` command to see the pipeline running. To add this functionality to your script, you can use the [list_pipeline](/sdk/api/pps/#pachyderm_sdk.api.pps.ApiStub.list_pipeline) method.
