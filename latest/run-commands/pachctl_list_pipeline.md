## pachctl list pipeline

Return info about all pipelines.

### Synopsis

Return info about all pipelines.

```
pachctl list pipeline [<pipeline>] [flags]
```

### Options

```
  -A, --all-projects        Show pipelines form all projects.
  -c, --commit string       List the pipelines as they existed at this commit.
      --full-timestamps     Return absolute timestamps (as opposed to the default, relative timestamps).
  -h, --help                help for pipeline
      --history string      Return revision history for pipelines. (default "none")
  -o, --output string       Output format when --raw is set: "json" or "yaml" (default "json")
      --project string      Project containing pipelines. (default "openCV")
      --raw                 Disable pretty printing; serialize data structures to an encoding such as json or yaml
  -s, --spec                Output 'create pipeline' compatibility specs.
      --state stringArray   Return only pipelines with the specified state. Can be repeated to include multiple states
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

