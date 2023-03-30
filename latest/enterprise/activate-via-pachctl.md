---
# metadata # 
title: Activate Enterprise via Pachctl
description: Learn how to deploy the Enterprise edition of {{%productName%}} using the pachctl CLI for an existing cluster.
date: 
# taxonomy #
tags: ["enterprise"]
series:
seriesPart:
directory: true 
---

## Before You Start 

- You must have a {{%productName%}} [Enterprise License Key](https://www.pachyderm.com/trial/).
- You must have pachctl and {{%productName%}} installed. 
- You must have the {{%productName%}} Helm repo downloaded.

## How to Activate Enterprise {{%productName%}} via Pachctl 

1. Open your terminal.
2. Input the following command:

```s
echo <your-activation-token> | pachctl license activate
```

3. Verify the status of the enterprise activation:

```s
pachctl enterprise get-state

# ACTIVE
```

You have unlocked {{%productName%}}'s enterprise features.
