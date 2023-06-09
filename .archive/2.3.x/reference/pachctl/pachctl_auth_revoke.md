---
# metadata # 
title:  pachctl auth revoke
description: "Revoke a {{%productName%}} auth token."
date:  2022-10-14T09:34:42-04:00
tags:
  - auth
cliGlossary:  a
---

### Synopsis

Revoke a {{%productName%}} auth token.

```
pachctl auth revoke [flags]
```

### Options

```
      --enterprise     Revoke an auth token (or all auth tokens minted for one user) on the enterprise server
  -h, --help           help for revoke
      --token string   {{%productName%}} auth token that should be revoked (one of --token or --user must be set)
      --user string    User whose {{%productName%}} auth tokens should be revoked (one of --token or --user must be set)
```

### Inherited Options

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

