---
# metadata #
title: Local Installation Guide
description: Learn how to locally install and use the JupyterLab Mount Extension.
date:
# taxonomy #
tags: ["integrations", "jupyterlab", "notebooks"]
series:
seriesPart:
weight: 3
beta: true
---

## Before You Start

- You must have a {{% productName %}} cluster running.
- Install [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) (`pip install jupyterlab`)
- Install [jupyterlab pachyderm](https://pypi.org/search/?q=jupyterlab+pachyderm) (`pip install jupyterlab-pachyderm`)

## Local Installation Steps

1. Open your terminal.
2. Open your `zshrc` profile:
   ```s
   vim ~/.zshrc
   ```
3. Create a `/pfs` directory to mount your data to. This is the default directory used; alternatively, you can define an empty output folder that PFS should mount by adding `export PFS_MOUNT_DIR=/<directory>/<path>` to your bash/zshrc profile.
4. Update the source by restarting your computer or executing the following command:
   ```s
   source ~/.zshrc
   ```
5. Run `jupyter lab`.

If you have an existing pachyderm config file at `~/.pachyderm/config.json`, the extension automatically connects to the active context. Otherwise, you must enter the cluster address manually in the extension UI.