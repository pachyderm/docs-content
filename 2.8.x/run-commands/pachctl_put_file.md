---
date: 2023-10-18T16:51:53-04:00
title: "pachctl put file"
description: "Learn about the pachctl put file command"
---

## pachctl put file

Put a file into the filesystem.

### Synopsis

This command puts a file into the filesystem.  This command supports a number of ways to insert data into PFS. 

Files, Directories, & URLs: 
 To upload via local filesystem, use the `-f` flag 
 To upload via URL, use the `-f` flag with a URL as the argument 
 To upload via filepaths & urls within a file, use the `i` flag 
 To upload to a specific path in the repo, use the `-f` flag and add the path to the `repo@branch:/path` 
 To upload recursively from a directory, use the `-r` flag 
 To upload tar files and have them automatically untarred, use the `-untar` flag 

Compression, Parallelization, Appends: 
 To compress files before uploading, use the `-c` flag 
 To define the maximum number of files that can be uploaded in parallel, use the `-p` flag 
 To append to an existing file, use the `-a` flag 

Other: 
 To enable progress bars, use the `-P` flag 


```
pachctl put file <repo>@<branch-or-commit>[:<path/to/file>] [flags]
```

### Examples

```
 pachctl put file repo@master-f image.png 
 pachctl put file repo@master:/logs/log-1.txt  
 pachctl put file -r repo@master -f my-directory 
 pachctl put file -r repo@branch:/path -f my-directory 
 pachctl put file repo@branch -f http://host/example.png 
 pachctl put file repo@branch:/dir -f http://host/example.png 
 pachctl put file repo@branch -r -f s3://my_bucket 
 pachctl put file repo@branch -i file 
 pachctl put file repo@branch -i http://host/path 
 pachctl put file repo@branch -f -untar dir.tar 
 pachctl put file repo@branch -f -c image.png 

```

### Options

```
  -a, --append              Specify file contents should be appended to existing content from previous commits or previous calls to 'pachctl put file' within this commit.
      --compress            Specify data should be compressed during upload. This parameter might help you upload your uncompressed data, such as CSV files, to Pachyderm faster. Use 'compress' with caution, because if your data is already compressed, this parameter might slow down the upload speed instead of increasing.
  -f, --file strings        Specify the file to be put; it can be a local file or a URL. (default [-])
      --full-path           Specify entire path provided to -f should be the target filename in PFS; by default only the base of the path is used.
  -h, --help                help for file
  -i, --input-file string   Specify file provided contains a list of files to be put (as paths or URLs).
  -p, --parallelism int     Set the maximum number of files that can be uploaded in parallel. (default 10)
      --progress            Print progress bars. (default true)
      --project string      Specify the project (by name) where the repo for uploading this file is located. (default "video-to-frame-traces")
  -r, --recursive           Specify files should be recursively put into a directory.
      --untar               Specify file(s) with the extension .tar should be untarred and put as a separate file for each file within the tar stream(s); gzipped (.tar.gz or .tgz) tar file(s) are handled as well
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

### SEE ALSO

* [pachctl put](../pachctl_put)	 - Insert data into Pachyderm.

