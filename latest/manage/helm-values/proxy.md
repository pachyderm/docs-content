---
# metadata # 
title:  Proxy HCVs
description: Centralize all traffic on a single port that's safe to expose to the Internet. 
date: 
# taxonomy #
tags: ["helm"]
series: ["helm"]
seriesPart:
weight: 14
label: required 
--- 

## About

Proxy is a service that handles all {{% productName %}} traffic (S3, Console, OIDC, Dex, GRPC) on a single port; It's great for exposing you cluster directly to the Internet. 

## Values

```s
proxy:
  # If enabled, create a proxy deployment (based on the Envoy proxy) and a service to expose it.  If
  # ingress is also enabled, any Ingress traffic will be routed through the proxy before being sent
  # to pachd or Console.
  enabled: true
  # The external hostname (including port if nonstandard) that the proxy will be reachable at.
  # If you have ingress enabled and an ingress hostname defined, the proxy will use that.
  # Ingress will be deprecated in the future so configuring the proxy host instead is recommended.
  host: ""
  # The number of proxy replicas to run.  1 should be fine, but if you want more for higher
  # availability, that's perfectly reasonable.  Each replica can handle 50,000 concurrent
  # connections.  There is an affinity rule to prefer scheduling the proxy pods on the same node as
  # pachd, so a number here that matches the number of pachd replicas is a fine configuration.
  # (Note that we don't guarantee to keep the proxy<->pachd traffic on-node or even in-region.)
  replicas: 1
  # The envoy image to pull.
  image:
    repository: "envoyproxy/envoy-distroless"
    tag: "v1.27.1"
    pullPolicy: "IfNotPresent"
  # Set up resources.  The proxy is configured to shed traffic before using 500MB of RAM, so that's
  # a resonable memory limit.  It doesn't need much CPU.
  resources:
    requests:
      cpu: 100m
      memory: 512Mi
    limits:
      memory: 512Mi
  # Any additional labels to add to the pods.  These are also added to the deployment and service
  # selectors.
  labels: {}
  # Any additional annotations to add to the pods.
  annotations: {}
  # A nodeSelector statement for each pod in the proxy Deployment, if desired.
  nodeSelector: {}
  # A tolerations statement for each pod in the proxy Deployment, if desired.
  tolerations: []
  # A priority class name for each pod in the proxy Deployment, if desired.
  priorityClassName: ""
  # Configure the service that routes traffic to the proxy.
  service:
    # The type of service can be ClusterIP, NodePort, or LoadBalancer.
    type: ClusterIP
    # If the service is a LoadBalancer, you can specify the IP address to use.
    loadBalancerIP: ""
    # The port to serve plain HTTP traffic on.
    httpPort: 80
    # The port to serve HTTPS traffic on, if enabled below.
    httpsPort: 443
    # If the service is a NodePort, you can specify the port to receive HTTP traffic on.
    httpNodePort: 30080
    httpsNodePort: 30443
    # Any additional annotations to add.
    annotations: {}
    # Any additional labels to add to the service itself (not the selector!).
    labels: {}
    # The proxy can also serve each backend service on a numbered port, and will do so for any port
    # not numbered 0 here.  If this service is of type NodePort, the port numbers here will be used
    # for the node port, and will need to be in the node port range.
    legacyPorts:
      console: 0 # legacy 30080, conflicts with default httpNodePort
      grpc: 0 # legacy 30650
      s3Gateway: 0 # legacy 30600
      oidc: 0 # legacy 30657
      identity: 0 # legacy 30658
      metrics: 0 # legacy 30656
    # externalTrafficPolicy determines cluster-wide routing policy; see "kubectl explain
    # service.spec.externalTrafficPolicy".
    externalTrafficPolicy: ""
  # Configuration for TLS (SSL, HTTPS).
  tls:
    # If true, enable TLS serving.  Enabling TLS is incompatible with support for legacy ports (you
    # can't get a generally-trusted certificate for port numbers), and disables support for
    # cleartext communication (cleartext requests will redirect to the secure server, and HSTS
    # headers are set to prevent downgrade attacks).
    #
    # Note that if you are planning on putting the proxy behind an ingress controller, you probably
    # want to configure TLS for the ingress controller, not the proxy.  This is intended for the
    # case where the proxy is exposed directly to the Internet.  (It is possible to have your
    # ingress controller talk to the proxy over TLS, in which case, it's fine to enable TLS here in
    # addition to in the ingress section above.)
    enabled: false
    # The secret containing "tls.key" and "tls.crt" keys that contain PEM-encoded private key and
    # certificate material.  Generate one with "kubectl create secret tls <name> --key=tls.key
    # --cert=tls.cert".  This format is compatible with the secrets produced by cert-manager, and
    # the proxy will pick up new data when cert-manager rotates the certificate.
    secretName: ""
    # If set, generate the secret from values here.  This is intended only for unit tests.
    secret: {}
preflightCheckJob:
  # If true, install a Kubernetes job that runs preflight checks from the configured Pachyderm
  # release.
  enabled: false

  # The version to preflight.  It is totally fine if this is newer than the currently-running pachd
  # version.
  image:
    repository: "pachyderm/pachd"
    pullPolicy: "IfNotPresent"
    tag: ""

  # misc k8s settings
  affinity: {}
  annotations: {}
  resources:
    {}
    #limits:
    #  cpu: "1"
    #  memory: "2G"
    #requests:
    #  cpu: "1"
    #  memory: "2G"
  priorityClassName: ""
  podLabels: {}
  nodeSelector: {}
  tolerations: []

  # logging settings
  sqlQueryLogs: false
  disableLogSampling: false
```