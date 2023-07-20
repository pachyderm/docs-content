from pachyderm_sdk import Client 
from pachyderm_sdk.config import Context
from pachyderm_sdk.api import pfs


client = Client(host="localhost", port="80")
context = Context

version = client.get_version()


print(version)
print(context.cluster_name)


