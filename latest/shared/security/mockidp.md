---
title: Mockidp Security Warning
---

{{% notice warning %}}
Setting up [Authentication](/{{%release%}}/set-up/connectors)? 

**Do not use [mockIDP](/{{%release%}}/set-up/connectors/mockidp) for clusters that will be deployed into production.**  If you do upgrade a cluster with mockIDP enabled, you must revoke the default mockIDP admin user by running the following command:

```s
pachctl auth revoke --user kilgore@kilgore.trout
```
{{% /notice %}}