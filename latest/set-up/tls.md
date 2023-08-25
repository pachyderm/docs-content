---
# metadata # 
title: TLS (SSL, HTTPS)
description: Learn how to deploy a cluster with Transport Layer Security (TLS).
date: 
# taxonomy #
tags: ["deployment", "TLS", "SSL", "HTTPS", "security","authentication","authorization","enterprise"]
series:
seriesPart:
weight: 10
directory: true 
--- 

Secure internet browser connections and transactions via data encryption by deploying {{% productName %}} with Transport Layer Security ([TLS](https://cert-manager.io/docs/reference/tls-terminology/)). Once set up, users can access {{% productName %}} through a secure HTTPS connection (e.g., `https://console.yourdomain.com`)


## Before You Start 

- You must have admin control over the domain you wish to use
- You must have already set up a subdomain for your {{% productName %}} cluster (e.g., `console.yourdomain.com`)
- You must have added the subdomain to the `proxy.host` value in your Helm `values.yaml` file

### About DNS Records
You will need to access your domain's DNS records to complete the setup. For example, if you are deploying {{% productName %}} in GCP, you will need to navigate to the Networking section of your GCP project. If your domain is registered with a third-party provider (e.g., Cloudflare), you will also need to log in to your account with that provider as well to register the subdomain with an `NS` record that matches the values of your subdomain's `NS` record in GCP.

The following guide assumes that you already have the following DNS records set up for your subdomain:

|Record Type|Example DNS Name|Value|
|-|-|-|
|`A`|`console.yourdomain.com.`| `<pachyderm.proxy.external.ip>`|
|`NS`|`console.yourdomain.com.`| auto generated; do not edit |
|`SOA`|`console.yourdomain.com.`| auto generated; do not edit |

{{%notice tip%}}
 You can use [Google's Dig tool](https://toolbox.googleapps.com/apps/dig/) to verify that records are accessible.
{{%/notice%}}
---

## How to Deploy with TLS Enabled


At a high level, you need to do all of the following to enable TLS:

1. Create a signed certificate (obtainable from any CA, such as [Let's Encrypt](https://letsencrypt.org/), [HashiCorp Vault](https://www.vaultproject.io/), or [Venafi](https://www.venafi.com/)).
2. Create a Kubernetes secret with the certificate.
3. Configure the TLS section of your Helm `values.yaml` file by enabling TLS and specifying the secret name.
4. Upgrade your Cluster.
5. Connect using `pachctl connect grpcs://<your.proxy.host.value>:443`.

{{%notice note%}}
When using custom CA-signed certs (instead of certs from Let's Encrypt, HashiCorp Vault, or Venafi) the `.crt` must include the full certificate chain (root, intermediates, and leaf). You must also set `global.customCaCerts` to `true` in the Helm `values.yaml` file.
{{%/notice%}}

### Via certbot (Let's Encrypt)

The following steps are just one example of how to obtain a signed certificate from Let's Encrypt.

1. Install [certbot](https://certbot.eff.org/).

{{< stack type="wizard" >}}
{{% wizardRow id="Options" %}}
 {{% wizardButton option="Mac" state="active" %}}
 {{% wizardButton option="Linux" %}}
{{% /wizardRow %}}
{{% wizardResults %}}
{{% wizardResult val1="options/mac" %}}
   ```s
   brew install certbot
   ```
{{%/wizardResult%}}
{{% wizardResult val1="options/linux" %}}
   ```s
   sudo snap install --classic certbot
   sudo ln -s /snap/bin/certbot /usr/bin/certbot
   ```
{{%/wizardResult%}}
{{%/wizardResults%}}
{{</stack>}}

2. Run the following command (replace `<your@email.address>` and `<your.proxy.host.value>`):
   ```s
   certbot certonly --manual -v \
    --preferred-challenges=dns \
    --email <your@email.address> \
    --server https://acme-v02.api.letsencrypt.org/directory \
    --agree-tos \
    --manual-public-ip-logging-ok \
    -d <your.proxy.host.value>
   ```

   You will be asked to fill out some identifying information. When prompted, create a TXT record with your DNS provider. The TXT record will look something like this:
   ```s
   _acme-challenge.<your.proxy.host.value>. IN TXT "<random-string>"
   ```
   Once you have created the TXT record, press `Enter` to continue in the terminal. If the TXT record is not created and accessible, the command will fail.

3. Create a secret (replace `<your.proxy.host.value>`):
   ```s
   kubectl create secret tls pachyderm-tls-secret-001 \
    --cert /etc/letsencrypt/live/<your.proxy.host.value>/fullchain.pem \
    --key /etc/letsencrypt/live/<your.proxy.host.value>/privkey.pem \
    --dry-run=client \
    --output=yaml > pachyderm-tls-secret-001.yaml
   ```
4. Apply the secret:
   ```s
   kubectl apply -f pachyderm-tls-secret-001.yaml
   ```
5. Configure the TLS section of your Helm values.yaml file by enabling TLS and specifying the secret name:
   ```s
   tls: 
      enabled: true
      secretName: pachyderm-tls-secret-001
   ```
   
6. Upgrade your Helm chart:
   ```s
   helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
   ```
7. Connect to {{% productName %}} via SSL:
   ```s
   pachctl connect grpcs://<your.proxy.host.value>:443
   ```

That's it! You can now consider setting up [Authentication](/{{%release%}}/set-up/connectors) to take advantage of our [Authorization (RBAC) system](/{{%release%}}/set-up/authorization).

## Troubleshooting

### Can't Connect to Console Through Subdomain

It's possible that the external IP address of your cluster has changed during a Helm upgrade. To check, run the following command:
```s
kubectl get service pachyderm-proxy -o wide | grep pachyderm-proxy | awk '{print $4}'
```

If that IP address does not match the IP address found in your `A` DNS record, you will need to update your DNS records to point to the new IP address.
