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
- Try out this [Glob Tool](https://www.digitalocean.com/community/tools/glob) to learn how to use glob patterns to select files and directories.

### Context

### How {{%productName%}} Works

{{% productName %}} deploys a Kubernetes cluster to manage and version your data using [projects](/{{%release%}}/learn/glossary/project), [input repositories](/{{%release%}}/learn/glossary/input-repo), [pipelines](/{{%release%}}/learn/glossary/pipeline), [datums](/{{%release%}}/build-dags/datum-operations) and [output repositories](/{{%release%}}/learn/glossary/output-repo). A project can house many repositories and pipelines, and when a pipeline runs a data transformation [job](/{{%release%}}/learn/glossary/job/) it chunks your inputs into datums for processing. The number of datums is determined by the [glob pattern](/{{%release%}}/learn/glossary/glob-pattern/) defined in your [pipeline specification](/{{%release%}}/learn/glossary/pipeline-specification/); if the shape of your glob pattern encompasses all inputs, it it will process one datum; if the shape of your glob pattern encompasses each input individually, it will process one datum per file in the input, and so on.  

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

<!-- ![input-repo](/images/beginner-tutorial/input-repo.svg) -->



### 3. Create the Video Converter Pipeline 

We want to make sure that our DAG can handle videos in multiple formats, so first we'll create a pipeline that will:
- skip images 
- skip videos already in the correct format (`.mp4`)
- convert videos to `.mp4` format

The converted videos will be made available to the next pipeline in the DAG via the `video_mp4_converter` repo by declaring in the user code to save all converted images to `/pfs/out/`. This is the standard location for storing output data so that it can be accessed by the next pipeline in the DAG.

1. Open your IDE terminal.
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

{{< figure src="/images/beginner-tutorial/step-1.svg" class="figure">}}

{{% notice info %}}
Every pipeline, at minimum, needs a `name`, an `input`, and a `transform`. The input is the data that the pipeline will process, and the transform is the user code that will process the data. `transform.image` is the Docker image available in a container registry ([Docker Hub](https://hub.docker.com/)) that will be used to run the user code. `transform.cmd` is the command that will be run inside the Docker container; it is the entrypoint for the user code to be executed against the input data.
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

{{< figure src="/images/beginner-tutorial/step-2.svg" class="figure">}}

### 5. Create the Image Tracing Pipeline: 

Up until this point, we've used a simple single input from the Pachyderm file system (`input.pfs`) and a basic [glob pattern](/{{%release%}}/learn/glossary/glob-pattern/) (`/*`) to specify shape of our datums. This particular pattern treats each top-level file and directory as a single datum. However, in this pipeline, we have some special requirements:

- We want to process *only* the raw images from the `raw_videos_and_images` repo
- We want to process *all* of the flattened video frame images from the `image_flattener` pipeline

To achieve this, we're going to need to use a [union input](/{{%release%}}/build-dags/pipeline-spec/input-union/) (`input.union`) to combine the two inputs into a single input for the pipeline. 

- For the `raw_videos_and_images` input, we can use a more powerful glob pattern to ensure that only image files are processed (`/*.{png,jpg,jpeg}`)
- For the `image_flattener` input, we can use the same glob pattern as before (`/*`) to ensure that each video's collection of frames is processed together

Notice how we also update the `transform.cmd` to accommodate having two inputs.

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

{{< figure src="/images/beginner-tutorial/step-3.svg" class="figure">}}

### 6. Create the Gif Pipeline

Next, we'll create a pipeline that will create two gifs:
  1. A gif of the original video's flattened frames (from the `image_flattener` output repo)
  2. A gif of the video's traced frames (from the `image_tracer` output repo)

To make a gif of both the original video frames and the traced frames, we're going to again need to use a union input so that we can process the `image_flattener` and `image_tracer` output repos.

Notice that the glob pattern has changed; here, we want to treat each directory in an input as a single datum, so we use the glob pattern `/*/`. This is because we've declared in the user code to store the video frames in a directory with the same name as the video file.

```s
cat <<EOF > movie_gifer.yaml
pipeline:
  name: movie_gifer
description: A pipeline that converts frames into a gif using the OpenCV library.
input:
  union:
    - pfs:
        repo: image_flattener
        glob: "/*/"
    - pfs:
        repo: image_tracer
        glob: "/*/"
transform:
  image: lbliii/movie_gifer:1.0.5
  cmd:
    - python3
    - /movie_gifer.py
    - --input
    - /pfs/image_flattener
    - /pfs/image_tracer
    - --output
    - /pfs/out/
autoscaling: true
EOF
```

```s
pachctl create pipeline -f movie_gifer.yaml
```

### 7. Create the Content Shuffler Pipeline

We have everything we need to make the comparison collage, but before we do that we need to re-shuffle the content so that the original images and gifs are in one directory (`originals`) and the traced images and gifs are in another directory (`edges`). This will help us more easily process the data via our user code for the collage. This is a common step you will encounter while using {{%productName%}} referred to as a *shuffle pipeline*.

```s
cat <<EOF > content_shuffler.yaml
pipeline:
  name: content_shuffler
  description: A pipeline that collapses our inputs into one datum for the collager.
input:
  union:
    - pfs:
        repo: movie_gifer
        glob: "/"
    - pfs:
        repo: raw_videos_and_images
        glob: "/*.{png,jpg,jpeg}"
    - pfs:
        repo: image_tracer
        glob: "/*.{png,jpg,jpeg}"

transform:
  image: lbliii/content_shuffler:1.0.0
  cmd:
    - python3
    - /content_shuffler.py
    - --input
    - /pfs/movie_gifer
    - /pfs/raw_videos_and_images
    - /pfs/image_tracer
    - --output
    - /pfs/out/
autoscaling: true
EOF
```

```s
pachctl create pipeline -f content_shuffler.yaml
```

### 8. Create the Content Collager Pipeline

Finally, we'll create a pipeline that produces a static html page for viewing the original and traced content side-by-side.

```s
cat <<EOF > content_collager.yaml
pipeline:
  name: content_collager
  description: A pipeline that creates a static HTML collage.
input:
  pfs:
    glob: "/"
    repo: content_shuffler


transform:
  image: lbliii/content_collager:1.0.64
  cmd:
    - python3
    - /content_collager.py
    - --input
    - /pfs/content_shuffler
    - --output
    - /pfs/out/
autoscaling: true
```

```s
pachctl create pipeline -f content_collager.yaml
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
