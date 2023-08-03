from pachyderm_sdk import Client 
from pachyderm_sdk.config import Context
from pachyderm_sdk.api import pfs
from pachyderm_sdk.api import pps 

client = Client(host="localhost", port="80")
context = Context

version = client.get_version()

print("Pachyderm Version:", version)
print("Pachd Address:", context.pachd_address)

# Creates a project, repo, and branch
project = pfs.Project(name="sdk-basic-pipeline-4")
repo = pfs.Repo(name="housing_data", project=project)
branch = pfs.Branch.from_uri(f"{repo}@main")

try:
    client.pfs.create_project(project=project, description='blah')
    client.pfs.create_repo(repo=repo, description="my first sdk-created repo")
    print("Project and Repo creation successful.")
except Exception as e:
    print("Error creating project or repo:", e)
    exit(1)

# Loads data into the repo as a commit
try:
    with client.pfs.commit(branch=branch) as commit:
        with open("../build-dags/tutorials/basic-ml/housing-simplified-1.csv", "rb") as source:
            commit.put_file_from_file(path="/housing-simplified-1.csv", file=source)
    print("Data loaded into the repo as a commit.")
except Exception as e:
    print("Error loading data into the repo:", e)
    exit(1)

# Creates a pipeline
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

try: 
    result = client.pps.list_pipeline(details=True)
    print("Pipeline list:", result)
except Exception as e:
    print("Error listing the pipelines:", e)
    exit(1)