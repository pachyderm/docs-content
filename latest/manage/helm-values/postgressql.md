---
# metadata # 
title:  PostgreSQL Subchart HCVs
description: Use the bundled version of PostgreSQL (metadata storage) for testing on your personal machine.
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 10
label: Not For Production
--- 
## About

The PostgresQL section controls the Bitnami PostgreSQL subchart. {{% productName %}} runs on Kubernetes, is backed by an object store of your choice, and comes with a bundled version of PostgreSQL (metadata storage) by default.

**We recommended disabling this bundled PostgreSQL** and using a managed database instance (such as RDS, CloudSQL, or PostgreSQL Server) for production environments. 

See storage class details for your provider:

- [AWS](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html) | Min: 500Gi (GP2) / 1,500 IOP
- [GCP](https://cloud.google.com/compute/docs/disks/performance#disk_types) | Min: 50Gi / 1,500 IOPS
- [Azure](https://docs.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes) | Min: 256Gi / 1,100 IOPS

## Values 

```yaml
postgresql:
  # enabled controls whether to install postgres or not.
  # If not using the built in Postgres, you must specify a Postgresql
  # database server to connect to in global.postgresql
  # The enabled value is watched by the 'condition' set on the Postgresql
  # dependency in Chart.yaml
  enabled: true
  image:
    repository: pachyderm/postgresql
    tag: "13.3.0"
  # DEPRECATED from pachyderm 2.1.5
  initdbScripts:
    dex.sh: |
      #!/bin/bash
      set -e
      psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        CREATE DATABASE dex;
        GRANT ALL PRIVILEGES ON DATABASE dex TO "$POSTGRES_USER";
      EOSQL
  fullnameOverride: postgres
  persistence:
    # Specify the storage class for the postgresql Persistent Volume (PV)
    # See notes in Bitnami chart values.yaml file for more information.
    # More info for setting up storage classes on various cloud providers:
    # AWS: https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html
    # GCP: https://cloud.google.com/compute/docs/disks/performance#disk_types
    # Azure: https://docs.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes
    storageClass: ""
    # storageSize specifies the size of the volume to use for postgresql
    # Recommended Minimum Disk size for Microsoft/Azure: 256Gi  - 1,100 IOPS https://azure.microsoft.com/en-us/pricing/details/managed-disks/
    # Recommended Minimum Disk size for Google/GCP: 50Gi        - 1,500 IOPS https://cloud.google.com/compute/docs/disks/performance
    # Recommended Minimum Disk size for Amazon/AWS: 500Gi (GP2) - 1,500 IOPS https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html
    size: 10Gi
    labels:
      suite: pachyderm
  primary:
    priorityClassName: ""
    nodeSelector: {}
    tolerations: []
  readReplicas:
    priorityClassName: ""
    nodeSelector: {}
    tolerations: []
```

