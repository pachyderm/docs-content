---
date: 2023-08-04T13:05:50-04:00
title: "pachctl auth"
slug: "Learn about the pachctl_auth command"
---

## pachctl auth

Auth commands manage access to data in a Pachyderm cluster

### Synopsis

Auth commands manage access to data in a Pachyderm cluster

### Options

```
  -h, --help   help for auth
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl](/commands/pachctl/)	 - 
* [pachctl auth activate](/commands/pachctl_auth_activate/)	 - Activate Pachyderm's auth system
* [pachctl auth check](/commands/pachctl_auth_check/)	 - Check whether a subject has a permission on a resource
* [pachctl auth deactivate](/commands/pachctl_auth_deactivate/)	 - Delete all ACLs, tokens, admins, IDP integrations and OIDC clients, and deactivate Pachyderm auth
* [pachctl auth get](/commands/pachctl_auth_get/)	 - Get the role bindings for a resource
* [pachctl auth get-config](/commands/pachctl_auth_get-config/)	 - Retrieve Pachyderm's current auth configuration
* [pachctl auth get-groups](/commands/pachctl_auth_get-groups/)	 - Get the list of groups a user belongs to
* [pachctl auth get-robot-token](/commands/pachctl_auth_get-robot-token/)	 - Get an auth token for a robot user with the specified name.
* [pachctl auth login](/commands/pachctl_auth_login/)	 - Log in to Pachyderm
* [pachctl auth logout](/commands/pachctl_auth_logout/)	 - Log out of Pachyderm by deleting your local credential
* [pachctl auth revoke](/commands/pachctl_auth_revoke/)	 - Revoke a Pachyderm auth token
* [pachctl auth roles-for-permission](/commands/pachctl_auth_roles-for-permission/)	 - List roles that grant the given permission
* [pachctl auth rotate-root-token](/commands/pachctl_auth_rotate-root-token/)	 - Rotate the root user's auth token
* [pachctl auth set](/commands/pachctl_auth_set/)	 - Set the role bindings for a resource
* [pachctl auth set-config](/commands/pachctl_auth_set-config/)	 - Set Pachyderm's current auth configuration
* [pachctl auth use-auth-token](/commands/pachctl_auth_use-auth-token/)	 - Read a Pachyderm auth token from stdin, and write it to the current user's Pachyderm config file
* [pachctl auth whoami](/commands/pachctl_auth_whoami/)	 - Print your Pachyderm identity

