---
# metadata # 
title: Auth0
description: Learn how to enable authentication through Auth0 as an Identity Provider.
date: 
# taxonomy #
tags:  ["identity-providers", "permissions", "management", "integrations"]
series:
seriesPart:
weight: 02
---

## Before You Start 

- You must have the following enabled on your cluster:
  - [Enterprise](/{{%release%}}/set-up/enterprise/activate-via-helm)
  - [TLS](/{{%release%}}/set-up/tls) 
- You must have an [Auth0](https://auth0.com) account
- You should know the value of your [`proxy.host`](/{{%release%}}/manage/helm-values/proxy/) setting in your Helm `values.yaml` file


## How to Enable Auth0 as an IdP

{{%notice warning%}}
The following guide does not cover how to create user pools in Auth0; once initially configured, any user with a Gmail account can log in to your {{%productName%}} instance. Refer to the [official Auth0 documentation](https://auth0.com/docs/manage-users/user-accounts/manage-user-access-to-applications) on how to manage users.
{{%/notice%}}

### 1. Create an App on Auth0

1. Log in to your Auth0 account.
2. In **Applications**, click **Create Application**.
3. Type the name of your application, such as **{{%productName%}}**.
4. In the application type, select **Regular Web Application**.
5. Click **Create**.
6. Go to the application settings.
7. Scroll down to **Application URIs**.
8. In the **Allowed Callback URLs**, add the {{%productName%}} callback link in the
   following format:
 ```s
 https://<your.proxy.host.value>/dex/callback
 ```
9. Scroll down to **Show Advanced Settings**.
10.  Select **Grant Types**.
11.  Verify that **Authorization Code** and **Refresh Token** are selected.

   ![Auth0 Grant Settings](/images/auth0-grant-settings.png)

### 2. Define Helm Config

The following steps add the [OIDC](/{{%release%}}/manage/helm-values/oidc/) section to your Helm chart. When an upstream IdP is successfully added to the list, {{%productName%}}'s default [MockIdP](/{{%release%}}/set-up/connectors/mockidp) is disabled automatically. You can add multiple IdPs to `upstreamIDPs`.

1. Navigate to your `values.yamls` file or obtain your current Helm `values.yaml` overrides:
   ```s
   helm get values pachyderm/pachyderm --show-only-overrides > values.yaml
   ```
2. Add the following section:

{{< stack type="wizard" >}}
{{% wizardRow id="Syntax" %}}
 {{% wizardButton option="json" %}}
 {{% wizardButton option="yaml" state="active"%}}
{{% /wizardRow %}}

{{% wizardResults %}}

{{% wizardResult val1="syntax/json" %}}
``` json
{
  "oidc": {
    "upstreamIDPs": [
      {
        "type": "oidc",
        "id": "auth0",
        "name": "Auth0",
        "version": 1,
        "config": {
          "issuer": "https://<auth0.app.domain.url>/",
          "clientID": "FbTzaVdABC9TbX07pXqxHwofuEOux004",
          "clientSecret": "1kbxtx22DLLMNOrjJgV-RaaUsmTzGoQ3h4UEeQ2hmduP1qPLK5yTOsrmwwVNXP9U",
          "redirectURI": "https://<proxy.host.value.com>/dex/callback",
          "insecureEnableGroups": true,
          "insecureSkipEmailVerified": true,
          "insecureSkipIssuerCallbackDomainCheck": false
        }
      }
    ]
  }
}

```
{{% /wizardResult %}}

{{% wizardResult val1="syntax/yaml" %}}

``` yaml
oidc:
  upstreamIDPs:
  - type: oidc
    id: auth0
    name: Auth0
    version: 1
    config:
        issuer: https://<auth0.app.domain.url>/
        clientID: FbTzaVdFCB9TbX07pXqxBwofuEOux004
        clientSecret: 1kbxtx22DLGSULrjJgV-TaaUsmTzGoQ3h4UZeQ2hmduP1qPLK5yTOsrmwwVNXP9U
        redirectURI: https://<proxy.host.value.com>/dex/callback 
        insecureEnableGroups: true
        insecureSkipEmailVerified: true
        insecureSkipIssuerCallbackDomainCheck: false
```
{{% notice note %}}
Note that {{% productName %}}'s YAML format is **a simplified version** of Dex's [sample config](https://dexidp.io/docs/connectors/oidc/).
{{% /notice %}}
{{% /wizardResult %}}


{{% /wizardResults %}}

{{</stack>}}

3. Update the following attributes:
   
| Field          | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| `issuer`       | The Auth0 App's domain URL, found under **Settings** > **Basic Information**; must have `https://` and a trailing slash `/`. |
| `clientID`     | The Auth0 App's client ID, found under **Settings** > **Basic Information**.                    |
| `clientSecret` | The Auth0 App's client secret, found under **Settings** > **Basic Information**.                |
| `redirectURI`  | A combination of your proxy host value and `/dex/callback`. For example, `https://console.pachdemo.com/dex/callback`. |

4. Save your changes and upgrade your cluster:
   ```s
   helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
   ```

{{%notice tip%}}

Alternatively, you can [create a secret](/{{%release%}}/manage/secrets) containing your dex connectors (Key: upstream-idps) and reference its name in the field [oidc.upstreamIDPsSecretName](https://github.com/pachyderm/pachyderm/blob/{{% majorMinorVersion %}}/etc/helm/pachyderm/values.yaml#L805).

{{%/notice%}}
 
### 3. Login
The users registered with your IdP are now ready to [Log in to {{% productName %}}](/{{%release%}}/get-started/connect-to-existing)

