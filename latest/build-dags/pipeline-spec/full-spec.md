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
  "tf_job": {
    "tf_job": string,
  },
  "transform": {
    "image": string,
    "cmd": [ string ],
    "err_cmd": [ string ],
    "env": {
        string: string
    },
    "secrets": [ {
        "name": string,
        "mount_path": string
    },
    {
        "name": string,
        "env_var": string,
        "key": string
    } ],
    "image_pull_secrets": [ string ],
    "stdin": [ string ],
    "err_stdin": [ string ],
    "accept_return_code": [ int ],
    "debug": bool,
    "user": string,
    "working_dir": string,
    "dockerfile": string,
    "memory_volume": bool,
  },
  "parallelism_spec": {
    "constant": int
  },
  "egress": {
    // Egress to an object store
    "URL": "s3://bucket/dir"
    // Egress to a database
    "sql_database": {
        "url": string,
        "file_format": {
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
  "output_branch": string,
  [
    {
      "worker_id": string,
      "job_id": string,
      "datum_status" : {
        "started": timestamp,
        "data": []
      }
    }
  ],
  "s3_out": bool,
  "resource_requests": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
    }
    "disk": string,
  },
  "resource_limits": {
    "cpu": number,
    "memory": string,
    "gpu": {
      "type": string,
      "number": int
    }
    "disk": string,
  },
  "sidecar_resource_limits": {
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
    "internal_port": int,
    "external_port": int
  },
  "spout": {
    \\ Optionally, you can combine a spout with a service:
    "service": {
      "internal_port": int,
      "external_port": int
    }
  },
  "datum_set_spec": {
    "number": int,
    "size_bytes": int,
    "per_worker": int,
  }
  "datum_timeout": string,
  "job_timeout": string,
  "salt": string,
  "datum_tries": int,
  "scheduling_spec": {
    "node_selector": {string: string},
    "priority_class_name": string
  },
  "pod_spec": string,
  "pod_patch": string,
  "spec_commit": {
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
  "reprocess_spec": string,
  "autoscaling": bool
}

------------------------------------
"pfs" input
------------------------------------

"pfs": {
  "name": string,
  "repo": string,
  "repo_type":string,
  "branch": string,
  "commit":string,
  "glob": string,
  "join_on":string,
  "outer_join": bool,
  "group_by": string,
  "lazy" bool,
  "empty_files": bool,
  "s3": bool,
  "trigger": {
    "branch": string,
    "all": bool,
    "cron_spec": string,
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
      "empty_files": bool,
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
      "empty_files": bool,
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
      "join_on": string,
      "outer_join": bool,
      "lazy": bool,
      "empty_files": bool,
      "s3": bool
    }
  },
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "join_on": string,
      "outer_join": bool,
      "lazy": bool,
      "empty_files": bool,
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
      "group_by": string,
      "lazy": bool,
      "empty_files": bool,
      "s3": bool
    }
  },
  {
    "pfs": {
      "name": string,
      "repo": string,
      "branch": string,
      "glob": string,
      "group_by": string,
      "lazy": bool,
      "empty_files": bool,
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