---
# metadata # 
title:  pachctl run cron
description: "Run an existing {{%productName%}} cron pipeline now"
date:  2022-10-14T09:34:42-04:00
tags:
  - run
cliGlossary:  r
---

### Synopsis

Run an existing {{%productName%}} cron pipeline now

```
pachctl run cron <pipeline> [flags]
```

### Examples

```

		# Run a cron pipeline "clock" now
		$ pachctl run cron clock
```

### Options

```
  -h, --help             help for cron
      --project string   Project containing pipeline.
```

### Inherited Options

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

