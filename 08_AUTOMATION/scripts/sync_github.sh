#!/usr/bin/env bash
set -e

REPO_DIR="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
cd "$REPO_DIR"

echo "=== Syncing AI Titans Thoughtcast with GitHub ==="
# Sync docs for GitHub Pages
mkdir -p docs
cp -r 07_DASHBOARD/* docs/

git add -A
if git diff --staged --quiet; then
  echo "Nothing new to commit."
else
  COMMIT_MSG="chore(sync): automated sync $(date '+%Y-%m-%d %H:%M:%S')"
  git commit -m "$COMMIT_MSG"
  echo "Committed changes: $COMMIT_MSG"
fi

git push origin main
echo "✓ Successfully pushed to GitHub (origin/main)!"
