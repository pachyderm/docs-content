---
# metadata #
title: Troubleshooting
description: Learn how to troubleshoot the JupyterLab Mount Extension.
date:
# taxonomy #
tags: ["integrations", "jupyterlab", "notebooks"]
series:
seriesPart:
weight: 5
beta: true
---

## Known Issues

### M1 Users With Docker Desktop < `4.6`

A [documented issue between qemu and Docker Desktop](https://gitlab.com/qemu-project/qemu/-/issues/340) prevents you from running our pre-built Mount Extension Image in Docker Desktop.

We recommend the following:

  - Use [Podman](https://podman.io) (See installation instructions)
  ```shell
  brew install podman
  podman machine init --disk-size 50
  podman machine start
  podman machine ssh
  sudo rpm-ostree install qemu-user-static && sudo systemctl reboot THEN
  ```
   then replace the keyword `docker` with `podman` in all the commands above.
  - Or make sure that your qemu version is > `6.2`