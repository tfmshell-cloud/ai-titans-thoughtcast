#!/usr/bin/env python3
"""Generate all 10 standalone Hero Master-Dossier Studio webpages in 07_DASHBOARD/episodes/."""
import json
import os

ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
DASH = os.path.join(ROOT, "07_DASHBOARD")
EP_OUT_DIR = os.path.join(DASH, "episodes")
os.makedirs(EP_OUT_DIR, exist_ok=True)

raw_idx = open(os.path.join(DASH, "data", "season1_index.js"), encoding="utf-8").read()
prefix = "window.SEASON1_INDEX = "
season = json.loads(raw_idx[len(prefix):].rstrip(";\n "))

TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EP{ep} — {name} | Мастер-Досьє Cinematic Thoughtcast</title>
  <link rel="stylesheet" href="../assets/episode_app.css?v=20261108_v1">
</head>
<body>
  <div id="episodeApp"></div>
  <script src="../data/season1_index.js?v=20261108_v1"></script>
  <script src="../data/suno_master_pool.js?v=20261108_v1"></script>
  <script src="../data/media_acquisition_pool.js?v=20261108_v1"></script>
  <script src="../data/episodes/ep{ep}.js?v=20261108_v1"></script>
  <script src="../assets/episode_app.js?v=20261108_v1"></script>
</body>
</html>
"""

for item in season:
    ep = item["ep"]
    fname = os.path.basename(item["page_url"])
    out_path = os.path.join(EP_OUT_DIR, fname)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(TEMPLATE.format(ep=ep, name=item["name"]))
    print(f"Generated {out_path}")
