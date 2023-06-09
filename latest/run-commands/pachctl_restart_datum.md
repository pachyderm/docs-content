## pachctl restart datum

Restart a stuck datum during a currently running job.

### Synopsis

Restart a stuck datum during a currently running job; does not solve failed datums. Optionally, you can configure a job to skip failed datums via the transform.err_cmd setting of your pipeline spec.

```
pachctl restart datum <pipeline>@<job> <datum-path1>,<datum-path2>,... [flags]
```

### Options

```
  -h, --help             help for datum
      --project string   Project containing the datum job (default "openCV")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

