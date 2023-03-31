---
# metadata # 
title: Features Overview
description: Learn about the main features unique to the Enterprise edition.
date: 
# taxonomy #
tags: ["enterprise"]
series:
seriesPart:
---

{{% notice note %}}
To get more information about {{%productName%}} Enterprise Edition, to ask questions, or to get access for evaluation, don't hesitate to get in touch with us at [sales@pachyderm.io](mailto:sales@pachyderm.io) or on our [Slack](https://www.pachyderm.com/slack/). 
{{% /notice %}}


## Enterprise Features List

{{%productName%}} Enterprise Edition helps you scale and manage {{%productName%}} data pipelines in an enterprise setting.

It delivers the most recent version of the Community Edition of {{%productName%}} along with additional features(#additioanl-features).

{{% notice warning %}} 
THE ENTERPRISE EDITION LIFTS **ALL SCALING LIMITATIONS**

Note that the activation of the Enterprise Edition [**lifts all scaling limits of the Community Edition**](../../reference/scaling-limits/). You can run as many pipelines as you need and parallelize your jobs without constraints.
{{% /notice %}}


### Additional Features

{{%productName%}} Enterprise unlocks a series of additional administrative and security features needed for enterprise-scale deployments of {{%productName%}}, namely:

- [**Authentication**](../auth/authentication/idp-dex): {{%productName%}} allows for authentication **against any OIDC provider**. Users can authenticate to {{%productName%}} by logging into their favorite Identity Provider. 
- [**Role-Based Access Control - RBAC**](../auth/authorization/): Enterprise-scale deployments require access control.  {{%productName%}} Enterprise Edition gives teams the ability to control access to production pipelines and data.  Administrators can silo data, prevent unintended modifications to production pipelines, and support multiple data scientists or even multiple data science groups by controlling users' access to {{%productName%}} resources.
- [**Enterprise Server**](../auth/enterprise-server/setup/): An organization can have **many {{%productName%}} clusters registered with one single Enterprise Server** that manages the ßEnterprise licensing and the integration with a company's Identity Provider.
- Additionally, you have access to a pachctl command that [pauses (`pachctl enterprise pause`) and unpauses (`pachctl enterprise unpause`) your cluster](../../deploy-manage/manage/backup-restore) for a backup and restore.

### Tooling

{{%productName%}} CE comes with an indispensable complementary tool 
when designing and debugging pipelines: **{{%productName%}} Console**; 
a full Web UI for visualizing pipelines and exploring data. 

While Console is now part of {{%productName%}} Community Edition, 
enabling Enterprise allows you to benefit 
from the full Authentication and Role-Based Access Control capabilities 
by restricting the access to specific resources to authorized users only. 
Unauthorized users will not be able to visualize the content 
of given clusters, repos, and pipelines.







