---
# metadata # 
title: Authentication
description: Learn how to activate Authentication.
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 4
directory: true
---

{{%productName%}} has an embedded Open ID Connect based on Dex, allowing for vendor-neutral authentication using your existing credentials from various back-ends. [Refer to our compatible connectors.](/{{%release%}}/set-up/connectors/)
## Before You Start 

- You must be using [Enterprise](/{{%release%}}/set-up/enterprise) to set up authentication and [authorization]({{%release%}}/set-up/authorization). 

## Activate User Access Management

1. Activate authentication using the following command:

```s
pachctl auth activate 

# {{% productName %}} root token:
# 54778a770c554d0fb84563033c9cb808
```
2. Save the root token value in a secure place.

You can use this token in the future to log in to the initial root admin user by entering the following comand: 

```s
pachctl auth use-auth-token

# Please paste your {{% productName %}} auth token:
```

As a *Root User* (or initial admin), 
you can now configure {{% productName %}} to work with
the identity management provider (IdP) of your choice.

## License Expiration 
When an Enterprise License expires, a
{{% productName %}} cluster with enabled User Access Management goes into an
`admin-only` state. In this state, only `ClusterAdmins` have
access to the data stored in {{% productName %}}. This safety measure keeps sensitive data protected, even when an enterprise subscription becomes stale. To return the cluster to its previous state, run `pachctl license activate` and submit your new code.

