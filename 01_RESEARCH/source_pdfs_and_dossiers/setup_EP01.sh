#!/usr/bin/env bash
# Автоматична ініціалізація структури епізоду EP01 — Сем Альтман
# Стандарт DaVinci Resolve 19 Smart Bins (Cinematic Thoughtcast)
set -euo pipefail

BASE_DIR="${1:-./EP01_Sam_Altman}"
mkdir -p "$BASE_DIR/01_VO_UA"
mkdir -p "$BASE_DIR/01_VO_EN"
mkdir -p "$BASE_DIR/02_MUS_92BPM"
mkdir -p "$BASE_DIR/03_AMB"
mkdir -p "$BASE_DIR/04_SFX"
mkdir -p "$BASE_DIR/05_VID_4K_ACT1"
mkdir -p "$BASE_DIR/05_VID_4K_ACT2"
mkdir -p "$BASE_DIR/05_VID_4K_ACT3"
mkdir -p "$BASE_DIR/05_VID_4K_ACT4"
mkdir -p "$BASE_DIR/06_ARCHIVE_PARALLAX"
mkdir -p "$BASE_DIR/07_DAVINCI_EXPORTS"

cat > "$BASE_DIR/SMART_BINS_RULE.txt" << 'EOF'
Правило іменування Smart Bins: EP01_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]
Timeline: 3840x1606 (2.39:1 Anamorphic Scope) @ 24.000 fps
Suno Tempo Lock: 92 BPM (1 такт = 2.61 с / 62-63 кадри)
Fairlight Sidechain: A1 (Voice HPF 75Hz, +3.2kHz) -> Send 1 -> A2 (Music Listen 1, -24dB, 3.5:1, Attack 35ms, Release 400ms -> -3.2 dB)
Color Tree: Node 1 Balance -> Node 2 Cyan/Gold Split -> Node 3 Rec709 Kodak 2383 D60 -> Node 4 35mm Grain (0.35)
EOF

echo "✅ Структуру для EP01 (Сем Альтман) успішно створено у: $BASE_DIR"