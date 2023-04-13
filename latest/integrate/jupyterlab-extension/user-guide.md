---
# metadata # 
title: User Guide
description: Learn how to use the JupyterLab Mount Extension.
date: 
# taxonomy #
tags: ["integrations", "jupyterlab", "notebooks"]
series:
seriesPart:
weight: 4
beta: true 
---

## Select a Project 

You can filter mountable repositories by selecting a project.

1. Open the JupyterLab UI. 
2. Navigate to the **Pachyderm Mount** tab ({{< jupyterlabMountIcon >}}).
3. Navigate to the **Project** dropdown.
4. Select an existing project or the `default` project.

![project select](/images/jupyterlab-extension/mount-project-select.gif)

## Create a Repo & Repo Branch 

1. Open the JupyterLab UI.
2. Open a **Terminal** from the launcher.
3. Input the following:
   
   ```s
   pachctl create repo demo
   pachctl create branch demo@master
   ```
4. Open the **Pachyderm Mount** tab ({{< jupyterlabMountIcon >}}).
5. Check the Unmounted Repositories section.

![create repo and branch](/images/jupyterlab-extension/mount-create-repo-branch.gif)

{{% notice tip %}}

Your repo is created within the project [set to your current context](../../../build-dags/project-operations/set-project).

{{% /notice %}}

## Create a Pipeline

1. Open the JupyterLab UI.
2. Create a notebook from the launcher (it can be left blank). 
3. Navigate to the Pachyderm Mount tab ({{< jupyterlabMountIcon >}}).
4. Select **Pipeline** in the side panel.
5. Input values for all of the following:
   - `Name`: The name of your pipeline.
   - `Image`: The Docker Hub image that has your user code.
   - `Requirements`: A `requirements.txt` file that contains the dependencies for your code.
   - `Input Spec`: The input spec for your pipeline in YAML format. See the [Pipeline Specification](/{{%release%}}/build-dags/pipeline-spec) for input options.
6. Select **Save**.
7. Select **Create Pipeline**.
8. Track the status of your pipeline using the command `pachctl list pipelines` in a terminal or view the pipeline in Console.

{{% notice tip %}}
You can view the full compiled pipeline spec from the **Pipline Spec Preview** section.
{{% /notice %}}


## Mount a Repo Branch

1. Open the JupyterLab UI.
2. Navigate to the **Pachyderm Mount** tab ({{< jupyterlabMountIcon >}}).
3. Navigate to the **Unmounted Repositories** section.
4. Scroll to a repository's row.
5. Select **Mount**.

![mount repo](/images/jupyterlab-extension/mount-mount-repo.gif)

<!-- 2. Open a **Terminal** from the launcher.
1. Navigate to the **Mounted Repositories** tab.
2. Input the following to see a demo repo appear:
 ```s
 pachctl create repo demo
 pachctl create branch demo@master
 ```
1. Scroll to the **Unmounted Repositories** section.
2. Select **Mount** next to the **Demo** repository. 
3. Input the following to create a simple text file:
 ```s
 echo "Version 1 of file" | pachctl put file demo@master:/myfile.txt
 ```
1. Unmount and re-mount your repo to attach to the latest commit containing the new file.
   ![re-mount repo](/images/jupyterlab-extension/mount-repo.gif)
2.  Read the file using the following:
 ```s
 cat /pfs/demo/myfile.txt
 ``` -->

## Mount (and Test) a Datum

You can mount to a specific datum in your repository from the JupyterLab UI using an **input spec**. This is useful when:

-  Working on data that is deeply nested within a specific directory of your repository.
-  Testing and exploring viable glob patterns to use for your datums.

1. Open the JupyterLab UI.
2. Navigate to the **Pachyderm Mount** tab ({{< jupyterlabMountIcon >}}).
3. Mount to a repo from the **Unmounted Repositories** section. (e.g., mounting to `demo` would look like  `/pfs/demo/` in the file browser).
4. Navigate to the **Mounted Repositories** section and select **Datum**. 

   ![mount and test datums](/images/jupyterlab-extension/mount-test-datum.gif)

   You should see the following:
      ```yaml
      pfs:
         repo: demo
         branch: master
         glob: / 
      ```
5. Update the glob pattern to match the datums you wish to focus on.
      ##### Directory Example 

   ```yaml
   pfs:
      repo: demo
      branch: master
      glob: /images/2022/*
   ```

   ##### Extension Example 

   ```yaml
   pfs:
      repo: demo
      branch: master
      glob: /images/**.png
   ```
6. Select **Mount Datums**.
7. The file browser updates to display the matching datums. 

When you return to the mounted view by selecting **Back**, the file browser will return to displaying datums that match your default glob pattern.

## Explore Directories & Files

At the bottom of the **Mounted Repositories** tab, you'll find the file browser. 

- Mounted repositories are nested within the root `/pfs` ({{% productName %}}'s File System)
- These repositories are **read-only**
- Mounted repositories have a `/` glob pattern applied to their directories and files
- Files only downloaded locally when you access them (saving you time)

Using the previous example, while the **Demo** repository is mounted, you can select the **demo** folder to reveal the example `myfile.txt`. 


