---
# metadata # 
title: File
description: Learn about the concept of a file, which is a Unix filesystem object that stores data. 
glossaryDefinition: A Unix filesystem object (directory or file) that stores data.
date: 
# taxonomy #
tags: ["concepts", "pachctl", "data-operations"]
series: ["glossary"]
seriesPart:
--- 

A file is a Unix filesystem object, which is a directory or file, that stores data. Unlike source code version-control systems that are most suitable for storing plain text files, you can store any type of file in {{% productName %}}, including binary files. 

Often, data scientists operate with comma-separated values (CSV), JavaScript Object Notation (JSON), images, and other plain text and binary file formats. {{% productName %}} supports all file sizes and formats and applies storage optimization techniques, such as deduplication, in the background.
