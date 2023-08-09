---
date: 2023-08-04T13:05:50-04:00
title: "pachctl create pipeline"
slug: "Learn about the pachctl_create_pipeline command"
---

## pachctl create pipeline

Create a new pipeline.

### Synopsis

This command creates a new pipeline from a pipeline specification. 
 
You can create a pipeline using a JSON/YAML file or a jsonnet template file -- via either a local filepath or URL. Multiple pipelines can be created from one file.For details on the format, see https://docs.pachyderm.com/latest/reference/pipeline_spec/. 
 
	- To create a pipeline from a JSON/YAML file, use the `--file` flag 
	- To create a pipeline from a jsonnet template file, use the `--jsonnet` flag; you can optionally pay multiple arguments separately using `--arg` 
	- To push your local images to docker registry, use the `--push-images` and `--username` flags 
	- To push your local images to custom registry, use the `--push-images`, `--registry`, and `--username` flags 


```
pachctl create pipeline [flags]
```

### Examples

```
	 pachctl create pipeline -file regression.json 
	 pachctl create pipeline -file foo.json --project bar 
	 pachctl create pipeline -file foo.json --push-images --username lbliii 
	 pachctl create pipeline --jsonnet /templates/foo.jsonnet --arg myimage=bar --arg src=image 

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
  -u, --username string   Specify the username to push images as.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

