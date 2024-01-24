---
title: Client Initialization (Start Here)
description: Learn how to install the Pachyderm SDK, import a client, and initialize it with your configuration settings.
directory: true 
weight: 01
---

The [Pachyderm SDK](https://pypi.org/project/pachyderm-sdk/) enables you to interact with {{%productName%}}'s API, client, and configuration directly in a powerful way.

## 1. Installation

Before using the Pachyderm SDK, make sure you have it installed. You can install the SDK using pip:

```python
pip install pachyderm_sdk
```

## 2. Import the Client

To use the Client class, you need to import it from the Pachyderm SDK:

```python
from pachyderm_sdk import Client
```

## 3. Creating a Client Instance
To interact with a Pachyderm cluster, you need to create an instance of the `Client` class. The `Client` class provides multiple ways to create a client instance based on your requirements.

### Default Settings

```python
client = Client()
```

This creates a client that connects to the local Pachyderm cluster running on `localhost:30650` with default authentication settings.


### Custom Settings

You can customize the client settings by providing the relevant parameters to the Client constructor. Here's an example:


```python
client = Client(
    host='localhost',
    port=8080,
    auth_token='your-auth-token',
    root_certs=None,
    transaction_id=None,
    tls=False
)
```

In the above example, the client is configured to connect to the local Pachyderm cluster running on localhost:8080 without TLS encryption. 

- The `auth_token` parameter allows you to specify an authentication token for accessing the cluster. 
- The `root_certs` parameter can be used to provide custom root certificates for secure connections. 
- The `transaction_id` parameter allows you to specify a transaction ID to run operations on.

{{% notice tip %}}
By default, the client will attempt to read the authentication token from the AUTH_TOKEN_ENV environment variable. You can also set the authentication token after creating the client using the auth_token property:
{{% /notice %}}

## 4. Connect

The Client class provides different methods to connect to a Pachyderm cluster based on your deployment configuration.

### From Within a Cluster
If you're running the code within a Pachyderm cluster, you can use the `new_in_cluster` method to create a client instance that operates within the cluster. This method reads the cluster configuration from the environment and creates a client based on the available configuration.

```python
client = Client.new_in_cluster(auth_token='your-auth-token', transaction_id='your-transaction-id')
```

### Via PachD Address

If you have the Pachd address (host:port) of the {{%productName%}} cluster, you can create a client instance using the `from_pachd_address` method:

```python
client = Client.from_pachd_address('pachd-address', auth_token='your-auth-token', root_certs='your-root-certs', transaction_id='your-transaction-id')
```

### Referencing a Config File

If you have a {{%productName%}} configuration file, you can create a client instance using the from_config method:

```python
client = Client.from_config('path-to-config-file')
```
--- 

## Test Connection

If you'd like to quickly test out working with the Pachyderm SDK on your local machine (e.g., using a locally deployed Docker Desktop instance), try out the following:

```python
from pachyderm_sdk import Client 

client = Client(host="localhost", port="80")
version = client.get_version()
print(version)
```

**Example Output**

```s
Version(major=2, minor=6, micro=4, git_commit='358bd1229130eb262c22caf82ed87b3cc91ec81c', git_tree_modified='false', build_date='2023-06-22T14:49:32Z', go_version='go1.20.5', platform='arm64')
```

If you see this, you are ready to start working with the SDK.