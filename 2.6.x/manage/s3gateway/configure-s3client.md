---
# metadata # 
title: Credentials
description: Learn how to configure an S3 client.
date: 
# taxonomy #
tags: 
series:
seriesPart:
--- 

## Before You Start 

- You must configure an S3 Client (Boto3, AWS, MinIO)
- You must have [authentication](/{{%release%}}/set-up/connectors/) enabled.


## How to Set Your Credentials

{{<stack type="wizard">}}

{{% wizardRow id="Auth"%}}
{{% wizardButton option="Enabled" state="active" %}}
{{% wizardButton option="Disabled" %}}
{{% /wizardRow %}}

{{% wizardResults %}}
{{% wizardResult val1="auth/enabled" %}}

1. Run the following command: 

```s
more ~/.pachyderm/config.json
```
2. Search for your session token: `"session_token": "your-session-token-value"`.
3. Make sure to fill both fields `Access Key ID` and `Secret Access Key` with that same value.

```s
AWS_ACCESS_KEY_ID="somevalue" AWS_SECRET_ACCESS_KEY="somevalue" aws --endpoint-url http://pach-address s3 ls s3://branch.repo.project
```

{{% /wizardResult %}}

{{% wizardResult val1="auth/disabled" %}}
You must set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to any matching, non-empty string. 

For example, you could set both values to `"x"`. 

```s
AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=x aws --endpoint-url http://pach-address s3 ls s3://branch.repo.project
```

{{% /wizardResult %}}

{{% /wizardResults %}}

{{</stack>}}

## Robot Users
Depending on your use case, it might make sense to pass the credentials of a robot-user or another type of user altogether. Refer to the [RBAC](/{{%release%}}/set-up/rbac) for more information.

