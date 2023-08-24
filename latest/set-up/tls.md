---
# metadata # 
title: TLS (SSL, HTTPS)
description: Learn how to deploy a cluster with Transport Layer Security (TLS).
date: 
# taxonomy #
tags: ["deployment"]
series:
seriesPart:
weight: 10
directory: true 
--- 

Secure internet browser connections and transactions via data encryption by deploying {{% productName %}} with Transport Layer Security ([TLS](https://cert-manager.io/docs/reference/tls-terminology/)). Once set up, users can access {{% productName %}} through a secure HTTPS connection (e.g., `https://console.yourdomain.com`)


## Before You Start 
- You must have admin control over the domain you wish to use.
- You must obtain a certificate from a trusted Certificate Authority (CA) such as:
  - [Let's Encrypt](https://letsencrypt.org/)
  - [HashiCorp Vault](https://www.vaultproject.io/)
  - [Venafi](https://www.venafi.com/)
- The `.crt` file you are using must contain the full certificate chain (root, intermediates, and leaf) if you are using a custom CA-signed certificate.
---

## How to Deploy with TLS Enabled

There are many ways to set up TLS. The methods listed in this section are the most common.
### Via certbot (Let's Encrypt)

1. Install certbot.
   ```s
   brew install certbot
   ```
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
3. Create a secret (replace `<your.proxy.host.value>`):
   ```s
   kubectl create secret tls pachyderm-tls-secret-001 --cert /etc/letsencrypt/live/<your.proxy.host.value>/fullchain.pem --key /etc/letsencrypt/live/<your.proxy.host.value>/privkey.pem --dry-run=client --output=yaml > pachyderm-tls-secret-001.yaml
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
6. Update the Proxy section of your Helm values.yaml file by updating the host value:
   ```s
   proxy:
      host: <your.proxy.host.value>
   ```
7. Upgrade your Helm chart:
   ```s
   helm upgrade pachyderm pachyderm/pachyderm -f values.yaml
   ```
8. Connect to {{% productName %}} via SSL:
   ```s
   pachctl connect grpcs://<your.proxy.host.value>:443
   ```
### Self-Signed & Custom Certificates

When using self signed certificates or custom certificate authority (instead of Lets Encrypt, HashiCorp Vault, or Venafi), you must set `global.customCaCerts` to `true` to add {{% productName %}}'s certificate and CA to the list of trusted authorities for console and enterprise. 

If you are using a custom ca-signed cert, **you must include the full certificate chain in the root.crt file**.

