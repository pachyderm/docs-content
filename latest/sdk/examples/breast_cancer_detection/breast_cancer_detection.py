import dataclasses

from pachyderm_sdk import Client
from pachyderm_sdk.api import pfs, pps


def main(client: Client):
    for f in ['models', 'sample_data']:
        client.pfs.create_repo(repo=pfs.Repo(f))
        client.pfs.put_files(commit=pfs.Commit.from_uri(f'{f}@master'), source=f'{f}/', path='/')
    for s in ['crop', 'extract_centers', 'generate_heatmaps', 'classify']:
        r = pps.CreatePipelineRequest().from_json(open(f'multi-stage/{s}.json').read())
        client.pps.create_pipeline(**{f.name: getattr(r, f.name) for f in dataclasses.fields(r)})



def clean(client: Client):
    client.pps.delete_pipeline(pipeline=pps.Pipeline(name="classify"))
    client.pps.delete_pipeline(pipeline=pps.Pipeline(name="generate_heatmaps"))
    client.pps.delete_pipeline(pipeline=pps.Pipeline(name="extract_centers"))
    client.pps.delete_pipeline(pipeline=pps.Pipeline(name="crop"))
    client.pfs.delete_repo(repo=pfs.Repo.from_uri("sample_data"), force=True)
    client.pfs.delete_repo(repo=pfs.Repo.from_uri("models"), force=True)


if __name__ == "__main__":
    # Connects to a pachyderm cluster using the pachctl config file located
    # at ~/.pachyderm/config.json. For other setups, you'll want one of the 
    # alternatives:
    # 1) To connect to pachyderm when this script is running inside the
    #    cluster, use `Client.new_in_cluster()`.
    # 2) To connect to pachyderm via a pachd address, use
    #    `Client.new_from_pachd_address`.
    # 3) To explicitly set the host and port, pass parameters into
    #    `Client()`.
    # 4) To use a config file located elsewhere, pass in the path to that
    #    config file to Client.from_config()
    client = Client.from_config()
    clean(client)
    main(client)
