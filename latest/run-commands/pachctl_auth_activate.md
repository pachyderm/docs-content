---
date: 2024-02-13T16:12:03-05:00
title: "pachctl auth activate"
description: "Learn about the pachctl auth activate command"
---

## pachctl auth activate

Activate Pachyderm's auth system

### Synopsis

This command manually activates Pachyderm's auth system and restricts access to existing data to the root user. 

This method of activation is not recommended for production. Instead, configure OIDC from Helm values file; auth will be activated automatically when an enterprise key/secret is provided.

```
pachctl auth activate [flags]
```

### Examples

```
 pachctl auth activate pachctl auth activate --supply-root-token pachctl auth activate --enterprise pachctl auth activate --issuer http://pachd:1658/ --redirect http://localhost:30657/authorization-code/callback --client-id pachd
```

### Options

```
      --client-id string        Set the client ID for this pachd. (default "pachd")
      --enterprise              Activate auth on the active enterprise context.
  -h, --help                    help for activate
      --issuer string           Set the issuer for the OIDC service. (default "http://pachd:1658/")
      --only-activate           Activate auth without configuring the OIDC service.
      --redirect string         Set the redirect URL for the OIDC service. (default "http://localhost:30657/authorization-code/callback")
      --scopes strings          Provide a comma-separated list of scopes to request. (default [email,profile,groups,openid])
      --supply-root-token       Prompt the user to input a root token on stdin, rather than generating a random one.
      --trusted-peers strings   Provide a comma-separated list of OIDC client IDs to trust.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

