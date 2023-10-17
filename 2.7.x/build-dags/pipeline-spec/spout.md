---
# metadata # 
title:  Spout PPS
description: Ingest streaming data using a spout pipeline.
date: 
# taxonomy #
tags: ["pipelines", "pps"]
series: ["pps"]
seriesPart:
label: optional
weight: 1
---
## Spec 
This is a top-level attribute of the pipeline spec. 

```s
{
  "pipeline": {...},
  "transform": {...},
  "spout": {
  \\ Optionally, you can combine a spout with a service:
  "service": {
    "internal_port": int,
    "external_port": int
    }
  },
  ...
}

```

## Attributes 

|Attribute| Description|
|-|-|
|`service`|An optional field that is used to specify how to expose the spout as a Kubernetes service.|
|internal_port| Used for the spout's container.|
|external_port| Used for the Kubernetes service that exposes the spout.|

## Behavior 

- Does not have a PFS input; instead, it consumes data from an outside source.
- Can have a service added to it. See [Service](/{{%release%}}/build-dags/pipeline-spec/service).
- Its code runs continuously, waiting for new events.
- The output repo, `pfs/out` is not directly accessible. To write into the output repo, you must to use the put file API call via any of the following:
  - `pachctl put file`
  - A {{% productName%}} SDK (for golang or Python )
  - Your own API client.
- {{% productName %}} CLI (PachCTL) is packaged in the base image of your spout as well as your authentication information. As a result, the authentication is seamless when using PachCTL.


## Diagram 

![spout-tldr](/images/spout_tldr.png)
## When to Use 

You should use the `spout` field in a {{% productName %}} Pipeline Spec when you want to read data from an external source that is not stored in a {{% productName %}} repository. This can be useful in situations where you need to read data from a service that is not integrated with {{% productName %}}, such as an external API or a message queue.

Example scenarios:

- **Data ingestion**: If you have an external data source, such as a web service, that you want to read data from and process with {{% productName %}}, you can use the spout field to read the data into {{% productName %}}.

- **Real-time data processing**: If you need to process data in real-time and want to continuously read data from an external source, you can use the spout field to read the data into {{% productName %}} and process it as it arrives.

- **Data integration**: If you have data stored in an external system, such as a message queue or a streaming service, and you want to integrate it with data stored in {{% productName %}}, you can use the spout field to read the data from the external system and process it in {{% productName %}}.

## Example 


```s
{
  "pipeline": {
    "name": "my-spout"
  },
    "spout": {
  },
  "transform": {
    "cmd": [ "go", "run", "./main.go" ],
    "image": "myaccount/myimage:0.1",
    "env": {
        "HOST": "kafkahost",
        "TOPIC": "mytopic",
        "PORT": "9092"
    }
  }
}
```

{{% notice tip %}}
For a first overview of how spouts work, see our [spout101 example](https://github.com/pachyderm/pachyderm/tree/{{% majorMinorVersion %}}/examples/spouts/spout101).
{{% /notice %}}