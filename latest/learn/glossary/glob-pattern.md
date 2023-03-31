---
# metadata # 
title: Glob Pattern
description: Learn about the concept of a glob pattern, which is a string of characters that specifies a set of filenames or paths in a file system. 
date: 
# taxonomy #
tags: ["concepts", "pachctl", "datums","pipelines", "data-operations"]
series: ["glossary"]
seriesPart:
--- 

A glob pattern is a string of characters that specifies a set of filenames or paths in a file system. The term "glob" is short for "global," and refers to the fact that a glob pattern can match multiple filenames or paths at once. For {{% productName %}}, you can use glob patterns to define the shape of your [datums](TBD) against your inputs, which are spread across [{{% productName %}} workers](TBD) for [distributing computing](TBD).

## Examples

| Glob Pattern     | Datum created|
|-----------------|---------------------------------|
| `/` | {{% productName %}} denotes the **whole repository as a single datum** and sends all input data to a single worker node to be processed together.|
| `/*`| {{% productName %}} defines **each top-level files / directories** in the input repo, **as a separate datum**. For example, if you have a repository with ten files and no directory structure, {{% productName %}} identifies each file as a single datum and processes them independently.|
| `/*/*`| {{% productName %}} processes **each file / directory in each subdirectories as a separate datum**.|
| `/**` | {{% productName %}} processes **each file in all directories and subdirectories as a separate datum**.|


Glob patterns can also use other special characters, such as the question mark (`?`) to match a single character, or brackets (`[...]`) to match a set of characters. 

