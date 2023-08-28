---
# metadata # 
title: Manage RBAC via Console
description: Learn how to grant and modify roles on given resources for a user.
date: 
# taxonomy #
tags: ["permissions", "management", "roles", "rbac"]
series:
seriesPart:
weight: 01
---


## Before You Start 

- You must have an active [Enterprise](/{{%release%}}/set-up/enterprise/activate-via-helm) key 
- You must have [TLS](/{{%release%}}/set-up/tls) enabled on your cluster
- You must have an [Authentication Provider (IdP)](/{{%release%}}/set-up/connectors) set up
    - [Auth0](/{{%release%}}/set-up/connectors/auth0)
    - [Okta](/{{%release%}}/set-up/connectors/okta)
- Review the [Roles & Permissions](/{{%release%}}/set-up/authorization/permissions).
- Review the [User Types](/{{%release%}}/set-up/authorization/#authorization-rbac-users-types) 
- Confirm you have the right role(s) to grant a user access to a given resource (e.g., you have the `projectOwner` role on a given project you wish to add other users to)
- [Cluster-level admin roles](/{{%release%}}/set-up/authorization/permissions/#access-control-rbac-roles--permissions-admin-roles) are not currently implementable via Console


## How to Assign Roles to a User 

### On a Project

Roles granted at the Project level are inherited by all repositories within that project. If you grant a user `repoReader` on a project, they will have `repoReader` on all repositories within that project and that role will not be removable on the repo level.

1. Log in to the {{%productName%}} Console.
2. Scroll to a project you wish to add a user to.
3. Select the ellipsis icon {{< figure src="/images/console/ellipses.svg" class="inline">}} > **Edit Project Roles**
    ![rbac](/images/console/rbac-project.png)
4. Select a [User Type](/{{%release%}}/set-up/authorization/#authorization-rbac-users-types)  from the dropdown:
   - **user**: an individual by name or email address
   - **group**: a group of users; requires that your [IdP](/{{%release%}}/set-up/connectors) supports groups tied to an email address
   - **robot**: a service account
   - **allClusterUsers**: all users on the cluster
5. If not `allClusterUsers`, provide a name or email address.
6. Select a [**Role**](/{{%release%}}/set-up/authorization/permissions) from the dropdown.
   - **projectViewer**: Can view the project and see a list of its repositories.
   - **projectWriter**: projectViewer permissions + can also create repositories.
   - **projectOwner**: projectWriter permissions + can also delete repositories and modify role bindings.
   - **repoReader**: Can read every repository in the project.
   - **repoWriter** repoReader permissions + can also push to every repository in the project.
   - **repoOwner** repoWriter permissions + can also delete repositories and modify role bindings.
7. Select **Add**.
8. Select **Done**.

{{% notice tip %}}
You can add more roles to a user by selecting the plus icon {{< figure src="/images/console/add-role.svg" class="inline" height="15">}} and remove them by selecting the X icon {{< figure src="/images/console/remove-role.svg" class="inline" height="15">}}.
{{% /notice %}}

### On a Repository

Roles granted at the Repository level are not inherited by other repositories within that project. This is useful if you want to grant a user `repoReader` on a single repository within a project, but not on all repositories within that project.

1. Log in to the {{%productName%}} Console.
2. Select a **View Project** on the project containing the repository you wish to add a user to.
3. Select the repo (either from the DAG view or the List view).
4. Select **Set Roles**.
   ![rbac](/images/console/rbac-repo.png)
5.  Select a [User Type](/{{%release%}}/set-up/authorization/#authorization-rbac-users-types)  from the dropdown.
6. If not `allClusterUsers`, provide a name or email address.
7. Select a [**Role**](/{{%release%}}/set-up/authorization/permissions) from the dropdown.
8. Select **Add**.
9.  Select **Done**.