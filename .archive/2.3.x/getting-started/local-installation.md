---
# metadata # 
title:  Local Installation  
description: Learn how to install locally using your favorite container solution.
date: 
# taxonomy #
tags:  ["deployment"]
series:
seriesPart: 1
---

{{% notice tip %}}
Looking to upgrade to **pachd** 2.3.0+ from an older version? Remember to also upgrade **pachctl** for the best experience.
{{% /notice %}}
  
This guide covers how you can quickly get started using {{%productName%}} locally on macOS®, Linux®, or Microsoft® Windows®. To install {{%productName%}} on Windows, first look at [Deploy {{%productName%}} on Windows](../wsl-deploy).

{{%productName%}} is a data-centric pipeline and data versioning application written in go that runs on top of a Kubernetes cluster. 
A common way to interact with {{%productName%}} is by using {{%productName%}} command-line tool `pachctl`, from a terminal window. To check the state of your deployment, you will also need to install `kubectl`, Kubernetes command-line tool. 

Additionally, we will show you how to deploy and access {{%productName%}} UIs **[JupyterLab Mount Extension](../../how-tos/jupyterlab-extension/)** and **[Console](../../deploy-manage/deploy/console)** on your local cluster. 

Note that each web UI addresses different use cases:

- **JupyterLab Mount Extension** allows you to experiment and explore your data, then build your pipelines' code from your familiar Notebooks.
- **Console** helps you visualize your DAGs (Directed Acyclic Graphs), monitor your pipeline executions, access your logs, and troubleshoot while your pipelines are running.
  
{{% notice warning %}}
- A local installation is **not designed to be a production  
environment**. It is meant to help you learn and experiment quickly with {{%productName%}}.   
- A local installation is designed for a **single-node cluster**.  
This cluster uses local storage on disk and does not create  
Persistent Volumes (PVs). If you want to deploy a production multi-node  
cluster, follow the instructions for your cloud provider or on-prem  
installation as described in [Deploy {{%productName%}}](../../deploy-manage/deploy/).  
New Kubernetes nodes cannot be added to this single-node cluster.   
{{% /notice %}}  

{{%productName%}} uses `Helm` for all deployments.  

{{% notice warning %}}
We are now shipping {{%productName%}} with an **optional embedded proxy** 
allowing your cluster to expose one single port externally. This deployment setup is optional.

If you choose to deploy {{%productName%}} with a Proxy, check out our new recommended architecture and [deployment instructions](../../deploy-manage/deploy/deploy-w-proxy).
{{% /notice%}}

## Prerequisites  

For a successful local deployment of {{%productName%}}, you will need:  
  
- A [Kubernetes cluster](#setup-a-local-kubernetes-cluster) running on your local environment (pick the virtual machine of your choice):   
      - [Docker Desktop](#using-kubernetes-on-docker-desktop),  
      - [Minikube](#using-minikube)  
      - [Kind](#using-kind)  
      - Oracle® VirtualBox™ 
- [Helm](#install-helm) to deploy {{%productName%}} on your Kubernetes cluster.  
- [{{%productName%}} Command Line Interface (`pachctl`)](#install-pachctl) to interact with your {{%productName%}} cluster.
- [Kubernetes Command Line Interface (`kubectl`)](https://kubernetes.io/docs/tasks/tools/) to interact with your underlying Kubernetes cluster.

### Setup A Local Kubernetes Cluster

Pick the virtual machine of your choice.

#### Using Minikube  
  
On your local machine, you can run {{%productName%}} in a minikube virtual machine.  
Minikube is a tool that creates a single-node Kubernetes cluster. This limited  
installation is sufficient to try basic {{%productName%}} functionality and complete  
the Beginner Tutorial.  
  
To configure Minikube, follow these steps:  
  
1. Install minikube and VirtualBox in your operating system as described in  
the [Kubernetes documentation](https://kubernetes.io/docs/setup/).    
1. Start `minikube`:  
  
      ```s  
      minikube start  
      ```  
      Linux users, add this `--driver` flag:
      ```s
      minikube start --driver=kvm2
      ```
{{% notice note %}}
Any time you want to stop and restart {{%productName%}}, run `minikube delete`  and `minikube start`. Minikube is not meant to be a production environment and does not handle being restarted well without a full wipe.  
{{% /notice %}}
  
#### Using Kubernetes on Docker Desktop   
  
You can use Kubernetes on Docker Desktop instead of Minikube on macOS or Linux by following these steps:  
  
1. In the Docker Desktop Preferences, enable Kubernetes:  
   ![Docker Desktop Enable K8s](../images/k8s_docker_desktop.png)  
  
2. From the command prompt, confirm that Kubernetes is running:  
   ```s  
   kubectl get all  
   ```  
   ```s  
   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE  
   service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   5d  
   ```  
      To reset your Kubernetes cluster that runs on Docker Desktop, click the **Reset Kubernetes cluster** button. See image above.   
  
#### Using Kind  
  
1. Install Kind according to its [documentation](https://kind.sigs.k8s.io/).  
  
1. From the command prompt, confirm that Kubernetes is running:  
   ```s  
   kubectl get all  
   ```  
   ```s  
   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE  
   service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   5d  
   ```  
  
### Install `pachctl`  

{{% notice note %}}
`pachctl` is a command-line tool that you can use to interact with a {{%productName%}} cluster in your terminal.  
{{% /notice %}}

{{% notice warning %}}
{{%productName%}} now offers **universal Multi-Arch docker images that can serve both ARM and AMD users**.

- Brew users: The download of the package matching your architecture is automatic—nothing specific to do.
- Debian-based and other Linux flavors users not relying on [Homebrew](https://docs.brew.sh/Homebrew-on-Linux):

Run `uname -m` to identify your architecture, then choose the command in the `AMD` section below if the output is `x86_64` , or `ARM` if it is `aarch64`.
{{% /notice %}}
  
1. Run the corresponding steps for your operating system:  
   * For **macOS or Brew users**, run:  

     ```s  
     brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@{{% majorMinorNumber %}} 
     ```  

   * For a **Debian-based Linux 64-bit or Windows 10 or later running on WSL** (Choose the command matching your architecture):  
         
     - AMD Architectures (amd64):
          
       ```s  
       curl -o /tmp/pachctl.deb -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_amd64.deb && sudo dpkg -i /tmp/pachctl.deb  
       ``` 

     - ARM Architectures (arm64):

       ```s  
       curl -o /tmp/pachctl.deb -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_arm64.deb && sudo dpkg -i /tmp/pachctl.deb  
       ```  

   * For all **other Linux flavors** (Choose the command matching your architecture):  

     - AMD Architectures (amd64):
               
       ```s  
       curl -o /tmp/pachctl.tar.gz -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_linux_amd64.tar.gz && tar -xvf /tmp/pachctl.tar.gz -C /tmp && sudo cp /tmp/pachctl_{{% latestPatchNumber %}}_linux_amd64/pachctl /usr/local/bin 
       ``` 

     - ARM Architectures (arm64):

       ```s  
       curl -o /tmp/pachctl.tar.gz -L https://github.com/pachyderm/pachyderm/releases/download/v{{% latestPatchNumber %}}/pachctl_{{% latestPatchNumber %}}_linux_arm64.tar.gz && tar -xvf /tmp/pachctl.tar.gz -C /tmp && sudo cp /tmp/pachctl_{{% latestPatchNumber %}}_linux_arm64/pachctl /usr/local/bin 
       ```  
            
2. Verify that installation was successful by running `pachctl version --client-only`:  
  
      ```s  
      pachctl version --client-only  
      ```  
  
      **System Response:**  
  
      ```s  
      COMPONENT           VERSION  
      pachctl             {{% latestPatchNumber %}}  
      ```  
  
      If you run `pachctl version` without the flag `--client-only`, the command times  
      out. This is expected behavior because {{%productName%}} has not been deployed yet (`pachd` is not yet running).  

{{% notice tip %}}
If you are new to {{%productName%}}, try [{{%productName%}} Shell](../../deploy-manage/manage/pachctl-shell/). This add-on tool suggests `pachctl` commands as you type. It will help you learn {{%productName%}}'s main commands faster.  
{{% /notice %}}
  
{{% notice Note  %}}
A look at [{{%productName%}} high-level architecture diagram](../../deploy-manage/#overview) will help you build a mental image of {{%productName%}} various architectural components.  

For information, you can also check what a production setup looks like in this [infrastructure diagram](../../deploy-manage/deploy/ingress/#deliver-external-traffic-to-pachyderm).  
{{% /notice %}}
  
### Install `Helm`  
  
Follow Helm's [installation guide](https://helm.sh/docs/intro/install/).  
  
## Deploy {{%productName%}}
  
When done with the [Prerequisites](#prerequisites), deploy {{%productName%}} on your local cluster by following these steps. Your default installation comes with Console ({{%productName%}}'s Web UI).

Additionally, for JupyterLab users,  you can [**install {{%productName%}} JupyterLab Mount Extension**](#notebooks-users-install-pachyderm-jupyterlab-mount-extension) on your local {{%productName%}} cluster to experience {{%productName%}} from your familiar notebooks. 

Note that you can run both Console and JupyterLab on your local installation.
  
* Get the Repo Info:  

    ```s  
    helm repo add pach https://helm.pachyderm.com  
    helm repo update 
    ```  

* Install {{%productName%}}:  

{{% notice warning %}} 
To request a FREE trial enterprise license key, [click here](../../enterprise). 
{{% /notice %}}

### {{%productName%}} Community Edition (Includes Console)

This command will install {{%productName%}}'s latest available GA version with Console Community Edition.

 ```s  
 helm install --wait --timeout 10m pachd pach/pachyderm --set deployTarget=LOCAL  
 ```    

 Add the following `--set console.enabled=false` to the command above to install without Console.

### Enterprise
This command will unlock your enterprise features and install Console Enterprise. Note that Console Enterprise requires authentication. By default, **we create a default mock user (username:`admin`, password: `password`)** to [authenticate to Console](../../deploy-manage/deploy/console/#connect-to-console) without having to connect your Identity Provider. 

 - Create a `license.txt` file in which you paste your [Enterprise Key](../../enterprise).
 - Then, run the following helm command to **install {{%productName%}}'s latest Enterprise Edition**: 

  ```s  
  helm install --wait --timeout 10m pachd pach/pachyderm --set deployTarget=LOCAL  --set pachd.enterpriseLicenseKey=$(cat license.txt) --set console.enabled=true  
  ``` 

{{% notice note %}}
This installation can take several minutes. Run a quick `helm list --all` in a separate tab to witness the installation happening in the background.
{{% /notice %}}

{{% notice tip %}} 
To uninstall {{%productName%}} fully.

Running `helm uninstall pachd` leaves persistent volume claims behind. To wipe your instance clean, run:

```s
helm uninstall pachd 
kubectl delete pvc -l suite=pachyderm 
```
{{% /notice %}}

{{% notice info %}}
More [details on {{%productName%}}'s Helm installation](../../deploy-manage/deploy/helm-install/).
{{%/notice %}}

## Check Your Install

Check the status of the {{%productName%}} pods by periodically running `kubectl get pods`. When {{%productName%}} is ready for use, all {{%productName%}} pods must be in the **Running** status.

Because {{%productName%}} needs to pull the {{%productName%}} Docker images from DockerHub, it might take a few minutes for the {{%productName%}} pods status to change to `Running`.

```s
kubectl get pods
```

**System Response:**
At a very minimum, you should see the following pods (console depends on your choice above): 

```s
NAME                                           READY   STATUS      RESTARTS   AGE
pod/console-5b67678df6-s4d8c                   1/1     Running     0          2m8s
pod/etcd-0                                     1/1     Running     0          2m8s
pod/pachd-c5848b5c7-zwb8p                      1/1     Running     0          2m8s
pod/pg-bouncer-7b855cb797-jqqpx                1/1     Running     0          2m8s
pod/postgres-0                                 1/1     Running     0          2m8s
```

If you see a few restarts on the `pachd` nodes, that means that
Kubernetes tried to bring up those pods before `etcd` or `postgres` were ready. Therefore,
Kubernetes restarted those pods. Re-run `kubectl get pods`
 
## Connect `pachctl` to Your Cluster

Assuming your `pachd` is running as shown above, the easiest way to connect `pachctl` to your local cluster is to use the `port-forward` command.

- To connect to your new {{%productName%}} instance, run:
  ```s
  pachctl config import-kube local --overwrite
  pachctl config set active-context local
  ```

- Then:
  ```s
  pachctl port-forward
  ``` 

### Verify that `pachctl` and your cluster are connected. 
  
```s  
pachctl version  
```  

**System Response:**  

```s  
COMPONENT           VERSION  
pachctl             {{% latestPatchNumber %}}  
pachd               {{% latestPatchNumber %}}  
```  
You are all set!  

### If You Have Deployed {{%productName%}} Community Edition

You are ready!
To connect to your Console ({{%productName%}} UI), point your browser to **`localhost:4000`**.
### If You Have Deployed {{%productName%}} Enterprise

- To connect to your Console ({{%productName%}} UI), point your browser to **`localhost:4000`** 
and authenticate using the mock User (username: `admin`, password: `password`).

- Alternatively, you can connect to your Console ({{%productName%}} UI) directly by
pointing your browser to port `4000` on your minikube IP (run `minikube ip` to retrieve minikube's external IP) or docker desktop IP **`http://<dockerDesktopIdaddress-or-minikube>:4000/`** 
then authenticate using the mock User (username: `admin`, password: `password`).

- To use `pachctl`, you need to run `pachctl auth login` then
authenticate again (to {{%productName%}} this time) with the mock User (username: `admin`, password: `password`).

## Next Steps  
  
Complete the [Beginner Tutorial](../beginner-tutorial) to learn the basics of {{%productName%}}, such as adding data to a repository and building analysis pipelines.  
  
{{% notice note %}}
See Also: [General Troubleshooting](../../troubleshooting/general-troubleshooting) 
{{% /notice %}}