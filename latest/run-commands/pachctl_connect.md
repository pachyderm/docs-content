---
date: 2024-02-13T16:12:03-05:00
title: "pachctl connect"
description: "Learn about the pachctl connect command"
---

## pachctl connect

Connect to a Pachyderm Cluster

### Synopsis

This command creates a Pachyderm context at the given address and sets it as active. It stores the pachd address, cluster deployment ID, and actively set project name. 

If the actively set project no longer exists due to deletion or hard restart / reinstall, you may get an error that can be resolved by setting an existing project (e.g., `default`) to the context. 
 To list all contexts, use `pachctl config list contexts`. 
 To view details, use `pachctl config get context <context>`. 
 To clean up your contexts, use `pachctl config delete context <context>`. 
 To set a different context as active, use `pachctl config set active-context <context>`. 
 To set a different project as active, use `pachctl config update context --project foo`.

```
pachctl connect <address> [flags]
```

### Examples

```
 pachctl connect localhost:80 pachctl connect localhost:80 --alias my-private-cluster
```

### Options

```
      --alias string   Set an alias for the context that is created.
  -h, --help           help for connect
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl](../pachctl)	 - 

