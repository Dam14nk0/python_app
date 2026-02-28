#!/usr/bin/env bash
set -euo pipefail

BASE_BRANCH="${1:-main}"
REMOTE="${2:-origin}"

current_branch="$(git branch --show-current)"
if [[ -z "$current_branch" ]]; then
  echo "Cannot detect current branch."
  exit 1
fi

echo "Current branch: $current_branch"
echo "Rebasing on $REMOTE/$BASE_BRANCH ..."

git fetch "$REMOTE"
git rebase "$REMOTE/$BASE_BRANCH"

echo "Rebase completed."
echo "Run tests, then push with: git push --force-with-lease"
