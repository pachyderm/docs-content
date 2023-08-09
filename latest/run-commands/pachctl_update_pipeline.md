---
date: 2023-08-04T13:05:50-04:00
title: "pachctl update pipeline"
slug: "Learn about the pachctl_update_pipeline command"
---

## pachctl update pipeline

Update an existing Pachyderm pipeline.

### Synopsis

This command updates a Pachyderm pipeline with a new pipeline specification. For details on the format, see https://docs.pachyderm.com/latest/reference/pipeline-spec/ 
 
	- To update a pipeline from a JSON/YAML file, use the `--file` flag 
	- To update a pipeline from a jsonnet template file, use the `--jsonnet` flag. You can optionally pay multiple arguments separately using `--arg` 
	- To reprocess all data in the pipeline, use the `--reprocess` flag 
	- To push your local images to docker registry, use the `--push-images` and `--username` flags 
	- To push your local images to custom registry, use the `--push-images`, `--registry`, and `--username` flags 


```
pachctl update pipeline [flags]
```

### Examples

```
	 pachctl update pipeline -file regression.json 
	 pachctl update pipeline -file foo.json --project bar 
	 pachctl update pipeline -file foo.json --push-images --username lbliii 
	 pachctl update pipeline --jsonnet /templates/foo.jsonnet --arg myimage=bar --arg src=image 

```

### Options

```
      --arg stringArray   Provide a top-level argument in the form of 'param=value' passed to the Jsonnet template; requires --jsonnet. For multiple args, --arg may be set more than once.
  -f, --file string       Provide a JSON/YAML file (url or filepath) for one or more pipelines. "-" reads from stdin (the default behavior). Exactly one of --file and --jsonnet must be set.
  -h, --help              help for pipeline
      --jsonnet string    Provide a Jsonnet template file (url or filepath) for one or more pipelines. "-" reads from stdin. Exactly one of --file and --jsonnet must be set. Jsonnet templates must contain a top-level function; strings can be passed to this function with --arg (below)
      --project string    Specify the project (by name) in which to create the pipeline. (default "standard-ml-tutorial")
  -p, --push-images       Specify that the local docker images should be pushed into the registry (docker by default).
  -r, --registry string   Specify an alternative registry to push images to. (default "index.docker.io")
      --reprocess         Reprocess all datums that were already processed by previous version of the pipeline.
  -u, --username string   Specify the username to push images as.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

