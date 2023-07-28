---
title: First Project
description: Learn how to create your first project, including repos and branches, using the SDK.
directory: true 
---

## 1. Import the dependencies.

```python
from pachyderm_sdk import Client 
from pachyderm_sdk.config import Context
from pachyderm_sdk.api import pfs
```

## 2. Initiate the Client.

```python
client = Client(host="localhost", port="80")
```

## 3. Create a Project, Repo, & Branch

```python
project = pfs.Project(name="first-project")
repo = pfs.Repo(name="first-repo", project=project)
branch = pfs.Branch.from_uri(f"{repo}@main")

client.pfs.create_project(project=project, description='my first sdk-created project')
client.pfs.create_repo(repo=repo, description="my first sdk-created repo")
```

## 4. Commit Files 

### As Raw Data 

```python
with client.pfs.commit(branch=branch) as commit:
    file = commit.put_file_from_bytes(path=f"/directory-a/filename-a.md", data=b"## raw data here \n this is a **markdown** sentence.")
    file = commit.put_file_from_bytes(path=f"/directory-b/filename-b.md", data=b"## raw data here \n this is a **markdown** sentence.")
```

### From URL 

```python
with client.pfs.commit(branch=branch) as commit:

    file = commit.put_file_from_url(path="/directory-c/locations.csv", url="https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv")
```

### From File 

```python
with client.pfs.commit(branch=branch) as commit:

    with open("pfs-operations.md", "rb") as source:
        commit.put_file_from_file(path="/docs/pfs-operations.md", file=source)
```