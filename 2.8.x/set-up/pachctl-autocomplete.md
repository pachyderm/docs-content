---
# metadata # 
title: Pachctl Auto-completion
description: Learn how to install our auto-completion helper tool (it's great for learning PachCTL commands).
date: 
# taxonomy #
tags: ["deployment"]
series:
seriesPart: 
weight: 2
directory: true 
---

{{% productName %}} auto-completion allows you to automatically finish partially typed commands by pressing `TAB`. 

## Before You Start 

- You must already have PachCTL installed


## How to Install Auto-Completion

{{< stack type="wizard" >}}
 {{% wizardRow id="Command Shell" %}}
  {{% wizardButton option="Zsh" state="active" %}}
  {{% wizardButton option="Bash" %}}
 {{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="command-shell/bash"%}}
1. Verify that `bash-completion` is installed on your machine.
   For example, if you have installed bash completion by using Homebrew,
   type:

   ```s
   brew info bash-completion
   ```

   This command returns information about the directory in which
   `bash-completion` and bash completion scripts are installed.
   For example,  `/usr/local/etc/bash_completion.d/`. You need
   to specify the path to `bash_completion.d` as the path to which install
   `pachctl` autocompletion. Also, the output of the info
   command might have a suggestion to include the path to
   `bash-completion` into your `~/.bash_profile` file.

2. Install `pachctl` autocompletion:
3. 
   ```s

   pachctl completion bash --install --path <path/to/bash-completion>
   ```

   For example, if you specify the path to `bash-completion` as
   `/usr/local/etc/bash_completion.d/pachctl`, your system response
   looks like this:

   **System response:**

   ```
   Bash completions installed in /usr/local/etc/bash_completion.d/pachctl, you must restart bash to enable completions.
   ```

4. Restart your terminal.

   `pachctl` autocomplete should now be enabled in your system.
{{% /wizardResult %}}

{{% wizardResult val1="command-shell/zsh"%}}

1. Install `zsh-completions`: 
   ```s
   brew install zsh-completions
   ```

2. Install `pachctl` autocompletion:

   {{% notice tip %}}
   
   You'll need to install this in the same directory your `zsh-completions` are installed in. You can run the following to find the correct path:
   ```s
   echo $fpath
   ```
   {{% /notice %}}

   ```s
   pachctl completion bash --install --path /opt/homebrew/share/zsh-completions/_pachctl
   ```

3. Restart your terminal; `pachctl` autocomplete should now be enabled in your system. 
   
   If you run into warnings in your terminal related to `zsh compinit: insecure directories`, you can run the following to fix it:

   ```s
   chmod go-w /opt/homebrew/share
   ```
{{% /wizardResult %}}
{{% /wizardResults %}}
 {{< /stack >}}
 

## Testing

You can perform the following tests to verify that `pachctl` autocompletion is working:

1. Open a new terminal.
2. Input the following:

   ```s
   pachctl v
   ```
3. Hit `TAB`. You should see the following output:

```s
validate  -- Validate the specification of a Pachyderm resource.
version   -- Print Pachyderm version information.
```