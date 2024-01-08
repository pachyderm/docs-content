---
# metadata # 
title:  First-Time Setup
description: 
date: 
# taxonomy #
tags: 
series:
seriesPart:
weight: 2
directory: true
---

{{% productName %}} can be deployed in Kubernetes using a wide variety of container orchestrators, but to get you set up for the very first time, we recommend using Docker Desktop. This installation method is very fast and will provide you with everything you need to start the [Beginner Tutorial](/{{%release%}}/get-started/beginner-tutorial). 

## Before You Start

{{< stack type="wizard" >}}
 {{% wizardRow id="operating-system" %}}
  {{% wizardButton option="macOS" state="active" %}}
  {{% wizardButton option="Windows" %}}
  {{% wizardButton option="Linux" %}}
 {{% /wizardRow %}}

{{% wizardResults %}}
 {{% wizardResult val1="operating-system/macos" %}}
  - You must have [Homebrew](https://brew.sh/) installed. 
  ```s
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
 {{% /wizardResult %}}
 {{% wizardResult val1="operating-system/windows" %}}
 - You must have [Windows Subsystem for Linux (WSL) 2](https://learn.microsoft.com/en-us/windows/wsl/install) enabled (`wsl --install`) and a Linux distribution installed; if Linux does not boot in your WSL terminal after downloading from the Microsoft store, see the [manual installation guide](https://learn.microsoft.com/en-us/windows/wsl/install-manual).


**Manual Step Summary**:

1. Open a PowerShell terminal.
2. Run each of the following:

```s
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
3. Run each of the following:
```s
wsl --update

wsl --set-default-version 2

wsl --install -d Ubuntu 
```
4. Restart your machine.
5. Start a WSL terminal and set up your first Ubuntu user.
6. Update Ubuntu.
```s
sudo apt update
sudo apt upgrade -y
```
7. Install Homebrew in Ubuntu so you can complete the rest of this guide:
```s
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
All installation steps after [1. Install Docker Desktop](#1-install-docker-desktop) must be run through the WSL terminal (Ubuntu) and not in PowerShell. 

You are now ready to continue to Step 1.
 {{% /wizardResult %}}
 {{% wizardResult val1="operating-system/linux" %}}
  - You can optionally install [Homebrew](https://brew.sh/) to easily install tools like Helm. 
```s
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
 {{% /wizardResult %}}
{{% /wizardResults %}}
{{< /stack >}}

## 1. Install Docker Desktop

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your machine.
2. Navigate to **Settings** for [Mac](https://docs.docker.com/desktop/settings/mac/), [Windows](https://docs.docker.com/desktop/settings/windows/), or [Linux](https://docs.docker.com/desktop/settings/linux/). 
   - Adjust your resources (~4 CPUs and ~12GB Memory) 
   - [Enable Kubernetes](https://docs.docker.com/desktop/kubernetes/)
3. Select **Apply & Restart**.


## 2. Install Pachctl CLI
{{< stack type="wizard" >}}
 {{% wizardRow id="operating-system" %}}
  {{% wizardButton option="MacOs & Windows" state="active" %}}
  {{% wizardButton option="Debian" %}}
  {{% wizardButton option="Linux" %}}
 {{% /wizardRow %}}

 {{% wizardResults %}}
 {{% wizardResult val1="operating-system/macos-windows" %}}
 ```s
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@{{% majorMinorNumber %}}  
```
 {{% /wizardResult%}}
 {{% wizardResult val1="operating-system/debian" %}}

```s
curl -o /tmp/pachctl.deb -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_amd64.deb && sudo dpkg -i /tmp/pachctl.deb
```
 {{% /wizardResult%}}

 {{% wizardResult val1="operating-system/linux" %}}

  **AMD**
 ```s
 curl -L https://github.com/pachyderm/pachyderm/releases/download/v{{%latestPatchNumber%}}/pachctl_{{%latestPatchNumber%}}_linux_amd64.tar.gz | sudo tar -xzv --strip-components=1 -C /usr/local/bin
 ```
**ARM**
```s
curl-L https://github.com/pachyderm/pachyderm/releases/download/v{{%latestPatchNumber%}}/pachctl_{{%latestPatchNumber%}}_linux_arm64.tar.gz | sudo  tar -xzv --strip-components=1 -C /usr/local/bin
```
 {{%/wizardResult%}}
 {{%/wizardResults%}}
 {{</stack>}}


## 3. Install & Configure Helm

1. Install [Helm](https://helm.sh/docs/intro/install/):
```s
brew install helm
```
2. Add the Pachyderm repo to Helm:
```s
helm repo add pachyderm https://helm.pachyderm.com  
helm repo update  
```
3. Install PachD: 

{{%notice tip%}}
Open your browser and check `http://localhost` before installing. If any other tools are using the same port as {{%productName%}}, add the following argument to the below command: `--set proxy.service.httpPort=8080`
{{%/notice%}}

{{< stack type="wizard" >}}
 {{% wizardRow id="version" %}}
  {{% wizardButton option="Community Edition" state="active" %}}
  {{% wizardButton option="Enterprise" %}}
 {{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="version/community-edition" %}}

**For Docker Desktop:**

```s
helm install pachyderm pachyderm/pachyderm \
  --set deployTarget=LOCAL \
  --set proxy.enabled=true \
  --set proxy.service.type=LoadBalancer  \
  --set proxy.host=localhost
```

**For Minikube:**

```s
helm install pachyderm pachyderm/pachyderm \
  --set deployTarget=LOCAL \
  --set proxy.enabled=true \
  --set proxy.service.type=LoadBalancer  \
  --set proxy.host=localhost
```

{{% /wizardResult %}}
{{% wizardResult val1="version/enterprise" %}}
Are you using an [Enterprise](/{{%release%}}/set-up/enterprise) trial key? If so, you can set up Enterprise Pachyderm locally by storing your trial key in a `license.txt` file and passing it into the following Helm command: 

```s  
helm install pachyderm pachyderm/pachyderm \
  --set deployTarget=LOCAL \
  --set pachd.enterpriseLicenseKey="$(cat license.txt)" \
  --set proxy.enabled=true \
  --set proxy.service.type=LoadBalancer  \
  --set proxy.host=localhost

``` 
This unlocks Enterprise features but also [requires user authentication](/{{%release%}}/set-up/connectors)  to access Console. A mock user is created by default to get you started, with the **username**: `admin` and **password**: `password`.
{{% /wizardResult %}}
{{% /wizardResults %}}
{{< /stack >}}


   This may take several minutes to complete. 

## 4. Verify Installation 

1. In a new terminal, run the following command to check the status of your pods:
 ```s
 kubectl get pods
 ```
 ```
 NAME                                           READY   STATUS      RESTARTS   AGE
pod/console-5b67678df6-s4d8c                   1/1     Running     0          2m8s
pod/etcd-0                                     1/1     Running     0          2m8s
pod/pachd-c5848b5c7-zwb8p                      1/1     Running     0          2m8s
pod/pg-bouncer-7b855cb797-jqqpx                1/1     Running     0          2m8s
pod/postgres-0                                 1/1     Running     0          2m8s
 ```
2. Re-run this command after a few minutes if `pachd` is not ready.

## 5. Connect to Cluster

```s
pachctl connect http://localhost:80
```
{{% notice warning %}}
If you set the `httpPort` to a new value, such as `8080`, use that value in the command. `pachctl connect http://localhost:8080`
{{%/notice %}}

Optionally open your browser and navigate to the [Console UI](http://localhost).

{{% notice tip %}}
You can check your Pachyderm version and connection to `pachd` at any time with the following command:
   ```s
   pachctl version
   ```
   ```
   COMPONENT           VERSION  

   pachctl             {{% latestPatchNumber %}}  
   pachd               {{% latestPatchNumber %}}  
   ```
{{% /notice %}}
