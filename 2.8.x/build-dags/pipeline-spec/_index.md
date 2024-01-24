---
# metadata # 
title:  Pipeline Specification (PPS)
description:  Learn about the different attributes of a pipeline spec. 
date: 
# taxonomy #
tags: ["pipeline", "pipelines", "pipeline specification", "pps", "pipeline spec" ]
series:
seriesPart:

weight: 2
---


This document discusses each of the fields present in a pipeline specification.


## Before You Start 
- {{% productName %}}'s pipeline specifications can be written in JSON or YAML.
- {{% productName %}} uses its json parser if the first character is `{`.
- A pipeline specification file can contain multiple pipeline declarations at once.

## Minimal Spec 

Generally speaking, the only attributes that are strictly required for all scenarios are `pipeline.name` and [`transform`](transform). Beyond those, other attributes are conditionally required based on your pipeline's use case. The following are a few examples of common use cases along with their minimally required attributes.

{{< stack type="wizard">}}

{{% wizardRow id="Use Case"%}}
{{% wizardButton option="Cron" state="active" %}}
{{% wizardButton option="Egress (DB)" %}}
{{% wizardButton option="Egress (Storage)" %}}
{{% wizardButton option="Input" %}}
{{% wizardButton option="Service" %}}
{{% wizardButton option="Spout" %}}
{{% wizardButton option="S3" %}}
{{% wizardButton option="Full" %}}

{{% /wizardRow %}}

{{% wizardResults  %}}
{{% wizardResult val1="use-case/cron"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
    "cron": {
      {
          "name": string,
          "spec": string,
          "repo": string,
          "start": time,
          "overwrite": bool
      }
    }
  }
}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/egress-db"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
        "pfs": {
            "repo": "data",
            "glob": "/*"
        }
    },
  "egress": {
      "sqlDatabase": {
          "url": string,
          "fileFormat": {
              "type": string,
              "columns": [string]
          },
          "secret": {
              "name": string,
              "key": "PACHYDERM_SQL_PASSWORD"
          }
      }
    },

}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/egress-storage"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
        "pfs": {
            "repo": "data",
            "glob": "/*"
        }
    },
  "egress": {
      "URL": "s3://bucket/dir"
    },

}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/input"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
        "pfs": {
            "repo": "data",
            "glob": "/*"
        }
    }
}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/service"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
        "pfs": {
            "repo": "data",
            "glob": "/*"
        }
    },
  "service": {
      "internalPort": int,
      "externalPort": int
    },
}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/spout"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "spout": {
  },
}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/s3"%}}
```s
{
  "pipeline": {
    "name": "wordcount",
    "project": {
      "name": "projectName"
    }
  },
  "transform": {
    "image": "wordcount-image",
    "cmd": ["/binary", "/pfs/data", "/pfs/out"]
  },
  "input": {
        "pfs": {
            "repo": "data",
            "glob": "/*"
        }
    },
  "s3Out": true,
}
```
{{% /wizardResult %}}

{{% wizardResult val1="use-case/full" %}}
```s
{
  "pipeline": {
    "name": string,
    "project": {
      "name": "projectName"
    },
  },
  "description": string,
  "metadata": {
    "annotations": {
        "annotation": string
    },
    "labels": {
        "label": string
    }
  },
  "tfJob": {
    "tfJob": string,
  },
  "transform": {
    "image": string,
    "cmd": [ string ],
    "errCmd": [ string ],
    "env": {
        string: string
    },
    "secrets": [ {
        "name": string,
        "mountPath": string
    },
    {
        "name": string,
        "envVar": string,
        "key": string
    } ],
    "imagePullSecrets": [ string ],
    "stdin": [ string ],
    "errStdin": [ string ],
    "acceptReturnCode": [ int ],
    "debug": bool,
    "user": string,
    "workingDir": string,
    "dockerfile": string,
    "memoryVolume": bool,
  },
  "parallelismSpec": {
    "constant": int
  },
  "egress": {
    // Egress to an object store
    "URL": "s3://bucket/dir"
    // Egress to a database
    "sqlDatabase": {
        "url": string,
        "fileFormat": {
            "type": string,
            "columns": [string]
        },
        "secret": {
            "name": string,
            "key": "PACHYDERM_SQL_PASSWORD"
        }
    }
  },
  "update": bool,
  "outputBranch": string,
  [
    {
      "workerId": string,
      "jobId": string,
      "datumStatus" : {
        "started": timestamp,
        "data": []
      }
    }
  ],
  "s3Out": bool,
  "resourceRequests": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
    }
    "disk": string,
  },
  "resourceLimits": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
    }
    "disk": string,
  },
  "sidecarResourceLimits": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
    }
    "disk": string,
  },
  "input": {
    <"pfs", "cross", "union", "join", "group" or "cron" see below>
  },
  "description": string,
  "reprocess": bool,
  "service": {
    "internalPort": int,
    "externalPort": int
  },
  "spout": {
    \\ Optionally, you can combine a spout with a service:
    "service": {
      "internalPort": int,
      "externalPort": int
    }
  },
  "datumSetSpec": {
    "number": int,
    "sizeBytes": int,
    "perWorker": int,
  }
  "datumTimeout": string,
  "jobTimeout": string,
  "salt": string,
  "datumTries": int,
  "schedulingSpec": {
    "nodeSelector": {string: string},
    "priorityClassName": string
  },
  "podSpec": string,
  "podPatch": string,
  "specCommit": {
    "option": false,
    "branch": {
      "option": false,
      "repo": {
        "option": false,
        "name": string,
        "type": string,
        "project":{
          "option": false,
          "name": string,
        },
      },
      "name": string
    },
    "id": string,
  }
  "metadata": {

  },
  "reprocessSpec": string,
  "autoscaling": bool
}

------------------------------------
"pfs" input
------------------------------------

"pfs": {
  "name": string,
  "repo": string,
  "repoType":string,
  "branch": string,
  "commit":string,
  "glob": string,
  "joinOn":string,
  "outerJoin": bool,
  "groupBy": string,
  "lazy" bool,
  "emptyFiles": bool,
  "s3": bool,
  "trigger": {
    "branch": string,
    "all": bool,
    "cronSpec": string,
  },
}

------------------------------------
"cross" or "union" input
------------------------------------

"cross" or "union": [
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "lazy" bool,
      "emptyFiles": bool,
      "s3": bool
    }
  },
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "lazy" bool,
      "emptyFiles": bool,
      "s3": bool
    }
  }
  ...
]


------------------------------------
"join" input
------------------------------------

"join": [
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "joinOn": string,
      "outerJoin": bool,
      "lazy": bool,
      "emptyFiles": bool,
      "s3": bool
    }
  },
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "joinOn": string,
      "outerJoin": bool,
      "lazy": bool,
      "emptyFiles": bool,
      "s3": bool
    }
  }
]


------------------------------------
"group" input
------------------------------------

"group": [
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "groupBy": string,
      "lazy": bool,
      "emptyFiles": bool,
      "s3": bool
    }
  },
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "groupBy": string,
      "lazy": bool,
      "emptyFiles": bool,
      "s3": bool
    }
  }
]



------------------------------------
"cron" input
------------------------------------

"cron": {
    "name": string,
    "spec": string,
    "repo": string,
    "start": time,
    "overwrite": bool
}
```
{{% /wizardResult%}}

{{% /wizardResults %}}

{{</stack>}}

{{% notice note %}}
For a single-page view of all PPS options, go to the [PPS series page](/series/pps).
{{% /notice %}}