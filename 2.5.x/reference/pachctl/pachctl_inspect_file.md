## pachctl inspect file

Return info about a file.

### Synopsis

Return info about a file.

```
pachctl inspect file <repo>@<branch-or-commit>:<path/in/pfs> [flags]
```

### Options

```
  -h, --help             help for file
  -o, --output string    Output format when --raw is set: "json" or "yaml" (default "json")
      --project string   Project in which repo is located. (default "joins")
      --raw              Disable pretty printing; serialize data structures to an encoding such as json or yaml
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

