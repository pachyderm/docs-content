---
# metadata # 
title:  Connect to a Cluster
description: Learn how to connect to clusters locally and on the cloud.
date: 
# taxonomy #
tags: ["cli"]
series:
seriesPart:
--- 

After you deploy a {{%productName%}} cluster, you can interact with {{%productName%}} using
the command-line interface `pachctl` in a terminal, connect to the [{{%productName%}} Console](../console), use [Notebooks via {{%productName%}}'s Mount Extension](../../../how-tos/jupyterlab-extension/), or
configure third-party applications to access your cluster programmatically.

Often all you need to do is just continue to use the command-line
interface to create repositories, pipelines, and upload your data.
At other times, you might have multiple {{%productName%}} clusters deployed
and need to switch between them.

You might not need to configure anything specific to start using the
{{%productName%}} CLI right after deployment. However, the {{%productName%}}
console and the S3 gateway require
explicit port-forwarding or direct access through an externally
exposed IP address and port.

This section describes the various options available for you to connect
to your {{%productName%}} cluster.

{{% notice warning %}}
We are now shipping {{%productName%}} with an **optional embedded proxy** 
allowing your cluster to expose one single port externally. This deployment setup is optional.

If you choose to deploy {{%productName%}} with a Proxy, check out our new recommended architecture and [deployment instructions](../deploy-w-proxy/) as they alter the way you connect to a cluster.
{{%/notice %}}

## Connect to a Local Cluster

If you are just exploring {{%productName%}}, use port-forwarding to
access both `pachd` and the {{%productName%}} Console.

By default, {{%productName%}} enables port-forwarding from `pachctl` to `pachd`.
If you do not want to use port-forwarding for `pachctl` operations,
configure a `pachd_address` as described in
[Connect by using a {{%productName%}} context](#connect-by-using-a-pachyderm-context).

To connect to the {{%productName%}} Console, you can either use port-forwarding,
or the IP address of the virtual machine on which your Kubernetes cluster
is running.

The following example shows how to access {{%productName%}} Console
that runs in `minikube`.

* To use port-forwarding, run:

  ```s
  pachctl port-forward
  ```

* To use the IP address of the VM:`

  1. Get the minikube IP address:

     ```s
     minikube ip
     ```

  1. Point your browser to the following address:

     ```s
     <minikube_ip>:30080
     ```

## Connect to a Cluster Deployed on a Cloud Platform

As in a local cluster deployment, a {{%productName%}} cluster
deployed on a cloud platform has implicit port-forwarding enabled.
This means that, if you are connected to the cluster so
that `kubectl` works, `pachctl` can communicate with `pachd`
without any additional configuration.
Other services still need explicit port forwarding.
For example, to access {{%productName%}} console,
you need to run pachctl port-forward.
Since a {{%productName%}} cluster
deployed on a cloud platform is more likely to become
a production deployment, configuring a `pachd_address`
as described in
[Connect by using a {{%productName%}} context](#connect-by-using-a-pachyderm-context)
is the preferred way.

### Connect by using a {{%productName%}} context

You can specify an IP address that you use to connect to the
Console ({{%productName%}} UI) and the S3 gateway by storing that address in the
{{%productName%}} configuration file as the `pachd_address` parameter.

This configuration, recommended in production environments, requires that you deploy an ingress controller
and a reliable security method to protect the traffic between the
{{%productName%}} pods and your client machine. Remember that exposing your
traffic through a public ingress might
create a security issue. Therefore, if you expose your `pachd` endpoint,
you need to make sure that you take steps to protect the endpoint and
traffic against common container security threats. Port-forwarding
might be an alternative which might result in sufficient performance
if you place the data that is consumed by your pipeline in object
store buckets located in the same region.

For more information about {{%productName%}} contexts, see
[Manage Cluster Access](../../manage/cluster-access).

To connect by using a {{%productName%}} context, complete the following
steps:

1. Get the current context:

      ```s
      pachctl config get active-context
      ```

      This command returns the name of the currently active context.
      Use this as the argument to the command below.

      If no IP address is set up for this cluster, you get the following
      output:

      ```s
      pachctl config get context <name>
      {

      }
      ```

1. Set up `pachd_address`:

      ```s
      pachctl config update context <name> --pachd-address <host:port>
      ```

      **Example:**

      ```s
      pachctl config update context local --pachd-address 192.168.1.15:30650
      ```

      **Note:** By default, the `pachd` port is `30650`.

1. Verify that the configuration has been updated:

      ```s
      pachctl config get context local
      ```

      **System Response:**

      ```s
      {
         "pachd_address": "192.168.1.15:30650"
      }
      ```

### Connect by Using Port-Forwarding

The {{%productName%}} port-forwarding is the simplest way to enable cluster access
and test basic {{%productName%}} functionality. {{%productName%}} automatically starts
port-forwarding from `pachctl` to `pachd`. Therefore, the traffic
from the local machine goes to the `pachd` endpoint through the
Kubernetes API. However, to open a persistent tunnel to other ports, including
the {{%productName%}} Console, authentication callbacks, the built-in HTTP
file API, and other, you need to run port-forwarding explicitly.

Also, if you are connecting with port-forward, you are using the `0.0.0.0`.
Therefore, if you are using a proxy, it needs to handle that appropriately.

Although port-forwarding is convenient for testing, for production
environments, this connection might be too slow and unreliable.
The speed of the port-forwarded traffic is limited to `1 MB/s`.
Therefore, if you experience high latency with `put file` and
`get file` operations, or if you anticipate high throughput
in your {{%productName%}} environment, you need to enable ingress access
to your Kubernetes cluster. Each cloud provider has its own
requirements and procedures for enabling ingress controller and
load balancing traffic at the application layer for better performance.

Remember that exposing your traffic through a public ingress might
create a security issue. Therefore, if you expose your `pachd` endpoint,
you need to make sure that you take steps to protect the endpoint and
traffic against common container security threats. Port-forwarding
might be an alternative which might provide satisfactory performance
if you place the data that is consumed by your pipeline in object
store buckets located in the same region.

To enable port-forwarding, run `pachctl port-forward` in a new terminal window.

The command does not stop unless you manually interrupt it.
You can run other `pachctl` commands from another window.
If any of your `pachctl` commands hang, verify if the
`kubectl` port-forwarding has had issues that prevent
`pachctl port-forward` from running properly.
