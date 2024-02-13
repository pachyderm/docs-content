---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth revoke"
description: "Learn about the pachctl auth revoke command"
---

## pachctl auth revoke

Revoke a Pachyderm auth token

### Synopsis

This command revokes a Pachyderm auth token.

```
pachctl auth revoke [flags]
```

### Examples

```
 pachctl auth revoke --token <token> pachctl auth revoke --user <user> pachctl auth revoke --enterprise --user <user>
```

### Options

```
      --enterprise     Revoke an auth token (or all auth tokens minted for one user) on the enterprise server.
  -h, --help           help for revoke
      --token string   Pachyderm auth token that should be revoked (one of --token or --user must be set).
      --user string    User whose Pachyderm auth tokens should be revoked (one of --token or --user must be set).
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

