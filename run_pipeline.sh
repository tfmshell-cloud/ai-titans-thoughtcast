#!/usr/bin/env bash
# Майстер-скрипт оркестрації екосистеми «Cinematic Thoughtcast: AI Titans»
# 1) Перевірка синтаксису JS (jsc) -> 2) Дзеркало docs/ (GitHub Pages) -> 3) Git Push -> 4) Google Drive Backup
set -euo pipefail

REPO_DIR="/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
cd "$REPO_DIR"

echo "=== [1/3] Перевірка цілісності даних та JS-синтаксису ==="
JSC="/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
python3 - << 'PY'
import glob, subprocess
JSC = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
files = [
    "07_DASHBOARD/data/season1_index.js",
    "07_DASHBOARD/data/suno_master_pool.js",
    "07_DASHBOARD/data/media_acquisition_pool.js",
    "07_DASHBOARD/data/titans_1000_quotes.js",
    "07_DASHBOARD/assets/hub_app.js",
    "07_DASHBOARD/assets/episode_app.js",
] + sorted(glob.glob("07_DASHBOARD/data/episodes/ep*.js"))

for f in files:
    src = open(f, encoding="utf-8").read()
    stub = (
        "var window={addEventListener:function(){},scrollTo:function(){}}, "
        "document={title:'',body:{},getElementById:function(){return null;},querySelectorAll:function(){return [];}}, "
        "localStorage={getItem:function(){return null;},setItem:function(){}}, "
        "location={hash:''}, history={replaceState:function(){}};\n" + src
    )
    open("/tmp/_ct_jsc_test.js", "w", encoding="utf-8").write(stub)
    res = subprocess.run([JSC, "/tmp/_ct_jsc_test.js"], capture_output=True, text=True)
    if res.returncode != 0:
        raise SystemExit(f"JSC syntax/runtime error in {f}:\n{res.stdout}\n{res.stderr}")
print(f"✓ Перевірено {len(files)} JS-модулів — 0 помилок.")
PY
rm -f /tmp/_ct_jsc_test.js

echo "=== [2/3] Синхронізація з GitHub та GitHub Pages (/docs) ==="
bash "$REPO_DIR/08_AUTOMATION/scripts/sync_github.sh"

echo "=== [3/3] Резервне копіювання на Google Drive ==="
bash "$REPO_DIR/08_AUTOMATION/scripts/backup_gdrive.sh"

echo "✅ Повний цикл run_pipeline.sh виконано успішно!"
