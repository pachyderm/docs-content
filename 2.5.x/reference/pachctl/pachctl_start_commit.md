## pachctl start commit

Start a new commit.

### Synopsis

Start a new commit with parent-commit as the parent on the given branch; if the branch does not exist, it will be created.

```
pachctl start commit <repo>@<branch> [flags]
```

### Examples

```

# Start a commit in repo "test" on branch "master"
$ pachctl start commit test@master

# Start a commit with "master" as the parent in repo "test", on a new branch "patch"; essentially a fork.
$ pachctl start commit test@patch -p master

# Start a commit with XXX as the parent in repo "test" on the branch "fork"
$ pachctl start commit test@fork -p XXX
```

### Options

```
      --description string   A description of this commit's contents (synonym for --message)
  -h, --help                 help for commit
  -m, --message string       A description of this commit's contents
  -p, --parent string        The parent of the new commit, unneeded if branch is specified and you want to use the previous head of the branch as the parent.
      --project string       Project in which repo is located. (default "joins")
```

### Options inherited from parent commands

```
      --no-color   Turn off colors.
  -v, --verbose    Output verbose logs
```

