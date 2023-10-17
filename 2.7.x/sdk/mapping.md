---
title: Method Mapping 
description: Use this quick reference guide for mapping methods between Python Pachyderm and the new Pachyderm SDK
directory: true 
tags: ["python","sdk", "methods"]
weight: 02
---

## About

The original `python_pachyderm` SDK will be deprecated in a future release (spring 2024). The new `pachyderm_sdk` SDK is a complete rewrite of the original SDK, and it is not backwards compatible. This guide provides a quick reference for mapping methods between the two SDKs.

## Methods

| python_pachyderm | pachyderm_sdk |
|---|---|
| client.inspect_cluster | client.admin.inspect_cluster |
| client.activate_auth | client.auth.activate |
| client.authenticate_id_token | client.auth.authenticate |
| client.authenticate_oidc | client.auth.authenticate |
| client.authorize | client.auth.authorize |
| client.deactivate_auth | client.auth.deactivate |
| client.extract_auth_tokens | client.auth.extract_auth_tokens |
| client.get_auth_configuration | client.auth.get_configuration |
| client.get_groups | client.auth.get_groups |
| client.get_oidc_login | client.auth.get_oidc_login |
| client.get_robot_token | client.auth.get_robot_token |
| client.get_role_binding | client.auth.get_role_binding |
| client.get_roles_for_permission | client.auth.get_roles_for_permission |
| client.get_users | client.auth.get_users |
| client.modify_members | client.auth.modify_members |
| client.modify_role_binding | client.auth.modify_role_binding |
| client.restore_auth_token | client.auth.restore_auth_token |
| client.revoke_auth_token | client.auth.revoke_auth_token |
| client.set_auth_configuration | client.auth.set_configuration |
| client.set_groups_for_user | client.auth.set_groups_for_user |
| client.who_am_i | client.auth.who_am_i |
| client.binary | client.debug.binary |
| client.dump | client.debug.dump |
| client.profile_cpu | client.debug.profile (w/ profile=Profile(name="cpu")) |
| client.activate_enterprise | client.enterprise.activate |
| client.deactivate_enterprise | client.enterprise.deactivate |
| client.get_activation_code | client.enterprise.get_activation_code |
| client.get_enterprise_state | client.enterprise.get_state |
| client.get_pause_status | client.enterprise.pause_status |
| client.pause_enterprise | client.enterprise.pause |
| client.unpause_enterprise | client.enterprise.unpause |
| client.create_idp_connector | client.identity.create_idp_connector |
| client.create_oidc_client | client.identity.create_oidc_client |
| client.delete_all_identity | client.identity.delete_all |
| client.delete_idp_connector | client.identity.delete_idp_connector |
| client.delete_oidc_client | client.identity.delete_oidc_client |
| client.get_identity_server_config | client.identity.get_identity_server_config |
| client.get_idp_connector | client.identity.get_idp_connector |
| client.get_oidc_client | client.identity.get_oidc_client |
| client.list_idp_connectors | client.identity.list_idp_connectors |
| client.list_oidc_clients | client.identity.list_oidc_clients |
| client.set_identity_server_config | client.identity.set_identity_server_config |
| client.update_idp_connector | client.identity.update_idp_connector |
| client.update_oidc_client | client.identity.update_oidc_client |
| client.activate_license | client.license.activate |
| client.add_cluster | client.license.add_cluster |
| client.delete_all_license | client.license.delete_all |
| client.delete_cluster | client.license.delete_cluster |
| client.get_activation_code | client.license.get_activation_code |
| client.list_clusters | client.license.list_clusters |
| client.list_user_clusters | client.license.list_user_clusters |
| client.update_cluster | client.license.update_cluster |
| client.commit | client.pfs.commit |
| client.copy_file | client.pfs.copy_file |
| client.create_branch | client.pfs.create_branch |
| client.create_project | client.pfs.create_project |
| client.create_repo | client.pfs.create_repo |
| client.delete_all_repos | client.pfs.delete_all |
| client.delete_branch | client.pfs.delete_branch |
| client.delete_file | client.pfs.delete_file |
| client.delete_project | client.pfs.delete_project |
| client.delete_repo | client.pfs.delete_repo |
| client.diff_file | client.pfs.diff_file |
| client.drop_commit | client.pfs.drop_commit |
| client.finish_commit | client.pfs.finish_commit |
| client.fsck | client.pfs.fsck |
| client.get_file | client.pfs.get_file or client.pfs.pfs_file |
| client.get_file_tar | client.pfs.get_file_tar or client.pfs.pfs_tar_file |
| client.glob_file | client.pfs.glob_file |
| client.inspect_branch | client.pfs.inspect_branch |
| client.inspect_commit | client.pfs.inspect_commit |
| client.inspect_file | client.pfs.inspect_file |
| client.inspect_project | client.pfs.inspect_project |
| client.inspect_repo | client.pfs.inspect_repo |
| client.list_branch | client.pfs.list_branch |
| client.list_commit | client.pfs.list_commit |
| client.list_file | client.pfs.list_file |
| client.list_project | client.pfs.list_project |
| client.list_repo | client.pfs.list_repo |
| client.modify_file_client | -- |
| client.path_exists | client.pfs.path_exists |
| client.put_file_bytes | client.pfs.put_file_from_bytes |
| client.put_file_url | client.pfs.put_file_from_url |
| client.squash_commit | client.pfs.squash_commit |
| client.start_commit | client.pfs.start_commit |
| client.subscribe_commit | client.pfs.subscribe_commit |
| client.wait_commit | client.pfs.wait_commit |
| client.walk_file | client.pfs.walk_file |
| client.create_pipeline | client.pps.create_pipeline |
| client.create_pipeline_from_request | -- |
| client.create_secret | client.pps.create_secret |
| client.delete_all_pipelines | client.pps.delete_all |
| client.delete_job | client.pps.delete_job |
| client.delete_pipeline | client.pps.delete_pipeline |
| client.delete_secret | client.pps.delete_secret |
| client.get_job_logs | client.pps.get_logs |
| client.get_kube_events | client.pps.get_kube_events |
| client.get_pipeline_logs | client.pps.get_logs |
| client.inspect_datum | client.pps.inspect_datum |
| client.inspect_job | client.pps.inspect_job |
| client.inspect_pipeline | client.pps.inspect_pipeline |
| client.inspect_secret | client.pps.inspect_secret |
| client.list_datum | client.pps.list_datum |
| client.list_job | client.pps.list_job |
| client.list_pipeline | client.pps.list_pipeline |
| client.list_secret | client.pps.list_secret |
| client.restart_datum | client.pps.restart_datum |
| client.run_cron | client.pps.run_cron |
| client.start_pipeline | client.pps.start_pipeline |
| client.stop_job | client.pps.stop_job |
| client.stop_pipeline | client.pps.stop_pipeline |
| client.batch_transaction | client.transaction.batch_transaction |
| client.delete_all_transactions | client.transaction.delete_all |
| client.delete_transaction | client.transaction.delete_transaction |
| client.finish_transaction | client.transaction.finish_transaction |
| client.inspect_transaction | client.transaction.inspect_transaction |
| client.list_transaction | client.transaction.list_transaction |
| client.start_transaction | client.transaction.start_transaction |
| client.transaction | client.transaction.transaction |