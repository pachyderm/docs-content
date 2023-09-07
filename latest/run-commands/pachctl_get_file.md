---
date: 2023-09-07T13:28:03-04:00
title: "pachctl get file"
description: "Learn about the pachctl_get_file command"
---

## pachctl get file

Return the contents of a file.

### Synopsis

This command returns the contents of a file. While using this command, take special note of how you can use ancestry syntax (e.g., appending`^2` or `.-1` to `repo@branch`) to retrieve the contents of a file from a previous commit. 

- To specify the project where the repo is located, use the --project flag 
- To specify the output path, use the --output flag 
- To specify the number of bytes to offset the read by, use the --offset-bytes flag 
- To retry the operation if it fails, use the --retry flag 


```
pachctl get file <repo>@<branch-or-commit>:<path/in/pfs> [flags]
```

### Examples

```
 pachctl get file foo@master:image.png 
 pachctl get file foo@0001a0100b1c10d01111e001fg00h00i:image.png 
 pachctl get file foo@master:/directory -r 
 pachctl get file foo@master:image.png --output /path/to/image.png 
 pachctl get file foo@master:/logs/log.txt--offset-bytes 100 
 pachctl get file foo@master:image.png --retry 
 pachctl get file foo@master:/logs/log.txt --output /path/to/image.png --offset-bytes 100 --retry 
 pachctl get file foo@master^:chart.png 
 pachctl get file foo@master^2:chart.png  
 pachctl get file foo@master.1:chart.png  
 pachctl get file foo@master.-1:chart.png  
 pachctl get file 'foo@master:/test\[\].txt'

```

### Options

```
  -h, --help             help for file
      --offset int       Set the number of bytes in the file to skip ahead when reading.
  -o, --output string    Set the path where data will be downloaded.
      --progress         {true|false} Whether or not to print the progress bars. (default true)
      --project string   Specify the project (by name) where the file's repo is located. (default "video-to-frame-traces")
  -r, --recursive        Download multiple files, or recursively download a directory.
      --retry            {true|false} Whether to append the missing bytes to an existing file. No-op if the file doesn't exist.
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl get](../pachctl_get)	 - Get the raw data represented by a Pachyderm resource.

