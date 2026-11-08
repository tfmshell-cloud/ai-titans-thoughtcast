#!/usr/bin/env bash
# AI Titans Thoughtcast — Open File or Directory in macOS Finder
# Usage:
#   ./open_in_finder.sh                         # Opens 05_RAW_FOOTAGE in Finder
#   ./open_in_finder.sh BATCH4                  # Opens Batch 4 images
#   ./open_in_finder.sh EP01_FLOW_IMG_06        # Reveals specific image
#   ./open_in_finder.sh --bridge                # Starts background web bridge

PROJECT_ROOT="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"

if [ "$1" == "--bridge" ]; then
  echo "Starting Finder Bridge daemon on http://127.0.0.1:8765..."
  python3 "$PROJECT_ROOT/08_AUTOMATION/scripts/finder_bridge.py"
  exit 0
fi

if [ -z "$1" ]; then
  echo "Opening 05_RAW_FOOTAGE in Finder..."
  open "$PROJECT_ROOT/05_RAW_FOOTAGE"
  exit 0
fi

TARGET="$1"

# If it's a full or relative path that exists
if [ -e "$TARGET" ]; then
  open -R "$TARGET"
  echo "Revealed in Finder: $TARGET"
  exit 0
fi

if [ -e "$PROJECT_ROOT/$TARGET" ]; then
  open -R "$PROJECT_ROOT/$TARGET"
  echo "Revealed in Finder: $PROJECT_ROOT/$TARGET"
  exit 0
fi

# Search in 05_RAW_FOOTAGE or 03_AUDIO
FOUND=$(find "$PROJECT_ROOT/05_RAW_FOOTAGE" "$PROJECT_ROOT/03_AUDIO" -iname "*$TARGET*" | head -n 1)

if [ -n "$FOUND" ]; then
  open -R "$FOUND"
  echo "Found and revealed in Finder: $FOUND"
else
  echo "File or directory matching '$TARGET' not found."
  echo "Opening 05_RAW_FOOTAGE root instead..."
  open "$PROJECT_ROOT/05_RAW_FOOTAGE"
fi
