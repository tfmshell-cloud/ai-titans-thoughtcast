#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
cd "$REPO_DIR"

echo "=== Syncing AI Titans Thoughtcast with GitHub ==="
mkdir -p docs
touch 07_DASHBOARD/.nojekyll
rsync -a --delete 07_DASHBOARD/ docs/
touch docs/.nojekyll

git add -A
if git diff --staged --quiet; then
  echo "Nothing new to commit."
else
  DEFAULT_MSG="feat(studio): 16 WAV (40 Smart Bin tracks), 14 4K dossiers, archival B-roll, Tab 8 Media Pool & fast .nojekyll Pages deploy ($(date '+%Y-%m-%d %H:%M:%S'))"
  COMMIT_MSG="${1:-$DEFAULT_MSG}"
  git commit -m "$COMMIT_MSG"
  echo "Committed changes: $COMMIT_MSG"
fi

git push origin main
echo "✓ Successfully pushed to GitHub (origin/main)!"
