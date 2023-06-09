---
# metadata # 
title: File
description: Learn about the concept of a file. 
glossaryDefinition: A Unix filesystem object (directory or file) that stores data.
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series:
seriesPart:
--- 

A file is a Unix filesystem object, which is a directory or
file, that stores data. Unlike source code
version-control systems that are most suitable for storing plain text
files, you can store any type of file in {{%productName%}}, including
binary files. Often, data scientists operate with
comma-separated values (CSV), JavaScript Object Notation (JSON),
images, and other plain text and binary file
formats. {{%productName%}} supports all file sizes and formats and applies
storage optimization techniques, such as deduplication, in the
background.

To upload your files to a {{%productName%}} repository, run the
`pachctl put file` command. By using the `pachctl put file`
command, you can put both files and directories into a {{%productName%}} repository.

{{% notice warning %}}
- It is important to note that **directories are implied from the paths of the files**. Directories are not stored and will not exist **unless they contain files**. 
- Do not use [regex metacharacters](https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp) in a path or a file name.
{{% /notice %}}

## File Processing Strategies

{{%productName%}} provides the following file processing strategies:

### **Overwriting Files**
By default, when you put a file into a {{%productName%}} repository and a
file by the same name already exists in the repo, {{%productName%}} overwrites
the existing file with the new data.
For example, you have an `A.csv` file in a repository. If you upload the
same file to that repository, {{%productName%}} *overwrites* the existing
file with the data, which results in the `A.csv` file having only data
from the most recent upload.

####  Example

1. View the list of files:

     ```s
     pachctl list file images@master
     ```

     **System Response:**

     ```s
     NAME   TYPE SIZE
     /A.csv file 258B
     ```

1. Add the `A.csv` file once again:

     ```s
     pachctl put file images@master -f A.csv
     ```

1. Verify that the file size has not changed:

     ```s
     pachctl list file images@master
     ```

     **System Response:**

     ```s
     NAME   TYPE SIZE
     /A.csv file 258B
     ```

### **Appending to files**
When you enable the append mode by using the `--append`
flag or `-a`, the new files are appended to existing ones instead of overwriting them.
For example, you have an `A.csv` file in the `images` repository.
If you upload the same file to that repository with the
`--append` flag, {{%productName%}} *appends* to the file.

#### Example

1. View the list of files:

   ```s
   pachctl list file images@master
   ```

   **System Response:**

   ```s
   NAME   TYPE SIZE
   /A.csv file 258B
   ```

1. Add the `A.csv` file once again:

   ```s
   pachctl put file -a images@master -f A.csv
   ```

1. Verify that the file size has doubled:

   ```s
   pachctl list file images@master
   ```

   **System Response:**

   ```s
   NAME   TYPE SIZE
   /A.csv file 516B
   ```
