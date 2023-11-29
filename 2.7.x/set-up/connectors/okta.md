---
# metadata # 
title: Okta
description: Learn how to authenticate with Okta.
date: 
# taxonomy #
tags:  ["identity-providers", "permissions", "management", "integrations"]
series:
seriesPart:
weight: 03
---

## Before You Start 

- You must have the following enabled on your cluster:
  - [Enterprise](/{{%release%}}/set-up/enterprise/activate-via-helm)
  - [TLS](/{{%release%}}/set-up/tls) 
- You must have an [Okta](https://okta.com) account
- You should know the value of your [`proxy.host`](/{{%release%}}/manage/helm-values/proxy/) setting in your Helm `values.yaml` file

## How to Enable Okta as an IdP

### 1. Create an App on Okta

1. Log in to Okta.
2. Navigate to **Applications** > **Applications**.
3. Select **Create App Integration**.
4. Choose the **`OIDC - OpenID Connect`** sign-in method.
5. Choose the **`Web Application`** application type.
6. Click **Next**.
7. Name the application, such as **{{% productName %}}**.
8. Navigate to **General Settings** > **Grant Type** and check the following:
      - [x] **Authorization Code**
      - [x] **Refresh Token**
9. Navigate to **Sign-in Redirect URIs** and input the following:
      ```s
      https://<your.proxy.host.value>/dex/callback
      ```
10. Navigate to **Assignments** and select your preferred Controlled Access policy.
11. Click **Save**.

### 2. Define Helm Config

The following steps add the [OIDC](/{{%release%}}/manage/helm-values/oidc/) section to your Helm chart. When an upstream IdP is successfully added to the list, {{%productName%}}'s default [MockIdP](/{{%release%}}/set-up/connectors/mockidp) is disabled automatically. You can add multiple IdPs to `upstreamIDPs`.

1. Navigate to your `values.yamls` file or obtain your current Helm `values.yaml` overrides:
   ```s
   helm get values pachyderm > values.yaml
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
        "id": "okta",
        "name": "Okta",
        "config": {
          "issuer": "https://trial-1839456.okta.com/",
          "clientID": "0oa74mh2scJf29qOD697",
          "clientSecret": "VNwbzOBltNcaotD2CU5iRyTuqOPpwLR-RC16ai7wakta95W00p7X5HYkEgS_5UWH",
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
    id: okta
    name: Okta
    config:
        issuer: https://trial-1839456.okta.com/
        clientID: 0oa74mh2scJf29qOD697
        clientSecret: VNwbzOBltNcaotD2CU5iRyTuqOPpwLR-RC16ai7wakta95W00p7X5HYkEgS_5UWH
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
| `issuer`       | The Okta App's domain URL, found under **Sign On** > **OpenID Connect ID Token**; must have `https://`. |
| `clientID`     | The Okta App's client ID, found under **General** > **Client Credentials**.                    |
| `clientSecret` | The Okta App's client secret, found under **General** > **Client Secrets**.                |
| `redirectURI`  | A combination of your proxy host value and `/dex/callback`. For example, `https://console.pachdemo.com/dex/callback`. |

1. Save your changes and upgrade your cluster:
   ```s
   helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
   ```

{{%notice tip%}}
Alternatively, you can [create a secret](/{{%release%}}/manage/secrets) containing your dex connectors (Key: upstream-idps) and reference its name in the field [oidc.upstreamIDPsSecretName](https://github.com/pachyderm/pachyderm/blob/{{% majorMinorVersion %}}/etc/helm/pachyderm/values.yaml#L805).
{{%/notice%}}

### 3. Login
The users registered with your IdP are now ready to [Log in to {{% productName %}}](/{{%release%}}/get-started/connect-to-existing)

## Troubleshooting 

### PachD CrashLoopBackOff

If you encounter a `CrashLoopBackOff` error after running the `kubectl get pods` command, it's likely that one of the following needs to be fixed:
  - your `issuer` value is incorrect (sometimes it needs a trailing slash `/`, it should match exactly what you see in Okta).
  - you have an unexpected field such as `version` in the config section `oidc.updstreamIDPs entry`. 

**Example Error in PachD Pod logs**

You can obtain your pod logs by running: `kubectl logs <pachd-pod-name> > logs.txt`

```s
create connector with ID: "okta": unable to open connector: failed to get provider: oidc: issuer did not match the issuer returned by provider, expected "https://trial-1839456.okta.com/" got "https://trial-1839456.okta.com"
```

### Okta QR Code / Login Link Doesn't Work

You may need to download the [Okta Verify](https://www.okta.com/integrations/okta-verify/) app on your mobile device and scan the QR code through the app log in.