#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
cd "$REPO_DIR"

echo "=== Syncing AI Titans Thoughtcast with GitHub ==="
mkdir -p docs
rsync -a --delete 07_DASHBOARD/ docs/

git add -A
if git diff --staged --quiet; then
  echo "Nothing new to commit."
else
  COMMIT_MSG="feat(studio): 10 standalone hero master-dossier studio pages, SOP roadmap & 8-workshop architecture ($(date '+%Y-%m-%d %H:%M:%S'))"
  git commit -m "$COMMIT_MSG"
  echo "Committed changes: $COMMIT_MSG"
fi

git push origin main
echo "✓ Successfully pushed to GitHub (origin/main)!"
