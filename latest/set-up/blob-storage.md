---
# metadata # 
title: Blob/Object Storage
description: Learn how to set up blob/object storage for your cluster.
date: 
# taxonomy #
tags: ["configuration", "storage", "blob storage", "object storage", "gocdk"]
series:
seriesPart:
directory: true 
weight: 
--- 

You can enable blog/object storage for {{%productName%}} by updating the `pachd.storage` section in your Helm chart. The necessary configuration options depend on your chosen blob storage provider.


## Before You Start 

- You should be familiar with the storageURL options in [goCDK](https://gocloud.dev/howto/blob/) related to your blob storage provider.
  - [AWS S3](https://pkg.go.dev/gocloud.dev/blob/s3blob#URLOpener)
  - [Azure Blob](https://pkg.go.dev/gocloud.dev/blob/azureblob#URLOpener)
  - [GCS Blob](https://pkg.go.dev/gocloud.dev/blob/gcsblob#URLOpener)
- You should have the necessary credentials and permissions to create a bucket or container in your blob storage provider.



## How to Set Up Blob Storage 

1. Navigate to your `values.yaml` file or obtain your current Helm `values.yaml` overrides:
   ```s
   helm get values pachyderm  > values.yaml
   ```
2. Add the following `pachd.storage` fields to your `values.yaml` file:
   ```yaml
   pachd:
     storage:
       gocdkEnabled: true 
       storageURL: "s3://my-bucket" or "gs://my-bucket" or "azure://my-container"
    ```

3. Update the storageURL to include provider-specific configuration options as needed; for options, see the related goCDK packages.
  - [AWS S3](https://pkg.go.dev/gocloud.dev/blob/s3blob#URLOpener)
  - [Azure Blob](https://pkg.go.dev/gocloud.dev/blob/azureblob#URLOpener)
  - [GCS Blob](https://pkg.go.dev/gocloud.dev/blob/gcsblob#URLOpener) 
   
4. Save your changes and upgrade your cluster:
   ```s
   helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
   ```

## Limitations

Some configuration settings such as verifySSL may not be passable via the storageURL as query parameters. In such cases, you can use the `pachd.storage` section to set these options.




