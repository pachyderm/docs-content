from pachyderm_sdk import Client 
from pachyderm_sdk.api import pfs


client = Client.from_config()

version = client.get_version()
print(version)

repo = pfs.Repo(name="kida-milo")
client.pfs.create_repo(repo=repo)

