---
date: 2023-09-07T13:28:03-04:00
title: "pachctl auth login"
description: "Learn about the pachctl_auth_login command"
---

## pachctl auth login

Log in to Pachyderm

### Synopsis

Login to Pachyderm. Any resources that have been restricted to the account you have with your ID provider (e.g. GitHub, Okta) account will subsequently be accessible.

```
pachctl auth login [flags]
```

### Options

```
      --enterprise   Login for the active enterprise context
  -h, --help         help for login
  -t, --id-token     If set, read an ID token on stdin to authenticate the user
  -b, --no-browser   If set, don't try to open a web browser
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl auth](../pachctl_auth)	 - Auth commands manage access to data in a Pachyderm cluster

