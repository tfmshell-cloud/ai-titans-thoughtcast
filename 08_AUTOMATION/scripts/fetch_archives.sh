#!/usr/bin/env bash
# ==============================================================================
# Cinematic Thoughtcast // AI Titans — Точковий завантажувач архівного B-Roll
# Автоматично вирізає 5–12 секундні фрагменти у 4K/1080p MP4 без перекодування
# або з точною підрізкою по ключових кадрах під DaVinci Resolve Studio (24 fps).
#
# Приклади запуску:
#   ./08_AUTOMATION/scripts/fetch_archives.sh --starter   # Швидкий стартовий пул (EP01 + класика ШІ)
#   ./08_AUTOMATION/scripts/fetch_archives.sh --ep EP01   # Усі куровані архіви конкретного епізоду (EP01..EP10)
#   ./08_AUTOMATION/scripts/fetch_archives.sh --all       # Повний сезонний пул (усі 10 епізодів)
#   ./08_AUTOMATION/scripts/fetch_archives.sh --custom "URL" "00:12:10-00:12:18" "EP01_VID_ARCH_99_ACT3_24FPS_Custom"
# ==============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_DIR"

export PATH="$HOME/Library/Python/3.9/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"

ARCHIVE_DIR="05_RAW_FOOTAGE/archives"
mkdir -p "$ARCHIVE_DIR"

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "[!] yt-dlp не знайдено. Встановіть командою: python3 -m pip install --user yt-dlp imageio-ffmpeg"
  exit 1
fi

FFMPEG_BIN="$(command -v ffmpeg || true)"
if [[ -z "$FFMPEG_BIN" ]]; then
  FFMPEG_BIN="$(python3 -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())' 2>/dev/null || true)"
fi

if [[ -z "$FFMPEG_BIN" ]]; then
  echo "[!] ffmpeg не знайдено. Встановіть командою: python3 -m pip install --user imageio-ffmpeg"
  exit 1
fi

echo "[*] Каталог архівів: $REPO_DIR/$ARCHIVE_DIR"
echo "[*] Використовується yt-dlp: $(command -v yt-dlp)"
echo "[*] Використовується ffmpeg: $FFMPEG_BIN"

# Функція точкового скачування відрізка часу:
# fetch_clip "URL" "START-END" "FILENAME_NO_EXT"
fetch_clip() {
  local url="$1"
  local section="$2"
  local output="$3"
  local target_mp4="${ARCHIVE_DIR}/${output}.mp4"

  if [[ -s "$target_mp4" ]]; then
    echo " [✓] Вже існує, пропускаємо: $target_mp4"
    return 0
  fi

  echo " [→] Завантаження фрагмента: $output ($section)"
  yt-dlp \
    --ffmpeg-location "$FFMPEG_BIN" \
    --no-playlist \
    --quiet --no-warnings --progress \
    -S "vcodec:h264,res:1080,acodec:m4a" \
    -f "bv*+ba/b" \
    --merge-output-format mp4 \
    --download-sections "*${section}" \
    --force-keyframes-at-cuts \
    -o "${ARCHIVE_DIR}/${output}.%(ext)s" \
    "$url" || {
      echo " [!] Попередження: не вдалося завантажити $output з $url (перевірте доступність джерела)."
      return 0
    }
}

run_ep01() {
  # EP01 — Сем Альтман: Слухання у Сенаті США (16.05.2023 — Public Domain уряду США) + Вінтажний Apple Mac 1992
  fetch_clip "https://www.youtube.com/watch?v=TO0J2Yw7usM" "00:29:10-00:29:18" "EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup"
  fetch_clip "https://www.youtube.com/watch?v=TO0J2Yw7usM" "00:31:05-00:31:13" "EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement"
  fetch_clip "https://www.youtube.com/watch?v=5Vt0U9rYqkg" "00:00:04-00:00:12" "EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT"
}

run_ep02() {
  # EP02 — Дженсен Хуанг: Біографічні та технологічні архіви (Oneida/Stripe, Stanford GSB, 60 Minutes Denny's, OSU 2009, NTU 2023, GTC 2016 DGX-1, SIEPR 2024, GTC Blackwell)
  fetch_clip "https://www.youtube.com/watch?v=_waPvOwL9Z8" "00:14:20-00:14:28" "EP02_VID_ARCH_01_ACT3_24FPS_Huang_GTC_Stage_Walk"
  fetch_clip "https://www.youtube.com/watch?v=_waPvOwL9Z8" "00:46:10-00:46:18" "EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal"
  fetch_clip "https://www.youtube.com/watch?v=8Pfa8kPjUio" "00:09:44-00:10:00" "EP02_VID_ARCH_03_ACT1_24FPS_Huang_Oneida_Bathrooms_Age9"
  fetch_clip "https://www.youtube.com/watch?v=lXLBTBBil2U" "00:30:27-00:30:43" "EP02_VID_ARCH_04_ACT1_24FPS_Huang_Dennys_Dishwasher_NoTaskBeneath"
  fetch_clip "https://www.youtube.com/watch?v=DpQQi2scsHo" "00:07:49-00:08:09" "EP02_VID_ARCH_05_ACT1_24FPS_Huang_Dennys_Booth_Founding_60Min"
  fetch_clip "https://www.youtube.com/watch?v=DpQQi2scsHo" "00:08:21-00:08:36" "EP02_VID_ARCH_06_ACT1_24FPS_Huang_Dennys_Booth_Inside_60Min"
  fetch_clip "https://www.youtube.com/watch?v=lMW5v7wK7zo" "00:02:40-00:02:56" "EP02_VID_ARCH_07_ACT2_24FPS_Huang_2009_OSU_We_Failed"
  fetch_clip "https://www.youtube.com/watch?v=TOXp-Yk_Gsk" "00:11:46-00:12:04" "EP02_VID_ARCH_08_ACT2_24FPS_Huang_Sega_Lifeline_NTU2023"
  fetch_clip "https://www.youtube.com/watch?v=8Pfa8kPjUio" "00:28:00-00:28:18" "EP02_VID_ARCH_09_ACT2_24FPS_Huang_Invented_CUDA_Stripe2024"
  fetch_clip "https://www.youtube.com/watch?v=1ayGJDO6PKU" "00:01:26-00:01:44" "EP02_VID_ARCH_10_ACT3_24FPS_Huang_GTC2016_DGX1_Reveal"
  fetch_clip "https://www.youtube.com/watch?v=cEg8cOx7UZk" "00:37:58-00:38:22" "EP02_VID_ARCH_11_ACT4_24FPS_Huang_Stanford_Pain_And_Suffering"
  fetch_clip "https://www.youtube.com/watch?v=TOXp-Yk_Gsk" "00:21:08-00:21:24" "EP02_VID_ARCH_12_ACT4_24FPS_Huang_NTU2023_Run_Dont_Walk"
  # 13..16: NVIDIA Official Pressroom (nvidianews.nvidia.com corporate B-roll)
  fetch_clip "https://www.youtube.com/watch?v=0c8i4T9BSqY" "00:01:55-00:02:14" "EP02_VID_ARCH_17_ACT1_24FPS_Huang_CHM_Oneida_Kentucky"
  fetch_clip "https://www.youtube.com/watch?v=0c8i4T9BSqY" "00:44:45-00:45:05" "EP02_VID_ARCH_18_ACT2_24FPS_Huang_CHM_Sega_Generosity"
  fetch_clip "https://www.youtube.com/watch?v=y6NfxiemvHg" "00:21:14-00:21:32" "EP02_VID_ARCH_19_ACT3_24FPS_Huang_Acquired_DGX_Scale"
  fetch_clip "https://www.youtube.com/watch?v=yU3GUHDf0mk" "00:02:50-00:03:08" "EP02_VID_ARCH_20_ACT2_24FPS_Huang_2013_No_Business_Plan"
}

run_ep03() {
  # EP03 — Деміс Гассабіс: Нобелівська лекція 2024 + AlphaGo (Move 37) + The Thinking Game + Stanford GSB + WSJ + CBS 60 Minutes + Lex Chess
  fetch_clip "https://www.youtube.com/watch?v=YtPaZsasmNA" "00:02:15-00:02:23" "EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024"
  fetch_clip "https://www.youtube.com/watch?v=WXuK6gekU1Y" "00:51:20-00:51:28" "EP03_VID_ARCH_02_ACT3_24FPS_AlphaGo_Seoul_Move37_Reaction"
  fetch_clip "https://www.youtube.com/watch?v=Ea6ajW5hcCY" "00:00:36-00:00:52" "EP03_VID_ARCH_03_ACT1_24FPS_Hassabis_Chess_Age4_WSJ"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:22:50-00:23:18" "EP03_VID_ARCH_04_ACT1_24FPS_Hassabis_Childhood_Chess_ThinkingGame"
  fetch_clip "https://www.youtube.com/watch?v=UbkB-vhjhHA" "00:01:25-00:01:45" "EP03_VID_ARCH_05_ACT1_24FPS_Hassabis_Playing_Chess_Board"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:26:20-00:26:39" "EP03_VID_ARCH_06_ACT1_24FPS_Hassabis_Leaving_Chess_Realization"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:39:17-00:39:44" "EP03_VID_ARCH_07_ACT1_24FPS_Hassabis_Bullfrog_ThemePark_GapYear"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:03:20-00:03:38" "EP03_VID_ARCH_08_ACT2_24FPS_Hassabis_Neuroscience_Brain_Goal"
  fetch_clip "https://www.youtube.com/watch?v=DsewHeVbL-0" "00:09:12-00:09:30" "EP03_VID_ARCH_09_ACT2_24FPS_DeepMind_Solve_Intelligence_Plan"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:11:36-00:11:58" "EP03_VID_ARCH_10_ACT2_24FPS_DeepMind_Atari_Breakout_Tunnel"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "00:35:52-00:36:18" "EP03_VID_ARCH_11_ACT2_24FPS_Google_650M_Deal_Military_Ethics"
  fetch_clip "https://www.youtube.com/watch?v=WXuK6gekU1Y" "00:50:00-00:50:25" "EP03_VID_ARCH_12_ACT3_24FPS_AlphaGo_Move37_Fifth_Line_Shock"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "01:15:12-01:15:36" "EP03_VID_ARCH_13_ACT3_24FPS_AlphaFold_200M_Proteins_Open_Data"
  fetch_clip "https://www.youtube.com/watch?v=1XF-NG_35NE" "00:10:05-00:10:42" "EP03_VID_ARCH_14_ACT3_24FPS_AlphaFold_Protein_Fold_60Minutes"
  fetch_clip "https://www.youtube.com/watch?v=YtPaZsasmNA" "00:14:20-00:14:46" "EP03_VID_ARCH_15_ACT4_24FPS_Nobel_Lecture_CASP14_Atomic_Accuracy"
  fetch_clip "https://www.youtube.com/watch?v=d95J8yzvjbQ" "01:19:50-01:20:16" "EP03_VID_ARCH_16_ACT4_24FPS_Hassabis_AGI_Horizon_Life_Moment"
}

run_ep04() {
  # EP04 — Джеффрі Хінтон: Стокгольм Нобель 2024 + CBS 60 Minutes + BBC + Diary Of A CEO + ACM Turing 2018 + UofT Presser
  fetch_clip "https://www.youtube.com/watch?v=-f5WQAk3dYo" "00:00:35-00:00:43" "EP04_VID_ARCH_01_ACT4_24FPS_Hinton_Nobel_Warning_2024"
  fetch_clip "https://www.youtube.com/watch?v=giT0ytynSqg" "01:19:53-01:20:24" "EP04_VID_ARCH_02_ACT1_24FPS_Hinton_Ancestry_Boole_Everest"
  fetch_clip "https://www.youtube.com/watch?v=giT0ytynSqg" "01:20:39-01:21:05" "EP04_VID_ARCH_03_ACT1_24FPS_Hinton_Joan_Los_Alamos_Cousin"
  fetch_clip "https://www.youtube.com/watch?v=HzilDIhWhrE" "00:01:44-00:02:16" "EP04_VID_ARCH_04_ACT2_24FPS_Hinton_Second_AI_Winter_Turing"
  fetch_clip "https://www.youtube.com/watch?v=XDE9DjpcSdI" "00:01:46-00:02:14" "EP04_VID_ARCH_05_ACT2_24FPS_Hinton_Boltzmann_Machine_Nobel_Lecture"
  fetch_clip "https://www.youtube.com/watch?v=XDE9DjpcSdI" "00:20:15-00:20:39" "EP04_VID_ARCH_06_ACT2_24FPS_Hinton_Backpropagation_Nobel_Lecture"
  fetch_clip "https://www.youtube.com/watch?v=66WiF8fXL0k" "00:16:45-00:17:10" "EP04_VID_ARCH_07_ACT2_24FPS_Hinton_Sejnowski_1980s_Neuroscience"
  fetch_clip "https://www.youtube.com/watch?v=VsnQf7exv5I" "00:27:12-00:27:36" "EP04_VID_ARCH_08_ACT3_24FPS_Hinton_Two_Students_GPUs_Turing"
  fetch_clip "https://www.youtube.com/watch?v=giT0ytynSqg" "01:11:51-01:12:28" "EP04_VID_ARCH_09_ACT3_24FPS_Hinton_AlexNet_DNNresearch_Auction"
  fetch_clip "https://www.youtube.com/watch?v=HzilDIhWhrE" "00:04:50-00:05:14" "EP04_VID_ARCH_10_ACT3_24FPS_Hinton_Turing_2018_Three_Fathers"
  fetch_clip "https://www.youtube.com/watch?v=giT0ytynSqg" "01:15:02-01:15:24" "EP04_VID_ARCH_11_ACT3_24FPS_Hinton_Leaving_Google_Speak_Freely"
  fetch_clip "https://www.youtube.com/watch?v=DsBGaHywRhs" "00:00:02-00:00:28" "EP04_VID_ARCH_12_ACT3_24FPS_Hinton_BBC_Regret_Warning_2023"
  fetch_clip "https://www.youtube.com/watch?v=giT0ytynSqg" "00:57:41-00:58:14" "EP04_VID_ARCH_13_ACT3_24FPS_Hinton_Digital_Weights_Trillions_Bits"
  fetch_clip "https://www.youtube.com/watch?v=QH6QqjIwv68" "00:11:50-00:12:28" "EP04_VID_ARCH_14_ACT3_24FPS_Hinton_60Minutes_Species_Control"
  fetch_clip "https://www.youtube.com/watch?v=H7DgMFqrON0" "00:03:16-00:03:40" "EP04_VID_ARCH_15_ACT4_24FPS_Hinton_UofT_Students_Nobel_Presser"
  fetch_clip "https://www.youtube.com/watch?v=-f5WQAk3dYo" "00:02:26-00:02:52" "EP04_VID_ARCH_16_ACT4_24FPS_Hinton_Banquet_Existential_Threat"
}

run_ep05() {
  # EP05 — Ян Лекун: Історична демонстрація LeNet-1 (Bell Labs 1989) + повний 4-актний архів (16 HD кліпів)
  fetch_clip "https://www.youtube.com/watch?v=FwFduRA_L6Q" "00:00:12-00:00:20" "EP05_VID_ARCH_01_ACT2_24FPS_LeCun_BellLabs_1989_Digits"
  fetch_clip "https://www.youtube.com/watch?v=72Xj8k5WQX4" "00:02:55-00:03:20" "EP05_VID_ARCH_02_ACT1_24FPS_LeCun_Chomsky_Piaget_Debate_ETH"
  fetch_clip "https://www.youtube.com/watch?v=VsnQf7exv5I" "00:14:38-00:15:02" "EP05_VID_ARCH_03_ACT1_24FPS_Hinton_LeCun_Minsky_Perceptrons_Turing"
  fetch_clip "https://www.youtube.com/watch?v=H0oEr40YhrQ" "00:00:25-00:00:58" "EP05_VID_ARCH_04_ACT2_24FPS_LeCun_1989_ConvNet_Restored"
  fetch_clip "https://www.youtube.com/watch?v=VsnQf7exv5I" "00:46:26-00:46:48" "EP05_VID_ARCH_05_ACT2_24FPS_LeCun_Young_Bell_Labs_Holmdel_Photo"
  fetch_clip "https://www.youtube.com/watch?v=VsnQf7exv5I" "00:44:32-00:45:00" "EP05_VID_ARCH_06_ACT2_24FPS_LeCun_Hubel_Wiesel_Visual_Cortex"
  fetch_clip "https://www.youtube.com/watch?v=VsnQf7exv5I" "00:43:28-00:43:54" "EP05_VID_ARCH_07_ACT2_24FPS_LeCun_20_Percent_US_Checks_Turing"
  fetch_clip "https://www.youtube.com/watch?v=psl1wY2V-L0" "00:04:16-00:04:44" "EP05_VID_ARCH_08_ACT2_24FPS_LeCun_Neural_Net_Winter_SVM_Sequel"
  fetch_clip "https://www.youtube.com/watch?v=SGSOCuByo24" "00:28:10-00:28:36" "EP05_VID_ARCH_09_ACT2_24FPS_LeCun_Bell_Labs_DSP_Compiler_Lex36"
  fetch_clip "https://www.youtube.com/watch?v=SGzMElJ11Cc" "01:51:10-01:51:38" "EP05_VID_ARCH_10_ACT3_24FPS_LeCun_FAIR_PyTorch_Open_Source_Lex258"
  fetch_clip "https://www.youtube.com/watch?v=SGzMElJ11Cc" "02:02:48-02:03:14" "EP05_VID_ARCH_11_ACT3_24FPS_LeCun_Gutenberg_Printing_Press_Lex258"
  fetch_clip "https://www.youtube.com/watch?v=SGzMElJ11Cc" "00:21:30-00:21:58" "EP05_VID_ARCH_12_ACT3_24FPS_LeCun_House_Cat_Common_Sense_Lex258"
  fetch_clip "https://www.youtube.com/watch?v=4__gg83s_Do" "00:00:00-00:00:26" "EP05_VID_ARCH_13_ACT3_24FPS_LeCun_No_AGI_By_Scaling_LLMs"
  fetch_clip "https://www.youtube.com/watch?v=72Xj8k5WQX4" "00:25:14-00:25:48" "EP05_VID_ARCH_14_ACT4_24FPS_LeCun_JEPA_Architecture_ETH_Zurich"
  fetch_clip "https://www.youtube.com/watch?v=72Xj8k5WQX4" "00:06:24-00:06:52" "EP05_VID_ARCH_15_ACT4_24FPS_LeCun_Baby_3D_Intuitive_Physics_ETH"
  fetch_clip "https://www.youtube.com/watch?v=pJyoqapCRZE" "00:04:46-00:05:14" "EP05_VID_ARCH_16_ACT4_24FPS_LeCun_Davos_2026_Embodied_AI"
}

run_ep06() {
  # EP06 — Ілля Суцкевер: Лекція в Інституті Саймонса (Берклі) про генералізацію та стиснення
  fetch_clip "https://www.youtube.com/watch?v=AKMuA_TVz3A" "00:03:10-00:03:18" "EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture"
}

run_ep07() {
  # EP07 — Даріо Амодей: Свідчення у Юридичному комітеті Сенату США (25.07.2023 — Public Domain)
  fetch_clip "https://www.youtube.com/watch?v=yBgvqGrJ3g8" "00:36:15-00:36:23" "EP07_VID_ARCH_01_ACT3_24FPS_Amodei_Senate_Biosecurity_Hearing"
}

run_ep08() {
  # EP08 — Фей-Фей Лі: Знакова доповідь про створення ImageNet та комп'ютерний зір
  fetch_clip "https://www.youtube.com/watch?v=40riCqvRoMs" "00:06:30-00:06:38" "EP08_VID_ARCH_01_ACT2_24FPS_FeiFeiLi_ImageNet_Stage"
}

run_ep09() {
  # EP09 — Йошуа Бенжіо: Свідчення у Сенаті США щодо екзистенційних ризиків ШІ (25.07.2023 — Public Domain)
  fetch_clip "https://www.youtube.com/watch?v=hm1zexCjELo" "00:27:40-00:27:48" "EP09_VID_ARCH_01_ACT3_24FPS_Bengio_Senate_Testimony"
}

run_ep10() {
  # EP10 — Ендрю Ин: Класична лекція Stanford CS229 Machine Learning біля зеленої дошки
  fetch_clip "https://www.youtube.com/watch?v=jGwO_UgTS7I" "00:01:40-00:01:48" "EP10_VID_ARCH_01_ACT2_24FPS_AndrewNg_Stanford_CS229_Chalkboard"
}

MODE="${1:---starter}"

case "$MODE" in
  --starter)
    run_ep01
    run_ep04
    run_ep05
    ;;
  --ep)
    EP_CODE="${2:-EP01}"
    case "$EP_CODE" in
      EP01|01) run_ep01 ;;
      EP02|02) run_ep02 ;;
      EP03|03) run_ep03 ;;
      EP04|04) run_ep04 ;;
      EP05|05) run_ep05 ;;
      EP06|06) run_ep06 ;;
      EP07|07) run_ep07 ;;
      EP08|08) run_ep08 ;;
      EP09|09) run_ep09 ;;
      EP10|10) run_ep10 ;;
      *) echo "Невідомий код епізоду: $EP_CODE (використовуйте EP01..EP10)"; exit 1 ;;
    esac
    ;;
  --all)
    run_ep01; run_ep02; run_ep03; run_ep04; run_ep05
    run_ep06; run_ep07; run_ep08; run_ep09; run_ep10
    ;;
  --custom)
    if [[ $# -lt 4 ]]; then
      echo "Використання: $0 --custom \"URL\" \"00:01:00-00:01:08\" \"EP01_VID_ARCH_Custom\""
      exit 1
    fi
    fetch_clip "$2" "$3" "$4"
    ;;
  *)
    echo "Невідомий режим: $MODE. Доступні: --starter | --ep EP01..EP10 | --all | --custom"
    exit 1
    ;;
esac

echo "[✓] Завантаження архівного пулу в $ARCHIVE_DIR завершено."
ls -lh "$ARCHIVE_DIR"/*.mp4 2>/dev/null || true
