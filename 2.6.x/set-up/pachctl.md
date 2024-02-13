---
# metadata # 
title: Pachctl
description: Learn how to install PachCTL.
date: 
# taxonomy #
tags: ["deployment"]
series:
seriesPart: 
weight: 1
directory: true 
---


{{< stack type="wizard" >}}
 {{% wizardRow id="operating-system" %}}
  {{% wizardButton option="MacOs, Windows, & Darwin" state="active" %}}
  {{% wizardButton option="Debian" %}}
 {{% /wizardRow %}}

 {{% wizardResults %}}
 {{% wizardResult val1="operating-system/macos-windows-darwin" %}}
 ```s
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@{{% majorMinorNumber %}}  
```
 {{% /wizardResult%}}
 {{% wizardResult val1="operating-system/debian" %}}

```s
curl -o /tmp/pachctl.deb -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_amd64.deb && sudo dpkg -i /tmp/pachctl.deb
```
 {{% /wizardResult%}}
 {{% /wizardResults%}}
 {{</stack>}}
 