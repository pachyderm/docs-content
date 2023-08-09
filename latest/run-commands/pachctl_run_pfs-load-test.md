---
date: 2023-08-04T13:05:50-04:00
title: "pachctl run pfs-load-test"
slug: "Learn about the pachctl_run_pfs-load-test command"
---

## pachctl run pfs-load-test

Run a PFS load test.

### Synopsis

This command runs a PFS load test.

```
pachctl run pfs-load-test <spec-file> [flags]
```

### Examples

```

Specification:

-- CommitSpec --

count: int
modifications: [ ModificationSpec ]
fileSources: [ FileSourceSpec ]
validator: ValidatorSpec

-- ModificationSpec --

count: int
putFile: PutFileSpec

-- PutFileSpec --

count: int 
source: string

-- FileSourceSpec --

name: string 
random: RandomFileSourceSpec

-- RandomFileSourceSpec --

directory: RandomDirectorySpec
sizes: [ SizeSpec ]
incrementPath: bool

-- RandomDirectorySpec --

depth: SizeSpec 
run: int

-- SizeSpec --

min: int
max: int
prob: int [0, 100]

-- ValidatorSpec --

frequency: FrequencySpec

-- FrequencySpec --

count: int
prob: int [0, 100]

Example: 

count: 5
modifications:
  - count: 5
    putFile:
      count: 5
      source: "random"
fileSources:
  - name: "random"
    random:
      directory:
        depth: 3
        run: 3
      size:
        - min: 1000
          max: 10000
          prob: 30 
        - min: 10000
          max: 100000
          prob: 30 
        - min: 1000000
          max: 10000000
          prob: 30 
        - min: 10000000
          max: 100000000
          prob: 10 
validator: {}

```

### Options

```
  -b, --branch string     Specify the branch to use for generating the load.
  -h, --help              help for pfs-load-test
      --project string    Specify the project (by name) where the repo is located. (default "standard-ml-tutorial")
  -s, --seed int          Set the seed to use for generating the load.
      --state-id string   Set the ID of the base state to use for the load.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

