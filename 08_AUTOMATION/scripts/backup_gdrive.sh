#!/usr/bin/env bash
set -e

SRC_DIR="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
DEST_DIR="/Users/volodymyrkatasonov/Library/CloudStorage/GoogleDrive-tfmshell@gmail.com/Мій диск/[00]_MASTER_PROJECTS_BACKUP_2026/[03]_MEDIA_ECOSYSTEMS/ai-titans-thoughtcast"

echo "=== Syncing AI Titans Thoughtcast with Google Drive ==="
mkdir -p "$DEST_DIR"

rsync -av --delete \
  --exclude ".git" \
  "$SRC_DIR/" \
  "$DEST_DIR/"

echo "✓ Successfully mirrored to Google Drive: $DEST_DIR"
