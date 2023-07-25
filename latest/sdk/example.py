from pachyderm_sdk import Client 
from pachyderm_sdk.config import Context
from pachyderm_sdk.api import pfs
from pachyderm_sdk.api import pps 


client = Client(host="localhost", port="80")
context = Context

version = client.get_version()


print(version)
print(context.cluster_name)


# Creates a pachyderm repo called `test`
project = pfs.Project(name="second-project")
repo = pfs.Repo(name="wowow", project=project)
branch = pfs.Branch.from_uri(f"{repo}@main")


# client.pfs.create_project(project=project, description='blah')
# client.pfs.create_repo(repo=repo, description="my first sdk-created repo")

# with client.pfs.commit(branch=branch) as commit:

#     with open("pfs-operations.md", "rb") as source:
#         commit.put_file_from_file(path="/docs/pfs-operations.md", file=source)

    # file = commit.put_file_from_bytes(path=f"/directory-a/filename.md", data=b"## raw data here \n this is a **markdown** sentence.")
    # file = commit.put_file_from_bytes(path=f"/directory-a/filename-b.md", data=b"## raw data two \n this is a **markdown** sentence.")

    # file = commit.put_file_from_url(path="/directory-b/locations.csv", url="https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv")


def transform_my_data(stuff):
    print(stuff)

pipeline = pps.Pipeline(name="pipeline-001", project=project)

client.pps.create_pipeline(pipeline=pipeline, input=repo, transform=transform_my_data(repo))