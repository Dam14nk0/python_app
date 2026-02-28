# Merge conflicts fix guide (for this branch)

If GitHub shows **"This branch has conflicts that must be resolved"**, run the steps below locally.

## 1) Ensure you are on your feature branch
```bash
git checkout work
```

## 2) Add the target/base branch remote (example: `origin/main`)
```bash
git remote add origin <YOUR_REPO_URL>   # only once if missing
git fetch origin
```

## 3) Rebase your branch on top of latest main
```bash
git rebase origin/main
```

If conflicts appear, Git will stop and mark files as conflicted.

## 4) Resolve conflicts file by file
```bash
git status
```

Edit files, remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then mark resolved:
```bash
git add <resolved_file>
```

Continue until done:
```bash
git rebase --continue
```

If needed:
```bash
git rebase --abort
```

## 5) Run checks after resolving
```bash
pytest backend/tests -q
cd frontend && npm install && npm run build
```

## 6) Push updated branch
```bash
git push --force-with-lease
```

Use `--force-with-lease` because rebase rewrites commit history.
