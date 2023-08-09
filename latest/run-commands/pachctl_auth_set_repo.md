---
date: 2023-08-04T13:05:50-04:00
title: "pachctl auth set repo"
---

## pachctl auth set repo

Set the roles that 'subject' has on 'repo'

### Synopsis

Set the roles that 'subject' has on 'repo'

```
pachctl auth set repo <repo> [role1,role2 | none ] <subject> [flags]
```

### Options

```
  -h, --help             help for repo
      --project string   The project containing the repo. (default "standard-ml-tutorial")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```