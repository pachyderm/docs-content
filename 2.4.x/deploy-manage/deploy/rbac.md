---
# metadata # 
title:  RBAC
description: Learn how our platform supports Kubernetes' Role-Base Access Controls (RBAC).
date: 
# taxonomy #
tags: ["configuration", "permissions"]
series:
seriesPart:
--- 

{{%productName%}} has support for Kubernetes Role-Based Access
Controls (RBAC), which is a default part of all
{{%productName%}} deployments. In most use cases, {{%productName%}}
sets all the RBAC permissions automatically. However,
if you are deploying {{%productName%}} on a cluster that your
company owns, security policies might not allow certain
RBAC permissions by default. Therefore, you need to
contact your Kubernetes administrator and provide the
following list of required permissions:

```s
Rules: []rbacv1.PolicyRule{{
		APIGroups: []string{""},
		Verbs:     []string{"get", "list", "watch"},
		Resources: []string{"nodes", "pods", "pods/log", "endpoints"},
		}, {
		APIGroups: []string{""},
		Verbs:     []string{"get", "list", "watch", "create", "update", "delete"},
		Resources: []string{"replicationcontrollers", "services"},
		}, {
		APIGroups:     []string{""},
		Verbs:         []string{"get", "list", "watch", "create", "update", "delete"},
		Resources:     []string{"secrets"},
		ResourceNames: []string{client.StorageSecretName},
		}},
```

The following table explains how {{%productName%}} uses those permissions:

| Permission       | Description   |
| ---------------- | ------------- |
| Access to nodes    | Used for metrics reporting, disabling should not affect {{%productName%}}'s operation. |
| Access to pods, replica controllers, and services | {{%productName%}} uses this permission to monitor the created pipelines. The permissions related to `replicationcontrollers` and `services` are used in the setup and deletion of pipelines. Each pipeline has its own RC and service in addition to the pods.
| Access to secrets | Required to give various kinds of credentials to pipelines, including storage credentials to access S3 or other object storage backends, Docker credentials to pull from a private registry, and others. |

## RBAC and DNS

In older Kubernetes versions, `kube-dns` did not work properly with RBAC.
To check if your cluster is affected by this issue, run:

```s
kubectl get all --namespace=kube-system
```

**System response:**

```s
NAME              DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/kube-dns   1         1         1            0           3m

NAME                     DESIRED   CURRENT   READY     AGE
rs/kube-dns-86f6f55dd5   1         1         0         3m

NAME                            READY     STATUS    RESTARTS   AGE
po/kube-addon-manager-oryx      1/1       Running   0          3m
po/kube-dns-86f6f55dd5-xksnb    2/3       Running   4          3m
po/kubernetes-console-bzjjh     1/1       Running   0          3m
po/storage-provisioner          1/1       Running   0          3m

NAME                      DESIRED   CURRENT   READY     AGE
rc/kubernetes-console   1         1         1         3m

NAME                       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)         AGE
svc/kube-dns               ClusterIP   10.96.0.10     <none>        53/UDP,53/TCP   3m
svc/kubernetes-console     NodePort    10.97.194.16   <none>        80:30000/TCP    3m
```

In the output above, `po/kubernetes-console-bzjjh` has only
two out of three pods ready and has restarted four times.
To fix this issue, run:

```s
kubectl -n kube-system create sa kube-dns
kubectl -n kube-system patch deploy/kube-dns -p '{"spec": {"template": {"spec": {"serviceAccountName": "kube-dns"}}}}'
```

These commands enforce `kube-dns` to use the appropriate
`ServiceAccount`. Kubernetes has created the `ServiceAccount`, but
does not use it until you run the above commands.

## Resolving RBAC Permissions on GKE

When you deploy {{%productName%}} on GKE, you might see the following error:

```s
Error from server (Forbidden): error when creating "STDIN": clusterroles.rbac.authorization.k8s.io "pachyderm" is forbidden: attempt to grant extra privileges:
```

To fix this issue, run the following command and redeploy
{{%productName%}}:

```s
kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)
```

