(function () {
  "use strict";

  var epData = window.EPISODE_DATA;
  var seasonIndex = window.SEASON1_INDEX || [];

  if (!epData) {
    document.body.innerHTML = "<div style='padding:2rem;color:#fb7185;'>Помилка: дані епізоду (window.EPISODE_DATA) не завантажено.</div>";
    return;
  }

  var STORAGE_KEY = "aititans_progress_v2_" + epData.ep;
  var state = {
    activeTab: "sop",
    mediaSubTab: "videos",
    vaultVidOrigin: "all",
    vaultVidUniqueOnly: false,
    vaultVidOnly169: false,
    vaultVidCat: "all",
    vaultVidSearch: "",
    vaultImgOrigin: "all",
    vaultImgUniqueOnly: false,
    vaultImgCat: "all",
    vaultImgSearch: "",
    triadFilter: "all",
    triadSearch: "",
    scriptMode: "full",
    promptFilter: "all",
    promptSearch: "",
    quoteCat: "all",
    quoteSearch: "",
    mediaDockFilter: "all",
    mediaActiveIndex: 0,
    reelAutoAnimate: true,
    checked: loadProgress()
  };

  function loadProgress() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function saveProgress() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.checked));
    } catch (e) {
      // ignore storage quota errors
    }
    updateTopProgress();
  }

  function esc(str) {
    if (str === null || str === undefined) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  var toastTimer = null;
  function showToast(msg) {
    var el = document.getElementById("studioToast");
    if (!el) return;
    el.textContent = msg;
    el.classList.add("visible");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      el.classList.remove("visible");
    }, 2400);
  }

  function copyText(text, label) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showToast("✓ Скопійовано: " + (label || "буфер обміну"));
      }).catch(function () {
        fallbackCopy(text, label);
      });
    } else {
      fallbackCopy(text, label);
    }
  }

  function fallbackCopy(text, label) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      showToast("✓ Скопійовано: " + (label || "буфер обміну"));
    } catch (e) {
      showToast("Не вдалося скопіювати автоматично");
    }
    document.body.removeChild(ta);
  }

  function downloadBlob(filename, content, mime) {
    var blob = new Blob([content], { type: mime || "text/plain;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 150);
    showToast("📥 Завантажено: " + filename);
  }

  function computeReadiness() {
    var sopTotal = 0;
    var sopDone = 0;
    (epData.sop_steps || []).forEach(function (st) {
      (st.tasks || []).forEach(function (t) {
        sopTotal += 1;
        if (state.checked[t.id]) sopDone += 1;
      });
    });

    var vidDone = 0;
    for (var i = 1; i <= 100; i++) {
      if (state.checked["vid_" + i]) vidDone += 1;
    }

    var importedMap = {};
    (window.SUNO_MASTER_POOL || []).forEach(function (t) {
      importedMap[t.smart_bin] = true;
      (t.extra_bins || []).forEach(function (eb) {
        importedMap[eb.smart_bin] = true;
      });
    });

    var sunoTotal = (epData.suno_registry || []).length || 16;
    var sunoDone = 0;
    for (var s = 0; s < sunoTotal; s++) {
      var sItem = (epData.suno_registry || [])[s];
      if (state.checked["suno_" + s] || (sItem && importedMap[sItem.filename])) sunoDone += 1;
    }

    var voTotal = (epData.vo_registry || []).length || 10;
    var voDone = 0;
    for (var v = 0; v < voTotal; v++) {
      if (state.checked["vo_" + v]) voDone += 1;
    }

    // Weighted studio readiness: 70% SOP milestones + 15% Video shots + 10% Suno + 5% VO
    var sopRatio = sopTotal > 0 ? sopDone / sopTotal : 0;
    var vidRatio = vidDone / 100;
    var sunoRatio = sunoDone / sunoTotal;
    var voRatio = voDone / voTotal;
    var pct = Math.round((sopRatio * 70) + (vidRatio * 15) + (sunoRatio * 10) + (voRatio * 5));
    if (sopDone === sopTotal && sopTotal > 0 && pct < 100 && vidDone === 0 && sunoDone === 0 && voDone === 0) {
      pct = 100;
    }
    return {
      pct: Math.min(100, pct),
      sopDone: sopDone,
      sopTotal: sopTotal,
      vidDone: vidDone,
      sunoDone: sunoDone,
      sunoTotal: sunoTotal,
      voDone: voDone,
      voTotal: voTotal
    };
  }

  function updateTopProgress() {
    var stats = computeReadiness();
    var fill = document.getElementById("epProgressFill");
    var lbl = document.getElementById("epProgressLabel");
    var badgeSop = document.getElementById("badgeSopCount");
    var badgeVid = document.getElementById("badgeVidCount");
    var badgeMediaTab = document.getElementById("badgeMediaTabCount");
    if (fill) fill.style.width = stats.pct + "%";
    if (lbl) lbl.textContent = stats.pct + "% (" + stats.sopDone + "/" + stats.sopTotal + " SOP)";
    if (badgeSop) badgeSop.textContent = stats.sopDone + "/" + stats.sopTotal;
    if (badgeVid) badgeVid.textContent = stats.vidDone + "/100";
    if (badgeMediaTab) {
      var vInv = (window.PROJECT_VAULT_INVENTORY || {})[epData.ep];
      if (vInv && vInv.summary) {
        badgeMediaTab.textContent = "🎥 " + (vInv.summary.videos_count || 0) + " • 🖼️ " + (vInv.summary.images_count || 0);
      }
    }
  }

  function textToSSML(cleanText) {
    var paragraphs = cleanText.split(/\n+/).map(function (p) { return p.trim(); }).filter(Boolean);
    var lines = [
      "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
      "<speak>",
      "  <!-- Стандарт Cinematic Thoughtcast: 115-120 слів/хв (Cloud TTS Chirp HD / Studio) -->",
      "  <prosody rate=\"84%\" pitch=\"-1.5st\">"
    ];
    paragraphs.forEach(function (p) {
      var escaped = p
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
      // Insert 1.0s breath pause before direct Ukrainian quotes «...»
      escaped = escaped.replace(/«/g, "<break time=\"1.0s\"/>«");
      lines.push("    <p>" + escaped + "</p>");
      lines.push("    <break time=\"0.8s\"/>");
    });
    lines.push("  </prosody>");
    lines.push("</speak>");
    return lines.join("\n");
  }

  function cleanTextForElevenLabs(cleanText) {
    return cleanText.replace(/«/g, "[deep breath] «");
  }

  function buildAIStudioPrompt(scriptText) {
    return [
      "[SYSTEM INSTRUCTION ДЛЯ GOOGLE AI STUDIO | Temp: 0.45 | Top-P: 0.85]",
      "Ти — головний технічний режисер та промпт-інженер документального проєкту «Cinematic Thoughtcast: Архітектори Розуму».",
      "Епізод " + epData.ep + ": " + epData.name + " («" + epData.title + "»).",
      "Конвертуй наведений дикторський сценарій у:",
      "1) Таблицю візуальних промптів для Google Flow / Google Veo (англійською) за формулою: [Camera Movement & Lens (" + epData.camera_lens + ")] + [Physical/Abstract Subject] + [Lighting & Color Palette (" + epData.visual_key + ")] + [35mm Film Grain, Kodak 2383, 4k 24fps]. ЗАБОРОНЕНО генерувати балакучі обличчя реальних людей. Кожні 12-15 секунд чергуй 3D-абстракцію Flow із тактильним макро Veo.",
      "2) Дикторський скрипт із розміткою SSML (<prosody rate=\"84%\" pitch=\"-1.5st\">, <break time=\"1.0s\"/> перед цитатами) під темп 115 слів/хв.",
      "",
      "=== ТЕКСТ СЦЕНАРІЮ ===",
      scriptText
    ].join("\n");
  }

  function generateSetupScript() {
    var epCode = "EP" + epData.ep;
    var folderName = epCode + "_" + epData.latin.replace(/\s+/g, "_");
    return [
      "#!/usr/bin/env bash",
      "# Автоматична ініціалізація структури епізоду " + epCode + " — " + epData.name,
      "# Стандарт DaVinci Resolve 19 Smart Bins (Cinematic Thoughtcast)",
      "set -euo pipefail",
      "",
      "BASE_DIR=\"${1:-./" + folderName + "}\"",
      "mkdir -p \"$BASE_DIR/01_VO_UA\"",
      "mkdir -p \"$BASE_DIR/01_VO_EN\"",
      "mkdir -p \"$BASE_DIR/02_MUS_92BPM\"",
      "mkdir -p \"$BASE_DIR/03_AMB\"",
      "mkdir -p \"$BASE_DIR/04_SFX\"",
      "mkdir -p \"$BASE_DIR/05_VID_4K_ACT1\"",
      "mkdir -p \"$BASE_DIR/05_VID_4K_ACT2\"",
      "mkdir -p \"$BASE_DIR/05_VID_4K_ACT3\"",
      "mkdir -p \"$BASE_DIR/05_VID_4K_ACT4\"",
      "mkdir -p \"$BASE_DIR/06_ARCHIVE_PARALLAX\"",
      "mkdir -p \"$BASE_DIR/07_DAVINCI_EXPORTS\"",
      "",
      "cat > \"$BASE_DIR/SMART_BINS_RULE.txt\" << 'EOF'",
      "Правило іменування Smart Bins: " + epData.smart_bin_rule,
      "Timeline: 3840x1606 (2.39:1 Anamorphic Scope) @ 24.000 fps",
      "Suno Tempo Lock: 92 BPM (1 такт = 2.61 с / 62-63 кадри)",
      "Fairlight Sidechain: A1 (Voice HPF 75Hz, +3.2kHz) -> Send 1 -> A2 (Music Listen 1, -24dB, 3.5:1, Attack 35ms, Release 400ms -> -3.2 dB)",
      "Color Tree: Node 1 Balance -> Node 2 Cyan/Gold Split -> Node 3 Rec709 Kodak 2383 D60 -> Node 4 35mm Grain (0.35)",
      "EOF",
      "",
      "echo \"✅ Структуру для " + epCode + " (" + epData.name + ") успішно створено у: $BASE_DIR\""
    ].join("\n");
  }

  function generateDaVinciMarkersCSV() {
    var rows = [
      "\"#\",\"Record In\",\"Record Out\",\" Color\",\"Notes\",\"Name\""
    ];
    var idx = 1;
    (epData.prompts_100 || []).forEach(function (p) {
      var color = p.is_key ? "Yellow" : (p.act === 1 ? "Blue" : (p.act === 2 ? "Cyan" : (p.act === 3 ? "Purple" : "Green")));
      var smpteIn = p.smpte || "01:00:00:00";
      var note = (p.filename + " | " + p.cue_ua).replace(/"/g, "'");
      var name = ("ACT" + p.act + " #" + String(p.num).padStart(3, "0") + (p.is_key ? " [KEY]" : "")).replace(/"/g, "'");
      rows.push("\"" + idx + "\",\"" + smpteIn + "\",\"" + smpteIn + "\",\"" + color + "\",\"" + note + "\",\"" + name + "\"");
      idx += 1;
    });
    return rows.join("\n");
  }



  function revealInFinder(filePath, label) {
    if (!filePath) return;
    var fullPath = filePath.startsWith("/")
      ? filePath
      : ("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/" + filePath);

    // Copy to clipboard immediately so the user always has the path
    copyText(fullPath, label || "шлях файлу");

    fetch("http://127.0.0.1:8765/reveal?path=" + encodeURIComponent(fullPath))
      .then(function (res) { return res.json(); })
      .then(function (data) {
        if (data.status === "ok") {
          showToast("📁 Відкрито у Finder: " + (label || fullPath.split("/").pop()));
        } else {
          showToast("📋 Шлях скопійовано: " + fullPath.split("/").pop());
        }
      })
      .catch(function () {
        showToast("📋 Шлях скопійовано! (Запустіть ./open_in_finder.sh --bridge)");
      });
  }

  function getVeoStatusMap() {
    try {
      var raw = localStorage.getItem("ai_titans_veo_status");
      if (raw) return JSON.parse(raw);
    } catch (e) {}
    var initMap = {};
    var pipeline = window.VEO_ANIMATION_PIPELINE || [];
    pipeline.forEach(function (item) {
      initMap[item.id] = !!item.default_done;
    });
    return initMap;
  }

  function setVeoStatus(id, isDone) {
    var map = getVeoStatusMap();
    map[id] = isDone;
    try {
      localStorage.setItem("ai_titans_veo_status", JSON.stringify(map));
    } catch (e) {}
    renderMedia();
    updateTopProgress();
  }

  function renderShell() {
    var switcherHtml = seasonIndex.map(function (item) {
      var activeCls = item.ep === epData.ep ? " active" : "";
      var fname = item.page_url.split("/").pop();
      return "<a class=\"ep-pill-link" + activeCls + "\" href=\"" + esc(fname) + "\" title=\"" + esc(item.name + " — " + item.title) + "\">EP" + esc(item.ep) + "</a>";
    }).join("");

    var epMediaInit = (window.MEDIA_ACQUISITION_POOL || {})[epData.ep] || {};
        var epVeos = (window.VEO_ANIMATION_PIPELINE || []).filter(function (v) { return v.ep === epData.ep; });
    var vStatusMap = getVeoStatusMap();
    var epVeoDone = epVeos.filter(function (v) { return !!vStatusMap[v.id]; }).length;
    var epVeoTotal = epVeos.length;
    var rawPhotosCount = ((window.MEDIA_ACQUISITION_POOL || {})[epData.ep] || {}).flow_gallery ? ((window.MEDIA_ACQUISITION_POOL || {})[epData.ep].flow_gallery || []).length : 12;

    var epThemeTrack = (epMediaInit.audio && epMediaInit.audio.length) ? epMediaInit.audio[0] : null;
    var soundscapeBar = epThemeTrack ? [
      "<div style=\"display:flex;align-items:center;justify-content:space-between;gap:8px;background:rgba(16,185,129,0.07);border:1px solid rgba(52,211,153,0.3);border-radius:8px;padding:6px 12px;margin-top:0.75rem;flex-wrap:wrap;\">",
      "  <div style=\"display:flex;align-items:center;gap:6px;\">",
      "    <span style=\"font-size:14px;\">🎧</span>",
      "    <span style=\"font-size:11.5px;color:var(--emerald);font-weight:600;\">Тема епізоду (Suno 92 BPM): <strong>" + esc(epThemeTrack.name) + "</strong> (" + esc(epThemeTrack.duration) + ")</span>",
      "    <span class=\"chip chip-emerald\" style=\"font-size:10px;\">A2 DaVinci Track</span>",
      "  </div>",
      "  <div style=\"display:flex;align-items:center;gap:8px;\">",
      "    <audio controls preload=\"none\" style=\"height:26px;width:210px;\" src=\"../assets/audio_previews/" + esc(epThemeTrack.preview) + "\"></audio>",
      "    <button class=\"btn\" style=\"padding:2px 7px;font-size:10.5px;\" data-copy-text=\"/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/suno_stems/" + esc(epThemeTrack.bin_dir) + "/" + esc(epThemeTrack.smart_bin) + "\">Шлях WAV</button>",
      "  </div>",
      "</div>"
    ].join("\n") : "";

    var pipelineBarHtml = [
      "<div class=\"pipeline-status-bar\" style=\"margin-top:0.85rem;background:rgba(15,23,42,0.85);border:1px solid rgba(56,189,248,0.32);border-radius:10px;padding:0.75rem 1rem;\">",
      "  <div style=\"display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;flex-wrap:wrap;gap:6px;\">",
      "    <div style=\"font-size:11px;font-weight:700;color:var(--cyan);text-transform:uppercase;letter-spacing:0.05em;display:flex;align-items:center;gap:6px;\">",
      "      <span>🏭 7-Стадійний Виробничий Конвеєр Епізоду " + esc(epData.ep) + "</span>",
      "      <span class=\"chip chip-cyan\">DaVinci Resolve 19 Workflow</span>",
      "    </div>",
      "    <div style=\"font-size:11px;color:var(--text-muted);\">115 WPM Диктор • 92 BPM Метроном • 4K Rec.709-A</div>",
      "  </div>",
      "  <div style=\"display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:6px;\">",
      "    <div style=\"padding:6px 8px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.3);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--emerald);font-weight:700;\">1. Сценарій (02_SCRIPTS)</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">✅ 4 Акти (100%)</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">" + esc(epData.script_total_words) + " слів диктора</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.35);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--amber);font-weight:700;\">2. Диктор (ElevenLabs)</div>",
      "      <div style=\"font-size:11px;color:var(--amber);font-weight:600;\">⏳ Текст готовий (115 WPM)</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">Очікує генерації WAV</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.3);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--emerald);font-weight:700;\">3. Музика Suno 92 BPM</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">✅ 4 Стеми у 03_AUDIO</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">A2 DaVinci Track</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.3);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--emerald);font-weight:700;\">4. Науковий VFX</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">✅ 4K Симуляція</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">V1 Video Track</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.3);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--emerald);font-weight:700;\">5. 2K Концепти</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">✅ " + rawPhotosCount + " Кадрів у базі</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">Midjourney / Flow</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:" + (epVeoDone === epVeoTotal ? "rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.3);" : "rgba(251,191,36,0.12);border:1px solid rgba(251,191,36,0.5);") + "border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--amber);font-weight:700;\">6. Veo Анімація</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">" + epVeoDone + " / " + epVeoTotal + " Готово</div>",
      "      <div style=\"font-size:9.5px;color:var(--amber);font-weight:600;\">⚡ ТОП-14 Кандидати</div>",
      "    </div>",
      "    <div style=\"padding:6px 8px;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.3);border-radius:6px;\">",
      "      <div style=\"font-size:10px;color:var(--purple);font-weight:700;\">7. DaVinci Resolve</div>",
      "      <div style=\"font-size:11px;color:var(--text-primary);font-weight:600;\">📦 Smart Bins Ready</div>",
      "      <div style=\"font-size:9.5px;color:var(--text-muted);\">Скрипти імпорту</div>",
      "    </div>",
      "  </div>",
      soundscapeBar,
      "</div>"
    ].join("\n");

    var vSummary = ((window.PROJECT_VAULT_INVENTORY || {})[epData.ep] || {}).summary || {};
    var totalVidClips = vSummary.videos_count || ((epMediaInit.archives || []).length + (epMediaInit.flow_queue || []).length + (epMediaInit.dossiers || []).length);
    var resDocsCount = vSummary.research_docs_count || 0;

    var contextLinksHtml = "<a class=\"btn-nav-stat\" href=\"../season1_telemetry_dashboard.html\">📊 Статистика (10 Героїв)</a>";
    contextLinksHtml += "<a class=\"btn-nav-context\" href=\"../media_vault_analysis.html?ep=" + esc(epData.ep) + "\">🗂️ Медіа-Волт</a>";
    if (epData.ep === "01") {
      contextLinksHtml += "<a class=\"btn-nav-context\" href=\"../cinematic_innovations.html\">🎬 20 Кіно-Фішок</a>";
    } else if (epData.ep === "02") {
      contextLinksHtml += "<a class=\"btn-nav-context\" href=\"../cinematic_innovations_ep02.html\">🎬 20 Тріад (Окрема)</a>";
    } else if (epData.ep === "03") {
      contextLinksHtml += "<a class=\"btn-nav-context\" href=\"../50_scenes_hassabis.html\">🎯 50 Сюжетів Хассабіса</a>";
      contextLinksHtml += "<a class=\"btn-nav-context\" href=\"../cinematic_innovations_ep03.html\">🎬 30 Тріад (Окрема)</a>";
    }

    var app = document.getElementById("episodeApp");
    app.innerHTML = [
      "<header class=\"ep-topbar\">",
      "  <div class=\"ep-topbar-inner\">",
      "    <div class=\"nav-hub-group\">",
      "      <a class=\"btn-back-hub\" href=\"../index.html\">← Головний Хаб</a>",
      contextLinksHtml,
      "      <nav class=\"ep-switcher\" aria-label=\"Швидкий перехід між епізодами\">" + switcherHtml + "</nav>",
      "    </div>",
      "    <div class=\"topbar-progress-wrap\">",
      "      <button class=\"btn btn-amber\" id=\"btnTopOpenCinema\" style=\"padding:4px 10px;font-size:11.5px;\" title=\"Відкрити спливаючий відеоплеєр з усіма архівами та майбутніми футажами\">🎬 Відео-Монітор (" + totalVidClips + " відео)</button>",
      "      <span style=\"font-size:11.5px;color:var(--text-secondary);\">Готовність випуску:</span>",
      "      <div class=\"progress-track\"><div class=\"progress-fill\" id=\"epProgressFill\" style=\"width:0%\"></div></div>",
      "      <span class=\"progress-label\" id=\"epProgressLabel\">0%</span>",
      "    </div>",
      "  </div>",
      "</header>",

      "<main class=\"ep-shell\">",
      "  <section class=\"hero-banner\">",
      "    <div class=\"hero-portrait-box\">",
      "      <img src=\"../assets/avatars/" + esc(epData.avatar) + "\" alt=\"" + esc(epData.name) + "\">",
      "      <span class=\"hero-ep-tag\">EP " + esc(epData.ep) + "</span>",
      "    </div>",
      "    <div>",
      "      <div class=\"hero-meta-top\">",
      "        <span class=\"chip chip-cyan\">МАСТЕР-ДОСЬЄ ЕПІЗОДУ " + esc(epData.ep) + "</span>",
      "        <span class=\"chip chip-purple\">" + esc(epData.archetype) + "</span>",
      "        <span class=\"chip chip-emerald\">" + esc(epData.duration) + " • " + esc(epData.script_total_words) + " слів диктора</span>",
      "        <span class=\"chip chip-amber\">100 промптів • 100 цитат • 16 WAV</span>",
      "        <button class=\"btn btn-cyan\" id=\"btnHeroJumpMedia\" style=\"padding:2px 9px;font-size:11px;\">🎬 Відео & Архів (" + totalVidClips + ")</button>",
      "        <button class=\"btn btn-amber\" id=\"btnHeroJumpTriads\" style=\"padding:2px 10px;font-size:11px;font-weight:700;\">🎯 Документальні Сюжети (" + getTriadsEp().length + "×3)</button>",
      (resDocsCount ? ("        <button class=\"btn btn-purple\" id=\"btnHeroJumpResearch\" style=\"padding:2px 9px;font-size:11px;\">📚 Джерела & Транскрипти (" + resDocsCount + ")</button>") : ""),
      "      </div>",
      "      <div class=\"hero-title-row\">",
      "        <h1>" + esc(epData.name) + "</h1>",
      "        <span class=\"hero-latin\">// " + esc(epData.latin) + "</span>",
      "      </div>",
      "      <div class=\"hero-subtitle\">«" + esc(epData.title) + "» — " + esc(epData.role) + "</div>",
      "      <div class=\"hero-quote-callout\">" + esc(epData.key_quote) + "</div>",
      "      <div class=\"hero-specs-grid\">",
      "        <div class=\"spec-mini-box\"><div class=\"spec-mini-label\">Метроном та сітка монтажу</div><div class=\"spec-mini-val\">" + esc(epData.bpm) + " (такт 2.61с / 62 кадри)</div></div>",
      "        <div class=\"spec-mini-box\"><div class=\"spec-mini-label\">Темп та озвучка (UA + EN)</div><div class=\"spec-mini-val\">" + esc(epData.wpm) + " • " + esc(epData.vo_settings) + "</div></div>",
      "        <div class=\"spec-mini-box\"><div class=\"spec-mini-label\">Візуальна палітра</div><div class=\"spec-mini-val\">" + esc(epData.visual_key) + "</div></div>",
      "        <div class=\"spec-mini-box\"><div class=\"spec-mini-label\">Віртуальна камера та лінзи</div><div class=\"spec-mini-val\">" + esc(epData.camera_lens) + "</div></div>",
      "      </div>",
      pipelineBarHtml,
      "    </div>",
      "  </section>",

      "  <nav class=\"studio-tabs\" id=\"studioTabs\">",
      "    <button class=\"studio-tab-btn active\" data-tab=\"sop\">🧭 1. Алгоритм дій (SOP) <span class=\"tab-count-badge\" id=\"badgeSopCount\">0/22</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"bio\">🧬 2. Біографія, кризи & Джерела <span class=\"tab-count-badge\">" + ((epData.biography || []).length + (resDocsCount ? (" • " + resDocsCount + " док.") : "")) + "</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"script\">🎬 3. Режисерський сценарій <span class=\"tab-count-badge\">4 акти</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"prompts\">🎥 4. 100 Візуальних промптів <span class=\"tab-count-badge\" id=\"badgeVidCount\">0/100</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"quotes\">💬 5. 100 Цитат і тез <span class=\"tab-count-badge\">100</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"audio\">🎵 6. Suno 92 BPM & Озвучка <span class=\"tab-count-badge\">4/4 Актів WAV</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"media\">🗂️ 7. Медіа-Пул, Архіви & Відео <span class=\"tab-count-badge\" id=\"badgeMediaTabCount\">🎬 " + totalVidClips + " MP4</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"davinci\">🎚️ 8. DaVinci Resolve 19 Студія</button>",
      "  </nav>",

      "  <div id=\"pane-sop\" class=\"tab-pane active\"></div>",
      "  <div id=\"pane-bio\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-script\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-prompts\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-quotes\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-audio\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-media\" class=\"tab-pane\"></div>",
      "  <div id=\"pane-davinci\" class=\"tab-pane\"></div>",
      "</main>",
      "<div class=\"cinema-modal-backdrop\" id=\"videoLightboxModal\"></div>",
      "<div class=\"studio-toast\" id=\"studioToast\"></div>"
    ].join("\n");

    document.getElementById("studioTabs").addEventListener("click", function (ev) {
      var btn = ev.target.closest(".studio-tab-btn");
      if (!btn) return;
      switchTab(btn.getAttribute("data-tab"), true);
    });

    var topCinemaBtn = document.getElementById("btnTopOpenCinema");
    if (topCinemaBtn) {
      topCinemaBtn.addEventListener("click", function () {
        openCinemaModal(state.mediaActiveIndex || 0);
      });
    }

    var heroJumpBtn = document.getElementById("btnHeroJumpMedia");
    if (heroJumpBtn) {
      heroJumpBtn.addEventListener("click", function () {
        switchTab("media-videos", true);
      });
    }
    var heroTriadJumpBtn = document.getElementById("btnHeroJumpTriads");
    if (heroTriadJumpBtn) {
      heroTriadJumpBtn.addEventListener("click", function () {
        switchTab("media-triads", true);
      });
    }
    var heroResJumpBtn = document.getElementById("btnHeroJumpResearch");
    if (heroResJumpBtn) {
      heroResJumpBtn.addEventListener("click", function () {
        switchTab("bio", true);
      });
    }
  }

  function switchTab(tabId, updateHash) {
    if (tabId) tabId = String(tabId).replace(/^pane-/, "");
    var rawHash = tabId;
    if (tabId && tabId.indexOf("media-") === 0) {
      var subPart = tabId.slice("media-".length);
      if (["videos", "images", "triads", "veo", "archives"].indexOf(subPart) !== -1) {
        state.mediaSubTab = subPart;
      }
      tabId = "media";
      renderMedia();
    }
    var valid = ["sop", "bio", "script", "prompts", "quotes", "audio", "media", "davinci"];
    if (valid.indexOf(tabId) === -1) {
      tabId = "sop";
      rawHash = "sop";
    }
    state.activeTab = tabId;

    var btns = document.querySelectorAll(".studio-tab-btn");
    for (var i = 0; i < btns.length; i++) {
      btns[i].classList.toggle("active", btns[i].getAttribute("data-tab") === tabId);
    }
    for (var j = 0; j < valid.length; j++) {
      var pane = document.getElementById("pane-" + valid[j]);
      if (pane) pane.classList.toggle("active", valid[j] === tabId);
    }
    if (updateHash) {
      try {
        history.replaceState(null, "", "#" + rawHash);
      } catch (e) {
        window.location.hash = rawHash;
      }
    }
  }

  /* ---------------- TAB 1: SOP ALGORITHM ---------------- */
  function renderSOP() {
    var pane = document.getElementById("pane-sop");
    var stagesHtml = (epData.sop_steps || []).map(function (st) {
      var doneInStage = 0;
      var tasksHtml = (st.tasks || []).map(function (t) {
        var isChecked = !!state.checked[t.id];
        if (isChecked) doneInStage += 1;
        return [
          "<label class=\"sop-task-item" + (isChecked ? " checked" : "") + "\" data-task-id=\"" + esc(t.id) + "\">",
          "  <input type=\"checkbox\" class=\"sop-checkbox\" data-sop-check=\"" + esc(t.id) + "\"" + (isChecked ? " checked" : "") + ">",
          "  <span class=\"sop-task-text\">" + esc(t.text) + "</span>",
          "</label>"
        ].join("\n");
      }).join("\n");

      var totalInStage = (st.tasks || []).length;
      var completeCls = (doneInStage === totalInStage && totalInStage > 0) ? " stage-complete" : "";

      return [
        "<div class=\"sop-stage-card" + completeCls + "\">",
        "  <div class=\"sop-stage-header\">",
        "    <div>",
        "      <span class=\"sop-step-num\">ЕТАП " + esc(st.step) + " • " + esc(st.phase) + "</span>",
        "      <div class=\"sop-stage-title\">" + esc(st.title) + "</div>",
        "      <div class=\"sop-stage-goal\">🎯 Критерій готовності: " + esc(st.goal) + "</div>",
        "    </div>",
        "    <span class=\"chip " + (completeCls ? "chip-emerald" : "") + "\">" + doneInStage + " / " + totalInStage + " виконано</span>",
        "  </div>",
        "  <div class=\"sop-task-list\">" + tasksHtml + "</div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var allVoText = (epData.full_acts || []).map(function (act) {
      return "=== " + act.title + " ===\n" + (act.scenes || []).map(function (sc) {
        return "[" + sc.tc + "] " + sc.narration;
      }).join("\n\n");
    }).join("\n\n====================\n\n");

    var scriptDir = (epData.script_md_path || "").split("/").slice(0, 2).join("/") || ("02_SCRIPTS/episode_" + epData.ep);
    var voMasterRelPath = scriptDir + "/EP" + epData.ep + "_VO_UA_ELEVENLABS_MASTER.txt";

    var voMasterBoxHtml = [
      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.45);background:linear-gradient(180deg,rgba(56,189,248,0.06),transparent);margin-bottom:1rem;\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\" style=\"color:var(--cyan);display:flex;align-items:center;gap:8px;\">",
      "        🎙️ 2. Закадровий Голос Диктора (ElevenLabs 115 WPM • Українська версія)",
      "        <span class=\"chip chip-amber\">⏳ Текст 100% Готовий • Очікує Генерації WAV</span>",
      "      </div>",
      "      <div class=\"panel-desc\">",
      "        Текст сценарію відкалібровано під темп 115 слів/хв (швидкість 0.86) для ідеального попадання в такт музики Suno 92 BPM. Самі аудіодоріжки (WAV) ще не згенеровані. Натисніть кнопку нижче, щоб скопіювати весь текст або відкрити файл у Finder для завантаження в ElevenLabs.",
      "      </div>",
      "    </div>",
      "    <div style=\"display:flex;gap:6px;align-items:center;flex-wrap:wrap;\">",
      "      <button class=\"btn btn-emerald\" id=\"btnCopyFullVoTxt\" style=\"padding:5px 10px;font-size:11.5px;font-weight:700;\">📋 Скопіювати повний текст для ElevenLabs</button>",
      "      <button class=\"btn btn-cyan\" id=\"btnOpenVoInFinder\" style=\"padding:5px 10px;font-size:11.5px;\">📁 Відкрити TXT у Finder</button>",
      "    </div>",
      "  </div>",
      "  <div style=\"background:rgba(0,0,0,0.35);border:1px solid var(--border);border-radius:8px;padding:9px 12px;font-size:11.5px;color:var(--text-secondary);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;\">",
      "    <div>",
      "      <span>Файл майстра: </span><code style=\"color:var(--cyan);\">" + esc(voMasterRelPath) + "</code>",
      "    </div>",
      "    <div style=\"display:flex;gap:6px;flex-wrap:wrap;\">",
      "      <span class=\"chip chip-purple\">Speed: 0.86 (115 WPM)</span>",
      "      <span class=\"chip chip-purple\">Stability: 55%</span>",
      "      <span class=\"chip chip-purple\">Clarity: 85%</span>",
      "      <span class=\"chip chip-cyan\">Доріжка DaVinci: A1</span>",
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n");

    pane.innerHTML = [
      voMasterBoxHtml,
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🧭 Покроковий алгоритм дій (SOP) — Віртуальна кіностудія одного шоуранера</div>",
      "      <div class=\"panel-desc\">Повний виробничий маршрут від ініціалізації папок до релізу двомовного 4K-майстра на YouTube. Усі відмітки автоматично зберігаються у браузері та синхронізуються з головним дашбордом.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-emerald\" id=\"btnDownloadSetupSop\">📥 Завантажити setup_EP" + esc(epData.ep) + ".sh</button>",
      "      <button class=\"btn btn-cyan\" id=\"btnDownloadMarkersSop\">📥 Маркери DaVinci (.csv)</button>",
      "      <button class=\"btn\" id=\"btnResetSop\">↺ Скинути чекліст</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"sprint-strip\">",
      "    <div class=\"sprint-day-card\"><div class=\"sprint-day-tag\">День 1 • Дослідження</div><div class=\"sprint-day-title\">NotebookLM + Сценарій</div><div class=\"sprint-day-dod\">100 цитат, кризові точки та вивірений 4-актний сценарій (UA + EN).</div></div>",
      "    <div class=\"sprint-day-card\"><div class=\"sprint-day-tag\">День 2 • Аудіо-каркас</div><div class=\"sprint-day-title\">ElevenLabs + Suno 92 BPM</div><div class=\"sprint-day-dod\">Доріжки голосу WAV 48kHz (115 WPM) + 16 треків/стемів у 03_AUDIO/.</div></div>",
      "    <div class=\"sprint-day-card\"><div class=\"sprint-day-tag\">День 3 • Генерація VFX</div><div class=\"sprint-day-title\">Google Veo + Google Flow</div><div class=\"sprint-day-dod\">Пакетний рендер 4K 24fps (чергування макро-фізики та 3D кожні 12–15 с).</div></div>",
      "    <div class=\"sprint-day-card\"><div class=\"sprint-day-tag\">День 4 • Пост-продакшн</div><div class=\"sprint-day-title\">DaVinci Resolve 19 Studio</div><div class=\"sprint-day-dod\">Сітка 92 BPM, Fairlight -3.2dB, Kodak 2383 D60, титри Fusion Inter +0.04.</div></div>",
      "    <div class=\"sprint-day-card\"><div class=\"sprint-day-tag\">День 5 • Реліз</div><div class=\"sprint-day-title\">YouTube Multi-Audio + Shorts</div><div class=\"sprint-day-dod\">4K Master з двома аудіодоріжками (UA + EN) та 3 вертикальні Shorts.</div></div>",
      "  </div>",
      "  <div class=\"sop-grid\">" + stagesHtml + "</div>",
      "</div>"
    ].join("\n");

    pane.querySelectorAll("[data-sop-check]").forEach(function (chk) {
      chk.addEventListener("change", function () {
        var id = chk.getAttribute("data-sop-check");
        if (chk.checked) {
          state.checked[id] = true;
        } else {
          delete state.checked[id];
        }
        saveProgress();
        renderSOP();
      });
    });

    var copyVoBtn = document.getElementById("btnCopyFullVoTxt");
    if (copyVoBtn) {
      copyVoBtn.addEventListener("click", function () {
        copyText(cleanTextForElevenLabs(allVoText), "повний дикторський текст EP" + epData.ep + " для ElevenLabs");
      });
    }

    var openVoBtn = document.getElementById("btnOpenVoInFinder");
    if (openVoBtn) {
      openVoBtn.addEventListener("click", function () {
        revealInFinder(voMasterRelPath, "Майстер-текст диктора EP" + epData.ep);
      });
    }

    document.getElementById("btnDownloadSetupSop").addEventListener("click", function () {
      downloadBlob("setup_EP" + epData.ep + ".sh", generateSetupScript(), "text/x-shellscript;charset=utf-8");
    });
    document.getElementById("btnDownloadMarkersSop").addEventListener("click", function () {
      downloadBlob("EP" + epData.ep + "_DaVinci_Markers_24fps.csv", generateDaVinciMarkersCSV(), "text/csv;charset=utf-8");
    });
    document.getElementById("btnResetSop").addEventListener("click", function () {
      if (window.confirm("Скинути всі позначки виконання для Епізоду " + epData.ep + "?")) {
        state.checked = {};
        saveProgress();
        renderSOP();
        renderPrompts();
        renderAudio();
        showToast("Прогрес епізоду скинуто");
      }
    });
  }

  /* ---------------- TAB 2: BIOGRAPHY & NOTEBOOKLM ---------------- */
  function renderBio() {
    var pane = document.getElementById("pane-bio");
    var surname = epData.latin.split(" ").pop();
    var nbName = "AI_Titans_Ep" + epData.ep + "_" + surname;
    var nbPrompt = "Focus heavily on childhood psychological resilience, the darkest moment of career crisis, and philosophical principles for personal growth of " + epData.latin + ".";
    var rows = (epData.biography || []).map(function (b) {
      return [
        "<div class=\"bio-row\">",
        "  <div class=\"bio-stage\">" + esc(b.stage) + "</div>",
        "  <div class=\"bio-detail\">" + esc(b.detail) + "</div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var vEp = getVaultEp();
    var rDocs = vEp.research_docs || [];
    var rSum = vEp.summary || {};
    var docFilter = state.bioDocCat || "all";
    var docQuery = (state.bioDocSearch || "").trim().toLowerCase();

    var docCounts = { all: rDocs.length };
    rDocs.forEach(function (d) {
      docCounts[d.cat] = (docCounts[d.cat] || 0) + 1;
    });

    var filteredDocs = rDocs.filter(function (d) {
      if (docFilter !== "all" && d.cat !== docFilter) return false;
      if (docQuery && (d.title + " " + d.file + " " + d.cat_label + " " + (d.source_url || "")).toLowerCase().indexOf(docQuery) === -1) return false;
      return true;
    });

    var docCatOrder = [
      ["all", "📦 Усі (" + rDocs.length + ")"],
      ["transcript", "🎙️ Транскрипти (" + (docCounts.transcript || 0) + ")"],
      ["article", "📰 Статті & arXiv (" + (docCounts.article || 0) + ")"],
      ["registry", "🗂️ Реєстри (" + (docCounts.registry || 0) + ")"],
      ["dossier", "🧬 Досьє (" + (docCounts.dossier || 0) + ")"],
      ["pdf_md", "📕 PDF/MD (" + (docCounts.pdf_md || 0) + ")"]
    ];

    var docPillsHtml = docCatOrder.map(function (pair) {
      return "<button class=\"filter-pill" + (docFilter === pair[0] ? " active" : "") + "\" data-bio-doc-cat=\"" + pair[0] + "\">" + pair[1] + "</button>";
    }).join("");

    var docsGridHtml = filteredDocs.map(function (d) {
      var metaParts = [d.ext];
      if (d.word_count > 0) metaParts.push(d.word_count.toLocaleString("uk-UA") + " слів");
      if (d.size_kb > 0) metaParts.push(d.size_kb + " KB");
      return [
        "<div style=\"background:rgba(15,23,42,0.72);border:1px solid var(--border);border-radius:10px;padding:0.75rem 0.9rem;display:flex;flex-direction:column;gap:6px;justify-content:space-between;\">",
        "  <div>",
        "    <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:4px;flex-wrap:wrap;\">",
        "      <span class=\"chip chip-cyan\" style=\"font-size:10.5px;\">" + esc(d.cat_label) + "</span>",
        "      <span style=\"font-family:var(--mono);font-size:10.5px;color:var(--text-muted);\">" + esc(metaParts.join(" • ")) + "</span>",
        "    </div>",
        "    <div style=\"font-size:13px;font-weight:700;color:var(--text-primary);line-height:1.35;margin-bottom:4px;\">" + esc(d.title) + "</div>",
        "    <div style=\"font-family:var(--mono);font-size:10.5px;color:var(--cyan);word-break:break-all;\">" + esc(d.rel_path) + "</div>",
        "  </div>",
        "  <div class=\"btn-group\" style=\"margin-top:4px;\">",
        (d.source_url ? ("    <a class=\"btn btn-emerald\" style=\"padding:3px 8px;font-size:11px;text-decoration:none;\" href=\"" + esc(d.source_url) + "\" target=\"_blank\" rel=\"noopener\">🌐 Першоджерело ↗</a>") : ""),
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-reveal-finder=\"" + esc(d.rel_path) + "\">📁 Finder</button>",
        "    <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" data-copy-doc-path=\"" + esc(d.rel_path) + "\">📋 Шлях</button>",
        "  </div>",
        "</div>"
      ].filter(Boolean).join("\n");
    }).join("\n");

    var researchPanelHtml = [
      "<div class=\"panel-card\" style=\"margin-top:1rem;border-color:rgba(56,189,248,0.4);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">📚 База Знань, Транскрипти, Статті & Реєстри NotebookLM — EP" + esc(epData.ep) + " (" + rDocs.length + " файлів)</div>",
      "      <div class=\"panel-desc\">Повний локальний корпус першоджерел: <b>" + (rSum.transcripts_count || 0) + " транскриптів</b>, <b>" + (rSum.articles_count || 0) + " наукових статей</b> та <b>" + ((rSum.research_words || 0).toLocaleString("uk-UA")) + " слів</b> фактажу для NotebookLM та сценарію.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-amber\" id=\"btnBioJumpArchives\">📼 Відео-архіви & Фото (#media-archives) →</button>",
      "      <a class=\"btn btn-cyan\" style=\"text-decoration:none;\" href=\"../media_vault_analysis.html?ep=" + esc(epData.ep) + "\">🗂️ Медіа-Волт (Усі файли) →</a>",
      "    </div>",
      "  </div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">" + docPillsHtml + "</div>",
      "    <input type=\"search\" id=\"bioDocSearchInput\" class=\"search-input\" placeholder=\"Пошук транскрипту, arXiv або PDF...\" value=\"" + esc(state.bioDocSearch || "") + "\">",
      "  </div>",
      "  <div style=\"display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:0.75rem;\">" + (docsGridHtml || "<div style='color:var(--text-muted);padding:1rem;'>Документів за цим фільтром не знайдено.</div>") + "</div>",
      "</div>"
    ].join("\n");

    pane.innerHTML = [
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🧬 Хронологічне досьє, злами та точки опори — " + esc(epData.name) + "</div>",
      "      <div class=\"panel-desc\">Верифікована біографічна матриця Мастер-Досьє для фактчекінгу закадрового наративу та титрів.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-cyan\" id=\"btnCopyNbName\">📋 Назва блокнота: " + esc(nbName) + "</button>",
      "      <button class=\"btn btn-purple\" id=\"btnCopyNbPrompt\">🎧 Інструкція Audio Overview (NotebookLM)</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"bio-timeline\">" + rows + "</div>",
      "</div>",
      researchPanelHtml
    ].join("\n");

    document.getElementById("btnCopyNbName").addEventListener("click", function () {
      copyText(nbName, "назва блокнота NotebookLM");
    });
    document.getElementById("btnCopyNbPrompt").addEventListener("click", function () {
      copyText(nbPrompt, "інструкція Audio Overview для NotebookLM");
    });
    var bioArchBtn = document.getElementById("btnBioJumpArchives");
    if (bioArchBtn) {
      bioArchBtn.addEventListener("click", function () {
        switchTab("media-archives", true);
      });
    }
    pane.querySelectorAll("[data-bio-doc-cat]").forEach(function (pill) {
      pill.addEventListener("click", function () {
        state.bioDocCat = pill.getAttribute("data-bio-doc-cat");
        renderBio();
      });
    });
    var docSearchEl = document.getElementById("bioDocSearchInput");
    if (docSearchEl) {
      docSearchEl.addEventListener("input", function () {
        state.bioDocSearch = docSearchEl.value || "";
        renderBio();
        var refEl = document.getElementById("bioDocSearchInput");
        if (refEl) {
          refEl.focus();
          try { var L = refEl.value.length; refEl.setSelectionRange(L, L); } catch (e) {}
        }
      });
    }
    pane.querySelectorAll("[data-copy-doc-path]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        copyText(btn.getAttribute("data-copy-doc-path"), "шлях першоджерела");
      });
    });
  }

  /* ---------------- TAB 3: DIRECTOR'S SCRIPT ---------------- */
  function renderScript() {
    var pane = document.getElementById("pane-script");
    var fullAllVo = (epData.full_acts || []).map(function (a) { return a.clean_vo || ""; }).join("\n\n");
    var estMinutes = Math.max(1, Math.round((epData.script_total_words || 1350) / 115));

    var actsHtml = "";
    if (state.scriptMode === "full") {
      actsHtml = (epData.full_acts || []).map(function (act, idx) {
        var scenesHtml = (act.scenes || []).map(function (sc) {
          return [
            "<div class=\"scene-block\">",
            "  <div class=\"scene-meta-row\">",
            "    <span class=\"tc-badge\">⏱ " + esc(sc.tc) + "</span>",
            sc.sfx ? ("<span class=\"cue-tag\">🔊 " + esc(sc.sfx) + "</span>") : "",
            "    <span class=\"chip\">" + esc(sc.word_count) + " слів</span>",
            "  </div>",
            sc.prompt ? ("<div class=\"scene-prompt-preview\">🎥 VEO / FLOW: " + esc(sc.prompt) + "</div>") : "",
            "  <div class=\"scene-narration\">" + esc(sc.narration) + "</div>",
            "</div>"
          ].join("\n");
        }).join("\n");

        return [
          "<div class=\"act-card\">",
          "  <div class=\"act-header\">",
          "    <div>",
          "      <div class=\"act-title\">АКТ " + esc(act.actNum) + ": " + esc(act.title) + " (" + esc(act.time) + ")</div>",
          "      <div class=\"act-music-bar\">🎵 " + esc(act.music_desc) + " • " + esc(act.word_count) + " слів (~" + Math.max(1, Math.round((act.word_count || 300) / 115)) + " хв @ 115 WPM)</div>",
          "    </div>",
          "    <div class=\"btn-group\">",
          "      <button class=\"btn btn-emerald\" data-copy-act-vo=\"" + idx + "\">🎙️ Текст Акту " + esc(act.actNum) + " (ElevenLabs)</button>",
          "      <button class=\"btn btn-purple\" data-copy-act-ssml=\"" + idx + "\">🔊 SSML Акту " + esc(act.actNum) + "</button>",
          "    </div>",
          "  </div>",
          scenesHtml,
          "</div>"
        ].join("\n");
      }).join("\n");
    } else {
      actsHtml = (epData.beat_acts || []).map(function (act) {
        var beatsHtml = (act.beats || []).map(function (b) {
          var cuesBadges = (b.cues || []).map(function (c) {
            return "<span class=\"cue-tag\">" + esc(c) + "</span>";
          }).join(" ");
          return [
            "<div class=\"scene-block\">",
            "  <div class=\"scene-meta-row\"><span class=\"tc-badge\">⏱ " + esc(b.tc) + "</span> " + cuesBadges + "</div>",
            "  <div class=\"scene-narration\">" + esc(b.narration) + "</div>",
            "</div>"
          ].join("\n");
        }).join("\n");

        return [
          "<div class=\"act-card\">",
          "  <div class=\"act-header\">",
          "    <div>",
          "      <div class=\"act-title\">АКТ " + esc(act.actNum) + ": " + esc(act.title) + " (" + esc(act.time) + ")</div>",
          "      <div class=\"act-music-bar\">🎵 Smart Bin Music Stem: " + esc(act.music_file) + "</div>",
          "    </div>",
          "  </div>",
          beatsHtml,
          "</div>"
        ].join("\n");
      }).join("\n");
    }

    pane.innerHTML = [
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎬 Режисерський 4-актний сценарій — " + esc(epData.script_total_words) + " слів (~" + estMinutes + " хв чистого голосу + паузи = " + esc(epData.duration) + ")</div>",
      "      <div class=\"panel-desc\">Перемикайтеся між повним дикторським текстом і монтажною картою Мастер-Досьє з точними іменами аудіо/відео файлів.</div>",
      "    </div>",
      "    <div class=\"mode-toggle-bar\">",
      "      <button class=\"mode-btn" + (state.scriptMode === "full" ? " active" : "") + "\" data-script-mode=\"full\">📜 Повний дикторський сценарій</button>",
      "      <button class=\"mode-btn" + (state.scriptMode === "beats" ? " active" : "") + "\" data-script-mode=\"beats\">🎞️ Монтажна карта Мастер-Досьє</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"btn-group\" style=\"margin-bottom:1rem;\">",
      "    <button class=\"btn btn-emerald\" id=\"btnCopyAllEleven\">🎙️ Копіювати весь чистий текст для ElevenLabs (Speed 0.86)</button>",
      "    <button class=\"btn btn-purple\" id=\"btnCopyAllSSML\">🔊 Копіювати повний SSML-код (Cloud TTS 84% / -1.5st)</button>",
      "    <button class=\"btn btn-cyan\" id=\"btnCopyAIStudio\">🤖 Промпт + Сценарій для Google AI Studio (Temp 0.45)</button>",
      "    <button class=\"btn\" id=\"btnDownloadSSMLFile\">📥 Завантажити EP" + esc(epData.ep) + "_voiceover.ssml</button>",
      "  </div>",
      actsHtml,
      "</div>"
    ].join("\n");

    pane.querySelectorAll("[data-script-mode]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.scriptMode = b.getAttribute("data-script-mode");
        renderScript();
      });
    });

    document.getElementById("btnCopyAllEleven").addEventListener("click", function () {
      copyText(cleanTextForElevenLabs(fullAllVo), "чистий дикторський текст усіх 4 актів (ElevenLabs)");
    });
    document.getElementById("btnCopyAllSSML").addEventListener("click", function () {
      copyText(textToSSML(fullAllVo), "SSML-розмітка всього епізоду (115 WPM)");
    });
    document.getElementById("btnCopyAIStudio").addEventListener("click", function () {
      copyText(buildAIStudioPrompt(fullAllVo), "системний пакет для Google AI Studio");
    });
    document.getElementById("btnDownloadSSMLFile").addEventListener("click", function () {
      downloadBlob("EP" + epData.ep + "_" + epData.page_slug + "_voiceover.ssml", textToSSML(fullAllVo), "application/ssml+xml;charset=utf-8");
    });

    pane.querySelectorAll("[data-copy-act-vo]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-act-vo"), 10);
        var act = epData.full_acts[i];
        if (act) copyText(cleanTextForElevenLabs(act.clean_vo || ""), "чистий текст Акту " + act.actNum);
      });
    });

    pane.querySelectorAll("[data-copy-act-ssml]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-act-ssml"), 10);
        var act = epData.full_acts[i];
        if (act) copyText(textToSSML(act.clean_vo || ""), "SSML-код Акту " + act.actNum);
      });
    });
  }

  /* ---------------- TAB 4: 100 VISUAL PROMPTS ---------------- */
  function renderPrompts() {
    var pane = document.getElementById("pane-prompts");
    var q = state.promptSearch.trim().toLowerCase();

    var filtered = (epData.prompts_100 || []).filter(function (p) {
      if (state.promptFilter === "key" && !p.is_key) return false;
      if (state.promptFilter === "act1" && p.act !== 1) return false;
      if (state.promptFilter === "act2" && p.act !== 2) return false;
      if (state.promptFilter === "act3" && p.act !== 3) return false;
      if (state.promptFilter === "act4" && p.act !== 4) return false;
      if (state.promptFilter === "todo" && state.checked["vid_" + p.num]) return false;
      if (q) {
        var hay = (p.prompt + " " + p.cue_ua + " " + p.filename + " " + p.tc).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });

    var cardsHtml = filtered.map(function (p) {
      var isDone = !!state.checked["vid_" + p.num];
      var isFlow = /abstract|neural|lattice|geometric|vector|node|cosmic|orbital|particle/i.test(p.prompt);
      var engineTag = isFlow ? "Google Flow (3D Абстракція)" : "Google Veo (Макро-реалізм)";
      return [
        "<div class=\"prompt-card" + (p.is_key ? " is-key-shot" : "") + (isDone ? " done-shot" : "") + "\">",
        "  <div class=\"prompt-top\">",
        "    <div style=\"display:flex;gap:6px;align-items:center;flex-wrap:wrap;\">",
        "      <span class=\"chip chip-cyan\">#" + String(p.num).padStart(3, "0") + " • АКТ " + p.act + "</span>",
        "      <span class=\"tc-badge\">" + esc(p.tc) + "</span>",
        p.is_key ? "<span class=\"chip chip-amber\">⭐ Канон</span>" : "",
        "      <span class=\"chip\">" + engineTag + "</span>",
        "    </div>",
        "    <label style=\"display:inline-flex;align-items:center;gap:5px;font-size:11.5px;cursor:pointer;color:var(--emerald);font-weight:600;\">",
        "      <input type=\"checkbox\" class=\"sop-checkbox\" data-vid-check=\"" + p.num + "\"" + (isDone ? " checked" : "") + "> Готово",
        "    </label>",
        "  </div>",
        "  <div class=\"prompt-cue-ua\">🎙️ «" + esc(p.cue_ua) + "»</div>",
        "  <div class=\"prompt-en-box\">" + esc(p.prompt) + "</div>",
        "  <div class=\"prompt-file-row\">",
        "    <span class=\"filename-mono\">" + esc(p.filename) + "</span>",
        "    <div class=\"btn-group\">",
        "      <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-copy-prompt=\"" + p.num + "\">Копіювати промпт</button>",
        "      <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" data-copy-vfile=\"" + p.num + "\">Ім'я .mp4</button>",
        "    </div>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var filters = [
      { id: "all", label: "Усі (100)" },
      { id: "key", label: "⭐ Ключові кадри" },
      { id: "act1", label: "Акт 1 (001–025)" },
      { id: "act2", label: "Акт 2 (026–050)" },
      { id: "act3", label: "Акт 3 (051–075)" },
      { id: "act4", label: "Акт 4 (076–100)" },
      { id: "todo", label: "⏳ Тільки незгенеровані" }
    ];

    var filterHtml = filters.map(function (f) {
      return "<button class=\"filter-pill" + (state.promptFilter === f.id ? " active" : "") + "\" data-pfilter=\"" + f.id + "\">" + f.label + "</button>";
    }).join("");

    pane.innerHTML = [
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎥 Покадрова таблиця 100 візуальних промптів (Google Veo 2 + Google Flow • 4K 24fps)</div>",
      "      <div class=\"panel-desc\">Правило контрасту кожні 12–15 с: тактильна макро-фізика Veo чергується з 3D-простором Flow. Жодних штучних «балакучих облич» реальних людей.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-emerald\" id=\"btnExportPromptsTxt\">📥 Завантажити всі 100 промптів (.txt)</button>",
      "      <button class=\"btn btn-cyan\" id=\"btnExportPromptsCsv\">📥 Таблиця для AI Studio (.csv)</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">" + filterHtml + "</div>",
      "    <input type=\"search\" class=\"search-input\" id=\"promptSearchInput\" placeholder=\"Пошук за кадром, об'єктом або текстом...\" value=\"" + esc(state.promptSearch) + "\">",
      "  </div>",
      "  <div style=\"font-size:12px;color:var(--text-muted);margin-bottom:0.75rem;\">Показано кадрів: <strong style=\"color:var(--text-primary);\">" + filtered.length + "</strong> зі 100</div>",
      "  <div class=\"prompts-grid\">" + cardsHtml + "</div>",
      "</div>"
    ].join("\n");

    pane.querySelectorAll("[data-pfilter]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.promptFilter = b.getAttribute("data-pfilter");
        renderPrompts();
      });
    });

    var sInput = document.getElementById("promptSearchInput");
    sInput.addEventListener("input", function () {
      state.promptSearch = sInput.value;
      var pos = sInput.selectionStart;
      renderPrompts();
      var nextInput = document.getElementById("promptSearchInput");
      if (nextInput) {
        nextInput.focus();
        try { nextInput.setSelectionRange(pos, pos); } catch (e) {}
      }
    });

    pane.querySelectorAll("[data-vid-check]").forEach(function (chk) {
      chk.addEventListener("change", function () {
        var num = chk.getAttribute("data-vid-check");
        if (chk.checked) state.checked["vid_" + num] = true;
        else delete state.checked["vid_" + num];
        saveProgress();
        renderPrompts();
      });
    });

    pane.querySelectorAll("[data-copy-prompt]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = parseInt(btn.getAttribute("data-copy-prompt"), 10);
        var item = (epData.prompts_100 || [])[num - 1];
        if (item) copyText(item.prompt, "промпт #" + String(num).padStart(3, "0"));
      });
    });

    pane.querySelectorAll("[data-copy-vfile]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = parseInt(btn.getAttribute("data-copy-vfile"), 10);
        var item = (epData.prompts_100 || [])[num - 1];
        if (item) copyText(item.filename, item.filename);
      });
    });

    document.getElementById("btnExportPromptsTxt").addEventListener("click", function () {
      var lines = (epData.prompts_100 || []).map(function (p) {
        return "#" + String(p.num).padStart(3, "0") + " [" + p.tc + "] " + p.filename + "\nUA CUE: " + p.cue_ua + "\nPROMPT: " + p.prompt + "\n";
      }).join("\n");
      downloadBlob("EP" + epData.ep + "_100_Veo_Flow_Prompts.txt", lines, "text/plain;charset=utf-8");
    });

    document.getElementById("btnExportPromptsCsv").addEventListener("click", function () {
      var rows = ["\"Num\",\"Act\",\"Timecode\",\"SMPTE_24fps\",\"SmartBin_Filename\",\"Narrator_Cue_UA\",\"Veo_Flow_Prompt_EN\""];
      (epData.prompts_100 || []).forEach(function (p) {
        rows.push("\"" + p.num + "\",\"ACT" + p.act + "\",\"" + p.tc + "\",\"" + p.smpte + "\",\"" + p.filename + "\",\"" + p.cue_ua.replace(/"/g, "''") + "\",\"" + p.prompt.replace(/"/g, "''") + "\"");
      });
      downloadBlob("EP" + epData.ep + "_100_Veo_Flow_Prompts.csv", rows.join("\n"), "text/csv;charset=utf-8");
    });
  }

  /* ---------------- TAB 5: 100 QUOTES & THESES ---------------- */
  function renderQuotes() {
    var pane = document.getElementById("pane-quotes");
    var catsMap = {};
    (epData.quotes_100 || []).forEach(function (qItem) {
      var c = qItem.cat || "Фундаментальна теза";
      catsMap[c] = (catsMap[c] || 0) + 1;
    });
    var cats = Object.keys(catsMap);
    var qSearch = state.quoteSearch.trim().toLowerCase();

    var filtered = (epData.quotes_100 || []).filter(function (qItem) {
      if (state.quoteCat !== "all" && qItem.cat !== state.quoteCat) return false;
      if (qSearch) {
        var hay = (qItem.text + " " + qItem.cat + " #" + qItem.num).toLowerCase();
        if (hay.indexOf(qSearch) === -1) return false;
      }
      return true;
    });

    var catPillsHtml = ["<button class=\"filter-pill" + (state.quoteCat === "all" ? " active" : "") + "\" data-qcat=\"all\">Усі (100)</button>"]
      .concat(cats.map(function (c) {
        return "<button class=\"filter-pill" + (state.quoteCat === c ? " active" : "") + "\" data-qcat=\"" + esc(c) + "\">" + esc(c) + " (" + catsMap[c] + ")</button>";
      })).join("");

    var cardsHtml = filtered.map(function (item) {
      return [
        "<div class=\"quote-card\">",
        "  <div class=\"quote-head\">",
        "    <span class=\"quote-num\">#" + String(item.num).padStart(3, "0") + "</span>",
        "    <span class=\"chip chip-purple\">" + esc(item.cat) + "</span>",
        "  </div>",
        "  <div class=\"quote-text\">" + esc(item.text) + "</div>",
        "  <div class=\"quote-foot\">",
        "    <span style=\"font-size:11px;color:var(--text-muted);\">" + esc(epData.name) + "</span>",
        "    <div class=\"btn-group\">",
        "      <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" data-copy-quote=\"" + item.num + "\">Копіювати</button>",
        "      <button class=\"btn btn-amber\" style=\"padding:3px 8px;font-size:11px;\" data-copy-fusion=\"" + item.num + "\">Титри Fusion</button>",
        "    </div>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    pane.innerHTML = [
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">💬 Повний банк 100 цитат та світоглядних тез — " + esc(epData.name) + "</div>",
      "      <div class=\"panel-desc\">Готова база для NotebookLM, швейцарської типографіки DaVinci Fusion (Inter +0.04) та нарізки YouTube Shorts.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-cyan\" id=\"btnCopyAllQuotes\">📋 Копіювати всі 100 цитат</button>",
      "      <button class=\"btn btn-emerald\" id=\"btnDownloadQuotesMd\">📥 Завантажити 100 цитат (.md)</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">" + catPillsHtml + "</div>",
      "    <input type=\"search\" class=\"search-input\" id=\"quoteSearchInput\" placeholder=\"Пошук серед 100 цитат героя...\" value=\"" + esc(state.quoteSearch) + "\">",
      "  </div>",
      "  <div style=\"font-size:12px;color:var(--text-muted);margin-bottom:0.75rem;\">Знайдено цитат: <strong style=\"color:var(--text-primary);\">" + filtered.length + "</strong> зі 100</div>",
      "  <div class=\"quotes-grid\">" + cardsHtml + "</div>",
      "</div>"
    ].join("\n");

    pane.querySelectorAll("[data-qcat]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.quoteCat = b.getAttribute("data-qcat");
        renderQuotes();
      });
    });

    var qIn = document.getElementById("quoteSearchInput");
    qIn.addEventListener("input", function () {
      state.quoteSearch = qIn.value;
      var pos = qIn.selectionStart;
      renderQuotes();
      var nextIn = document.getElementById("quoteSearchInput");
      if (nextIn) {
        nextIn.focus();
        try { nextIn.setSelectionRange(pos, pos); } catch (e) {}
      }
    });

    pane.querySelectorAll("[data-copy-quote]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var n = parseInt(btn.getAttribute("data-copy-quote"), 10);
        var qObj = (epData.quotes_100 || [])[n - 1];
        if (qObj) copyText(qObj.text + " — " + epData.name, "цитата #" + n);
      });
    });

    pane.querySelectorAll("[data-copy-fusion]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var n = parseInt(btn.getAttribute("data-copy-fusion"), 10);
        var qObj = (epData.quotes_100 || [])[n - 1];
        if (qObj) {
          var fusionCard = qObj.text.replace(/^«|»\.?$/g, "").toUpperCase() + "\n\n— " + epData.latin.toUpperCase();
          copyText(fusionCard, "титр Fusion (Inter Tracking +0.04)");
        }
      });
    });

    var allMd = "# 100 ЦИТАТ ТА ТЕЗ — " + epData.name.toUpperCase() + " (EP" + epData.ep + ")\n\n" +
      (epData.quotes_100 || []).map(function (qObj) {
        return qObj.num + ". **[" + qObj.cat + "]** " + qObj.text;
      }).join("\n");

    document.getElementById("btnCopyAllQuotes").addEventListener("click", function () {
      copyText(allMd, "усі 100 цитат (" + epData.name + ")");
    });
    document.getElementById("btnDownloadQuotesMd").addEventListener("click", function () {
      downloadBlob("EP" + epData.ep + "_" + epData.page_slug + "_100_quotes.md", allMd, "text/markdown;charset=utf-8");
    });
  }

  /* ---------------- TAB 6: SUNO 92 BPM & VO REGISTRY ---------------- */
  function renderAudio() {
    var pane = document.getElementById("pane-audio");
    var masterPool = window.SUNO_MASTER_POOL || [];
    var importedMap = {};
    masterPool.forEach(function (t) {
      importedMap[t.smart_bin] = { track: t, bin_dir: t.bin_dir, smart_bin: t.smart_bin };
      (t.extra_bins || []).forEach(function (eb) {
        importedMap[eb.smart_bin] = { track: t, bin_dir: eb.bin_dir, smart_bin: eb.smart_bin };
      });
    });

    // Sort so tracks assigned to THIS episode appear right at the top!
    var sortedPool = masterPool.slice().sort(function (a, b) {
      var aMatch = a.hero_ep === epData.ep || (a.extra_bins || []).some(function (eb) { return eb.smart_bin.indexOf("EP" + epData.ep + "_") === 0; });
      var bMatch = b.hero_ep === epData.ep || (b.extra_bins || []).some(function (eb) { return eb.smart_bin.indexOf("EP" + epData.ep + "_") === 0; });
      if (aMatch && !bMatch) return -1;
      if (!aMatch && bMatch) return 1;
      return parseInt(a.num, 10) - parseInt(b.num, 10);
    });

    var poolRowsHtml = sortedPool.map(function (t, idx) {
      var isThisEp = t.hero_ep === epData.ep || (t.extra_bins || []).some(function (eb) { return eb.smart_bin.indexOf("EP" + epData.ep + "_") === 0; });
      var rowStyle = isThisEp ? " style=\"background:rgba(52,211,153,0.07);\"" : "";
      var displayBin = t.smart_bin;
      var displayDir = t.bin_dir;
      if (t.hero_ep !== epData.ep && t.extra_bins) {
        t.extra_bins.forEach(function (eb) {
          if (eb.smart_bin.indexOf("EP" + epData.ep + "_") === 0) {
            displayBin = eb.smart_bin;
            displayDir = eb.bin_dir;
          }
        });
      }
      return [
        "<tr" + rowStyle + ">",
        "  <td><span class=\"chip " + (isThisEp ? "chip-emerald" : "chip-cyan") + "\">#" + esc(t.num) + "</span>" + (isThisEp ? "<div style=\"margin-top:4px;\"><span class=\"chip chip-emerald\">🎯 Цей епізод</span></div>" : "") + "</td>",
        "  <td><strong>" + esc(t.orig_name) + "</strong><div style=\"font-size:10.8px;color:var(--amber);margin-top:2px;\">" + esc(t.hero_label || "") + "</div><div style=\"font-size:11px;color:var(--cyan);font-family:var(--mono);margin-top:2px;\">→ " + esc(displayDir) + "/" + esc(displayBin) + "</div></td>",
        "  <td><span class=\"chip chip-purple\">" + esc(t.module) + "</span><div style=\"font-size:11px;color:var(--text-muted);margin-top:3px;\">" + esc(t.specs) + "</div></td>",
        "  <td style=\"min-width:235px;\"><audio controls preload=\"none\" style=\"height:32px;width:230px;\" src=\"../assets/audio_previews/" + esc(t.preview) + "\"></audio></td>",
        "  <td style=\"font-size:11.5px;color:var(--text-secondary);max-width:290px;\">" + esc(t.usage) + "</td>",
        "  <td><button class=\"btn\" style=\"padding:3px 7px;font-size:11px;\" data-copy-pool-dir=\"" + esc(displayDir) + "\" data-copy-pool-bin=\"" + esc(displayBin) + "\">Шлях WAV</button></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var masterModules = [
      {
        code: "Модуль A: Introspection (Акт 1)",
        prompt: "Instrumental ambient trip-hop, 92 bpm, deep warm analog sub-bass, sparse Rhodes electric piano chords, dusty vinyl crackle texture, slow hypnotic downtempo groove, distant clean guitar harmonics, melancholic philosophical mood, wide stereo mastering."
      },
      {
        code: "Модуль B: Tension & Crisis (Акти 2–3)",
        prompt: "Instrumental dark industrial downtempo, 92 bpm, clockwork ticking metallic percussion, driving muted analog bassline, brooding dark saxophone drone in deep reverb, modular synth arpeggio tension, psychological thriller score, high dynamic clarity."
      },
      {
        code: "Модуль C: Transcendence (Акт 4)",
        prompt: "Instrumental monumental neo-classical trip-hop, 92 bpm, Vangelis style soaring analog brass synthesizers, deep resonant sub-bass pulse, celestial ambient pad, slow triumphant rhythm, cosmic scale, IMAX documentary soundtrack mastering."
      }
    ];

    var modHtml = masterModules.map(function (m, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--cyan);\">",
        "  <h4>" + esc(m.code) + "</h4>",
        "  <div style=\"font-family:var(--mono);font-size:11px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(m.prompt) + "</div>",
        "  <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-copy-mod=\"" + idx + "\">📋 Копіювати еталон Suno 92 BPM</button>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var heroFourKit = [];
    masterPool.forEach(function (t) {
      if (t.hero_ep === epData.ep) {
        heroFourKit.push({ track: t, bin_dir: t.bin_dir, smart_bin: t.smart_bin, role: "Ексклюзивна тема героя (" + t.act + ")" });
      } else if (t.extra_bins) {
        t.extra_bins.forEach(function (eb) {
          if (eb.ep === epData.ep || eb.smart_bin.indexOf("EP" + epData.ep + "_") === 0) {
            heroFourKit.push({ track: t, bin_dir: eb.bin_dir, smart_bin: eb.smart_bin, role: eb.role || t.act });
          }
        });
      }
    });
    heroFourKit.sort(function (x, y) { return x.smart_bin.localeCompare(y.smart_bin); });

    var heroKitCardsHtml = heroFourKit.map(function (hk) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--emerald);background:rgba(16,185,129,0.05);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:4px;\">",
        "    <span class=\"chip chip-emerald\">" + esc(hk.role) + "</span>",
        "    <span style=\"font-size:11px;color:var(--amber);font-family:var(--mono);\">" + esc(hk.track.duration) + "</span>",
        "  </div>",
        "  <h4 style=\"margin:4px 0 2px 0;\">" + esc(hk.track.orig_name) + "</h4>",
        "  <div style=\"font-family:var(--mono);font-size:10.8px;color:var(--cyan);margin-bottom:6px;word-break:break-all;\">→ " + esc(hk.bin_dir) + "/" + esc(hk.smart_bin) + "</div>",
        "  <audio controls preload=\"none\" style=\"height:30px;width:100%;margin-bottom:6px;\" src=\"../assets/audio_previews/" + esc(hk.track.preview) + "\"></audio>",
        "  <div style=\"font-size:11px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(hk.track.specs) + "</div>",
        "  <button class=\"btn btn-emerald\" style=\"padding:3px 8px;font-size:11px;width:100%;\" data-copy-pool-dir=\"" + esc(hk.bin_dir) + "\" data-copy-pool-bin=\"" + esc(hk.smart_bin) + "\">📋 Копіювати шлях WAV для DaVinci A2</button>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var sunoRows = (epData.suno_registry || []).map(function (item, idx) {
      var matchedEntry = importedMap[item.filename];
      var matchedWav = matchedEntry ? matchedEntry.track : null;
      var done = !!state.checked["suno_" + idx] || !!matchedWav;
      var inlinePlayer = matchedWav
        ? "<div style=\"margin-top:6px;\"><audio controls preload=\"none\" style=\"height:28px;width:220px;\" src=\"../assets/audio_previews/" + esc(matchedWav.preview) + "\"></audio></div>"
        : "";
      return [
        "<tr" + (matchedWav ? " style=\"background:rgba(52,211,153,0.06);\"" : "") + ">",
        "  <td><input type=\"checkbox\" class=\"sop-checkbox\" data-suno-check=\"" + idx + "\"" + (done ? " checked" : "") + "></td>",
        "  <td><span class=\"chip chip-cyan\">" + esc(item.category) + " • " + esc(item.act) + "</span>" + (matchedWav ? "<div style=\"margin-top:4px;\"><span class=\"chip chip-emerald\">✅ WAV у 03_AUDIO</span></div>" : "") + "</td>",
        "  <td><span class=\"filename-mono\">" + esc(item.filename) + "</span>" + (matchedWav ? ("<div style=\"font-size:10.5px;color:var(--emerald);margin-top:3px;\">Імпортовано: " + esc(matchedWav.orig_name) + " (" + esc(matchedWav.duration) + ") → " + esc(matchedEntry.bin_dir) + "</div>" + inlinePlayer) : "") + "</td>",
        "  <td style=\"font-size:11.5px;color:var(--text-secondary);\">" + esc(item.davinci_track) + "</td>",
        "  <td style=\"font-family:var(--mono);font-size:11px;color:#cbd5e1;max-width:390px;\">" + esc(item.suno_prompt) + "</td>",
        "  <td>",
        "    <div class=\"btn-group\">",
        "      <button class=\"btn btn-emerald\" style=\"padding:3px 7px;font-size:11px;\" data-copy-suno-p=\"" + idx + "\">Промпт</button>",
        "      <button class=\"btn\" style=\"padding:3px 7px;font-size:11px;\" data-copy-suno-f=\"" + idx + "\">Ім'я .wav</button>",
        "    </div>",
        "  </td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var voRows = (epData.vo_registry || []).map(function (v, idx) {
      var done = !!state.checked["vo_" + idx];
      return [
        "<tr>",
        "  <td><input type=\"checkbox\" class=\"sop-checkbox\" data-vo-check=\"" + idx + "\"" + (done ? " checked" : "") + "></td>",
        "  <td><span class=\"chip chip-amber\">" + esc(v.act) + "</span></td>",
        "  <td><strong>" + esc(v.label) + "</strong></td>",
        "  <td><span class=\"filename-mono\">" + esc(v.ua_file) + "</span> <button class=\"btn\" style=\"padding:2px 6px;font-size:10.5px;\" data-copy-vo-ua=\"" + idx + "\">📋</button></td>",
        "  <td><span class=\"filename-mono\">" + esc(v.en_file) + "</span> <button class=\"btn\" style=\"padding:2px 6px;font-size:10.5px;\" data-copy-vo-en=\"" + idx + "\">📋</button></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var scriptDir = (epData.script_md_path || "").split("/").slice(0, 2).join("/") || ("02_SCRIPTS/episode_" + epData.ep);
    var voMasterRelPath = scriptDir + "/EP" + epData.ep + "_VO_UA_ELEVENLABS_MASTER.txt";

    pane.innerHTML = [
      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.45);background:linear-gradient(180deg,rgba(56,189,248,0.06),transparent);margin-bottom:1rem;\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\" style=\"color:var(--cyan);display:flex;align-items:center;gap:8px;\">",
      "        🎙️ Майстер-Текст Диктора (ElevenLabs 115 WPM • Готовий до озвучення)",
      "        <span class=\"chip chip-amber\">⏳ Текст 100% Готовий • Очікує Синтезу WAV</span>",
      "      </div>",
      "      <div class=\"panel-desc\">",
      "        Файл: <code style=\"color:var(--cyan);\">" + esc(voMasterRelPath) + "</code> (" + esc(epData.script_total_words) + " слів • " + esc(epData.duration) + " • Speed 0.86). Скопіюйте текст в один клік для ElevenLabs або відкрийте TXT файл у Finder.",
      "      </div>",
      "    </div>",
      "    <div style=\"display:flex;gap:6px;align-items:center;flex-wrap:wrap;\">",
      "      <button class=\"btn btn-emerald\" id=\"btnAudioCopyVoTxt\" style=\"padding:5px 10px;font-size:11.5px;font-weight:700;\">📋 Скопіювати текст для ElevenLabs</button>",
      "      <button class=\"btn btn-cyan\" id=\"btnAudioOpenVoFinder\" style=\"padding:5px 10px;font-size:11.5px;\">📁 Відкрити TXT у Finder</button>",
      "    </div>",
      "  </div>",
      "</div>",

      "<div class=\"panel-card\" style=\"border-color:rgba(52,211,153,0.55);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎯 Готовий 4-Актний Аудіо-Комплект цього Епізоду (" + heroFourKit.length + " WAV у папці Smart Bin)</div>",
      "      <div class=\"panel-desc\">Повний музичний каркас випуску (Акт 1 Introspection • Акт 2 Drone • Акт 3 Climax • Акт 4 Finale) вже розкладений у <code>03_AUDIO/suno_stems/EP" + esc(epData.ep) + "_..._SMART_BINS/</code> і готовий до перетягування на доріжку A2 у DaVinci Resolve.</div>",
      "    </div>",
      "    <span class=\"chip chip-emerald\">✅ Suno Етап Закрито (4/4 Актів)</span>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + heroKitCardsHtml + "</div>",
      "</div>",

      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.35);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎧 Уся Імпортована Майстер-Бібліотека Сезону (16 WAV-майстрів • 40 Smart Bin слотів • 61 хв 31 с)</div>",
      "      <div class=\"panel-desc\">Треки цього героя підсвічені зверху (🎯 Цей епізод), а нижче доступний увесь 16-трековий пул сезону з таймкодами під голос диктора.</div>",
      "    </div>",
      "    <span class=\"chip chip-cyan\">48 kHz WAV + Веб-Плеєр</span>",
      "  </div>",
      "  <div class=\"studio-table-wrap\">",
      "    <table class=\"studio-table\">",
      "      <thead><tr><th>№</th><th>Оригінал Suno → Smart Bin (.wav)</th><th>Модуль та Акустика</th><th>Прослухати трек</th><th>Драматургічне призначення</th><th>Шлях</th></tr></thead>",
      "      <tbody>" + poolRowsHtml + "</tbody>",
      "    </table>",
      "  </div>",
      "</div>",

      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎵 Suno Pro (Custom Instrumental • 92 BPM) — 3 базові модулі та 16 іменних файлів епізоду</div>",
      "      <div class=\"panel-desc\">Строгий темп 92 BPM гарантує, що кожна склейка кадру в DaVinci Resolve (24 fps) лягає в сильну долю такту кожні 2.61 секунди (62–63 кадри).</div>",
      "    </div>",
      "  </div>",
      "  <div class=\"node-tree-grid\" style=\"margin-bottom:1rem;\">" + modHtml + "</div>",
      "  <div class=\"studio-table-wrap\">",
      "    <table class=\"studio-table\">",
      "      <thead><tr><th>✓</th><th>Тип / Акт</th><th>Ім'я файлу Smart Bin (.wav)</th><th>Доріжка Fairlight</th><th>Готовий промпт Suno Pro v4 / SFX</th><th>Дії</th></tr></thead>",
      "      <tbody>" + sunoRows + "</tbody>",
      "    </table>",
      "  </div>",
      "</div>",

      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎙️ Двомовний реєстр дикторської озвучки (UA + EN YouTube Multi-Language Audio • WAV 48kHz / 24-bit)</div>",
      "      <div class=\"panel-desc\">ElevenLabs Multilingual v2: Speed = 0.86, " + esc(epData.vo_settings) + " | Google Cloud TTS: rate=\"84%\" pitch=\"-1.5st\".</div>",
      "    </div>",
      "  </div>",
      "  <div class=\"studio-table-wrap\">",
      "    <table class=\"studio-table\">",
      "      <thead><tr><th>✓</th><th>Акт</th><th>Смисловий блок</th><th>Українська майстер-доріжка (A1 UA)</th><th>Англійська майстер-доріжка (A1 EN)</th></tr></thead>",
      "      <tbody>" + voRows + "</tbody>",
      "    </table>",
      "  </div>",
      "</div>"
    ].join("\n");

    var audios = pane.querySelectorAll("audio");
    for (var a = 0; a < audios.length; a++) {
      audios[a].addEventListener("play", function (ev) {
        for (var b = 0; b < audios.length; b++) {
          if (audios[b] !== ev.target) audios[b].pause();
        }
      });
    }

    pane.querySelectorAll("[data-copy-pool-bin]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var bDir = btn.getAttribute("data-copy-pool-dir");
        var bName = btn.getAttribute("data-copy-pool-bin");
        copyText("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/suno_stems/" + bDir + "/" + bName, bName);
      });
    });

    pane.querySelectorAll("[data-copy-mod]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-mod"), 10);
        copyText(masterModules[i].prompt, masterModules[i].code);
      });
    });

    pane.querySelectorAll("[data-suno-check]").forEach(function (chk) {
      chk.addEventListener("change", function () {
        var i = chk.getAttribute("data-suno-check");
        if (chk.checked) state.checked["suno_" + i] = true;
        else delete state.checked["suno_" + i];
        saveProgress();
      });
    });

    pane.querySelectorAll("[data-vo-check]").forEach(function (chk) {
      chk.addEventListener("change", function () {
        var i = chk.getAttribute("data-vo-check");
        if (chk.checked) state.checked["vo_" + i] = true;
        else delete state.checked["vo_" + i];
        saveProgress();
      });
    });

    pane.querySelectorAll("[data-copy-suno-p]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-suno-p"), 10);
        var row = epData.suno_registry[i];
        if (row) copyText(row.suno_prompt, "промпт " + row.filename);
      });
    });

    pane.querySelectorAll("[data-copy-suno-f]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-suno-f"), 10);
        var row = epData.suno_registry[i];
        if (row) copyText(row.filename, row.filename);
      });
    });

    pane.querySelectorAll("[data-copy-vo-ua]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-vo-ua"), 10);
        var row = epData.vo_registry[i];
        if (row) copyText(row.ua_file, row.ua_file);
      });
    });

    pane.querySelectorAll("[data-copy-vo-en]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-vo-en"), 10);
        var row = epData.vo_registry[i];
        if (row) copyText(row.en_file, row.en_file);
      });
    });

    var aCopyVoBtn = document.getElementById("btnAudioCopyVoTxt");
    if (aCopyVoBtn) {
      aCopyVoBtn.addEventListener("click", function () {
        var allVo = (epData.full_acts || []).map(function (act) {
          return "=== " + act.title + " ===\n" + (act.scenes || []).map(function (sc) {
            return "[" + sc.tc + "] " + sc.narration;
          }).join("\n\n");
        }).join("\n\n====================\n\n");
        copyText(cleanTextForElevenLabs(allVo), "дикторський текст EP" + epData.ep + " для ElevenLabs");
      });
    }

    var aOpenVoFinder = document.getElementById("btnAudioOpenVoFinder");
    if (aOpenVoFinder) {
      aOpenVoFinder.addEventListener("click", function () {
        revealInFinder(voMasterRelPath, "Майстер-текст диктора EP" + epData.ep);
      });
    }
  }

  /* ---------------- TAB 7: DAVINCI RESOLVE 19 STUDIO ---------------- */
  function renderMontageStatus() {
    var ms = window.MONTAGE_STATUS && window.MONTAGE_STATUS[epData.ep];
    if (!ms) return "";
    var rows = (ms.acts || []).map(function (a) {
      return "<tr><td><strong>Акт " + esc(a.act) + "</strong><br><span style=\"color:var(--text-muted);font-size:11px;\">" + esc(a.title) + "</span></td>" +
        "<td style=\"font-family:var(--mono);\">" + esc(a.start) + "</td><td style=\"font-family:var(--mono);\">" + esc(a.duration) + "</td>" +
        "<td>" + esc(a.shots) + "</td><td>Д" + a.dubs.map(function (d) { return ("0" + d).slice(-2); }).join(", Д") + "</td>" +
        "<td style=\"font-size:11px;\">" + esc(a.music) + "</td>" +
        "<td style=\"font-family:var(--mono);font-size:11px;color:var(--cyan);\">" + esc(a.timeline) + "</td></tr>";
    }).join("");
    var cross = Object.keys(ms.cross_episode || {}).map(function (ep) {
      return "<span class=\"pill pill-purple\" title=\"" + esc(ms.cross_episode[ep].join("\n")) + "\">EP" + esc(ep) + ": " + ms.cross_episode[ep].length + " кліпів</span>";
    }).join(" ");
    var li = function (arr) { return (arr || []).map(function (x) { return "<li>" + esc(x) + "</li>"; }).join(""); };
    var td = "padding:6px 8px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top;";
    return [
      "<div class=\"panel-card\" style=\"border-color:rgba(245,158,11,0.5);background:linear-gradient(180deg,rgba(245,158,11,0.07),transparent);margin-bottom:1rem;\">",
      "  <div class=\"panel-head\"><div>",
      "    <div class=\"panel-title\">🎬 " + esc(ms.headline) + "</div>",
      "    <div class=\"panel-desc\">Проєкт <strong>" + esc(ms.project) + "</strong> • таймлайн <code style=\"color:var(--cyan);font-family:var(--mono);\">" + esc(ms.full_timeline) + "</code> • <strong>" + esc(ms.total_duration) + "</strong> • " + esc(ms.total_shots) + " планів • оновлено " + esc(ms.updated) + "</div>",
      "  </div></div>",
      "  <p style=\"font-size:13px;color:var(--text-secondary);margin:0 0 0.8rem;\">" + esc(ms.concept) + "</p>",
      "  <div style=\"overflow-x:auto;\"><table style=\"width:100%;border-collapse:collapse;font-size:12.5px;\">",
      "    <thead><tr><th style=\"" + td + "\">Акт</th><th style=\"" + td + "\">Старт</th><th style=\"" + td + "\">Довжина</th><th style=\"" + td + "\">Планів</th><th style=\"" + td + "\">Дублі</th><th style=\"" + td + "\">Музика</th><th style=\"" + td + "\">Таймлайн у Resolve</th></tr></thead>",
      "    <tbody>" + rows.replace(/<td/g, "<td style=\"" + td + "\"").replace(/style="([^"]*)" style="/g, "style=\"$1") + "</tbody>",
      "  </table></div>",
      "  <div class=\"node-tree-grid\" style=\"margin-top:0.9rem;\">",
      "    <div class=\"node-box\" style=\"border-top-color:var(--emerald);\"><h4>🎧 Звук</h4><ul style=\"font-size:12px;color:var(--text-secondary);padding-left:1.1rem;margin:0;\">" + li(ms.audio) + "</ul></div>",
      "    <div class=\"node-box\" style=\"border-top-color:var(--purple);\"><h4>🔗 Матеріали інших епізодів</h4><div style=\"display:flex;flex-wrap:wrap;gap:6px;\">" + cross + "</div></div>",
      "    <div class=\"node-box\" style=\"border-top-color:var(--cyan);\"><h4>⚙️ Скрипти збірки</h4><ul style=\"font-size:11.5px;font-family:var(--mono);color:var(--text-secondary);padding-left:1.1rem;margin:0;\">" + li(ms.scripts) + "</ul></div>",
      (ms.fixes ? "    <div class=\"node-box\" style=\"border-top-color:var(--rose,#f43f5e);\"><h4>🛠️ Виправлено</h4><ul style=\"font-size:12px;color:var(--text-secondary);padding-left:1.1rem;margin:0;\">" + li(ms.fixes) + "</ul></div>" : ""),
      "    <div class=\"node-box\" style=\"border-top-color:var(--amber);\"><h4>⏭️ Далі</h4><ul style=\"font-size:12px;color:var(--text-secondary);padding-left:1.1rem;margin:0;\">" + li(ms.next) + "</ul></div>",
      "  </div>",
      "</div>"
    ].join("\n");
  }

  function renderDaVinci() {
    var pane = document.getElementById("pane-davinci");
    pane.innerHTML = renderMontageStatus() + [
      "<div class=\"panel-card\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎚️ Складальний цех DaVinci Resolve 19 Studio — Конструктор Smart Bins та Автоматизація</div>",
      "      <div class=\"panel-desc\">Канонічне правило іменування файлів епізоду: <code style=\"color:var(--cyan);font-family:var(--mono);\">" + esc(epData.smart_bin_rule) + "</code></div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-emerald\" id=\"btnDvSetupSh\">📥 Скрипт папок setup_EP" + esc(epData.ep) + ".sh</button>",
      "      <button class=\"btn btn-cyan\" id=\"btnDvMarkersCsv\">📥 100 маркерів таймлайну (.csv)</button>",
      "    </div>",
      "  </div>",

      "  <div class=\"builder-grid\">",
      "    <div class=\"builder-field\">",
      "      <label>Категорія Smart Bin</label>",
      "      <select id=\"sbCat\">",
      "        <option value=\"VID\">VID (4K Відеокліп .mp4)</option>",
      "        <option value=\"VO_UA\">VO_UA (Голос UA .wav)</option>",
      "        <option value=\"VO_EN\">VO_EN (Голос EN .wav)</option>",
      "        <option value=\"MUS\">MUS (Музика Suno .wav)</option>",
      "        <option value=\"AMB\">AMB (Ембієнт/Дрон .wav)</option>",
      "        <option value=\"SFX\">SFX (Звуковий акцент .wav)</option>",
      "      </select>",
      "    </div>",
      "    <div class=\"builder-field\">",
      "      <label>Номер сцени / дубля</label>",
      "      <input type=\"text\" id=\"sbScene\" value=\"001\">",
      "    </div>",
      "    <div class=\"builder-field\">",
      "      <label>Акт драматургії</label>",
      "      <select id=\"sbAct\">",
      "        <option value=\"ACT1\">ACT1 (00:00–04:45)</option>",
      "        <option value=\"ACT2\">ACT2 (04:45–10:00)</option>",
      "        <option value=\"ACT3\">ACT3 (10:00–16:00)</option>",
      "        <option value=\"ACT4\">ACT4 (16:00–21:00)</option>",
      "      </select>",
      "    </div>",
      "    <div class=\"builder-field\">",
      "      <label>Короткий опис (Латиниця)</label>",
      "      <input type=\"text\" id=\"sbDesc\" value=\"Macro_Silicon_Wafer\">",
      "    </div>",
      "  </div>",

      "  <div style=\"display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap;background:#0b0d13;border:1px solid var(--border);padding:0.75rem 1rem;border-radius:8px;margin-bottom:1.1rem;\">",
      "    <div>",
      "      <div style=\"font-size:10.5px;color:var(--text-muted);text-transform:uppercase;\">Готове ім'я файлу для авто-сортування в DaVinci Smart Bins:</div>",
      "      <div id=\"sbPreview\" style=\"font-family:var(--mono);font-size:14px;font-weight:700;color:var(--emerald);margin-top:2px;\"></div>",
      "    </div>",
      "    <button class=\"btn btn-emerald\" id=\"btnCopySbName\">📋 Копіювати ім'я файлу</button>",
      "  </div>",

      "  <div class=\"node-tree-grid\">",
      "    <div class=\"node-box\" style=\"border-top-color:var(--cyan);\">",
      "      <h4>1. Вкладка EDIT (Сітка 92 BPM)</h4>",
      "      <p style=\"font-size:12px;color:var(--text-secondary);\">Timeline <strong>3840×1606 (2.39:1 Scope)</strong>, рівно <strong>24.000 fps</strong>. Увімкнути аудіо-хвилю треку Suno 92 BPM: кожна склейка між Veo, Flow та архівами виконується строго на піку бочки (кожні <strong>62–63 кадри / 2.61 с</strong>).</p>",
      "    </div>",
      "    <div class=\"node-box\" style=\"border-top-color:var(--emerald);\">",
      "      <h4>2. Вкладка FAIRLIGHT (Sidechain -3.2 dB)</h4>",
      "      <p style=\"font-size:12px;color:var(--text-secondary);\"><strong>A1 (Voice):</strong> EQ зріз гулу нижче 75Hz, підйом присутності +3.2kHz, <em>Sidechain Send 1</em>.<br><strong>A2 (Suno 92 BPM):</strong> Compressor <em>Sidechain Listen 1</em> (Threshold -24dB, Ratio 3.5:1, Attack 35ms, Release 400ms) → авто-присідання на <strong>-3.2 dB</strong>.</p>",
      "    </div>",
      "    <div class=\"node-box\" style=\"border-top-color:var(--purple);\">",
      "      <h4>3. Вкладка COLOR (4-Node Kodak 2383)</h4>",
      "      <p style=\"font-size:12px;color:var(--text-secondary);\"><strong>Node 1:</strong> Lift/Gamma/Gain експозиція.<br><strong>Node 2:</strong> Ціан у тінях / Золото у світлах (" + esc(epData.visual_key) + ").<br><strong>Node 3:</strong> LUT <em>Rec709 Kodak 2383 D60</em>.<br><strong>Node 4:</strong> OFX <em>Film Grain 35mm (Strength 0.35)</em>.</p>",
      "    </div>",
      "    <div class=\"node-box\" style=\"border-top-color:var(--amber);\">",
      "      <h4>4. Вкладка FUSION (Швейцарська типографіка)</h4>",
      "      <p style=\"font-size:12px;color:var(--text-secondary);\">Мінімалістичні титри цитат без кольорових плашок. Гарнітура <strong>Inter / Helvetica Now</strong>, Tracking <strong>+0.04</strong>, поява через <em>Gaussian Blur + Opacity</em> за 6 кадрів синхронно із <strong>Sub-drop 40Hz</strong> на доріжці A4.</p>",
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n");

    function updateBuilder() {
      var cat = document.getElementById("sbCat").value;
      var sc = (document.getElementById("sbScene").value || "001").replace(/[^0-9A-Za-z]/g, "");
      var act = document.getElementById("sbAct").value;
      var desc = (document.getElementById("sbDesc").value || "Shot").trim().replace(/\s+/g, "_").replace(/[^0-9A-Za-z_]/g, "");
      var tempoTag = "92BPM";
      var ext = "wav";
      if (cat === "VID") { tempoTag = "24FPS"; ext = "mp4"; }
      else if (cat === "VO_UA" || cat === "VO_EN") { tempoTag = "115WPM"; ext = "wav"; }
      else if (cat === "AMB") { tempoTag = "DRONE"; ext = "wav"; }
      else if (cat === "SFX") { tempoTag = "HIT"; ext = "wav"; }
      var built = "EP" + epData.ep + "_" + cat + "_" + sc + "_" + act + "_" + tempoTag + "_" + (desc || "Asset") + "." + ext;
      document.getElementById("sbPreview").textContent = built;
      return built;
    }

    ["sbCat", "sbScene", "sbAct", "sbDesc"].forEach(function (id) {
      document.getElementById(id).addEventListener("input", updateBuilder);
      document.getElementById(id).addEventListener("change", updateBuilder);
    });
    updateBuilder();

    document.getElementById("btnCopySbName").addEventListener("click", function () {
      var val = updateBuilder();
      copyText(val, val);
    });
    document.getElementById("btnDvSetupSh").addEventListener("click", function () {
      downloadBlob("setup_EP" + epData.ep + ".sh", generateSetupScript(), "text/x-shellscript;charset=utf-8");
    });
    document.getElementById("btnDvMarkersCsv").addEventListener("click", function () {
      downloadBlob("EP" + epData.ep + "_DaVinci_Markers_24fps.csv", generateDaVinciMarkersCSV(), "text/csv;charset=utf-8");
    });
  }

  function generateEpisodeTitlesSRT() {
    var pool = (window.MEDIA_ACQUISITION_POOL || {})[epData.ep] || {};
    var dossiers = pool.dossiers || [];
    var quotes = (epData.quotes || []).slice(0, 6);
    var blocks = [];
    var idx = 1;
    function pad2(n) { return String(n).padStart(2, "0"); }
    function secToSrt(sec) {
      var m = Math.floor(sec / 60);
      var s = Math.floor(sec % 60);
      return "00:" + pad2(m) + ":" + pad2(s) + ",000";
    }

    blocks.push(idx++ + "\n00:00:04,000 --> 00:00:11,000\nАРХІТЕКТОРИ РОЗУМУ // ЕПІЗОД " + epData.ep + "\n" + epData.name.toUpperCase() + " — " + epData.title.toUpperCase());

    dossiers.forEach(function (d, di) {
      var startSec = 155 + (di * 180);
      var m = String(d.timecode || "").match(/(\d+):(\d+)/);
      if (m) startSec = parseInt(m[1], 10) * 60 + parseInt(m[2], 10);
      blocks.push(idx++ + "\n" + secToSrt(startSec) + " --> " + secToSrt(startSec + 9) + "\nДОСЬЄ // " + d.title.toUpperCase() + "\n" + d.source_label);
    });

    quotes.forEach(function (q, qi) {
      var startSec = 240 + (qi * 165);
      blocks.push(idx++ + "\n" + secToSrt(startSec) + " --> " + secToSrt(startSec + 8) + "\n«" + q.text + "»\n— " + epData.name);
    });

    return blocks.join("\n\n") + "\n";
  }

  /* ---------------- TAB 7: MEDIA ACQUISITION, RIGHT-SIDE VIDEO DOCK & POPUP CINEMA ---------------- */
  var reelObserver = null;

  function buildEpisodeVideoPlaylist() {
    var allMedia = window.MEDIA_ACQUISITION_POOL || {};
    var epMedia = allMedia[epData.ep] || { dossiers: [], archives: [], flow_queue: [], portrait: {}, flow_gallery: [], archival_photos: [], scientific_vfx: [] };
    var repoRoot = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/";
    var list = [];

    // 1. Real Archival B-Roll MP4s
    (epMedia.archives || []).forEach(function (ar, idx) {
      var fileName = ar.file || ar.mp4_file || ("archive_" + (idx + 1) + ".mp4");
      var vUrl = ar.video_preview ? ("../" + ar.video_preview) : ("../assets/video_previews/archives/" + fileName);
      var descNote = ar.note || ar.davinci_usage || "";
      var srcSec = ar.section || ar.timecode || "";
      list.push({
        uid: "arch_" + idx,
        type: "video",
        kind: "archive",
        kindLabel: "📼 Реальний Архів MP4",
        chipClass: "chip-emerald",
        title: ar.title || fileName,
        file: fileName,
        tc: ar.tc || ar.timecode || "00:00",
        track: "DaVinci V2 • Архів B-Roll • Dynamic Zoom 1.00→1.05",
        desc: descNote + (ar.source ? " (" + ar.source + (srcSec ? ", відрізок " + srcSec : "") + ")" : ""),
        src: vUrl,
        localPath: repoRoot + "05_RAW_FOOTAGE/archives/" + fileName,
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/05_RAW_FOOTAGE/archives/" + encodeURIComponent(fileName),
        externalUrl: ar.url || "",
        prompt: ""
      });
    });

    // 2. Real Google Flow / Veo Videos (#01-#10) & 2K Keyframes
    (epMedia.flow_queue || []).forEach(function (fq, idx) {
      if (fq.status === "video_ready" && fq.video_preview) {
        var vFile = fq.file || ("flow_" + fq.num + ".mp4");
        list.push({
          uid: "flow_vid_" + fq.num,
          type: "video",
          kind: "flow_video",
          kindLabel: "🚀 Flow 4K/HD Відео (#" + fq.num + ")",
          chipClass: "chip-emerald",
          title: fq.title || ("Flow Сцена #" + fq.num + " — " + vFile),
          file: vFile,
          tc: fq.tc || "00:00",
          track: "DaVinci V1 • Speed 60% • " + (fq.specs || "24 fps 1080p/720p"),
          desc: "Згенеровано в Google Flow / Veo. " + (fq.specs || "") + ". Промпт: " + (fq.prompt || ""),
          src: "../" + fq.video_preview,
          poster: fq.keyframe_preview ? ("../" + fq.keyframe_preview) : "",
          localPath: repoRoot + (fq.raw_video_path || ("05_RAW_FOOTAGE/flow_renders/" + vFile)),
          githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/05_RAW_FOOTAGE/flow_renders/" + encodeURIComponent(vFile),
          externalUrl: "",
          prompt: fq.prompt || ""
        });
      }
      if (fq.keyframe_preview || fq.raw_image_path) {
        var kFile = fq.raw_image_path ? fq.raw_image_path.split("/").pop() : ((fq.file || ("flow_" + fq.num)).replace(/\.mp4$/, ".jpg"));
        list.push({
          uid: "flow_img_" + fq.num,
          type: "image",
          kind: "flow_image",
          kindLabel: "🖼️ 2K Кадр (#" + fq.num + (fq.status === "video_ready" ? " • Відео зведено" : " • Очікує відео") + ")",
          chipClass: fq.status === "video_ready" ? "chip-emerald" : "chip-cyan",
          title: (fq.title ? (fq.title + " (2K Кадр)") : ("Flow Кадр #" + fq.num)),
          file: kFile,
          tc: fq.tc || "00:00",
          track: "Концепт-кадр 2K • Підготовка відео Flow / Veo",
          desc: "Концепт-кадр 2K. Промпт: " + (fq.prompt || ""),
          src: "../" + (fq.keyframe_preview || ("assets/flow_keyframes/" + kFile)),
          poster: "../" + (fq.keyframe_preview || ("assets/flow_keyframes/" + kFile)),
          localPath: repoRoot + (fq.raw_image_path || ("05_RAW_FOOTAGE/flow_images/" + kFile)),
          githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + (fq.raw_image_path || ""),
          externalUrl: "",
          prompt: fq.prompt || ""
        });
      }
    });

    // 3. UHD 4K Dossier Zoom Videos (V2)
    (epMedia.dossiers || []).forEach(function (d, idx) {
      var vUrl = d.video_preview ? ("../" + d.video_preview) : ("../assets/video_previews/dossiers/" + (d.id || "doc") + ".mp4");
      var dFile = (d.id || "DOC") + ".mp4";
      list.push({
        uid: "dos_" + idx,
        type: "video",
        kind: "dossier",
        kindLabel: "🗂️ 4K Досьє (Zoom 1.00→1.06)",
        chipClass: "chip-amber",
        title: d.title || ("Досьє #" + (idx + 1)),
        file: dFile,
        tc: d.timecode || "00:00",
        track: "DaVinci V2 • UHD 4K Документальна пластина (Dynamic Zoom)",
        desc: "«" + (d.highlight || "") + "» — Джерело: " + (d.source_label || ""),
        src: vUrl,
        poster: d.web_preview ? ("../" + d.web_preview) : "",
        localPath: repoRoot + (d.raw_4k_png || ""),
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/07_DASHBOARD/" + (d.web_preview || ""),
        externalUrl: "",
        prompt: ""
      });
    });

    // 4. Scientific 3D Animations & VFX (1080p MP4)
    (epMedia.scientific_vfx || []).forEach(function (sc, idx) {
      var scFile = sc.file || (sc.raw_path ? sc.raw_path.split("/").pop() : ("vfx_" + idx + ".mp4"));
      list.push({
        uid: "sci_" + idx,
        type: "video",
        kind: "science",
        kindLabel: "🔬 Наукова 3D-Анімація (" + (sc.code || "VFX") + ")",
        chipClass: "chip-purple",
        title: sc.title || ("Науковий VFX #" + (idx + 1)),
        file: scFile,
        tc: sc.timecode || "00:00",
        track: "DaVinci V1/V2 • Науковий VFX • " + (sc.specs || "1080p"),
        desc: (sc.desc || "") + " (" + (sc.role || "") + ")",
        src: sc.web_preview ? ("../" + sc.web_preview) : "",
        poster: "",
        localPath: repoRoot + (sc.raw_path || ""),
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + (sc.raw_path || ""),
        externalUrl: "",
        prompt: ""
      });
    });

    // 5. Extra B-Roll & Study Stills
    (epMedia.flow_gallery || []).forEach(function (g, idx) {
      var code = g.code || "";
      var gFile = g.raw_path ? g.raw_path.split("/").pop() : (code + ".jpg");
      list.push({
        uid: "broll_" + idx,
        type: "image",
        kind: "broll",
        kindLabel: (code.indexOf("STUDY") === 0 ? "🎨 Концепт-дослідження (" : "🎞️ Кінокадр B-Roll (") + (code || "B-ROLL") + ")",
        chipClass: code.indexOf("STUDY") === 0 ? "chip-purple" : "chip-amber",
        title: g.title || ("Кадр " + code),
        file: gFile,
        tc: g.tc || "00:00",
        track: "Кінокадр / Дослідження • " + (g.dims || "2K"),
        desc: (g.badge || "") + " — " + (g.title || "") + ". Розмір: " + (g.dims || "2K"),
        src: g.web_preview ? ("../" + g.web_preview) : "",
        poster: g.web_preview ? ("../" + g.web_preview) : "",
        localPath: repoRoot + (g.raw_path || ""),
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + (g.raw_path || ""),
        externalUrl: "",
        prompt: ""
      });
    });

    // 6. Archival Photos & Real Portraits
    (epMedia.archival_photos || []).forEach(function (ph, idx) {
      var phId = ph.id || ph.code || ("PHOTO_" + (idx + 1));
      var phFile = (ph.raw_file ? ph.raw_file.split("/").pop() : "") || (ph.url ? ph.url.split("/").pop() : "") || (phId + ".jpg");
      var phSrc = ph.web_preview ? ("../" + ph.web_preview) : (ph.url || "");
      list.push({
        uid: "arch_photo_" + idx,
        type: "image",
        kind: "archival_photo",
        kindLabel: "📷 Архівне Фото (" + (ph.code || phId) + ")",
        chipClass: "chip-cyan",
        title: ph.title || ("Архівне фото #" + (idx + 1)),
        file: phFile,
        tc: "00:00",
        track: "DaVinci V2 • Історичний фотокадр • CC / Public Domain",
        desc: (ph.title || "") + " — Джерело: " + (ph.source || "Архів"),
        src: phSrc,
        poster: phSrc,
        localPath: repoRoot + (ph.raw_file || ("05_RAW_FOOTAGE/speaker_photos/" + phFile)),
        githubUrl: ph.url || ("https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + (ph.raw_file || "")),
        externalUrl: ph.url || "",
        prompt: ""
      });
    });

    // 7. Voiceover Master Takes (A1)
    (epMedia.voiceover || []).forEach(function (vo, idx) {
      list.push({
        uid: "vo_take_" + idx,
        type: "audio",
        kind: "voiceover",
        kindLabel: "🎙️ Диктор A1 (Take " + vo.num + ")",
        chipClass: "chip-emerald",
        title: "Take #" + vo.num + ": " + (vo.title || "Сцена"),
        file: (vo.wav_master ? vo.wav_master.split("/").pop() : "take.wav"),
        tc: vo.tc || "00:00",
        track: "DaVinci A1 • Broadcast 48k/24b WAV • 115 WPM",
        desc: (vo.voice || "Adam") + " (" + vo.duration + ") • " + (vo.words || 0) + " слів",
        src: "../" + vo.web_preview,
        poster: "../assets/avatars/" + (epData.avatar || "sam_altman.jpg"),
        localPath: repoRoot + vo.wav_master,
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + vo.wav_master,
        externalUrl: "",
        prompt: ""
      });
    });

    // 8. All Disk Vault Videos & Images (ensuring 100% coverage per episode)
    var seenFiles = {};
    list.forEach(function (it) {
      if (it.file) seenFiles[it.file.toLowerCase()] = true;
    });
    var vaultEp = getVaultEp();
    (vaultEp.videos || []).forEach(function (vv, idx) {
      if (seenFiles[vv.file.toLowerCase()]) return;
      seenFiles[vv.file.toLowerCase()] = true;
      var vSrc = resolveMediaSrc(vv.rel_path, vv.preview_path, vv.thumb);
      var vLabelPrefix = vv.is_cross ? "♻️ " : "";
      list.push({
        uid: "vault_vid_" + idx,
        type: "video",
        kind: "vault_video",
        kindLabel: vLabelPrefix + (vv.cat_label || "🎥 Відео з архіву проєкту"),
        chipClass: vv.is_cross ? "chip-emerald" : "chip-cyan",
        title: vv.display_name || vv.file,
        file: vv.file,
        rel_path: vv.rel_path,
        tc: vv.size_mb + " MB",
        track: (vv.source_label || vv.cat_label || "Медіа-Пул") + " • " + (vv.ext || "MP4"),
        desc: (vv.match_reason ? ("Підбір: " + vv.match_reason + " | ") : "") + "Файл: " + vv.rel_path + " (" + vv.size_mb + " MB)",
        src: vSrc,
        poster: vv.thumb ? ("../" + vv.thumb) : "",
        localPath: repoRoot + vv.rel_path,
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + encodeURIComponent(vv.rel_path).replace(/%2F/g, "/"),
        externalUrl: "",
        prompt: ""
      });
    });

    (vaultEp.images || []).forEach(function (vi, idx) {
      if (seenFiles[vi.file.toLowerCase()]) return;
      seenFiles[vi.file.toLowerCase()] = true;
      var iSrc = resolveMediaSrc(vi.rel_path, vi.preview_path, vi.thumb);
      var iLabelPrefix = vi.is_cross ? "♻️ " : "";
      list.push({
        uid: "vault_img_" + idx,
        type: "image",
        kind: "vault_image",
        kindLabel: iLabelPrefix + (vi.cat_label || "🖼️ Зображення проєкту"),
        chipClass: vi.is_cross ? "chip-cyan" : "chip-amber",
        title: vi.display_name || vi.file,
        file: vi.file,
        rel_path: vi.rel_path,
        tc: vi.size_mb + " MB",
        track: (vi.source_label || vi.cat_label || "Галерея") + " • " + (vi.ext || "JPG"),
        desc: (vi.match_reason ? ("Підбір: " + vi.match_reason + " | ") : "") + "Файл: " + vi.rel_path + " (" + vi.size_mb + " MB)",
        src: iSrc,
        poster: vi.thumb ? ("../" + vi.thumb) : iSrc,
        localPath: repoRoot + vi.rel_path,
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + encodeURIComponent(vi.rel_path).replace(/%2F/g, "/"),
        externalUrl: "",
        prompt: ""
      });
    });

    return list;
  }

  function getVaultEp() {
    var v = (window.PROJECT_VAULT_INVENTORY || {})[epData.ep];
    return v || {
      ep: epData.ep,
      primary_footage_dir: "05_RAW_FOOTAGE/",
      vo_dir: "03_AUDIO/voiceover/",
      videos: [],
      images: [],
      audio: [],
      summary: { videos_count: 0, images_count: 0, audio_count: 0, vo_count: 0, suno_count: 0, total_mb: 0 }
    };
  }

  function getTriadsEp() {
    var tr = (window.FLOW_TRIADS_POOL || {})[epData.ep];
    if (tr && tr.length) return tr;
    return ((window.MEDIA_ACQUISITION_POOL || {})[epData.ep] || {}).flow_queue || [];
  }

  function resolveMediaSrc(relPath, previewPath, thumbPath) {
    var isLocalFile = (window.location && window.location.protocol === "file:");
    if (isLocalFile && relPath) return "../../" + relPath;
    if (previewPath) return "../" + previewPath;
    if (thumbPath) return "../" + thumbPath;
    return relPath ? ("../../" + relPath) : "";
  }

  function findPlaylistIdxByFileOrPath(playlist, file, relPath) {
    var fl = (file || "").toLowerCase();
    var rl = (relPath || "").toLowerCase();
    for (var i = 0; i < playlist.length; i++) {
      var p = playlist[i];
      if (rl && p.rel_path && p.rel_path.toLowerCase() === rl) return i;
      if (rl && p.localPath && p.localPath.toLowerCase().endsWith("/" + rl)) return i;
      if (fl && p.file && p.file.toLowerCase() === fl) return i;
    }
    return -1;
  }

  function buildVaultVideosHtml(vaultEp, playlist) {
    var videos = vaultEp.videos || [];
    if (!videos.length) {
      return "<div class=\"panel-card\"><div class=\"panel-title\">🎥 Відеофайли ще не додані для EP" + esc(epData.ep) + "</div><div class=\"panel-desc\">Використайте вкладку «🚀 Тріади Flow» для генерації нових відеосцен або покладіть MP4/MOV файли у папку " + esc(vaultEp.primary_footage_dir) + ".</div></div>";
    }
    var nativeCnt = videos.filter(function (v) { return !v.is_cross; }).length;
    var crossCnt = videos.filter(function (v) { return !!v.is_cross; }).length;
    var dupCnt = videos.filter(function (v) { return !!v.is_dup_md5; }).length;
    var portraitCnt = videos.filter(function (v) { return !!v.is_portrait; }).length;
    var catCounts = {};
    var catLabels = {};
    videos.forEach(function (v) {
      catCounts[v.cat] = (catCounts[v.cat] || 0) + 1;
      catLabels[v.cat] = v.cat_label;
    });
    var originPillsHtml = [
      "<button class=\"filter-pill" + (state.vaultVidOrigin === "all" ? " active" : "") + "\" data-vvid-origin=\"all\">📦 Усі (" + videos.length + ")</button>",
      "<button class=\"filter-pill" + (state.vaultVidOrigin === "native" ? " active" : "") + "\" data-vvid-origin=\"native\">⭐ Власні героя (" + nativeCnt + ")</button>",
      "<button class=\"filter-pill" + (state.vaultVidOrigin === "cross" ? " active" : "") + "\" data-vvid-origin=\"cross\">🌌 Абстрактні & Спільні (" + crossCnt + ")</button>"
    ];
    if (dupCnt > 0) {
      originPillsHtml.push("<button class=\"filter-pill" + (state.vaultVidUniqueOnly ? " active" : "") + "\" id=\"btnToggleVidUnique\">✨ Без копій MD5 (" + (videos.length - dupCnt) + ")</button>");
    }
    if (portraitCnt > 0) {
      originPillsHtml.push("<button class=\"filter-pill" + (state.vaultVidOnly169 ? " active" : "") + "\" id=\"btnToggleVid169\">🖥️ Тільки 16:9 (" + (videos.length - portraitCnt) + ")</button>");
    }
    var pillsHtml = ["<button class=\"filter-pill" + (state.vaultVidCat === "all" ? " active" : "") + "\" data-vvid-cat=\"all\">Усі категорії (" + videos.length + ")</button>"];
    Object.keys(catCounts).sort().forEach(function (cat) {
      pillsHtml.push("<button class=\"filter-pill" + (state.vaultVidCat === cat ? " active" : "") + "\" data-vvid-cat=\"" + esc(cat) + "\">" + esc(catLabels[cat]) + " (" + catCounts[cat] + ")</button>");
    });

    var q = (state.vaultVidSearch || "").trim().toLowerCase();
    var filtered = videos.filter(function (v) {
      if (state.vaultVidOrigin === "native" && v.is_cross) return false;
      if (state.vaultVidOrigin === "cross" && !v.is_cross) return false;
      if (state.vaultVidUniqueOnly && v.is_dup_md5) return false;
      if (state.vaultVidOnly169 && v.is_portrait) return false;
      if (state.vaultVidCat !== "all" && v.cat !== state.vaultVidCat) return false;
      if (q && (v.file + " " + v.display_name + " " + v.rel_path + " " + v.cat_label + " " + (v.res_label || "") + " " + (v.match_reason || "") + " " + (v.source_label || "") + " " + (v.suggested_scenes || []).join(" ")).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });

    var cardsHtml = filtered.map(function (v) {
      var pIdx = findPlaylistIdxByFileOrPath(playlist, v.file, v.rel_path);
      var playSrc = resolveMediaSrc(v.rel_path, v.preview_path, "");
      var thumbSrc = v.thumb ? ("../" + v.thumb) : "";
      var scenesHtml = (v.suggested_scenes || []).map(function (sc) {
        return "<span class=\"vault-scene-tag\">#" + esc(sc) + "</span>";
      }).join("");
      var originBadgeHtml = v.is_cross
        ? "<span class=\"vault-origin-badge is-cross\">" + esc(v.source_label || "🌌 Універсальний B-Roll") + "</span>"
        : "<span class=\"vault-origin-badge is-native\">⭐ Власний EP" + esc(epData.ep) + "</span>";
      var dupBadgeHtml = v.is_dup_md5
        ? "<span class=\"vault-origin-badge is-dup\" title=\"Побайтова копія файлу: " + esc(v.dup_of || "") + "\">👯 Копія MD5</span>"
        : "";
      var portBadgeHtml = v.is_portrait
        ? "<span class=\"vault-origin-badge is-portrait\">📱 9:16 Портрет</span>"
        : "";
      var fmtTag = [v.res_label, v.dur_label, v.size_mb ? (v.size_mb + " MB") : ""].filter(Boolean).join(" • ");
      var rationaleHtml = v.match_reason
        ? "<div class=\"vault-rationale\"><b>🎯 Сценарій:</b> " + esc(v.match_reason) + (scenesHtml ? (" <span>(" + scenesHtml + ")</span>") : "") + "</div>"
        : "";
      return [
        "<div class=\"vault-card" + (v.is_cross ? " is-cross" : "") + "\">",
        "  <div class=\"vault-thumb-box\" data-inline-play-vid=\"" + esc(playSrc) + "\" title=\"Клікніть, щоб програти відео прямо тут\">",
        thumbSrc ? ("    <img src=\"" + esc(thumbSrc) + "\" alt=\"" + esc(v.display_name) + "\" loading=\"lazy\">") : "    <div style=\"display:flex;align-items:center;justify-content:center;height:100%;color:var(--text-muted);\">🎥 " + esc(v.ext) + "</div>",
        "    <span class=\"vault-tag-tl\">" + esc(v.cat_label) + "</span>",
        "    <span class=\"vault-tag-br\">" + esc(fmtTag || (v.ext + " • " + v.size_mb + " MB")) + "</span>",
        "    <div class=\"vault-play-badge\">▶</div>",
        "  </div>",
        "  <div style=\"display:flex;align-items:center;gap:5px;flex-wrap:wrap;\">" + originBadgeHtml + portBadgeHtml + dupBadgeHtml + "</div>",
        "  <div class=\"vault-title\">" + esc(v.display_name) + "</div>",
        rationaleHtml,
        "  <div class=\"vault-path-mono\" data-reveal-finder=\"" + esc(v.rel_path) + "\" title=\"Відкрити файл у Finder\">📁 " + esc(v.file) + "</div>",
        "  <div class=\"btn-group\">",
        (pIdx !== -1 ? "    <button class=\"btn btn-amber\" style=\"padding:3px 8px;font-size:11px;\" data-play-pidx=\"" + pIdx + "\">🖥️ У монітор</button>" : ""),
        (pIdx !== -1 ? "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-popup-pidx=\"" + pIdx + "\">🔍 Кінозал</button>" : ""),
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-reveal-finder=\"" + esc(v.rel_path) + "\">📁 Finder</button>",
        "    <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" data-copy-text=\"" + esc(v.rel_path) + "\">📋</button>",
        "  </div>",
        "</div>"
      ].filter(Boolean).join("\n");
    }).join("\n");

    return [
      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎥 Відеофайли — EP" + esc(epData.ep) + " (" + videos.length + " доступних: " + nativeCnt + " власних + " + crossCnt + " універсальних B-Roll)</div>",
      "      <div class=\"panel-desc\">Клік по прев'ю миттєво запускає HTML5-плеєр. У <b>🌌 Абстрактні & Спільні</b> зібрані лише перевірені безіменні кадри без чужих облич, аніме й тексту інших героїв.</div>",
      "    </div>",
      "    <button class=\"btn btn-cyan\" data-reveal-finder=\"" + esc(vaultEp.primary_footage_dir) + "\">📁 Папка у Finder</button>",
      "  </div>",
      "  <div class=\"vault-origin-bar\">" + originPillsHtml.join("") + "</div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">" + pillsHtml.join("") + "</div>",
      "    <input type=\"search\" id=\"vaultVidSearchInput\" class=\"search-input\" placeholder=\"Пошук відео, 4K або теми сцени...\" value=\"" + esc(state.vaultVidSearch) + "\">",
      "  </div>",
      "  <div class=\"vault-grid\">" + (cardsHtml || "<div style='color:var(--text-muted);padding:1rem;'>Немає відео за цим фільтром.</div>") + "</div>",
      "</div>"
    ].join("\n");
  }

  function buildVaultImagesHtml(vaultEp, playlist) {
    var images = vaultEp.images || [];
    if (!images.length) {
      return "<div class=\"panel-card\"><div class=\"panel-title\">🖼️ Зображення ще не додані для EP" + esc(epData.ep) + "</div></div>";
    }
    var nativeCnt = images.filter(function (im) { return !im.is_cross; }).length;
    var crossCnt = images.filter(function (im) { return !!im.is_cross; }).length;
    var dupCnt = images.filter(function (im) { return !!im.is_dup_md5; }).length;
    var catCounts = {};
    var catLabels = {};
    images.forEach(function (im) {
      catCounts[im.cat] = (catCounts[im.cat] || 0) + 1;
      catLabels[im.cat] = im.cat_label;
    });
    var originPillsHtml = [
      "<button class=\"filter-pill" + (state.vaultImgOrigin === "all" ? " active" : "") + "\" data-vimg-origin=\"all\">📦 Усі (" + images.length + ")</button>",
      "<button class=\"filter-pill" + (state.vaultImgOrigin === "native" ? " active" : "") + "\" data-vimg-origin=\"native\">⭐ Власні героя (" + nativeCnt + ")</button>",
      "<button class=\"filter-pill" + (state.vaultImgOrigin === "cross" ? " active" : "") + "\" data-vimg-origin=\"cross\">🌌 Абстрактні & Спільні (" + crossCnt + ")</button>"
    ];
    if (dupCnt > 0) {
      originPillsHtml.push("<button class=\"filter-pill" + (state.vaultImgUniqueOnly ? " active" : "") + "\" id=\"btnToggleImgUnique\">✨ Без копій MD5 (" + (images.length - dupCnt) + ")</button>");
    }
    var pillsHtml = ["<button class=\"filter-pill" + (state.vaultImgCat === "all" ? " active" : "") + "\" data-vimg-cat=\"all\">Усі категорії (" + images.length + ")</button>"];
    Object.keys(catCounts).sort().forEach(function (cat) {
      pillsHtml.push("<button class=\"filter-pill" + (state.vaultImgCat === cat ? " active" : "") + "\" data-vimg-cat=\"" + esc(cat) + "\">" + esc(catLabels[cat]) + " (" + catCounts[cat] + ")</button>");
    });

    var q = (state.vaultImgSearch || "").trim().toLowerCase();
    var filtered = images.filter(function (im) {
      if (state.vaultImgOrigin === "native" && im.is_cross) return false;
      if (state.vaultImgOrigin === "cross" && !im.is_cross) return false;
      if (state.vaultImgUniqueOnly && im.is_dup_md5) return false;
      if (state.vaultImgCat !== "all" && im.cat !== state.vaultImgCat) return false;
      if (q && (im.file + " " + im.display_name + " " + im.rel_path + " " + im.cat_label + " " + (im.match_reason || "") + " " + (im.source_label || "") + " " + (im.suggested_scenes || []).join(" ")).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });

    var cardsHtml = filtered.map(function (im) {
      var pIdx = findPlaylistIdxByFileOrPath(playlist, im.file, im.rel_path);
      var imgSrc = im.thumb ? ("../" + im.thumb) : resolveMediaSrc(im.rel_path, im.preview_path, im.thumb);
      var scenesHtml = (im.suggested_scenes || []).map(function (sc) {
        return "<span class=\"vault-scene-tag\">#" + esc(sc) + "</span>";
      }).join("");
      var originBadgeHtml = im.is_cross
        ? "<span class=\"vault-origin-badge is-cross\">" + esc(im.source_label || "🌌 Універсальний B-Roll") + "</span>"
        : "<span class=\"vault-origin-badge is-native\">⭐ Власний EP" + esc(epData.ep) + "</span>";
      var dupBadgeHtml = im.is_dup_md5
        ? "<span class=\"vault-origin-badge is-dup\" title=\"Побайтова копія файлу: " + esc(im.dup_of || "") + "\">👯 Копія MD5</span>"
        : "";
      var fmtTag = [im.res_label, im.ext, im.size_mb ? (im.size_mb + " MB") : ""].filter(Boolean).join(" • ");
      var rationaleHtml = im.match_reason
        ? "<div class=\"vault-rationale\"><b>🎯 Сценарій:</b> " + esc(im.match_reason) + (scenesHtml ? (" <span>(" + scenesHtml + ")</span>") : "") + "</div>"
        : "";
      return [
        "<div class=\"vault-card" + (im.is_cross ? " is-cross" : "") + "\">",
        "  <div class=\"vault-thumb-box\"" + (pIdx !== -1 ? (" data-popup-pidx=\"" + pIdx + "\"") : (" data-reveal-finder=\"" + esc(im.rel_path) + "\"")) + " title=\"Клікніть, щоб відкрити у великому вікні\">",
        "    <img src=\"" + esc(imgSrc) + "\" alt=\"" + esc(im.display_name) + "\" loading=\"lazy\">",
        "    <span class=\"vault-tag-tl\">" + esc(im.cat_label) + "</span>",
        "    <span class=\"vault-tag-br\">" + esc(fmtTag || (im.ext + " • " + im.size_mb + " MB")) + "</span>",
        "  </div>",
        "  <div style=\"display:flex;align-items:center;gap:5px;flex-wrap:wrap;\">" + originBadgeHtml + dupBadgeHtml + "</div>",
        "  <div class=\"vault-title\">" + esc(im.display_name) + "</div>",
        rationaleHtml,
        "  <div class=\"vault-path-mono\" data-reveal-finder=\"" + esc(im.rel_path) + "\" title=\"Відкрити файл у Finder\">📁 " + esc(im.file) + "</div>",
        "  <div class=\"btn-group\">",
        (pIdx !== -1 ? "    <button class=\"btn btn-amber\" style=\"padding:3px 8px;font-size:11px;\" data-play-pidx=\"" + pIdx + "\">🖥️ У монітор</button>" : ""),
        (pIdx !== -1 ? "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-popup-pidx=\"" + pIdx + "\">🔍 Збільшити</button>" : ""),
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-reveal-finder=\"" + esc(im.rel_path) + "\">📁 Finder</button>",
        "    <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" data-copy-text=\"" + esc(im.rel_path) + "\">📋</button>",
        "  </div>",
        "</div>"
      ].filter(Boolean).join("\n");
    }).join("\n");

    return [
      "<div class=\"panel-card\" style=\"border-color:rgba(251,191,36,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🖼️ Галерея Кадрів & Досьє — EP" + esc(epData.ep) + " (" + images.length + " доступних: " + nativeCnt + " власних + " + crossCnt + " універсальних)</div>",
      "      <div class=\"panel-desc\">2K концепт-кадри для старту Flow, архівні фото, формули й 4K плашки. Повністю очищено від дублів та сторонніх файлів.</div>",
      "    </div>",
      "  </div>",
      "  <div class=\"vault-origin-bar\">" + originPillsHtml.join("") + "</div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">" + pillsHtml.join("") + "</div>",
      "    <input type=\"search\" id=\"vaultImgSearchInput\" class=\"search-input\" placeholder=\"Пошук зображення або теми сцени...\" value=\"" + esc(state.vaultImgSearch) + "\">",
      "  </div>",
      "  <div class=\"vault-grid\">" + (cardsHtml || "<div style='color:var(--text-muted);padding:1rem;'>Немає зображень за цим фільтром.</div>") + "</div>",
      "</div>"
    ].join("\n");
  }

  function buildTriadsQueueHtml(triads, playlist) {
    var rdyVid = triads.filter(function (t) { return t.status === "video_ready"; }).length;
    var rdyImg = triads.filter(function (t) { return t.status === "image_ready"; }).length;
    var hasCrossCnt = triads.filter(function (t) { return (t.cross_candidates || []).length > 0; }).length;
    var todoCnt = triads.length - rdyVid - rdyImg;

    var q = (state.triadSearch || "").trim().toLowerCase();
    var filtered = triads.filter(function (t) {
      if (state.triadFilter === "has_cross") {
        if (!(t.cross_candidates || []).length) return false;
      } else if (state.triadFilter !== "all" && (t.status || "todo") !== state.triadFilter) {
        return false;
      }
      if (q && (t.title_ua + " " + t.title_en + " " + (t.vo_quote || "") + " " + (t.symbol || "") + " " + t.act + " " + t.p1_start + " " + t.p2_flow + " " + t.p3_end + " " + (t.cross_candidates || []).map(function (c) { return c.display_name + " " + c.match_reason; }).join(" ")).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });

    var cardsHtml = filtered.map(function (t) {
      var isDone = !!state.checked["triad_" + t.num];
      var statusCls = t.status === "video_ready" ? "status-video_ready" : (t.status === "image_ready" ? "status-image_ready" : "");
      var statusBadge = t.status === "video_ready"
        ? "<span class=\"chip chip-emerald\">✅ Відео 24fps готове</span>"
        : (t.status === "image_ready" ? "<span class=\"chip chip-cyan\">🖼️ Стартовий 2K кадр готовий</span>" : "<span class=\"chip chip-amber\">⏳ Очікує генерації</span>");

      var pVidIdx = t.raw_video_path ? findPlaylistIdxByFileOrPath(playlist, "", t.raw_video_path) : -1;
      var pImgIdx = t.raw_image_path ? findPlaylistIdxByFileOrPath(playlist, "", t.raw_image_path) : -1;

      var thumbHtml = "";
      if (t.keyframe_preview || t.raw_video_path) {
        var thumbSrc = t.keyframe_preview ? ("../" + t.keyframe_preview) : "";
        if (thumbSrc) {
          thumbHtml = "<img src=\"" + esc(thumbSrc) + "\" alt=\"" + esc(t.title_ua) + "\" style=\"width:136px;aspect-ratio:16/9;object-fit:cover;border-radius:6px;border:1px solid var(--border);\">";
        }
      }

      var voQuoteHtml = (t.vo_quote || t.concept) ? [
        "  <div style=\"margin-bottom:0.65rem;padding:0.55rem 0.75rem;border-radius:7px;background:rgba(56,189,248,0.06);border-left:3px solid var(--cyan);font-size:12px;line-height:1.5;color:#e2e8f0;\">",
        "    <span style=\"font-weight:700;color:var(--cyan);font-size:11px;text-transform:uppercase;letter-spacing:0.03em;\">🎙️ Документальна озвучка (VO Sync): </span>",
        "    <span>" + esc(t.vo_quote || t.concept) + "</span>",
        (t.symbol ? ("    <div style=\"margin-top:4px;font-size:11.2px;color:var(--amber);\"><b>💎 Художній символ:</b> " + esc(t.symbol) + "</div>") : ""),
        "  </div>"
      ].join("\n") : "";

      var cands = t.cross_candidates || [];
      var crossCandsHtml = cands.length ? [
        "  <div class=\"triad-cross-box\">",
        "    <div class=\"triad-cross-head\">",
        "      <span>♻️ Готові референси & B-Roll із Загальної Медіатеки проєкту (" + cands.length + " шт. — економія ресурсів Flow!)</span>",
        "    </div>",
        "    <div class=\"triad-cross-row\">",
        cands.slice(0, 6).map(function (c) {
          var cpIdx = findPlaylistIdxByFileOrPath(playlist, c.file, c.rel_path);
          var cThumb = c.thumb ? ("../" + c.thumb) : "";
          var cMeta = [c.res_label, c.dur_label].filter(Boolean).join(" · ");
          return [
            "<div class=\"triad-cross-item\">",
            (cThumb ? ("<img src=\"" + esc(cThumb) + "\" alt=\"" + esc(c.display_name) + "\" loading=\"lazy\">") : ""),
            "<div style=\"min-width:0;flex:1;\">",
            "  <div style=\"display:flex;align-items:center;gap:4px;\"><span style=\"font-size:11px;font-weight:700;color:var(--text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1;\">" + (c.media_type === "video" ? "🎥 " : "🖼️ ") + esc(c.display_name) + "</span>" + (cMeta ? ("<span class=\"vault-fmt-pill\">" + esc(cMeta) + "</span>") : "") + "</div>",
            "  <div style=\"font-size:10px;color:#94a3b8;line-height:1.3;\">" + esc(c.source_label) + " — " + esc(c.match_reason) + "</div>",
            "  <div style=\"display:flex;gap:4px;margin-top:4px;flex-wrap:wrap;\">",
            (cpIdx !== -1 ? ("<button class=\"btn btn-amber\" style=\"padding:1px 6px;font-size:10px;\" data-play-pidx=\"" + cpIdx + "\">▶️</button><button class=\"btn btn-cyan\" style=\"padding:1px 6px;font-size:10px;\" data-popup-pidx=\"" + cpIdx + "\">🔍</button>") : ""),
            "    <button class=\"btn\" style=\"padding:1px 6px;font-size:10px;\" data-reveal-finder=\"" + esc(c.rel_path) + "\">📁</button>",
            "  </div>",
            "</div>",
            "</div>"
          ].join("");
        }).join("\n"),
        "    </div>",
        "  </div>"
      ].join("\n") : "";

      return [
        "<article class=\"triad-card " + statusCls + "\">",
        "  <div class=\"triad-header\">",
        "    <div style=\"display:flex;gap:0.75rem;align-items:flex-start;flex:1;min-width:260px;\">",
        "      <input type=\"checkbox\" class=\"sop-checkbox\" data-triad-check=\"" + esc(t.num) + "\"" + (isDone ? " checked" : "") + " style=\"margin-top:4px;\">",
        thumbHtml,
        "      <div>",
        "        <div style=\"display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin-bottom:4px;\">",
        "          <span class=\"tc-badge\">#" + esc(t.num) + " • TC " + esc(t.tc) + "</span>",
        (t.vo_take ? ("          <span class=\"chip chip-cyan\">🎙️ " + esc(t.vo_take) + "</span>") : ""),
        "          <span class=\"chip chip-purple\">" + esc(t.act) + "</span>",
        "          <span class=\"chip\">" + esc(t.cat_label || "🎬 Тріада") + "</span>",
        statusBadge,
        "        </div>",
        "        <h4 style=\"font-size:14.5px;color:var(--text-primary);margin-bottom:2px;\">" + esc(t.title_ua) + " <span style=\"color:var(--text-muted);font-weight:500;font-size:12px;\">/ " + esc(t.title_en) + "</span></h4>",
        "      </div>",
        "    </div>",
        "    <div class=\"btn-group\">",
        (pVidIdx !== -1 ? "      <button class=\"btn btn-amber\" style=\"padding:4px 9px;font-size:11px;\" data-play-pidx=\"" + pVidIdx + "\">▶️ Відео</button>" : ""),
        (pImgIdx !== -1 && pVidIdx === -1 ? "      <button class=\"btn btn-cyan\" style=\"padding:4px 9px;font-size:11px;\" data-play-pidx=\"" + pImgIdx + "\">🖼️ Кадр</button>" : ""),
        (t.raw_video_path ? "      <button class=\"btn btn-cyan\" style=\"padding:4px 9px;font-size:11px;\" data-reveal-finder=\"" + esc(t.raw_video_path) + "\">📁 MP4</button>" : ""),
        (t.raw_image_path ? "      <button class=\"btn btn-cyan\" style=\"padding:4px 9px;font-size:11px;\" data-reveal-finder=\"" + esc(t.raw_image_path) + "\">📁 JPG</button>" : ""),
        "      <button class=\"btn btn-emerald\" style=\"padding:4px 10px;font-size:11px;\" data-copy-triad-full=\"" + esc(t.num) + "\">📋 Копіювати Тріаду (1+2+3)</button>",
        "    </div>",
        "  </div>",
        voQuoteHtml,
        "  <div class=\"triad-prompts-grid\">",
        "    <div class=\"triad-step-box step-1\">",
        "      <div class=\"triad-step-head\"><span style=\"color:var(--cyan);\">1. Start Image (Кадр А • 16:9)</span><button class=\"btn\" style=\"padding:2px 7px;font-size:10.5px;\" data-copy-triad-part=\"" + esc(t.num) + ":p1\">📋 Промпт 1</button></div>",
        "      <pre class=\"triad-prompt-code\">" + esc(t.p1_start) + "</pre>",
        "    </div>",
        "    <div class=\"triad-step-box step-2\">",
        "      <div class=\"triad-step-head\"><span style=\"color:var(--amber);\">2. Video Morph Action (Flow Перехід)</span><button class=\"btn btn-amber\" style=\"padding:2px 7px;font-size:10.5px;\" data-copy-triad-part=\"" + esc(t.num) + ":p2\">📋 Промпт 2</button></div>",
        "      <pre class=\"triad-prompt-code\">" + esc(t.p2_flow) + "</pre>",
        "    </div>",
        "    <div class=\"triad-step-box step-3\">",
        "      <div class=\"triad-step-head\"><span style=\"color:var(--emerald);\">3. End Image (Кадр В • Фінал)</span><button class=\"btn btn-emerald\" style=\"padding:2px 7px;font-size:10.5px;\" data-copy-triad-part=\"" + esc(t.num) + ":p3\">📋 Промпт 3</button></div>",
        "      <pre class=\"triad-prompt-code\">" + esc(t.p3_end) + "</pre>",
        "    </div>",
        "  </div>",
        crossCandsHtml,
        "  <div class=\"triad-footer-meta\">",
        "    <span><b>✂️ DaVinci Resolve:</b> " + esc(t.davinci_recipe) + "</span>",
        "    <span><b>🔊 SFX:</b> " + esc(t.sfx_cue) + "</span>",
        "  </div>",
        "</article>"
      ].join("\n");
    }).join("\n");

    return [
      "<div class=\"panel-card\" style=\"border-color:rgba(167,139,250,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🚀 Пріоритетна Черга Google Flow — Стандарт 3-Промптної Тріади (" + triads.length + " сцен × 3 промпти)</div>",
      "      <div class=\"panel-desc\">Єдиний формат по всіх 10 титанах: <b>Промпт 1 (Start Кадр A)</b> ➔ <b>Промпт 2 (Рух/Морф Flow 24fps)</b> ➔ <b>Промпт 3 (End Кадр B)</b>. Всі тексти очищено для 100% проходження фільтрів безпеки Google Flow (Policy-Safe).</div>",
      "    </div>",
      "    <span class=\"chip chip-emerald\">🛡️ 100% Policy-Safe</span>",
      "  </div>",
      "  <div class=\"filter-toolbar\">",
      "    <div class=\"filter-pills\">",
      "      <button class=\"filter-pill" + (state.triadFilter === "all" ? " active" : "") + "\" data-triad-filter=\"all\">Усі (" + triads.length + ")</button>",
      "      <button class=\"filter-pill" + (state.triadFilter === "video_ready" ? " active" : "") + "\" data-triad-filter=\"video_ready\">✅ Відео готові (" + rdyVid + ")</button>",
      "      <button class=\"filter-pill" + (state.triadFilter === "image_ready" ? " active" : "") + "\" data-triad-filter=\"image_ready\">🖼️ Лише 2K кадр (" + rdyImg + ")</button>",
      "      <button class=\"filter-pill" + (state.triadFilter === "has_cross" ? " active" : "") + "\" data-triad-filter=\"has_cross\">♻️ Є готовий B-Roll (" + hasCrossCnt + ")</button>",
      "      <button class=\"filter-pill" + (state.triadFilter === "todo" ? " active" : "") + "\" data-triad-filter=\"todo\">⏳ В черзі (" + todoCnt + ")</button>",
      "    </div>",
      "    <input type=\"search\" id=\"triadSearchInput\" class=\"search-input\" placeholder=\"Пошук сцен та промптів...\" value=\"" + esc(state.triadSearch) + "\">",
      "  </div>",
      "  <div class=\"triad-list\">" + (cardsHtml || "<div style='color:var(--text-muted);padding:1rem;'>Сцен за цим фільтром не знайдено.</div>") + "</div>",
      "</div>"
    ].join("\n");
  }

  function selectDockClip(playlistIndex, scrollIntoViewCard) {
    var playlist = buildEpisodeVideoPlaylist();
    if (!playlist.length) return;
    if (playlistIndex < 0) playlistIndex = playlist.length - 1;
    if (playlistIndex >= playlist.length) playlistIndex = 0;
    state.mediaActiveIndex = playlistIndex;

    var clip = playlist[playlistIndex];
    var vid = document.getElementById("dockMainVideo");
    var img = document.getElementById("dockMainImage");
    var badgeEl = document.getElementById("dockMetaBadge");
    var tcEl = document.getElementById("dockMetaTc");
    var titleEl = document.getElementById("dockMetaTitle");
    var subEl = document.getElementById("dockMetaSub");
    var idxEl = document.getElementById("dockCounterLabel");
    var soundBtn = document.getElementById("btnDockToggleSound");

    if (clip.type === "image") {
      if (vid) {
        vid.pause();
        vid.style.display = "none";
      }
      if (img) {
        img.src = clip.src;
        img.style.display = "block";
      }
      if (soundBtn) soundBtn.style.display = "none";
    } else {
      if (img) img.style.display = "none";
      if (vid) {
        vid.style.display = "block";
        if (vid.getAttribute("data-src") !== clip.src) {
          var keepMuted = vid.muted;
          vid.src = clip.src;
          vid.setAttribute("data-src", clip.src);
          vid.muted = keepMuted;
          var p = vid.play();
          if (p && p.catch) p.catch(function () {});
        }
      }
      if (soundBtn) soundBtn.style.display = "inline-flex";
    }

    if (badgeEl) {
      badgeEl.className = "chip " + clip.chipClass;
      badgeEl.textContent = clip.kindLabel;
    }
    if (tcEl) tcEl.textContent = "TC " + clip.tc;
    if (titleEl) titleEl.textContent = clip.title;
    if (subEl) subEl.textContent = clip.track + " — " + clip.desc;
    if (idxEl) idxEl.textContent = (playlistIndex + 1) + " / " + playlist.length;

    var cards = document.querySelectorAll("#dockReelScroll .reel-item-card");
    for (var i = 0; i < cards.length; i++) {
      var cIdx = parseInt(cards[i].getAttribute("data-pidx"), 10);
      var isAct = cIdx === playlistIndex;
      cards[i].classList.toggle("active", isAct);
      if (isAct && scrollIntoViewCard) {
        try { cards[i].scrollIntoView({ block: "nearest", behavior: "smooth" }); } catch (e) {}
      }
    }
  }

  function openCinemaModal(playlistIndex) {
    var playlist = buildEpisodeVideoPlaylist();
    if (!playlist.length) return;
    if (typeof playlistIndex !== "number" || isNaN(playlistIndex)) playlistIndex = state.mediaActiveIndex || 0;
    if (playlistIndex < 0) playlistIndex = playlist.length - 1;
    if (playlistIndex >= playlist.length) playlistIndex = 0;
    state.mediaActiveIndex = playlistIndex;

    var modal = document.getElementById("videoLightboxModal");
    if (!modal) return;
    var clip = playlist[playlistIndex];

    var sideItemsHtml = playlist.map(function (item, idx) {
      var activeCls = idx === playlistIndex ? " active" : "";
      var thumbHtml = item.type === "image"
        ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.poster || item.src) + "\" loading=\"lazy\" style=\"object-fit:cover;\">"
        : (item.type === "audio"
          ? "<div class=\"reel-thumb-video\" style=\"background:rgba(16,185,129,0.12);display:flex;align-items:center;justify-content:center;font-size:22px;\">🎙️</div>"
          : (item.poster
            ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.poster) + "\" loading=\"lazy\" style=\"object-fit:cover;\">"
            : "<video class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" muted loop playsinline preload=\"metadata\"></video>"));

      return [
        "<div class=\"reel-item-card" + activeCls + "\" data-modal-pidx=\"" + idx + "\">",
        "  <div class=\"reel-thumb-wrap\">",
        thumbHtml,
        "    <span class=\"reel-tc-tag\">" + esc(item.tc) + "</span>",
        "  </div>",
        "  <div style=\"min-width:0;\">",
        "    <span class=\"chip " + item.chipClass + "\" style=\"font-size:9.8px;padding:1px 6px;\">" + esc(item.kindLabel) + "</span>",
        "    <div class=\"reel-item-title\">" + esc(item.title) + "</div>",
        "    <div class=\"reel-item-file\">" + esc(item.file) + "</div>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var stageMediaHtml = clip.type === "image"
      ? "<div style=\"position:relative;cursor:pointer;\" data-reveal-finder=\"" + esc(clip.localPath || clip.file) + "\" title=\"Клікніть по фото, щоб відкрити його у Finder\"><img id=\"modalStageImage\" class=\"cinema-stage-video\" src=\"" + esc(clip.src) + "\" style=\"object-fit:contain;background:#05070c;\"><span style=\"position:absolute;top:10px;left:10px;background:rgba(12,14,19,0.88);color:var(--cyan);padding:4px 8px;border-radius:4px;font-size:11px;font-weight:700;\">📁 Клікніть, щоб відкрити цей файл у Finder</span></div>"
      : (clip.type === "audio"
        ? "<div style=\"position:relative;background:#05070c;padding:24px;border-radius:8px;text-align:center;\"><img src=\"" + esc(clip.poster || "") + "\" style=\"max-height:220px;border-radius:8px;margin-bottom:16px;box-shadow:0 8px 24px rgba(0,0,0,0.6);\"><div style=\"font-size:16px;font-weight:700;color:var(--emerald);margin-bottom:8px;\">" + esc(clip.title) + "</div><div style=\"font-size:12px;color:var(--cyan);font-family:var(--mono);margin-bottom:16px;\">" + esc(clip.file) + " • " + esc(clip.track) + "</div><audio id=\"modalStageAudio\" src=\"" + esc(clip.src) + "\" controls autoplay style=\"width:100%;max-width:540px;\"></audio></div>"
        : "<video id=\"modalStageVideo\" class=\"cinema-stage-video\" src=\"" + esc(clip.src) + "\" controls autoplay loop playsinline></video>");

    modal.innerHTML = [
      "<div class=\"cinema-modal-window\" role=\"dialog\" aria-modal=\"true\">",
      "  <div class=\"cinema-modal-header\">",
      "    <div style=\"display:flex;align-items:center;gap:0.65rem;flex-wrap:wrap;\">",
      "      <span class=\"chip chip-cyan\">🎬 СПЛИВАЮЧИЙ КІНОЗАЛ • EP" + esc(epData.ep) + " " + esc(epData.name) + "</span>",
      "      <span class=\"chip " + clip.chipClass + "\" id=\"modalKindChip\">" + esc(clip.kindLabel) + "</span>",
      "      <span class=\"tc-badge\" id=\"modalTcBadge\">TC " + esc(clip.tc) + "</span>",
      "      <span style=\"font-family:var(--mono);font-size:11.5px;color:var(--text-secondary);\" id=\"modalCounter\">Елемент " + (playlistIndex + 1) + " із " + playlist.length + "</span>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn\" id=\"btnModalPrev\">◀ Попереднє</button>",
      "      <button class=\"btn\" id=\"btnModalNext\">Наступне ▶</button>",
      "      <button class=\"btn btn-amber\" id=\"btnModalClose\">✕ Закрити (Esc)</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"cinema-modal-body\">",
      "    <div class=\"cinema-stage-col\">",
      stageMediaHtml,
      "      <div style=\"display:flex;justify-content:space-between;align-items:flex-start;gap:0.75rem;flex-wrap:wrap;\">",
      "        <div style=\"flex:1;min-width:240px;\">",
      "          <h3 style=\"font-size:16px;color:var(--text-primary);margin-bottom:4px;\" id=\"modalClipTitle\">" + esc(clip.title) + "</h3>",
      "          <div style=\"font-size:12px;color:var(--cyan);font-family:var(--mono);margin-bottom:4px;\" id=\"modalClipTrack\">" + esc(clip.track) + "</div>",
      "          <div style=\"font-size:12.5px;color:var(--text-secondary);line-height:1.5;\" id=\"modalClipDesc\">" + esc(clip.desc) + "</div>",
      "        </div>",
      "        <div class=\"btn-group\">",
      "          <button class=\"btn btn-cyan\" id=\"btnModalRevealFinder\">📁 Відкрити у Finder</button>",
      "          <button class=\"btn btn-emerald\" id=\"btnModalCopyPath\">📋 Локальний шлях</button>",
      (clip.prompt ? "          <button class=\"btn btn-purple\" id=\"btnModalCopyPrompt\">📋 Промпт Flow/Veo</button>" : ""),
      "          <a class=\"btn btn-cyan\" id=\"btnModalGithub\" href=\"" + esc(clip.githubUrl) + "\" target=\"_blank\" rel=\"noopener\">GitHub ↗</a>",
      (clip.externalUrl ? "          <a class=\"btn\" href=\"" + esc(clip.externalUrl) + "\" target=\"_blank\" rel=\"noopener\">Першоджерело YouTube ↗</a>" : ""),
      "        </div>",
      "      </div>",
      "    </div>",
      "    <div class=\"cinema-playlist-col\" id=\"modalPlaylistScroll\">",
      "      <div style=\"font-size:11.5px;font-weight:700;color:var(--cyan);margin-bottom:4px;\">🎞️ Прокрутка всіх медіафайлів епізоду (" + playlist.length + "):</div>",
      sideItemsHtml,
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n");

    modal.classList.add("open");

    // Animate visible thumbnails in modal sidebar on hover & play active
    modal.querySelectorAll("[data-modal-pidx]").forEach(function (card) {
      var v = card.querySelector("video");
      if (v) {
        var p = v.play();
        if (p && p.catch) p.catch(function () {});
      }
      card.addEventListener("click", function () {
        var nextIdx = parseInt(card.getAttribute("data-modal-pidx"), 10);
        openCinemaModal(nextIdx);
        selectDockClip(nextIdx, false);
      });
    });

    document.getElementById("btnModalClose").addEventListener("click", closeCinemaModal);
    document.getElementById("btnModalPrev").addEventListener("click", function () {
      openCinemaModal(playlistIndex - 1);
      selectDockClip(state.mediaActiveIndex, false);
    });
    document.getElementById("btnModalNext").addEventListener("click", function () {
      openCinemaModal(playlistIndex + 1);
      selectDockClip(state.mediaActiveIndex, false);
    });
    var fBtn = document.getElementById("btnModalRevealFinder");
    if (fBtn) {
      fBtn.addEventListener("click", function () {
        revealInFinder(clip.localPath || clip.file, clip.title);
      });
    }

    document.getElementById("btnModalCopyPath").addEventListener("click", function () {
      copyText(clip.localPath, clip.file);
    });
    var pBtn = document.getElementById("btnModalCopyPrompt");
    if (pBtn && clip.prompt) {
      pBtn.addEventListener("click", function () {
        copyText(clip.prompt, "Flow промпт");
      });
    }

    modal.onclick = function (ev) {
      if (ev.target === modal) closeCinemaModal();
    };
  }

  function closeCinemaModal() {
    var modal = document.getElementById("videoLightboxModal");
    if (!modal) return;
    modal.querySelectorAll("video").forEach(function (v) {
      try { v.pause(); } catch (e) {}
    });
    modal.classList.remove("open");
    modal.innerHTML = "";
  }

  if (document.addEventListener) {
    document.addEventListener("keydown", function (ev) {
      var modal = document.getElementById("videoLightboxModal");
      if (!modal || !modal.classList.contains("open")) return;
      if (ev.key === "Escape") closeCinemaModal();
      else if (ev.key === "ArrowRight") openCinemaModal((state.mediaActiveIndex || 0) + 1);
      else if (ev.key === "ArrowLeft") openCinemaModal((state.mediaActiveIndex || 0) - 1);
    });
  }

  function setupReelAnimationObserver() {
    if (reelObserver) {
      reelObserver.disconnect();
      reelObserver = null;
    }
    var container = document.getElementById("dockReelScroll");
    if (!container) return;
    var vids = container.querySelectorAll(".reel-thumb-video");
    if (!state.reelAutoAnimate) {
      for (var i = 0; i < vids.length; i++) {
        vids[i].pause();
      }
      return;
    }
    if ("IntersectionObserver" in window) {
      reelObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          var v = entry.target;
          if (entry.isIntersecting && state.reelAutoAnimate) {
            var p = v.play();
            if (p && p.catch) p.catch(function () {});
          } else {
            v.pause();
          }
        });
      }, { root: container, threshold: 0.25 });
      for (var j = 0; j < vids.length; j++) {
        reelObserver.observe(vids[j]);
      }
    } else {
      for (var k = 0; k < vids.length; k++) {
        var pr = vids[k].play();
        if (pr && pr.catch) pr.catch(function () {});
      }
    }
  }

  function renderMedia() {
    var pane = document.getElementById("pane-media");
    if (!pane) return;
    var allMedia = window.MEDIA_ACQUISITION_POOL || {};
    var epMedia = allMedia[epData.ep] || { dossiers: [], archives: [], flow_queue: [], portrait: {} };
    var repoRoot = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/";
    var playlist = buildEpisodeVideoPlaylist();

    if (state.mediaActiveIndex >= playlist.length) state.mediaActiveIndex = 0;
    var activeClip = playlist[state.mediaActiveIndex] || {
      kindLabel: "Відео",
      chipClass: "chip-cyan",
      title: "Немає кліпів",
      tc: "00:00",
      track: "",
      desc: "",
      src: ""
    };

    var nArch = (epMedia.archives || []).length;
    var nFlow = (epMedia.flow_queue || []).length;
    var nDos = (epMedia.dossiers || []).length;

    var dossiersHtml = (epMedia.dossiers || []).map(function (d, idx) {
      var pIdx = nArch + nFlow + idx;
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--amber);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-amber\">" + esc(d.act) + " • TC " + esc(d.timecode) + "</span>",
        "    <span class=\"chip chip-emerald\">3840×2160 4K PNG + MP4</span>",
        "  </div>",
        "  <div style=\"position:relative;cursor:pointer;overflow:hidden;border-radius:6px;border:1px solid var(--border);margin-bottom:8px;\" data-reveal-finder=\"" + esc(d.raw_4k_png) + "\" title=\"Клікніть, щоб відкрити цей 4K файл у Finder\">",
        "    <img src=\"../" + esc(d.web_preview) + "\" alt=\"" + esc(d.title) + "\" loading=\"lazy\" style=\"width:100%;border-radius:5px;display:block;\">",
        "    <span style=\"position:absolute;top:6px;left:6px;background:rgba(12,14,19,0.85);color:var(--amber);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700;\">📁 Відкрити у Finder</span>",
        "    <span style=\"position:absolute;bottom:8px;right:6px;background:rgba(12,14,19,0.88);color:var(--cyan);border:1px solid rgba(56,189,248,0.45);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700;\">4K PNG</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(d.title) + "</h4>",
        "  <div style=\"font-size:11px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;cursor:pointer;\" data-reveal-finder=\"" + esc(d.raw_4k_png) + "\" title=\"Клікніть, щоб відкрити файл у Finder\">📁 " + esc(d.raw_4k_png) + "</div>",
        "  <div style=\"font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;\">«" + esc(d.highlight) + "»</div>",
        "  <div class=\"btn-group\">",
        "    <button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;\" data-play-pidx=\"" + pIdx + "\">▶️ У монітор</button>",
        "    <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-reveal-finder=\"" + esc(d.raw_4k_png) + "\">📁 У Finder</button>",
        "    <button class=\"btn btn-emerald\" style=\"padding:4px 8px;font-size:11px;\" data-copy-dos-path=\"" + idx + "\">📋 Шлях</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var portrait = epMedia.portrait || {};
    var portraitCardHtml = portrait.web_preview ? [
      "<div class=\"node-box\" style=\"border-top-color:var(--cyan);\">",
      "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
      "    <span class=\"chip chip-cyan\">Реальне архівне фото спікера</span>",
      "    <span class=\"chip chip-purple\">Wikimedia Commons</span>",
      "  </div>",
      "  <div style=\"display:flex;gap:12px;align-items:center;\">",
      "    <a href=\"../" + esc(portrait.web_preview) + "\" target=\"_blank\" rel=\"noopener\">",
      "      <img src=\"../" + esc(portrait.web_preview) + "\" alt=\"" + esc(epData.name) + "\" style=\"width:96px;height:116px;object-fit:cover;border-radius:6px;border:1px solid var(--border);\">",
      "    </a>",
      "    <div style=\"flex:1;\">",
      "      <h4 style=\"margin:0 0 4px 0;\">" + esc(epData.name) + " — Офіційний портрет</h4>",
      "      <div style=\"font-family:var(--mono);font-size:10.8px;color:var(--cyan);margin-bottom:5px;word-break:break-all;\">05_RAW_FOOTAGE/speaker_portraits/" + esc(portrait.raw_file) + "</div>",
      "      <div style=\"font-size:11px;color:var(--text-secondary);margin-bottom:6px;\">Під Dynamic Zoom 1.00→1.05 + Kodak 2383 (65%).</div>",
      "      <div class=\"btn-group\">",
      "        <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" id=\"btnCopyPortraitPath\">📋 Шлях JPG</button>",
      "        <a class=\"btn\" style=\"padding:3px 8px;font-size:11px;text-decoration:none;\" href=\"" + esc(portrait.source_url) + "\" target=\"_blank\" rel=\"noopener\">Джерело ↗</a>",
      "      </div>",
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n") : "";

    
    var epVeos = (window.VEO_ANIMATION_PIPELINE || []).filter(function (v) { return v.ep === epData.ep; });
    var vStatusMap = getVeoStatusMap();
    var epVeoDone = epVeos.filter(function (v) { return !!vStatusMap[v.id]; }).length;

    var veoCardsHtml = epVeos.map(function (item) {
      var isDone = !!vStatusMap[item.id];
      var statusBadge = isDone
        ? '<span class="chip chip-emerald" style="box-shadow:0 0 10px rgba(16,185,129,0.35);">✅ ВІДЕО ГОТОВЕ (4K / 24 FPS)</span>'
        : '<span class="chip chip-amber" style="box-shadow:0 0 10px rgba(251,191,36,0.35);">⏳ В ЧЕРЗІ НА ГЕНЕРАЦІЮ (Veo 6–10с)</span>';

      var mediaPreview = "";
      if (isDone && item.video_preview) {
        mediaPreview = [
          '<div style="position:relative;margin-bottom:8px;">',
          '  <video controls loop preload="metadata" playsinline style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:8px;border:1px solid rgba(16,185,129,0.4);display:block;" src="../' + esc(item.video_preview) + '"></video>',
          '  <div style="position:absolute;top:6px;right:6px;background:rgba(15,23,42,0.85);padding:2px 6px;border-radius:4px;font-size:9.5px;color:var(--emerald);font-weight:700;">VEO / FLOW 4K</div>',
          '  <div style="position:absolute;bottom:6px;left:6px;background:rgba(15,23,42,0.85);padding:2px 6px;border-radius:4px;font-size:9.5px;color:var(--cyan);font-weight:600;cursor:pointer;" data-reveal-finder="' + esc(item.video_path || item.raw_path) + '">📁 Відкрити у Finder</div>',
          '</div>'
        ].join("\n");
      } else {
        mediaPreview = [
          '<div style="position:relative;margin-bottom:8px;overflow:hidden;border-radius:8px;border:1px solid rgba(251,191,36,0.35);cursor:pointer;" data-reveal-finder="' + esc(item.raw_path) + '" title="Клікніть по кадру, щоб відкрити його у Finder">',
          '  <img src="../' + esc(item.web_preview) + '" alt="' + esc(item.title) + '" style="width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 0.2s;" onmouseover="this.style.transform=\'scale(1.02)\'" onmouseout="this.style.transform=\'scale(1)\'">',
          '  <div style="position:absolute;top:6px;right:6px;background:rgba(15,23,42,0.85);padding:2px 6px;border-radius:4px;font-size:9.5px;color:var(--amber);font-weight:700;">2K KEYFRAME</div>',
          '  <div style="position:absolute;bottom:6px;left:6px;background:rgba(15,23,42,0.85);padding:2px 6px;border-radius:4px;font-size:9.5px;color:var(--cyan);font-weight:600;display:flex;align-items:center;gap:4px;">📁 Відкрити у Finder</div>',
          '</div>'
        ].join("\n");
      }

      return [
        '<div class="node-box" style="border-top-color:' + (isDone ? 'var(--emerald)' : 'var(--amber)') + ';background:rgba(251,191,36,0.03);display:flex;flex-direction:column;justify-content:space-between;">',
        '  <div>',
        '    <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap;">',
        '      <span class="chip ' + esc(item.chip) + '">' + esc(item.code) + '</span>',
        '      ' + statusBadge,
        '    </div>',
        mediaPreview,
        '    <h4 style="margin:2px 0 6px 0;line-height:1.35;">' + esc(item.title) + '</h4>',
        '    <div style="display:flex;gap:5px;flex-wrap:wrap;margin-bottom:6px;">',
        '      <span class="chip chip-purple">⏱️ ' + esc(item.tc) + '</span>',
        '      <span class="chip chip-cyan">' + esc(item.act) + '</span>',
        '      <span class="chip chip-emerald">' + esc(item.duration) + '</span>',
        '    </div>',
        '    <div style="font-size:11.5px;color:var(--text-secondary);background:rgba(56,189,248,0.06);border-left:3px solid var(--cyan);padding:6px 8px;border-radius:0 6px 6px 0;margin-bottom:8px;line-height:1.4;">',
        '      <strong>🎬 Рух камери:</strong> ' + esc(item.motion_direction),
        '    </div>',
        '    <div style="margin-bottom:8px;">',
        '      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:3px;">',
        '        <span style="font-size:10px;color:var(--amber);font-weight:700;">ПРОМПТ VEO 2 / FLOW:</span>',
        '        <button class="btn btn-purple" style="padding:2px 6px;font-size:10px;" data-copy-veo-prompt="' + esc(item.id) + '">📋 Копіювати</button>',
        '      </div>',
        '      <pre style="background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:6px;padding:6px;font-size:10.5px;color:var(--text-primary);white-space:pre-wrap;word-break:break-word;font-family:var(--mono);max-height:75px;overflow-y:auto;margin:0;">' + esc(item.prompt) + '</pre>',
        '    </div>',
        '  </div>',
        '  <div style="border-top:1px solid var(--border);padding-top:8px;margin-top:4px;display:flex;flex-direction:column;gap:6px;">',
        '    <button class="btn ' + (isDone ? 'btn-emerald' : 'btn-amber') + '" style="width:100%;padding:6px 10px;font-size:11.5px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;" data-toggle-ep-veo="' + esc(item.id) + '">',
        '      ' + (isDone ? '✅ Виконано (Повернути в чергу)' : '⏳ Позначити як виконано (відео згенеровано)'),
        '    </button>',
        '    <button class="btn btn-cyan" style="width:100%;padding:4px 8px;font-size:11px;cursor:pointer;" data-reveal-finder="' + esc(item.raw_path) + '">📁 Відкрити цей 2K-файл у Finder</button>',
        '  </div>',
        '</div>'
      ].join("\n");
    }).join("\n");

    var veoMasterSectionHtml = epVeos.length ? [
      '<div class="panel-card" style="border-color:rgba(251,191,36,0.55);background:linear-gradient(180deg,rgba(251,191,36,0.06),transparent);margin-bottom:1.2rem;">',
      '  <div class="panel-head">',
      '    <div>',
      '      <div class="panel-title" style="color:var(--amber);display:flex;align-items:center;gap:8px;">',
      '        🎬 ТОП-КАНДИДАТИ НА АНІМАЦІЮ (Google Veo 2 / Flow • 6–10с)',
      '        <span class="chip chip-amber">' + epVeos.length + ' Сцен для Епізоду ' + esc(epData.ep) + '</span>',
      '      </div>',
      '      <div class="panel-desc">Найважливіші концепт-кадри випуску для першочергової генерації рухомих 6–10с 4K/24fps шотів у Google Veo 2 / Flow. Клікайте кнопку на картці для оновлення статусу виконання — прогрес автоматично синхронізується з Головним Дашбордом.</div>',
      '    </div>',
      '    <div style="display:flex;gap:6px;align-items:center;">',
      '      <span class="chip ' + (epVeoDone === epVeos.length ? 'chip-emerald' : 'chip-amber') + '">' + epVeoDone + ' / ' + epVeos.length + ' виконано</span>',
      '    </div>',
      '  </div>',
      '  <div class="node-tree-grid">' + veoCardsHtml + '</div>',
      '</div>'
    ].join("\n") : "";

    var archiveRowsHtml = (epMedia.archives || []).map(function (ar, idx) {
      var pIdx = idx;
      var vUrl = ar.video_preview ? ("../" + ar.video_preview) : ("../assets/video_previews/archives/" + ar.file);
      return [
        "<tr>",
        "  <td style=\"width:225px;\">",
        "    <video class=\"inline-table-video\" controls loop preload=\"metadata\" playsinline src=\"" + esc(vUrl) + "\"></video>",
        "    <div style=\"font-size:10.5px;color:var(--amber);margin-top:4px;font-family:var(--mono);\">TC сценарію: " + esc(ar.tc) + "</div>",
        "  </td>",
        "  <td>",
        "    <div style=\"font-weight:700;color:var(--text-primary);margin-bottom:3px;\">" + esc(ar.title || ar.file) + "</div>",
        "    <span class=\"filename-mono\">" + esc(ar.file) + "</span>",
        "    <div style=\"font-size:11.5px;color:var(--text-secondary);margin-top:4px;\">" + esc(ar.note) + "</div>",
        "  </td>",
        "  <td style=\"font-size:11px;\">",
        "    <a href=\"" + esc(ar.url) + "\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--cyan);font-weight:600;\">" + esc(ar.source) + " ↗</a>",
        "    <div style=\"font-family:var(--mono);font-size:10.8px;color:var(--text-muted);margin-top:3px;\">Відрізок: " + esc(ar.section) + "</div>",
        "    <div style=\"margin-top:4px;\"><span class=\"chip chip-emerald\">✅ Синхронізовано: GitHub & GDrive</span></div>",
        "  </td>",
        "  <td>",
        "    <div class=\"btn-group\">",
        "      <button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;\" data-play-pidx=\"" + pIdx + "\">▶️ У монітор</button>",
        "      <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;\" data-popup-pidx=\"" + pIdx + "\">🔍 Вікно</button>",
        "      <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-reveal-finder=\"05_RAW_FOOTAGE/archives/" + esc(ar.file) + "\">📁 У Finder</button>",
        "      <button class=\"btn btn-emerald\" style=\"padding:3px 7px;font-size:11px;\" data-copy-arch-path=\"" + idx + "\">📋 Шлях</button>",
        "    </div>",
        "  </td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var flowRowsHtml = (epMedia.flow_queue || []).map(function (fq, idx) {
      var isVidReady = fq.status === "video_ready";
      var isImgReady = fq.status === "image_ready";
      var chkKey = "flowq_" + fq.num;
      var isDone = !!state.checked[chkKey] || isVidReady;

      var previewCol = "";
      if (isVidReady && fq.video_preview) {
        previewCol = [
          "<video class=\"inline-table-video\" controls loop preload=\"metadata\" playsinline src=\"../" + esc(fq.video_preview) + "\"></video>",
          "<div style=\"display:flex;justify-content:space-between;align-items:center;margin-top:4px;\">",
          "  <span class=\"chip chip-emerald\">✅ 4K/HD Відео (#" + esc(fq.num) + ")</span>",
          "  <span style=\"font-size:10.5px;color:var(--amber);font-family:var(--mono);\">TC " + esc(fq.tc) + "</span>",
          "</div>"
        ].join("\n");
      } else if (isImgReady && fq.keyframe_preview) {
        previewCol = [
          "<div style=\"position:relative;cursor:pointer;overflow:hidden;border-radius:7px;border:1px solid rgba(56,189,248,0.45);\" data-reveal-finder=\"" + esc(fq.raw_image_path || fq.keyframe_preview) + "\" title=\"Клікніть, щоб відкрити цей 2K файл у Finder\">",
          "  <img src=\"../" + esc(fq.keyframe_preview) + "\" alt=\"" + esc(fq.title) + "\" style=\"width:225px;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 0.2s;\">",
          "  <span style=\"position:absolute;top:4px;left:4px;background:rgba(12,14,19,0.88);color:var(--amber);padding:1px 6px;border-radius:4px;font-size:9.5px;font-weight:700;\">📁 Відкрити у Finder</span>",
          "  <span style=\"position:absolute;bottom:4px;right:4px;background:rgba(12,14,19,0.92);color:var(--cyan);padding:1px 6px;border-radius:4px;font-size:9.5px;font-family:var(--mono);font-weight:700;\">2K JPG</span>",
          "</div>",
          "<div style=\"display:flex;justify-content:space-between;align-items:center;margin-top:4px;\">",
          "  <span class=\"chip chip-cyan\">🖼️ 2K Кадр готовий</span>",
          "  <span style=\"font-size:10.5px;color:var(--amber);font-family:var(--mono);\">TC " + esc(fq.tc) + "</span>",
          "</div>"
        ].join("\n");
      } else {
        previewCol = [
          "<div style=\"width:225px;aspect-ratio:16/9;background:#0d1017;border:1px dashed var(--border);border-radius:7px;display:flex;align-items:center;justify-content:center;color:var(--text-muted);font-size:11px;\">⏳ Очікує генерації</div>",
          "<div style=\"display:flex;justify-content:space-between;align-items:center;margin-top:4px;\">",
          "  <span class=\"chip chip-purple\">#" + esc(fq.num) + "</span>",
          "  <span style=\"font-size:10.5px;color:var(--amber);font-family:var(--mono);\">TC " + esc(fq.tc) + "</span>",
          "</div>"
        ].join("\n");
      }

      var statusNote = "";
      if (isVidReady) {
        statusNote = "<div style=\"font-size:11px;color:var(--emerald);margin-top:4px;font-weight:600;\">✅ Фінальне відео згенеровано (24fps • DaVinci V1)</div><div style=\"font-size:10.5px;color:var(--text-muted);\">" + esc(fq.specs || "") + "</div>";
      } else if (isImgReady) {
        statusNote = "<div style=\"font-size:11px;color:var(--cyan);margin-top:4px;font-weight:600;\">🖼️ 2K Концепт-кадр готовий • Очікує генерації відео у Google Flow</div><div style=\"font-size:10.5px;color:var(--text-muted);\">" + esc(fq.specs || "") + "</div>";
      } else {
        statusNote = "<div style=\"font-size:11px;color:var(--amber);margin-top:4px;\">⏳ Сцена в розробці (Google Flow 4K)</div>";
      }

      var actionsHtml = [];
      if (isVidReady) {
        actionsHtml.push("<button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-play-flow-vid=\"" + esc(fq.num) + "\">▶️ Відео</button>");
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-popup-flow-vid=\"" + esc(fq.num) + "\">🔍 Вікно</button>");
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-reveal-finder=\"" + esc(fq.raw_video_path || ('05_RAW_FOOTAGE/flow_renders/' + fq.file)) + "\" data-copy-flowq-vpath=\"" + idx + "\">📁 MP4 (Finder)</button>");
      }
      if (isImgReady || fq.keyframe_preview || fq.raw_image_path) {
        var kfPath = fq.raw_image_path || ("05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/" + fq.file.replace(/\.mp4$/, ".jpg"));
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-play-flow-kf=\"" + esc(fq.num) + "\">🖼️ 2K Кадр</button>");
        actionsHtml.push("<button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-popup-flow-kf=\"" + esc(fq.num) + "\">🔍 2K Вікно</button>");
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;font-weight:700;\" data-reveal-finder=\"" + esc(kfPath) + "\" data-copy-flowq-ipath=\"" + idx + "\">📁 JPG (Finder)</button>");
      }
      actionsHtml.push("<button class=\"btn btn-purple\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-copy-flowq-p=\"" + idx + "\">📋 Промпт</button>");

      return [
        "<tr" + (isVidReady ? " style=\"background:rgba(52,211,153,0.04);\"" : (isImgReady ? " style=\"background:rgba(56,189,248,0.03);\"" : "")) + ">",
        "  <td><input type=\"checkbox\" class=\"sop-checkbox\" data-flowq-check=\"" + esc(fq.num) + "\"" + (isDone ? " checked" : "") + "></td>",
        "  <td style=\"width:225px;\">" + previewCol + "</td>",
        "  <td>",
        "    <div style=\"font-weight:700;color:var(--text-primary);margin-bottom:3px;\">" + esc(fq.title || fq.file) + "</div>",
        "    <div class=\"filename-mono\" style=\"cursor:pointer;display:inline-block;margin-bottom:3px;\" data-reveal-finder=\"" + esc(isVidReady ? (fq.raw_video_path || ('05_RAW_FOOTAGE/flow_renders/' + fq.file)) : (fq.raw_image_path || ('05_RAW_FOOTAGE/flow_renders/' + fq.file))) + "\" title=\"Клікніть, щоб відкрити цей файл у Finder\">📁 " + esc(isVidReady ? (fq.raw_video_path || ("05_RAW_FOOTAGE/flow_renders/" + fq.file)) : (fq.raw_image_path || ("05_RAW_FOOTAGE/flow_renders/" + fq.file))) + "</div>",
        statusNote,
        "  </td>",
        "  <td style=\"font-family:var(--mono);font-size:11px;color:#e2e8f0;max-width:360px;\">" + esc(fq.prompt) + "</td>",
        "  <td><div class=\"btn-group\">" + actionsHtml.join("\n") + "</div></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var sciCardsHtml = (epMedia.scientific_vfx || []).map(function (sc, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--purple);background:rgba(167,139,250,0.05);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-purple\">" + esc(sc.code) + " • " + esc(sc.role) + "</span>",
        "    <span style=\"font-size:10.5px;color:var(--amber);font-family:var(--mono);\">TC " + esc(sc.timecode) + "</span>",
        "  </div>",
        "  <video class=\"inline-table-video\" controls loop preload=\"metadata\" playsinline style=\"width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:6px;border:1px solid rgba(167,139,250,0.35);margin-bottom:8px;display:block;\" src=\"../" + esc(sc.web_preview) + "\"></video>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(sc.title) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;cursor:pointer;\" data-reveal-finder=\"" + esc(sc.raw_path) + "\" title=\"Клікніть, щоб відкрити файл у Finder\">📁 " + esc(sc.raw_path) + "</div>",
        "  <div style=\"font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(sc.desc) + "</div>",
        "  <div class=\"btn-group\">",
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;cursor:pointer;\" data-reveal-finder=\"" + esc(sc.raw_path) + "\">📁 У Finder</button>",
        "    <button class=\"btn btn-purple\" style=\"padding:3px 8px;font-size:11px;\" data-copy-text=\"" + esc(sc.raw_path) + "\">📋 Шлях MP4</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var sciSectionHtml = sciCardsHtml ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(167,139,250,0.55);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🔬 Наукова 3D-Анімація & VFX (Full HD 1080p • Проект «Цікава наука»)</div>",
      "      <div class=\"panel-desc\">Високобюджетні наукові симуляції (квантова механіка, молекулярна біологія, ДНК, атомні ґратки), що візуалізують фундаментальні відкриття героїв.</div>",
      "    </div>",
      "    <span class=\"chip chip-purple\">1080p VFX Master</span>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + sciCardsHtml + "</div>",
      "</div>"
    ].join("\n") : "";

    var audioCardsHtml = (epMedia.audio || []).map(function (au, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--emerald);background:rgba(16,185,129,0.04);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-emerald\">" + esc(au.role) + "</span>",
        "    <span style=\"font-size:11px;color:var(--amber);font-family:var(--mono);font-weight:700;\">" + esc(au.duration) + "</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(au.name) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;\">→ 03_AUDIO/suno_stems/" + esc(au.bin_dir) + "/" + esc(au.smart_bin) + "</div>",
        "  <audio controls preload=\"none\" style=\"height:32px;width:100%;margin-bottom:6px;\" src=\"../assets/audio_previews/" + esc(au.preview) + "\"></audio>",
        "  <div style=\"font-size:11px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(au.specs) + "</div>",
        "  <button class=\"btn btn-emerald\" style=\"padding:3px 8px;font-size:11px;width:100%;\" data-copy-pool-dir=\"" + esc(au.bin_dir) + "\" data-copy-pool-bin=\"" + esc(au.smart_bin) + "\">📋 Копіювати шлях WAV для DaVinci " + esc(au.davinci_track) + "</button>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var voCardsHtml = (epMedia.voiceover || []).map(function (vo, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--emerald);background:rgba(16,185,129,0.04);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-emerald\">Take #" + esc(vo.num) + " • " + esc(vo.tc) + "</span>",
        "    <span style=\"font-size:11px;color:var(--cyan);font-family:var(--mono);font-weight:700;\">⏱️ " + esc(vo.duration) + "</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(vo.title) + "</h4>",
        "  <div style=\"font-size:10.5px;color:var(--text-muted);margin-bottom:6px;\">🎙️ " + esc(vo.voice) + " • " + esc(vo.words) + " words</div>",
        "  <audio controls preload=\"none\" style=\"height:32px;width:100%;margin-bottom:6px;\" src=\"../" + esc(vo.web_preview) + "\"></audio>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;cursor:pointer;\" data-reveal-finder=\"" + esc(vo.wav_master) + "\">📁 " + esc(vo.wav_master) + "</div>",
        "  <div style=\"display:flex;gap:6px;\">",
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;flex:1;cursor:pointer;\" data-reveal-finder=\"" + esc(vo.wav_master) + "\">📁 У Finder (WAV)</button>",
        "    <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;cursor:pointer;\" data-copy-text=\"" + esc(vo.wav_master) + "\">📋 Шлях WAV</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var voSectionHtml = voCardsHtml ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(16,185,129,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎙️ Офіційні Дикторські Доріжки ElevenLabs (" + (epMedia.voiceover || []).length + " тейків • Adam Radio Announcer • 100% Готові)</div>",
      "      <div class=\"panel-desc\">Англомовний майстер-наратив для таймлайну DaVinci Resolve: Broadcast 48kHz / 24-bit LPCM WAV на доріжку A1 + швидкі MP3-прев'ю.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-cyan\" data-reveal-finder=\"03_AUDIO/voiceover/EP01_ALTMAN/\">📁 Папка голосу у Finder</button>",
      "      <span class=\"chip chip-emerald\">✅ 17/17 Готові (100%)</span>",
      "    </div>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + voCardsHtml + "</div>",
      "</div>"
    ].join("\n") : "";

    var photoCardsHtml = (epMedia.archival_photos || []).map(function (ph, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--amber);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-amber\">" + esc(ph.code) + "</span>",
        "    <span class=\"chip chip-purple\">" + esc(ph.source) + "</span>",
        "  </div>",
        "  <div style=\"position:relative;cursor:pointer;overflow:hidden;border-radius:6px;border:1px solid var(--border);margin-bottom:7px;\" data-reveal-finder=\"" + esc(ph.raw_file) + "\" title=\"Клікніть по фото, щоб відкрити його у Finder\">",
        "    <img src=\"../" + esc(ph.web_preview) + "\" alt=\"" + esc(ph.title) + "\" style=\"width:100%;aspect-ratio:16/10;object-fit:cover;display:block;transition:transform 0.2s;\">",
        "    <span style=\"position:absolute;top:6px;left:6px;background:rgba(12,14,19,0.85);color:var(--amber);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700;\">📁 Відкрити у Finder</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(ph.title) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;cursor:pointer;\" data-reveal-finder=\"" + esc(ph.raw_file) + "\" title=\"Клікніть, щоб відкрити файл у Finder\">📁 " + esc(ph.raw_file) + "</div>",
        "  <div style=\"font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(ph.desc) + "</div>",
        "  <div style=\"display:flex;gap:6px;margin-top:6px;\">",
        "    <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;flex:1;cursor:pointer;\" data-reveal-finder=\"" + esc(ph.raw_file) + "\">📁 У Finder</button>",
        "    <button class=\"btn\" style=\"padding:4px 8px;font-size:11px;cursor:pointer;\" data-copy-text=\"" + esc(ph.raw_file) + "\">📋 Шлях</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var nbHtml = epMedia.notebooklm_overview ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(167,139,250,0.55);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎙️ Google NotebookLM — Офіційний Український Audio Overview («" + esc(epMedia.notebooklm_overview.title) + "» • " + esc(epMedia.notebooklm_overview.duration) + ")</div>",
      "      <div class=\"panel-desc\">" + esc(epMedia.notebooklm_overview.desc) + "</div>",
      "    </div>",
      "    <span class=\"chip chip-purple\">NotebookLM UA Deep Dive</span>",
      "  </div>",
      "  <div style=\"padding:12px;background:rgba(167,139,250,0.06);border-radius:8px;\">",
      "    <audio controls preload=\"none\" style=\"height:36px;width:100%;\" src=\"../" + esc(epMedia.notebooklm_overview.preview) + "\"></audio>",
      "    <div style=\"display:flex;justify-content:space-between;align-items:center;margin-top:8px;font-size:11.5px;color:var(--text-secondary);flex-wrap:wrap;gap:6px;\">",
      "      <span>Файл майстра: <code>" + esc(epMedia.notebooklm_overview.master_wav) + "</code></span>",
      "      <button class=\"btn btn-purple\" style=\"padding:3px 8px;font-size:11px;\" data-copy-text=\"" + esc(epMedia.notebooklm_overview.master_wav) + "\">📋 Копіювати шлях майстра M4A</button>",
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n") : "";

    var archPhotoEraMap = {
      "01": "Ера St. Louis, John Burroughs, Loopt, YC, WWDC 2008, Stanford & OpenAI",
      "02": "Хронологічний фотоархів 1970–2026: Тайвань, Oneida, Aloha, OSU, Denny's Berryessa, NV1, RIVA 128, GeForce 256, GTX 580, DGX & Endeavor HQ",
      "03": "Хронологічний фотоархів 1976–2025: Північний Лондон, Шахи, ZX Spectrum, Кембридж, UCL, DeepMind King's Cross, AlphaGo, AlphaFold 2 & Стокгольм Нобель 2024",
      "04": "Хронологічний фотоархів 1847–2024: Джордж Буль, Еверест, Кембридж, Столярство, Единбург, CMU, Торонто, Тахо $44M, Тюрінг 2018 & Стокгольм Нобель 2024",
      "05": "Хронологічний фотоархів 1977–2026: Париж, Tektronix 475A, MOS 6502, ESIEE, Сорбонна, Мінський, Bell Labs Holmdel, NYU Курант, Meta FAIR, Гутенберг, Бейдевінд & AMI Labs",
      "06": "Хронологічний фотоархів 1986–2026: Горький, Єрусалим, UofT Кабінет №4306, GTX 580 GF110, Стенфорд, Google Brain 2014, OpenAI Pioneer SF, Багаття AGI, Тель-Авів & SSI",
      "07": "Хронологічний фотоархів 1983–2026: Сан-Франциско, Шкіра батька, Стенфорд, Принстон Сітківка 50x, Baidu, Googleplex, OpenAI, TPU v3, Клод Шеннон, Anthropic 500 Howard, Білий дім, Даунінг-стріт, Токіо 2025, BSL-4 & Онко-ДНК",
      "08": "Хронологічний фотоархів 1976–2026: Ченду, Фотокамера батька, Словник, Пральня Ormont Cleaners, Прінстон, Уолл-стріт 1999, Калтех, Кембрійські трилобіти, Gates CS SAIL, Графік ImageNet, Googleplex, AI for Good, Stanford HAI, Лікарня & 3D LiDAR World Labs",
      "09": "Хронологічний фотоархів 1964–2026: Париж 1978, Théâtre de Paris, Азімов, Макгілл 1991, Bell Labs, Університет Монреаля, Зима ШІ, Вектори слів, Cross-Attention, Бульвар Сен-Лоран (Mila), GFlowNets, Капітолій 2023, Блетчлі-Парк, Рада Безпеки ООН, Зимовий велосипед & Сяйво над Канадою",
      "10": "Хронологічний фотоархів 1976–2026: Гонконг, Raffles Сінгапур, Apple II (BASIC), Carnegie Mellon, MIT, Берклі, Стенфорд CS229, Автономний вертоліт RL, Googleplex, «Нейрон кота» 2012, Coursera HQ, Baidu Шанді, Сцена WSJ, Нитка нової електрики, Заводи Landing AI, Лампа Едісона & Світанок Землі з МКС"
    };
    var archPhotoEraNote = archPhotoEraMap[epData.ep] || "Автентичні знімки спікера та історичні артефакти епохи";
    var photoSectionHtml = photoCardsHtml ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(251,191,36,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">📸 Автентичні Історичні Фото Спікера (" + (epMedia.archival_photos || []).length + " фото • " + archPhotoEraNote + ")</div>",
      "      <div class=\"panel-desc\">Реальні історичні знімки та апаратні артефакти з відкритого архіву Wikimedia Commons та університетських/прес-архівів.</div>",
      "    </div>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + photoCardsHtml + "</div>",
      "</div>"
    ].join("\n") : "";

    var audioSectionHtml = audioCardsHtml ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(52,211,153,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🎧 Аудіо-Пул DaVinci Resolve — EP" + esc(epData.ep) + " (" + (epMedia.audio || []).length + " Майстер-Доріжки WAV • 48 kHz / 24-bit)</div>",
      "      <div class=\"panel-desc\">Повний музичний та ембієнт-каркас випуску. Кожен трек зведено на 92 BPM (такт 2.61 с) для монтажу у DaVinci Resolve на доріжки A2 (Music) та A3 (Ambience).</div>",
      "    </div>",
      "    <span class=\"chip chip-emerald\">✅ 4/4 Актів Готові</span>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + audioCardsHtml + "</div>",
      "</div>"
    ].join("\n") : "";
    var galleryCardsHtml = (epMedia.flow_gallery || []).map(function (g, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--cyan);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip " + esc(g.chip) + "\">" + esc(g.badge) + "</span>",
        "    <span style=\"font-family:var(--mono);font-size:10.5px;color:var(--amber);\">TC " + esc(g.tc) + "</span>",
        "  </div>",
        "  <div style=\"position:relative;cursor:pointer;overflow:hidden;border-radius:6px;border:1px solid var(--border);margin-bottom:7px;\" data-reveal-finder=\"" + esc(g.raw_path) + "\" title=\"Клікніть по кадру, щоб відкрити його у Finder\">",
        "    <img src=\"../" + esc(g.web_preview) + "\" alt=\"" + esc(g.title) + "\" loading=\"lazy\" style=\"width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 0.2s;\">",
        "    <span style=\"position:absolute;top:6px;left:6px;background:rgba(12,14,19,0.85);color:var(--amber);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700;\">📁 Відкрити у Finder</span>",
        "    <span style=\"position:absolute;bottom:6px;right:6px;background:rgba(12,14,19,0.92);color:var(--cyan);padding:1px 6px;border-radius:4px;font-size:9.5px;font-family:var(--mono);font-weight:700;\">" + esc(g.dims) + "</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(g.code) + " • " + esc(g.title) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;cursor:pointer;\" data-reveal-finder=\"" + esc(g.raw_path) + "\" title=\"Клікніть, щоб відкрити файл у Finder\">📁 " + esc(g.raw_path) + "</div>",
        "  <div class=\"btn-group\">",
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-play-gallery-idx=\"" + idx + "\">▶️ У монітор</button>",
        "    <button class=\"btn btn-amber\" style=\"padding:3px 8px;font-size:11px;\" data-popup-gallery-idx=\"" + idx + "\">🔍 У вікні</button>",
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;cursor:pointer;\" data-reveal-finder=\"" + esc(g.raw_path) + "\">📁 У Finder</button>",
        "    <button class=\"btn btn-emerald\" style=\"padding:3px 8px;font-size:11px;\" data-copy-gallery-path=\"" + idx + "\">📋 Шлях</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var filteredReelHtml = playlist.map(function (item, idx) {
      if (state.mediaDockFilter !== "all" && item.kind !== state.mediaDockFilter) return "";
      var activeCls = idx === state.mediaActiveIndex ? " active" : "";
      var thumbHtml = item.type === "image"
        ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.poster || item.src) + "\" loading=\"lazy\" style=\"object-fit:cover;\">"
        : (item.type === "audio"
          ? "<div class=\"reel-thumb-video\" style=\"background:rgba(16,185,129,0.12);display:flex;align-items:center;justify-content:center;font-size:22px;\">🎙️</div>"
          : (item.kind === "vault_video" && item.poster
            ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.poster) + "\" loading=\"lazy\" style=\"object-fit:cover;\">"
            : "<video class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" muted loop playsinline preload=\"metadata\"></video>"));

      return [
        "<div class=\"reel-item-card" + activeCls + "\" data-pidx=\"" + idx + "\">",
        "  <div class=\"reel-thumb-wrap\">",
        thumbHtml,
        "    <span class=\"reel-tc-tag\">" + esc(item.tc) + "</span>",
        "  </div>",
        "  <div style=\"min-width:0;\">",
        "    <div style=\"display:flex;justify-content:space-between;align-items:center;gap:4px;\">",
        "      <span class=\"chip " + item.chipClass + "\" style=\"font-size:9.8px;padding:1px 6px;\">" + esc(item.kindLabel) + "</span>",
        "      <button class=\"btn\" style=\"padding:1px 6px;font-size:10px;\" data-popup-pidx=\"" + idx + "\" title=\"Відкрити у великому спливаючому вікні\">🔍</button>",
        "    </div>",
        "    <div class=\"reel-item-title\">" + esc(item.title) + "</div>",
        "    <div class=\"reel-item-file\">" + esc(item.file) + "</div>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).filter(Boolean).join("\n");

    var countKind = function (k) {
      return playlist.filter(function (it) { return it.kind === k; }).length;
    };
    var nVoCount = countKind("voiceover");
    var nFlowVid = countKind("flow_video");
    var nFlowImg = countKind("flow_image");
    var nArchCount = countKind("archive");
    var nDosCount = countKind("dossier");
    var nSciCount = countKind("science");
    var nPhotoCount = countKind("archival_photo");
    var nBrollCount = countKind("broll");
    var nVaultVid = countKind("vault_video");
    var nVaultImg = countKind("vault_image");

    var filterPillsHtml = [
      '<button class="dock-pill' + (state.mediaDockFilter === "all" ? " active" : "") + '" data-dock-filter="all">Усі (' + playlist.length + ')</button>'
    ];
    if (nVoCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "voiceover" ? " active" : "") + '" data-dock-filter="voiceover">🎙️ Голос (' + nVoCount + ')</button>');
    if (nFlowVid > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "flow_video" ? " active" : "") + '" data-dock-filter="flow_video">🚀 Flow Відео (' + nFlowVid + ')</button>');
    if (nVaultVid > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "vault_video" ? " active" : "") + '" data-dock-filter="vault_video">🎥 Ваулт Відео (' + nVaultVid + ')</button>');
    if (nVaultImg > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "vault_image" ? " active" : "") + '" data-dock-filter="vault_image">🖼️ Ваулт Фото (' + nVaultImg + ')</button>');
    if (nFlowImg > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "flow_image" ? " active" : "") + '" data-dock-filter="flow_image">🖼️ 2K Кадри (' + nFlowImg + ')</button>');
    if (nArchCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "archive" ? " active" : "") + '" data-dock-filter="archive">📼 Архіви (' + nArchCount + ')</button>');
    if (nDosCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "dossier" ? " active" : "") + '" data-dock-filter="dossier">🗂️ Досьє (' + nDosCount + ')</button>');
    if (nSciCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "science" ? " active" : "") + '" data-dock-filter="science">🔬 VFX (' + nSciCount + ')</button>');
    if (nPhotoCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "archival_photo" ? " active" : "") + '" data-dock-filter="archival_photo">📸 Фото (' + nPhotoCount + ')</button>');
    if (nBrollCount > 0) filterPillsHtml.push('<button class="dock-pill' + (state.mediaDockFilter === "broll" ? " active" : "") + '" data-dock-filter="broll">🎞️ B-Roll (' + nBrollCount + ')</button>');

    var vaultEp = getVaultEp();
    var vSum = vaultEp.summary || {};
    var triadsEp = getTriadsEp();
    var readyTriadVids = triadsEp.filter(function (t) { return t.status === "video_ready"; }).length;
    var readyTriadImgs = triadsEp.filter(function (t) { return t.status === "image_ready"; }).length;
    var voTotalDisplay = Math.max(nVoCount, vSum.vo_count || 0);
    var sunoTotalDisplay = Math.max((epMedia.audio || []).length, vSum.suno_count || 0);
    var primaryDirDisplay = vaultEp.primary_footage_dir || "05_RAW_FOOTAGE/";
    var voDirDisplay = vaultEp.vo_dir || "03_AUDIO/voiceover/";

    var natVidCnt = (vSum.native_videos_count !== undefined) ? vSum.native_videos_count : (vSum.videos_count || 0);
    var crossVidCnt = vSum.cross_videos_count || 0;
    var natImgCnt = (vSum.native_images_count !== undefined) ? vSum.native_images_count : (vSum.images_count || 0);
    var crossImgCnt = vSum.cross_images_count || 0;

    var executiveHeroHtml = [
      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.4);background:linear-gradient(180deg, rgba(17,23,38,0.85), rgba(11,15,23,0.9));margin-bottom:0.85rem;\">",
      "  <div class=\"panel-head\" style=\"border-bottom:none;padding-bottom:0;\">",
      "    <div>",
      "      <div class=\"panel-title\" style=\"font-size:16px;color:var(--text-primary);display:flex;align-items:center;gap:8px;flex-wrap:wrap;\">",
      "        <span>🗂️ Медіа-Пул Епізоду " + esc(epData.ep) + " • " + esc(epData.name) + "</span>",
      "        <span class=\"chip chip-cyan\">🎥 " + (vSum.videos_count || 0) + " Відео (" + natVidCnt + " власних" + (crossVidCnt ? (" + " + crossVidCnt + " з фонду") : "") + ")</span>",
      "        <span class=\"chip chip-amber\">🖼️ " + (vSum.images_count || 0) + " Фото (" + natImgCnt + " власних" + (crossImgCnt ? (" + " + crossImgCnt + " з фонду") : "") + ")</span>",
      "        <span class=\"chip chip-purple\">🚀 " + triadsEp.length + " Тріад Flow (3-Промпт)</span>",
      "        <span class=\"chip chip-emerald\">🎙️ " + voTotalDisplay + " Голос • 🎵 " + sunoTotalDisplay + " Suno</span>",
      "      </div>",
      "      <div class=\"panel-desc\" style=\"margin-top:4px;\">Окрема чиста навігація: переглядайте всі відео окремо від зображень, копіюйте уніфіковані 3-промптні Тріади (Start A ➔ Flow Morph ➔ End B) та відкривайте файли у Finder.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-amber\" id=\"btnOpenFullCinemaHero\">🔍 Кінозал (" + playlist.length + ")</button>",
      "      <button class=\"btn btn-cyan\" data-reveal-finder=\"" + esc(primaryDirDisplay) + "\">📁 Папка Футажів</button>",
      "      <button class=\"btn btn-cyan\" data-reveal-finder=\"" + esc(voDirDisplay) + "\">🎙️ Папка Голосу</button>",
      "      <button class=\"btn btn-emerald\" id=\"btnDownloadEpSrt\">📥 Титри (.srt)</button>",
      "    </div>",
      "  </div>",
      "</div>"
    ].join("\n");

    var flowSectionHtml = [
      "<div class=\"panel-card\" style=\"border-color:rgba(167,139,250,0.55);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🚀 Пріоритетна Черга Google Flow / Veo (10 базових сцен) — " + nFlowVid + " Відео Готові • " + (epMedia.flow_queue || []).length + " Сцен</div>",
      "      <div class=\"panel-desc\">Сцени відтворюються через вбудовані плеєри. Клікніть на <strong>«▶️ Відео»</strong> або <strong>«🖼️ 2K Кадр»</strong> для завантаження у правий монітор, або <strong>«📁 MP4 / JPG (Finder)»</strong> для переходу у Finder.</div>",
      "    </div>",
      "    <button class=\"btn btn-cyan\" data-reveal-finder=\"05_RAW_FOOTAGE/flow_renders/\">📁 flow_renders/ у Finder</button>",
      "  </div>",
      "  <div class=\"studio-table-wrap\">",
      "    <table class=\"studio-table\">",
      "      <thead><tr><th>✓</th><th>Медіа-прев'ю (Відео / 2K Кадр)</th><th>Цільовий файл у flow_renders/</th><th>Промпт для Google Flow / Veo 4K</th><th>Дії</th></tr></thead>",
      "      <tbody>" + flowRowsHtml + "</tbody>",
      "    </table>",
      "  </div>",
      "</div>"
    ].join("\n");

    var gallerySectionHtml = (epMedia.flow_gallery || []).length ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🖼️ Галерея 2K Концепт-Кадрів та Кінокадрів B-Roll (" + (epMedia.flow_gallery || []).length + " Кадрів • 05_RAW_FOOTAGE/flow_images/)</div>",
      "      <div class=\"panel-desc\">Усі зображення зберігаються окремо у <code>05_RAW_FOOTAGE/flow_images/</code>. Клікніть на будь-який кадр або кнопку для відкриття у Finder, моніторі або спливаючому вікні.</div>",
      "    </div>",
      "    <button class=\"btn btn-cyan\" data-reveal-finder=\"" + esc(primaryDirDisplay) + "\">📁 Папка кадрів у Finder</button>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + galleryCardsHtml + "</div>",
      "</div>"
    ].join("\n") : "";

    var archiveSectionHtml = [
      "<div class=\"panel-card\" style=\"border-color:rgba(52,211,153,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">📼 Реальні Історичні Відеоархіви B-Roll (05_RAW_FOOTAGE/archives/)</div>",
      "      <div class=\"panel-desc\">Натисніть Play прямо у рядку або кнопку <strong>«▶️ У монітор»</strong> / <strong>«🔍 Вікно»</strong> для перегляду зі звуком.</div>",
      "    </div>",
      "    <div class=\"btn-group\">",
      "      <button class=\"btn btn-cyan\" data-reveal-finder=\"05_RAW_FOOTAGE/archives/\">📁 archives/ у Finder</button>",
      "      <button class=\"btn btn-purple\" id=\"btnCopyFetchEpCmd\">💻 fetch_archives.sh</button>",
      "    </div>",
      "  </div>",
      "  <div class=\"studio-table-wrap\">",
      "    <table class=\"studio-table\">",
      "      <thead><tr><th>Живий прев'ю-плеєр</th><th>Назва та файл Smart Bin</th><th>Першоджерело & Синхронізація</th><th>Дії</th></tr></thead>",
      "      <tbody>" + archiveRowsHtml + "</tbody>",
      "    </table>",
      "  </div>",
      "</div>"
    ].join("\n");

    var dossierSectionHtml = [
      "<div class=\"panel-card\" style=\"border-color:rgba(251,191,36,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">🗂️ Згенеровані 4K Документальні Артефакти («Досьє» • 3840×2160 PNG + 24fps Zoom MP4)</div>",
      "      <div class=\"panel-desc\">Клікніть по зображенню досьє, щоб переглянути його анімований кінематографічний наїзд камери (1.00→1.06) у правому моніторі або відкрити файл у Finder.</div>",
      "    </div>",
      "    <button class=\"btn btn-cyan\" data-reveal-finder=\"05_RAW_FOOTAGE/dossiers_press/\">📁 dossiers_press/ у Finder</button>",
      "  </div>",
      "  <div class=\"node-tree-grid\">" + dossiersHtml + portraitCardHtml + "</div>",
      "</div>"
    ].join("\n");

    var curSub = state.mediaSubTab || "videos";
    var hasVeo = !!(veoMasterSectionHtml && veoMasterSectionHtml.trim());
    var audioArchCount = (epMedia.voiceover || []).length + (epMedia.audio || []).length + (epMedia.archives || []).length + (epMedia.dossiers || []).length + (epMedia.scientific_vfx || []).length + (epMedia.archival_photos || []).length + (epMedia.notebooklm_overview ? 1 : 0);

    var mediaSubTabsHtml = [
      "<nav class=\"media-subtabs-bar\" aria-label=\"Розділи медіапулу\">",
      "  <button class=\"media-subtab-btn" + (curSub === "videos" ? " active" : "") + "\" data-media-subtab=\"videos\">🎥 Відеофайли <span class=\"media-subtab-count\">" + (vaultEp.videos || []).length + "</span></button>",
      "  <button class=\"media-subtab-btn" + (curSub === "triads" ? " active" : "") + "\" data-media-subtab=\"triads\">🎯 Документальні Сюжети (Тріади 3×) <span class=\"media-subtab-count\">" + triadsEp.length + "</span></button>",
      "  <button class=\"media-subtab-btn" + (curSub === "images" ? " active" : "") + "\" data-media-subtab=\"images\">🖼️ Зображення <span class=\"media-subtab-count\">" + (vaultEp.images || []).length + "</span></button>",
      (hasVeo ? ("  <button class=\"media-subtab-btn" + (curSub === "veo" ? " active" : "") + "\" data-media-subtab=\"veo\">🎞️ Veo Конвеєр</button>") : ""),
      "  <button class=\"media-subtab-btn" + (curSub === "archives" ? " active" : "") + "\" data-media-subtab=\"archives\">🎙️ Озвучка, Досьє & Архіви <span class=\"media-subtab-count\">" + audioArchCount + "</span></button>",
      "</nav>"
    ].filter(Boolean).join("\n");

    var activeSubPaneHtml = "";
    if (curSub === "videos") {
      activeSubPaneHtml = buildVaultVideosHtml(vaultEp, playlist);
    } else if (curSub === "images") {
      activeSubPaneHtml = buildVaultImagesHtml(vaultEp, playlist);
    } else if (curSub === "triads") {
      activeSubPaneHtml = buildTriadsQueueHtml(triadsEp, playlist);
    } else if (curSub === "veo") {
      activeSubPaneHtml = veoMasterSectionHtml || "<div class=\"panel-card\"><div class=\"panel-title\">🎞️ Veo Конвеєр</div><div class=\"panel-desc\">Використовуйте вкладку «🚀 Тріади Flow» для цього епізоду.</div></div>";
    } else {
      var jumpLinks = [
        archiveSectionHtml ? "<button class=\"filter-pill active\" data-scroll-arch=\"archSecVideos\">📼 Архівні відео (" + (epMedia.archives || []).length + ")</button>" : "",
        photoSectionHtml ? "<button class=\"filter-pill\" data-scroll-arch=\"archSecPhotos\">📸 Архівні фото (" + (epMedia.archival_photos || []).length + ")</button>" : "",
        dossierSectionHtml ? "<button class=\"filter-pill\" data-scroll-arch=\"archSecDossiers\">🗂️ 4K Досьє (" + (epMedia.dossiers || []).length + ")</button>" : "",
        sciSectionHtml ? "<button class=\"filter-pill\" data-scroll-arch=\"archSecSci\">🔬 Науковий VFX (" + (epMedia.scientific_vfx || []).length + ")</button>" : "",
        (audioSectionHtml || voSectionHtml) ? "<button class=\"filter-pill\" data-scroll-arch=\"archSecAudio\">🎧 Аудіо WAV (" + ((epMedia.audio || []).length + (epMedia.voiceover || []).length) + ")</button>" : ""
      ].filter(Boolean).join("");
      var jumpBar = jumpLinks ? ("<div class=\"panel-card\" style=\"padding:0.65rem 0.9rem;margin-bottom:0.85rem;border-color:rgba(56,189,248,0.35);\"><div class=\"filter-pills\">" + jumpLinks + "</div></div>") : "";
      activeSubPaneHtml = [
        jumpBar,
        archiveSectionHtml ? ("<div id=\"archSecVideos\">" + archiveSectionHtml + "</div>") : "",
        photoSectionHtml ? ("<div id=\"archSecPhotos\">" + photoSectionHtml + "</div>") : "",
        dossierSectionHtml ? ("<div id=\"archSecDossiers\">" + dossierSectionHtml + "</div>") : "",
        sciSectionHtml ? ("<div id=\"archSecSci\">" + sciSectionHtml + "</div>") : "",
        (voSectionHtml || audioSectionHtml || nbHtml) ? ("<div id=\"archSecAudio\">" + [voSectionHtml, audioSectionHtml, nbHtml].filter(Boolean).join("\n") + "</div>") : ""
      ].filter(Boolean).join("\n") || "<div class=\"panel-card\"><div class=\"panel-title\">🎙️ Озвучка та архіви ще не завантажені</div></div>";
    }

    pane.innerHTML = [
      "<div class=\"media-split-layout\">",
      "  <div class=\"media-main-col\">",
      executiveHeroHtml,
      mediaSubTabsHtml,
      "    <div id=\"mediaSubPaneBody\">" + activeSubPaneHtml + "</div>",
      "  </div>",

      "  <aside class=\"media-dock-right\" aria-label=\"Правий блок прокрутки та анімації медіа\">",
      "    <div class=\"dock-head\">",
      "      <div class=\"dock-title\">🎬 Відео-Монітор & Стрічка</div>",
      "      <button class=\"btn btn-amber\" style=\"padding:3px 9px;font-size:11px;\" id=\"btnDockExpandPopup\">🔍 У спливаючому вікні ↗</button>",
      "    </div>",
      "    <div class=\"dock-monitor-box\">",
      "      <video id=\"dockMainVideo\" class=\"dock-monitor-video\" src=\"" + esc(activeClip.src) + "\" data-src=\"" + esc(activeClip.src) + "\" controls autoplay muted loop playsinline" + (activeClip.type === "image" ? " style=\"display:none;\"" : "") + "></video>",
      "      <img id=\"dockMainImage\" class=\"dock-monitor-video\" src=\"" + (activeClip.type === "image" ? esc(activeClip.src) : "") + "\" style=\"" + (activeClip.type === "image" ? "display:block;" : "display:none;") + "object-fit:contain;background:#05070b;\">",
      "      <div class=\"dock-monitor-meta\">",
      "        <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;\">",
      "          <span class=\"chip " + activeClip.chipClass + "\" id=\"dockMetaBadge\">" + esc(activeClip.kindLabel) + "</span>",
      "          <span class=\"tc-badge\" id=\"dockMetaTc\">TC " + esc(activeClip.tc) + "</span>",
      "          <span style=\"font-family:var(--mono);font-size:10.5px;color:var(--text-muted);\" id=\"dockCounterLabel\">" + (state.mediaActiveIndex + 1) + " / " + playlist.length + "</span>",
      "        </div>",
      "        <div class=\"dock-monitor-title\" id=\"dockMetaTitle\">" + esc(activeClip.title) + "</div>",
      "        <div class=\"dock-monitor-sub\" id=\"dockMetaSub\">" + esc(activeClip.track + " — " + activeClip.desc) + "</div>",
      "        <div class=\"dock-nav-row\">",
      "          <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" id=\"btnDockPrev\">◀ Попереднє</button>",
      "          <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;" + (activeClip.type === "image" ? "display:none;" : "") + "\" id=\"btnDockToggleSound\">🔊 Увімкнути звук</button>",
      "          <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;cursor:pointer;\" id=\"btnDockRevealInFinder\">📁 Відкрити у Finder</button>",
      "          <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" id=\"btnDockNext\">Наступне ▶</button>",
      "        </div>",
      "      </div>",
      "    </div>",

      "    <div class=\"dock-filter-row\">",
      filterPillsHtml.join("\n"),
      "    </div>",

      "    <label class=\"dock-anim-toggle\" style=\"cursor:pointer;\">",
      "      <span>✨ Жива анімація карток при прокрутці стрічки</span>",
      "      <input type=\"checkbox\" class=\"sop-checkbox\" id=\"chkReelAutoAnim\"" + (state.reelAutoAnimate ? " checked" : "") + ">",
      "    </label>",

      "    <div class=\"media-reel-scroll\" id=\"dockReelScroll\">",
      filteredReelHtml,
      "    </div>",
      "  </aside>",
      "</div>"
    ].join("\n");

    // Start playing main dock video smoothly if video
    var mainVid = document.getElementById("dockMainVideo");
    if (mainVid && activeClip.type === "video" && typeof mainVid.play === "function") {
      var playPromise = mainVid.play();
      if (playPromise && playPromise.catch) playPromise.catch(function () {});
    }

    var soundBtn = document.getElementById("btnDockToggleSound");
    if (soundBtn && mainVid) {
      soundBtn.addEventListener("click", function () {
        mainVid.muted = !mainVid.muted;
        soundBtn.textContent = mainVid.muted ? "🔊 Увімкнути звук" : "🔇 Вимкнути звук";
      });
    }

    var prevBtn = document.getElementById("btnDockPrev");
    if (prevBtn) prevBtn.addEventListener("click", function () { selectDockClip(state.mediaActiveIndex - 1, true); });
    var nextBtn = document.getElementById("btnDockNext");
    if (nextBtn) nextBtn.addEventListener("click", function () { selectDockClip(state.mediaActiveIndex + 1, true); });

    var expandBtn = document.getElementById("btnDockExpandPopup");
    if (expandBtn) expandBtn.addEventListener("click", function () { openCinemaModal(state.mediaActiveIndex); });
    var heroCinemaBtn = document.getElementById("btnOpenFullCinemaHero");
    if (heroCinemaBtn) heroCinemaBtn.addEventListener("click", function () { openCinemaModal(state.mediaActiveIndex); });

    var dockRevealBtn = document.getElementById("btnDockRevealInFinder");
    if (dockRevealBtn) {
      dockRevealBtn.addEventListener("click", function () {
        var clip = playlist[state.mediaActiveIndex];
        if (clip) {
          revealInFinder(clip.localPath || clip.file, clip.title);
        }
      });
    }

    var mainImg = document.getElementById("dockMainImage");
    if (mainImg) {
      if (mainImg.style) mainImg.style.cursor = "pointer";
      mainImg.title = "Клікніть, щоб відкрити цей файл у Finder";
      mainImg.addEventListener("click", function () {
        var clip = playlist[state.mediaActiveIndex];
        if (clip) {
          revealInFinder(clip.localPath || clip.file, clip.title);
        }
      });
    }

    var animChk = document.getElementById("chkReelAutoAnim");
    if (animChk) {
      animChk.addEventListener("change", function () {
        state.reelAutoAnimate = !!animChk.checked;
        setupReelAnimationObserver();
      });
    }

    pane.querySelectorAll("[data-dock-filter]").forEach(function (pill) {
      pill.addEventListener("click", function () {
        state.mediaDockFilter = pill.getAttribute("data-dock-filter");
        renderMedia();
      });
    });

    pane.querySelectorAll("#dockReelScroll .reel-item-card").forEach(function (card) {
      card.addEventListener("click", function (ev) {
        if (ev.target.closest("[data-popup-pidx]")) return;
        var idx = parseInt(card.getAttribute("data-pidx"), 10);
        selectDockClip(idx, false);
      });
    });

    pane.querySelectorAll("[data-play-pidx]").forEach(function (el) {
      el.addEventListener("click", function () {
        var idx = parseInt(el.getAttribute("data-play-pidx"), 10);
        selectDockClip(idx, true);
        showToast("▶️ Відтворення у правому Відео-Моніторі");
      });
    });

    pane.querySelectorAll("[data-popup-pidx]").forEach(function (el) {
      el.addEventListener("click", function (ev) {
        ev.stopPropagation();
        var idx = parseInt(el.getAttribute("data-popup-pidx"), 10);
        openCinemaModal(idx);
      });
    });

    var srtBtn = document.getElementById("btnDownloadEpSrt");
    if (srtBtn) {
      srtBtn.addEventListener("click", function () {
        downloadBlob("EP" + epData.ep + "_" + epData.page_slug + "_Documentary_Titles_TrackV3.srt", generateEpisodeTitlesSRT(), "text/plain;charset=utf-8");
      });
    }

    var fetchCmdBtn = document.getElementById("btnCopyFetchEpCmd");
    if (fetchCmdBtn) {
      fetchCmdBtn.addEventListener("click", function () {
        copyText("cd " + repoRoot + " && ./08_AUTOMATION/scripts/fetch_archives.sh --ep EP" + epData.ep, "команда fetch_archives.sh");
      });
    }

    var portBtn = document.getElementById("btnCopyPortraitPath");
    if (portBtn && portrait.raw_file) {
      portBtn.addEventListener("click", function () {
        copyText(repoRoot + "05_RAW_FOOTAGE/speaker_portraits/" + portrait.raw_file, portrait.raw_file);
      });
    }

    pane.querySelectorAll("[data-copy-dos-path]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-dos-path"), 10);
        var d = epMedia.dossiers[i];
        if (d) copyText(repoRoot + d.raw_4k_png, d.id);
      });
    });

    pane.querySelectorAll("[data-copy-text]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var txt = btn.getAttribute("data-copy-text");
        if (txt) copyText(txt, "шлях файлу");
      });
    });

    var pAudios = pane.querySelectorAll("audio");
    for (var pai = 0; pai < pAudios.length; pai++) {
      pAudios[pai].addEventListener("play", function (ev) {
        for (var paj = 0; paj < pAudios.length; paj++) {
          if (pAudios[paj] !== ev.target) pAudios[paj].pause();
        }
      });
    }

    pane.querySelectorAll("[data-copy-arch-path]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-arch-path"), 10);
        var ar = epMedia.archives[i];
        if (ar) copyText(repoRoot + "05_RAW_FOOTAGE/archives/" + ar.file, ar.file);
      });
    });

    pane.querySelectorAll("[data-flowq-check]").forEach(function (chk) {
      chk.addEventListener("change", function () {
        var k = "flowq_" + chk.getAttribute("data-flowq-check");
        if (chk.checked) state.checked[k] = true;
        else delete state.checked[k];
        saveProgress();
      });
    });

    pane.querySelectorAll("[data-copy-flowq-p]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-flowq-p"), 10);
        var fq = epMedia.flow_queue[i];
        if (fq) copyText(fq.prompt, "Flow #" + fq.num);
      });
    });

    pane.querySelectorAll("[data-play-flow-kf]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = btn.getAttribute("data-play-flow-kf");
        var pIdx = -1;
        for (var i = 0; i < playlist.length; i++) {
          if (playlist[i].uid === "flow_img_" + num) { pIdx = i; break; }
        }
        if (pIdx !== -1) {
          selectDockClip(pIdx, true);
          showToast("🖼️ 2K кадр #" + num + " завантажено в правий монітор");
        } else {
          var fq = (epMedia.flow_queue || []).find(function (f) { return f.num === num; });
          if (fq) revealInFinder(fq.raw_image_path, "2K кадр #" + num);
        }
      });
    });

    pane.querySelectorAll("[data-popup-flow-kf]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = btn.getAttribute("data-popup-flow-kf");
        var pIdx = -1;
        for (var i = 0; i < playlist.length; i++) {
          if (playlist[i].uid === "flow_img_" + num) { pIdx = i; break; }
        }
        if (pIdx !== -1) {
          openCinemaModal(pIdx);
        } else {
          var fq = (epMedia.flow_queue || []).find(function (f) { return f.num === num; });
          if (fq) revealInFinder(fq.raw_image_path, "2K кадр #" + num);
        }
      });
    });

    pane.querySelectorAll("[data-copy-flowq-ipath]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-flowq-ipath"), 10);
        var fq = epMedia.flow_queue[i];
        if (fq) {
          var targetPath = fq.raw_image_path || ("05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/" + fq.file.replace(/\.mp4$/, ".jpg"));
          revealInFinder(targetPath, "2K JPG #" + fq.num);
        }
      });
    });

    pane.querySelectorAll("[data-play-flow-vid]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = btn.getAttribute("data-play-flow-vid");
        var pIdx = -1;
        for (var i = 0; i < playlist.length; i++) {
          if (playlist[i].uid === "flow_vid_" + num) { pIdx = i; break; }
        }
        if (pIdx !== -1) {
          selectDockClip(pIdx, true);
          showToast("🚀 Відео #" + num + " завантажено в правий монітор");
        }
      });
    });

    pane.querySelectorAll("[data-popup-flow-vid]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var num = btn.getAttribute("data-popup-flow-vid");
        var pIdx = -1;
        for (var i = 0; i < playlist.length; i++) {
          if (playlist[i].uid === "flow_vid_" + num) { pIdx = i; break; }
        }
        if (pIdx !== -1) {
          openCinemaModal(pIdx);
        }
      });
    });

    pane.querySelectorAll("[data-copy-flowq-vpath]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-copy-flowq-vpath"), 10);
        var fq = epMedia.flow_queue[i];
        if (fq) {
          var targetPath = fq.raw_video_path || ("05_RAW_FOOTAGE/flow_renders/" + fq.file);
          revealInFinder(targetPath, "Відео MP4 #" + fq.num);
        }
      });
    });

    pane.querySelectorAll("[data-toggle-ep-veo]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-toggle-ep-veo");
        var current = !!vStatusMap[id];
        setVeoStatus(id, !current);
        showToast((!current ? "✅ Виконано: " : "⏳ Повернуто в чергу: ") + id);
      });
    });

    pane.querySelectorAll("[data-copy-veo-prompt]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-copy-veo-prompt");
        var target = (window.VEO_ANIMATION_PIPELINE || []).find(function (p) { return p.id === id; });
        if (target) copyText(target.prompt, "Veo 2 Промпт " + id);
      });
    });

    pane.querySelectorAll("[data-play-gallery-idx]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = parseInt(btn.getAttribute("data-play-gallery-idx"), 10);
        var g = (epMedia.flow_gallery || [])[idx];
        if (!g) return;
        var pIdx = -1;
        var gFileName = g.raw_path ? g.raw_path.split("/").pop() : "";
        for (var i = 0; i < playlist.length; i++) {
          if ((gFileName && playlist[i].file === gFileName) || playlist[i].title === g.title) {
            pIdx = i; break;
          }
        }
        if (pIdx !== -1) {
          selectDockClip(pIdx, true);
          showToast("🖼️ Кадр «" + g.code + "» завантажено в правий монітор");
        } else {
          revealInFinder(g.raw_path, g.title);
        }
      });
    });

    pane.querySelectorAll("[data-popup-gallery-idx]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = parseInt(btn.getAttribute("data-popup-gallery-idx"), 10);
        var g = (epMedia.flow_gallery || [])[idx];
        if (!g) return;
        var pIdx = -1;
        var gFileName = g.raw_path ? g.raw_path.split("/").pop() : "";
        for (var i = 0; i < playlist.length; i++) {
          if ((gFileName && playlist[i].file === gFileName) || playlist[i].title === g.title) {
            pIdx = i; break;
          }
        }
        if (pIdx !== -1) {
          openCinemaModal(pIdx);
        } else {
          revealInFinder(g.raw_path, g.title);
        }
      });
    });

    pane.querySelectorAll("[data-copy-gallery-path]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = parseInt(btn.getAttribute("data-copy-gallery-path"), 10);
        var g = (epMedia.flow_gallery || [])[idx];
        if (g) {
          revealInFinder(g.raw_path, g.code);
        }
      });
    });

    pane.querySelectorAll("[data-play-pidx]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var pIdx = parseInt(btn.getAttribute("data-play-pidx"), 10);
        selectDockClip(pIdx, true);
      });
    });

    pane.querySelectorAll("[data-popup-pidx]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var pIdx = parseInt(btn.getAttribute("data-popup-pidx"), 10);
        openCinemaModal(pIdx);
      });
    });

    function refreshSubPaneOnly(subType, focusId) {
      var bodyEl = document.getElementById("mediaSubPaneBody");
      if (!bodyEl) return;
      var vEp = getVaultEp();
      var trEp = getTriadsEp();
      if (subType === "videos") bodyEl.innerHTML = buildVaultVideosHtml(vEp, playlist);
      else if (subType === "images") bodyEl.innerHTML = buildVaultImagesHtml(vEp, playlist);
      else if (subType === "triads") bodyEl.innerHTML = buildTriadsQueueHtml(trEp, playlist);
      bindMediaDynamicControls(bodyEl);
      if (focusId) {
        var inp = document.getElementById(focusId);
        if (inp) {
          inp.focus();
          try { var L = inp.value.length; inp.setSelectionRange(L, L); } catch (e) {}
        }
      }
    }

    function bindMediaDynamicControls(scopeEl) {
      scopeEl.querySelectorAll("[data-vvid-origin]").forEach(function (pill) {
        pill.addEventListener("click", function () {
          state.vaultVidOrigin = pill.getAttribute("data-vvid-origin");
          refreshSubPaneOnly("videos", null);
        });
      });
      var btnToggleVidUnique = scopeEl.querySelector("#btnToggleVidUnique");
      if (btnToggleVidUnique) {
        btnToggleVidUnique.addEventListener("click", function () {
          state.vaultVidUniqueOnly = !state.vaultVidUniqueOnly;
          refreshSubPaneOnly("videos", null);
        });
      }
      var btnToggleVid169 = scopeEl.querySelector("#btnToggleVid169");
      if (btnToggleVid169) {
        btnToggleVid169.addEventListener("click", function () {
          state.vaultVidOnly169 = !state.vaultVidOnly169;
          refreshSubPaneOnly("videos", null);
        });
      }
      scopeEl.querySelectorAll("[data-vvid-cat]").forEach(function (pill) {
        pill.addEventListener("click", function () {
          state.vaultVidCat = pill.getAttribute("data-vvid-cat");
          refreshSubPaneOnly("videos", null);
        });
      });
      var vidSearchEl = scopeEl.querySelector("#vaultVidSearchInput");
      if (vidSearchEl) {
        vidSearchEl.addEventListener("input", function () {
          state.vaultVidSearch = vidSearchEl.value || "";
          refreshSubPaneOnly("videos", "vaultVidSearchInput");
        });
      }

      scopeEl.querySelectorAll("[data-vimg-origin]").forEach(function (pill) {
        pill.addEventListener("click", function () {
          state.vaultImgOrigin = pill.getAttribute("data-vimg-origin");
          refreshSubPaneOnly("images", null);
        });
      });
      var btnToggleImgUnique = scopeEl.querySelector("#btnToggleImgUnique");
      if (btnToggleImgUnique) {
        btnToggleImgUnique.addEventListener("click", function () {
          state.vaultImgUniqueOnly = !state.vaultImgUniqueOnly;
          refreshSubPaneOnly("images", null);
        });
      }
      scopeEl.querySelectorAll("[data-vimg-cat]").forEach(function (pill) {
        pill.addEventListener("click", function () {
          state.vaultImgCat = pill.getAttribute("data-vimg-cat");
          refreshSubPaneOnly("images", null);
        });
      });
      var imgSearchEl = scopeEl.querySelector("#vaultImgSearchInput");
      if (imgSearchEl) {
        imgSearchEl.addEventListener("input", function () {
          state.vaultImgSearch = imgSearchEl.value || "";
          refreshSubPaneOnly("images", "vaultImgSearchInput");
        });
      }

      scopeEl.querySelectorAll("[data-triad-filter]").forEach(function (pill) {
        pill.addEventListener("click", function () {
          state.triadFilter = pill.getAttribute("data-triad-filter");
          refreshSubPaneOnly("triads", null);
        });
      });
      var trSearchEl = scopeEl.querySelector("#triadSearchInput");
      if (trSearchEl) {
        trSearchEl.addEventListener("input", function () {
          state.triadSearch = trSearchEl.value || "";
          refreshSubPaneOnly("triads", "triadSearchInput");
        });
      }

      scopeEl.querySelectorAll("[data-inline-play-vid]").forEach(function (box) {
        box.addEventListener("click", function () {
          if (box.querySelector("video")) return;
          var src = box.getAttribute("data-inline-play-vid");
          if (!src) return;
          box.innerHTML = "<video src=\"" + esc(src) + "\" controls autoplay playsinline style=\"width:100%;height:100%;object-fit:contain;background:#04060a;\"></video>";
          box.style.cursor = "default";
        });
      });

      scopeEl.querySelectorAll("[data-copy-triad-part]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var parts = btn.getAttribute("data-copy-triad-part").split(":");
          var num = parts[0], field = parts[1];
          var t = getTriadsEp().find(function (x) { return x.num === num; });
          if (!t) return;
          var txt = field === "p1" ? t.p1_start : (field === "p2" ? t.p2_flow : t.p3_end);
          copyText(txt, "Тріада #" + num + " (" + field.toUpperCase() + ")");
        });
      });

      scopeEl.querySelectorAll("[data-copy-triad-full]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var num = btn.getAttribute("data-copy-triad-full");
          var t = getTriadsEp().find(function (x) { return x.num === num; });
          if (!t) return;
          var full = [
            "=== ТРІАДА #" + t.num + ": " + t.title_ua + " (" + t.tc + ") ===",
            "1) START IMAGE (Frame A):",
            t.p1_start,
            "",
            "2) GOOGLE FLOW MORPH (Action A -> B):",
            t.p2_flow,
            "",
            "3) END IMAGE (Frame B):",
            t.p3_end
          ].join("\n");
          copyText(full, "Повна Тріада #" + num);
        });
      });

      scopeEl.querySelectorAll("[data-triad-check]").forEach(function (chk) {
        chk.addEventListener("change", function () {
          var k = "triad_" + chk.getAttribute("data-triad-check");
          if (chk.checked) state.checked[k] = true;
          else delete state.checked[k];
          saveProgress();
        });
      });

      scopeEl.querySelectorAll("[data-play-pidx]").forEach(function (btn) {
        if (btn.getAttribute("data-bound")) return;
        btn.setAttribute("data-bound", "1");
        btn.addEventListener("click", function () {
          var pIdx = parseInt(btn.getAttribute("data-play-pidx"), 10);
          selectDockClip(pIdx, true);
          showToast("▶️ Завантажено у правий Відео-Монітор");
        });
      });

      scopeEl.querySelectorAll("[data-popup-pidx]").forEach(function (btn) {
        if (btn.getAttribute("data-bound")) return;
        btn.setAttribute("data-bound", "1");
        btn.addEventListener("click", function () {
          var pIdx = parseInt(btn.getAttribute("data-popup-pidx"), 10);
          openCinemaModal(pIdx);
        });
      });

      scopeEl.querySelectorAll("[data-copy-text]").forEach(function (btn) {
        if (btn.getAttribute("data-bound")) return;
        btn.setAttribute("data-bound", "1");
        btn.addEventListener("click", function () {
          var txt = btn.getAttribute("data-copy-text");
          if (txt) copyText(txt, "шлях файлу");
        });
      });
    }

    // Mark already-bound elements outside/inside pane so refreshSubPaneOnly never double-binds
    pane.querySelectorAll("[data-play-pidx], [data-popup-pidx], [data-copy-text]").forEach(function (el) {
      el.setAttribute("data-bound", "1");
    });

    pane.querySelectorAll("[data-media-subtab]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        state.mediaSubTab = btn.getAttribute("data-media-subtab");
        renderMedia();
      });
    });

    pane.querySelectorAll("[data-scroll-arch]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var tid = btn.getAttribute("data-scroll-arch");
        var target = tid ? document.getElementById(tid) : null;
        if (target && target.scrollIntoView) {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      });
    });

    var subPaneBodyEl = document.getElementById("mediaSubPaneBody");
    if (subPaneBodyEl) {
      bindMediaDynamicControls(subPaneBodyEl);
    }

    setupReelAnimationObserver();
  }

  function init() {
    document.title = "EP" + epData.ep + " — " + epData.name + " | Мастер-Досьє та Студія Cinematic Thoughtcast";

    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest("[data-reveal-finder]");
      if (btn) {
        ev.preventDefault();
        var path = btn.getAttribute("data-reveal-finder");
        var label = btn.getAttribute("data-reveal-label") || "";
        revealInFinder(path, label);
      }
    });

    window.addEventListener("hashchange", function () {
      var h = (window.location.hash || "").replace(/^#/, "");
      if (h) switchTab(h, false);
    });

    var renderSteps = [
      ["Shell", renderShell],
      ["SOP", renderSOP],
      ["Bio", renderBio],
      ["Script", renderScript],
      ["Prompts", renderPrompts],
      ["Quotes", renderQuotes],
      ["Audio", renderAudio],
      ["Media", renderMedia],
      ["DaVinci", renderDaVinci]
    ];

    renderSteps.forEach(function (step) {
      try {
        step[1]();
      } catch (err) {
        console.error("Помилка рендерингу " + step[0] + ":", err);
      }
    });

    try { updateTopProgress(); } catch (e) { console.error(e); }

    var hash = (window.location.hash || "").replace(/^#/, "");
    if (hash) switchTab(hash, false);
  }

  init();
})();
