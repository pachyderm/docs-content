---
# metadata # 
title: Connection
description: Learn how to connect to your organization's publicly exposed cluster.
date: 
# taxonomy #
tags: ["load balancer", "tcp", "pachctl connect", "ip"]
series:
seriesPart:
weight: 5
directory: true
---

If you are exposing your cluster publicly (e.g. via a load balancer), you can connect to it using the `pachctl connect` command. This command will configure your local `pachctl` to connect to your cluster.

1. Open a terminal.
2. Retrieve the external IP address of your load balancer or your domain name.
   ```s
   kubectl get services | grep pachyderm-proxy | awk '{print $4}'
   ```
3. Update the context of your cluster using the IP address.
    ```s
    pachctl connect https://pachyderm.<your-proxy.host-value>
    ```
4. Verify you are using the correct context.
    ```s
    pachctl config get active-context
    ```
5. Verify you can connect to your cluster by printing the PachD version.
    ```s
    pachctl version
    ```