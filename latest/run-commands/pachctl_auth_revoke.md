## pachctl auth revoke

Revoke a {{% productName %}} auth token

### Synopsis

Revoke a {{% productName %}} auth token.

```
pachctl auth revoke [flags]
```

### Options

```
      --enterprise     Revoke an auth token (or all auth tokens minted for one user) on the enterprise server
  -h, --help           help for revoke
      --token string   {{% productName %}} auth token that should be revoked (one of --token or --user must be set)
      --user string    User whose {{% productName %}} auth tokens should be revoked (one of --token or --user must be set)
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

