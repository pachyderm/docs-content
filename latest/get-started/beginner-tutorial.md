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

{{< figure src="/images/beginner-tutorial/step-6.svg" class="figure">}}

### 1. Create a Project 

By default, when you first start up an instance, the `default` project is attached to your active context. Create a new project and set the project to your active PachCTL context to avoid having to specify the project name (e.g., `--project video-to-frame-traces`) in each command. 

```s
pachctl create project video-to-frame-traces
pachctl config update context --project video-to-frame-traces
pachctl list projects
```

{{%notice tip%}}
If you are using {{%productName%}} locally, you can view your project in Console and follow along at [http://localhost/lineage/video-to-frame-traces](http://localhost/lineage/video-to-frame-traces)
{{%/notice %}}

### 2. Create an Input Repo 

At the top of our DAG, we'll need an input repo that will store our raw videos and images. 
   
```s
pachctl create repo raw_videos_and_images
pachctl list repos
```

<!-- ![input-repo](/images/beginner-tutorial/input-repo.svg) -->



### 3. Create the Video Converter Pipeline 

We want to make sure that our DAG can handle videos in multiple formats, so first we'll create a pipeline that will:
- Skip images 
- Skip videos already in the correct format (`.mp4`)
- Convert videos to `.mp4` format

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

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-1.svg" class="figure">}}
{{% /wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# video_mp4_converter.py
import cv2
import pathlib
import os
import argparse
import shutil

def video_to_mp4(
    input, output, fps: int = 0, frame_size: tuple = (), fourcc: str = "XVID"
):

    print(f"Converting video: {input}")
    vidcap = cv2.VideoCapture(input)
    if not fps:
        fps = round(vidcap.get(cv2.CAP_PROP_FPS))
    success, arr = vidcap.read()
    if not frame_size:
        height, width, _ = arr.shape
        frame_size = width, height
    writer = cv2.VideoWriter(
        output,
        apiPreference=0,
        fourcc=cv2.VideoWriter_fourcc(*fourcc),
        fps=fps,
        frameSize=frame_size,
    )
    frame_count = 0
    while success:
        frame_count += 1
        writer.write(arr)
        success, arr = vidcap.read()
    writer.release()
    vidcap.release()

    print(f"Converted {frame_count} frames")


def process_video_files(input_path, output_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip non-video files
            if not file_path.lower().endswith(('.mp4', '.avi', '.mov')):
                print(f"Skipping: {file_path}")
                return

            # Convert video files to MP4
            if file_path.lower().endswith(('.avi', '.mov')):
                base_file = os.path.splitext(file)[0]
                out_path = os.path.join(output_path, base_file + ".mp4")
                video_to_mp4(file_path, output=out_path)
                print(f"Converted: {file} to {out_path}")
                
            else:
                # Copy existing MP4 files
                out_path = os.path.join(output_path, file)
                print(f"Copying: {file} to {out_path}")
                shutil.copy(file_path, out_path)


def main():
    parser = argparse.ArgumentParser(
        prog='convert_to_mp4.py',
        description='Convert non-MP4 videos to MP4'
    )
    parser.add_argument('-i', '--input', required=True, help='Input video directory')
    parser.add_argument('-o', '--output', required=True, help='Output video directory')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input directory does not exist.")
        return
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    process_video_files(args.input, args.output)


if __name__ == "__main__":
    main()

```
{{% /wizardResult%}}
{{% /wizardResults%}}
{{</stack>}}


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

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-2.svg" class="figure">}}
{{%/wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# image_flattener.py
import cv2
import os
import argparse
import pathlib

def flatten_video(vid_path, out_path, base_file):
    os.makedirs(out_path, exist_ok=True)

    current_frame = 0
    video = cv2.VideoCapture(vid_path)

    while True:
        ret, frame = video.read()

        if ret:
            name = os.path.join(out_path, f'{base_file}-frame-{current_frame:010d}.jpg')
            cv2.imwrite(name, frame)
            current_frame += 1
        else:
            break

    video.release()

def process_video_files(input_path, output_path):
    for root, _, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)

            if pathlib.Path(file_path).suffix.lower() == '.mp4':
                base_file = os.path.splitext(file)[0]
                out_path = os.path.join(output_path, base_file)
                print(f"Converting: {file}")
                flatten_video(file_path, out_path, base_file)
            else:
                print(f"Skipping: {file_path}")

def main():
    parser = argparse.ArgumentParser(
        prog='flatten_to_images.py',
        description='Flatten Video to Images'
    )
    parser.add_argument('-i', '--input', required=True, help='Input video directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input directory does not exist.")
        return
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    process_video_files(args.input, args.output)

if __name__ == "__main__":
    main()
```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}

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

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-3.svg" class="figure">}}
{{%/wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# image_tracer.py
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import argparse

def make_edges(image, input_path, output_path):
    try:
        img = cv2.imread(image)
        if img is None:
            print(f"Error reading image: {image}")
            return
        
        tail = os.path.split(image)[1]
        subdirectory = os.path.relpath(os.path.dirname(image), input_path)
        output_subdir = os.path.join(output_path, subdirectory)
        os.makedirs(output_subdir, exist_ok=True)
        
        edges = cv2.Canny(img, 100, 200)
        output_filename = os.path.splitext(tail)[0] + '_edges.png'
        output_filepath = os.path.join(output_subdir, output_filename)
        plt.imsave(output_filepath, edges, cmap='gray')
        print(f"Processed: {image} -> {output_filepath}")

    except Exception as e:
        print(f"Error processing image: {image}")
        print(f"Error details: {e}")

def process_image_files(input_path, output_path):
    for dirpath, dirs, files in os.walk(input_path):
        total = len(files)
        current = 0
        for file in files:                
            current += 1
            print(f"Processing {file}, #{current} of {total}")
            make_edges(os.path.join(dirpath, file), input_path, output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='image_tracer.py',
        description='Trace Images'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    for input_path in args.input:
        if not os.path.exists(input_path):
            print(f"Input directory does not exist: {input_path}")
        else:
            print(f"Processing images in: {input_path}")
            process_image_files(input_path, args.output)
    
    print("Done.")
    return

if __name__ == "__main__":
    main()
```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}

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

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-4.svg" class="figure">}}
{{%/wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# movie_gifer.py
import cv2
import os
import argparse
import imageio

def make_gifs(directory, input_path, output_path):
    try:
    
        # Create output folder if it doesn't exist
        relative_dir = os.path.relpath(directory, input_path)
        output_folder = os.path.join(output_path, relative_dir)
        os.makedirs(output_folder, exist_ok=True)

        # Get all the images in the provided directory
        images = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]

        # Sort the pngs so they are in order
        images.sort()

        # Create the output filename
        tail = os.path.split(directory)[1]
        base_filename = os.path.splitext(tail)[0]

        if 'tracer' in input_path:
           suffix = 'edges'
        else:
            suffix = 'original'
        output_filename = f'{base_filename}_{suffix}.gif'
        output_filepath = os.path.join(output_folder, output_filename)

        # Create the gif
        gif_images = [cv2.imread(i)[:, :, ::-1] for i in images]  # Convert BGR to RGB
        imageio.mimsave(output_filepath, gif_images, duration=0.1)

        print(f"Processed: {directory} -> {output_filepath}")

    except Exception as e:
        print(f"Error processing directory: {directory}")
        print(f"Error details: {e}")

def process_image_directories(input_path, output_path):
    # For each directory of images, make a gif
    for dirpath, dirs, files in os.walk(input_path):
        total = len(dirs)
        current = 0
        for dir in dirs:
            current += 1
            print(f"Processing {dir}, #{current} of {total}")
            make_gifs(os.path.join(dirpath, dir), input_path, output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='movie_gifer.py',
        description='Convert images to gifs'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print("======================")

    for input_path in args.input:
        if not os.path.exists(input_path):
            print(f"Input directory does not exist: {input_path}")
        else:
            print(f"Processing images in: {input_path}")
            process_image_directories(input_path, args.output)

    print("Done.")

if __name__ == "__main__":
    main()

```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}

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

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-5.svg" class="figure">}}
{{%/wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# content_shuffler.py
import argparse
import os
import shutil

def shuffle_content(input_path, output_path):
    # create an originals and edges directory in the output path
    originals_output_path = f"{output_path}/originals"
    if not os.path.exists(originals_output_path):
        os.makedirs(originals_output_path)

    edges_output_path = f"{output_path}/edges"
    if not os.path.exists(edges_output_path):
        os.makedirs(edges_output_path)

    for dirpath, dirs, files in os.walk(input_path):
        for file in files:
            if "frame" and "edges" not in file:
                # Copy the original image to the originals directory
                shutil.copy(f"{dirpath}/{file}", originals_output_path)
            elif "frame" not in file and "edges" in file:
                # Copy the images and gifs to the edges directory
                shutil.copy(f"{dirpath}/{file}", edges_output_path)

def main():
    parser = argparse.ArgumentParser(
        prog='content_collager.py',
        description='Convert images and gifs into a collage'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input} \nOutput: {args.output}\n")

    total_inputs = len(args.input)
    current_input = 0
    for input_path in args.input:
        try:
            current_input += 1
            print(f"{input_path}; {current_input}/{total_inputs}")
            shuffle_content(input_path, args.output)
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    main()

```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}

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
EOF
```

```s
pachctl create pipeline -f content_collager.yaml
```

{{<stack type="wizard">}}
{{% wizardRow id="view" %}}
{{% wizardButton option="Diagram" state="active" %}}
{{% wizardButton option="User Code" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="view/diagram" %}}
{{< figure src="/images/beginner-tutorial/step-6.svg" class="figure">}}
{{%/wizardResult%}}
{{% wizardResult val1="view/user-code" %}}
```s
# content_collager.py
import os
import argparse
from bs4 import BeautifulSoup
import shutil

html_template = """
<html>
<head>
<title>Content Collage</title>
<style>
  #collage-container {
    display: flex;
  }

  #originals,
  #edges {
    flex: 1;
    padding: 20px;
    border: 1px solid #ccc;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px; 
  }
</style>
</head>
<body>
<h1>Content collage</h1>
<div id="collage-container">
<div id="originals">
<h2>Original</h2>
</div>
<div id="edges">
<h2>Edges</h2>
</div>
</div>
</body>
</html>
"""

def create_html_page(output_path):
    index_path = os.path.join(output_path, "collage", "index.html")
    
    if not os.path.exists(os.path.join(output_path, "collage")):
        os.makedirs(os.path.join(output_path, "collage"))

    if not os.path.exists(index_path):
        with open(index_path, "w") as f:
            f.write(html_template)

def append_image_to_html_page(output_path, image_path):
    index_path = os.path.join(output_path, "collage", "index.html")

    with open(index_path, "r") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    # if the image path has the word "originals" in it, add it to the originals div
    if "edges" in image_path:
        originals_div = soup.find("div", id="edges")
        if originals_div:
            img_tag = soup.new_tag("img", src=image_path, width="300", style="display: block;")
            originals_div.append(img_tag)

        with open(index_path, "w") as f:
            f.write(str(soup))
    # otherwise, add it to the collage div
    else:
        collage_div = soup.find("div", id="originals")
        if collage_div:
            img_tag = soup.new_tag("img", src=image_path, width="300", style="display: block;")
            collage_div.append(img_tag)

        with open(index_path, "w") as f:
            f.write(str(soup))

def process_content(input_path, output_path):
    try:
        # Create the HTML page
        create_html_page(output_path)

        # Create the output directory /collage/static
        static_output_path = os.path.join(output_path, "collage", "static")
        if not os.path.exists(static_output_path):
            os.makedirs(static_output_path)

        for dirpath, _, files in os.walk(input_path):
            sorted_files = sorted(files)
            for file in sorted_files:
                print(f"Copying {file} to {static_output_path}")
                shutil.copy(os.path.join(dirpath, file), os.path.join(static_output_path, file))
                append_image_to_html_page(output_path, f"./static/{file}")

    except Exception as e:
        print(f"Exception: {e}")

def main():
    parser = argparse.ArgumentParser(
        prog='content_collager.py',
        description='Convert images and gifs into a collage'
    )
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input image directory')
    parser.add_argument('-o', '--output', required=True, help='Output image directory')
    args = parser.parse_args()

    print(f"Input: {args.input} \nOutput: {args.output}\n")

    try:
        process_content(args.input[0], args.output)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()

```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}


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

{{< figure src="/images/beginner-tutorial/active-pipeline.svg" class="figure">}}

## 10. Download & View the Collage

1. Navigate to your project in Console.
2. Click on the `content_collager` pipeline's **output** directory.
3. Click **Inspect Commit**.
4. Check the [x] collage directory.
5. Select the **Download** button.

{{< figure src="/images/beginner-tutorial/view-collage.gif" class="figure">}}
