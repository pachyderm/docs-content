---
# metadata # 
title:  Full Pipeline Specification 
description: View the full pipeline spec file in JSON
date: 
# taxonomy #
tags: ["pipelines", "pps", "pipeline spec"]
series: ["pps"]
seriesPart:
weight: 0
---

```json
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
}```