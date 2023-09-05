---
# metadata # 
title:  Beginner Tutorial
description: Learn how to quickly ingest photos, trace their outlines, and output a collage using the transformed data.
date: 
# taxonomy #
tags: ["tutorials"]
series:
seriesPart: 
weight: 1
directory: true 
---

## Before You Start 

- Install {{% productName %}} either [locally](/{{%release%}}/set-up/local-deploy) our within the [cloud](/{{%release%}}/set-up/cloud-deploy). 
- Install [{{% productName %}} Shell](/{{%release%}}/manage/pachctl-shell/).
- Join our [Slack Community](https://www.pachyderm.com/slack/) so you can ask any questions you may have!

### Context

### How it Works

{{% productName %}} deploys a Kubernetes cluster to manage and version your data using [projects](/{{%release%}}/learn/glossary/project), [input repositories](/{{%release%}}/learn/glossary/input-repo), [pipelines](/{{%release%}}/learn/glossary/pipeline), [datums](/{{%release%}}/build-dags/datum-operations) and [output repositories](/{{%release%}}/learn/glossary/output-repo). A project can house many repositories and pipelines, and when a pipeline runs a [job](/{{%release%}}/learn/glossary/job/) it chunks your inputs into many datums for processing. The number of datums is determined by the [glob pattern](/{{%release%}}/learn/glossary/glob-pattern/) defined in your [pipeline specification](/{{%release%}}/learn/glossary/pipeline-specification/). 

Once chunked, each datum is processed using your [user code](/{{%release%}}/learn/glossary/user-code) in a [worker pod](/{{%release%}}/learn/glossary/pachyderm-worker/). This user code is also referenced in the pipeline specification as a Docker image. The end result of your data transformation is stored in the pipeline's output repository, which shares the same name as the pipeline. Pipelines can be single-step or multi-step; multi-step pipelines are commonly referred to as [DAGs](/{{%release%}}/learn/glossary/dag), with each part of the DAG being a "step" pipeline.

Don't worry if this sounds confusing! We'll walk you through the process step-by-step.
### How to Interact with {{% productName %}}

You can interact your {{%productName%}} cluster using the PachCTL CLI or through Console, a GUI.

  - **PachCTL** is great for users already experienced with using a CLI.
  - **Console** is great for beginners and helps with visualizing relationships between projects, repos, and pipelines.

---

## Tutorial: Image & Video Processing with OpenCV

In this tutorial, we'll walk you through how to use {{% productName %}} to process images and videos using [OpenCV](https://opencv.org/). OpenCV is a popular open-source computer vision library that can be used to perform image processing and video analysis.

This DAG has 6 steps with the goal of intaking raw photos and video content, drawing edge-detected traces, and outputting a comparison collage of the original and processed images:
 
 1. Convert videos to MP4 format
 2. Extract frames from videos
 3. Trace the outline of each frame and standalone image
 4. Create `.gifs` from the traced video frames
 5. Re-shuffle the content so it is organized by "original" and "traced" images
 6. Build a comparison collage using a static HTML page

![DAG](/images/beginner-tutorial/vid-to-frametrace.svg)

### 1. Create a Project 

By default, when you first start up an instance, the `default` project is attached to your active context. Create a new project and set the project to your active PachCTL context to avoid having to specify the project name (e.g., `--project video-to-frame-traces`) in each command. 

```s
pachctl create project video-to-frame-traces
pachctl config update context --project video-to-frame-traces
pachctl list projects
```

### 2. Create an Input Repo 

At the top of our DAG, we'll need an input repo that will store our raw videos and images. 
   
```s
pachctl create repo raw_videos_and_images
pachctl list repos
```

### 3. Create the Video Converter Pipeline 

We want to make sure that our DAG can handle videos in multiple formats, so first we'll create a pipeline that will:
- skip images 
- skip videos already in the correct format (`.mp4`)
- convert videos to `.mp4` format

The converted videos will be made available to the next pipeline in the DAG via the `video_mp4_converter` repo by declaring in the user code to save the converted images to `/pfs/out/`. This is the standard location you should use to store your output data so that it can be accessed by the next pipeline in the DAG.

1. Open your terminal.
2. Create a new folder for your project called `video-to-frametrace`.
3. Copy and paste the following [pipeline spec](/{{%release%}}/build-dags/pipeline-spec/) into the terminal to create the file.

```s
cat <<EOF > video_mp4_converter.yaml
pipeline:
  name: video_mp4_converter
input:
  pfs:
    repo: raw_videos_and_images
    glob: "/*"
transform:
  image: lbliii/video_mp4_converter:1.0.14
  cmd:
    - python3
    - /video_mp4_converter.py
    - --input
    - /pfs/raw_videos_and_images/
    - --output
    - /pfs/out/
autoscaling: true
EOF
```
4. Create the pipeline by running the following command:
```s
pachctl create pipeline -f video_mp4_converter.yaml 
```

{{% notice info %}}
Every pipeline, at minimum, needs a `name`, an `input`, and a `transform`. The input is the data that the pipeline will process, and the transform is the user code that will process the data. `transform.image` is the Docker image available in a container registry ([Docker Hub](https://hub.docker.com/)) that will be used to run the user code. `transform.cmd` is the command that will be run inside the Docker container.
{{%/notice %}}

### 4. Create the Image Flattener Pipeline

Next, we'll create a pipeline that will flatten the videos into individual `.png` image frames. Like the previous pipeline, the user code outputs the frames to `/pfs/out` so that the next pipeline in the DAG can access them in the `image_flattener` repo. 

```s
cat <<EOF > image_flattener.yaml
pipeline:
  name: image_flattener
input:
  pfs:
    repo: video_mp4_converter
    glob: "/*"
transform:
  image: lbliii/image_flattener:1.0.0
  cmd:
    - python3
    - /image_flattener.py
    - --input
    - /pfs/video_mp4_converter
    - --output
    - /pfs/out/
autoscaling: true
EOF
```

```s
pachctl create pipeline -f image_flattener.yaml
```

### 5. Create the Image Tracing Pipeline: 

Up until this point, we've used a simple single input from the Pachyderm file system (`input.pfs`) and a basic [glob pattern](/{{%release%}}/learn/glossary/glob-pattern/) (`/*`) to specify shape of our the input data datums. This particular pattern treats each top-level file and directory as a single datum. However, in this pipeline, we have some special requirements:

- We want to process *only* the raw images from the `raw_videos_and_images` repo
- We want to process *all* of the flattened video frame images from the `image_flattener` pipeline

To achieve this, we're going to need to use a [union input](/{{%release%}}/build-dags/pipeline-spec/input-union/) (`input.union`) to combine the two inputs into a single input for the pipeline. 

- For the `raw_videos_and_images` input, we can use a more powerful glob pattern to ensure that only image files are processed (`/*.{png,jpg,jpeg}`). 
- For the `image_flattener` input, we can use the same glob pattern as before (`/*`) to ensure that each video's collection of frames is processed together.

```s
cat <<EOF > image_tracer.yaml
pipeline:
  name: image_tracer
description: A pipeline that performs image edge detection by using the OpenCV library.
input:
  union:
    - pfs:
        repo: raw_videos_and_images
        glob: "/*.{png,jpg,jpeg}"
    - pfs:
        repo: image_flattener
        glob: "/*"
transform:
  image: lbliii/image_tracer:1.0.8
  cmd:
    - python3
    - /image_tracer.py
    - --input
    - /pfs/raw_videos_and_images
    - /pfs/image_flattener
    - --output
    - /pfs/out/
autoscaling: true
EOF
```

```s
pachctl create pipeline -f image_tracer.yaml
```

### 6. Create the Gif Pipeline

Next, we'll create a pipeline that will create two gifs:
  1. a gif of the original video's flattened frames (from the `image_flattener` output repo)
  2. a gif of the video's traced frames (from the `image_tracer` output repo)

- [See User Code](./4_gif_images/movie_gifer.py)
- [See Pipeline Spec](./4_gif_images/movie_gifer.yaml)

```s
pachctl create pipeline -f 4_gif_images/movie_gifer.yaml
```

### 7. Create the Content Shuffler Pipeline

Next, we'll create a pipeline that will re-shuffle the content from the previous pipelines into two folders:
   - `edges`: contains the traced images and gifs
   - `originals`: contains the original images and gifs

This helps us keep the content organized for easy access and manipulation in the next pipeline.

- [See User Code](./5_shuffle_content/content_shuffler.py)
- [See Pipeline Spec](./5_shuffle_content/content_shuffler.yaml)

```s
pachctl create pipeline -f 5_shuffle_content/content_shuffler.yaml
```

### 8. Create the Content Collager Pipeline

Finally, we'll create a pipeline that will create a static html page that you can download and open to view the original and traced content side-by-side.

- [See User Code](./6_collage_content/content_collager.py)
- [See Pipeline Spec](./6_collage_content/content_collager.yaml)

```s
pachctl create pipeline -f 6_collage_content/content_collager.yaml
```

### 9. Add Videos and Images 

Now that we have our DAG set up, we can add some videos and images to the `raw_videos_and_images` repo to see the pipeline in action.

#### Videos (Coming Soon)
```s
pachctl put file raw_videos_and_images@master: -f 

```

### Upload Images
```s
pachctl put file raw_videos_and_images@master:liberty.png -f https://raw.githubusercontent.com/pachyderm/docs-content/main/images/opencv/liberty.jpg

pachctl put file raw_videos_and_images@master:robot.png -f https://raw.githubusercontent.com/pachyderm/docs-content/main/images/opencv/robot.jpg
```
