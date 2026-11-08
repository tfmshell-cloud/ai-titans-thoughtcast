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
    if (fill) fill.style.width = stats.pct + "%";
    if (lbl) lbl.textContent = stats.pct + "% (" + stats.sopDone + "/" + stats.sopTotal + " SOP)";
    if (badgeSop) badgeSop.textContent = stats.sopDone + "/" + stats.sopTotal;
    if (badgeVid) badgeVid.textContent = stats.vidDone + "/100";
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

  function renderShell() {
    var switcherHtml = seasonIndex.map(function (item) {
      var activeCls = item.ep === epData.ep ? " active" : "";
      var fname = item.page_url.split("/").pop();
      return "<a class=\"ep-pill-link" + activeCls + "\" href=\"" + esc(fname) + "\" title=\"" + esc(item.name + " — " + item.title) + "\">EP" + esc(item.ep) + "</a>";
    }).join("");

    var epMediaInit = (window.MEDIA_ACQUISITION_POOL || {})[epData.ep] || {};
    var totalVidClips = ((epMediaInit.archives || []).length + (epMediaInit.flow_queue || []).length + (epMediaInit.dossiers || []).length);

    var app = document.getElementById("episodeApp");
    app.innerHTML = [
      "<header class=\"ep-topbar\">",
      "  <div class=\"ep-topbar-inner\">",
      "    <div style=\"display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;\">",
      "      <a class=\"btn-back-hub\" href=\"../index.html\">← Головний Дашборд (10 Титанів)</a>",
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
      "        <button class=\"btn btn-cyan\" id=\"btnHeroJumpMedia\" style=\"padding:2px 9px;font-size:11px;\">🎬 Дивитися Архіви & Майбутні Футажі (" + totalVidClips + ")</button>",
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
      "    </div>",
      "  </section>",

      "  <nav class=\"studio-tabs\" id=\"studioTabs\">",
      "    <button class=\"studio-tab-btn active\" data-tab=\"sop\">🧭 1. Алгоритм дій (SOP) <span class=\"tab-count-badge\" id=\"badgeSopCount\">0/22</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"bio\">🧬 2. Біографія та кризи <span class=\"tab-count-badge\">" + (epData.biography || []).length + "</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"script\">🎬 3. Режисерський сценарій <span class=\"tab-count-badge\">4 акти</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"prompts\">🎥 4. 100 Візуальних промптів <span class=\"tab-count-badge\" id=\"badgeVidCount\">0/100</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"quotes\">💬 5. 100 Цитат і тез <span class=\"tab-count-badge\">100</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"audio\">🎵 6. Suno 92 BPM & Озвучка <span class=\"tab-count-badge\">4/4 Актів WAV</span></button>",
      "    <button class=\"studio-tab-btn\" data-tab=\"media\">🗂️ 7. Медіа-Пул, Архіви & Відео <span class=\"tab-count-badge\">🎬 " + totalVidClips + " MP4</span></button>",
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
        switchTab("media", true);
      });
    }
  }

  function switchTab(tabId, updateHash) {
    if (tabId) tabId = String(tabId).replace(/^pane-/, "");
    var valid = ["sop", "bio", "script", "prompts", "quotes", "audio", "media", "davinci"];
    if (valid.indexOf(tabId) === -1) tabId = "sop";
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
        history.replaceState(null, "", "#" + tabId);
      } catch (e) {
        window.location.hash = tabId;
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

    pane.innerHTML = [
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
      "</div>"
    ].join("\n");

    document.getElementById("btnCopyNbName").addEventListener("click", function () {
      copyText(nbName, "назва блокнота NotebookLM");
    });
    document.getElementById("btnCopyNbPrompt").addEventListener("click", function () {
      copyText(nbPrompt, "інструкція Audio Overview для NotebookLM");
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

    pane.innerHTML = [
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
  }

  /* ---------------- TAB 7: DAVINCI RESOLVE 19 STUDIO ---------------- */
  function renderDaVinci() {
    var pane = document.getElementById("pane-davinci");
    pane.innerHTML = [
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
    var epMedia = allMedia[epData.ep] || { dossiers: [], archives: [], flow_queue: [], portrait: {}, flow_gallery: [] };
    var repoRoot = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/";
    var list = [];

    // 1. Real Archival B-Roll MP4s
    (epMedia.archives || []).forEach(function (ar, idx) {
      var fileName = ar.file || ar.mp4_file || "";
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

    // 2. Real Google Flow / Veo Videos (#01-#04)
    (epMedia.flow_queue || []).forEach(function (fq, idx) {
      if (fq.status === "video_ready" && fq.video_preview) {
        list.push({
          uid: "flow_vid_" + fq.num,
          type: "video",
          kind: "flow_video",
          kindLabel: "🚀 Flow 4K/HD Відео (#" + fq.num + ")",
          chipClass: "chip-emerald",
          title: fq.title || ("Flow Сцена #" + fq.num + " — " + fq.file),
          file: fq.file,
          tc: fq.tc || "00:00",
          track: "DaVinci V1 • Speed 60% • " + (fq.specs || "24 fps 1080p/720p"),
          desc: "Згенеровано в Google Flow / Veo. " + (fq.specs || "") + ". Промпт: " + fq.prompt,
          src: "../" + fq.video_preview,
          poster: fq.keyframe_preview ? ("../" + fq.keyframe_preview) : "",
          localPath: repoRoot + (fq.raw_video_path || ("05_RAW_FOOTAGE/flow_renders/" + fq.file)),
          githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/05_RAW_FOOTAGE/flow_renders/" + encodeURIComponent(fq.file),
          externalUrl: "",
          prompt: fq.prompt || ""
        });
      } else if (fq.status === "image_ready" && fq.keyframe_preview) {
        // 3. Ready 2K Keyframes (#05, #06, #07)
        list.push({
          uid: "flow_img_" + fq.num,
          type: "image",
          kind: "flow_image",
          kindLabel: "🖼️ 2K Кадр (#" + fq.num + " • Очікує відео)",
          chipClass: "chip-cyan",
          title: fq.title || ("Flow Кадр #" + fq.num),
          file: (fq.raw_image_path ? fq.raw_image_path.split("/").pop() : (fq.file.replace(/\.mp4$/, ".jpg"))),
          tc: fq.tc || "00:00",
          track: "Концепт-кадр 2K (2752×1536) • Підготовка відео Flow / Veo",
          desc: "Концепт-кадр 2K згенеровано у 2752×1536. Наступний крок: генерація відео за цим кадром у Google Flow. Промпт: " + fq.prompt,
          src: "../" + fq.keyframe_preview,
          poster: "../" + fq.keyframe_preview,
          localPath: repoRoot + (fq.raw_image_path || ""),
          githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + (fq.raw_image_path || ""),
          externalUrl: "",
          prompt: fq.prompt || ""
        });
      }
    });

    // 4. UHD 4K Dossier Zoom Videos (V2)
    (epMedia.dossiers || []).forEach(function (d, idx) {
      var vUrl = d.video_preview ? ("../" + d.video_preview) : ("../assets/video_previews/dossiers/" + d.id + ".mp4");
      list.push({
        uid: "dos_" + idx,
        type: "video",
        kind: "dossier",
        kindLabel: "🗂️ 4K Досьє (Zoom 1.00→1.06)",
        chipClass: "chip-amber",
        title: d.title,
        file: d.id + ".mp4",
        tc: d.timecode || "00:00",
        track: "DaVinci V2 • UHD 4K Документальна пластина (Dynamic Zoom)",
        desc: "«" + d.highlight + "» — Джерело: " + d.source_label,
        src: vUrl,
        poster: d.web_preview ? ("../" + d.web_preview) : "",
        localPath: repoRoot + d.raw_4k_png,
        githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/07_DASHBOARD/" + d.web_preview,
        externalUrl: "",
        prompt: ""
      });
    });

    // 5. Extra B-Roll & Study Stills
    (epMedia.flow_gallery || []).forEach(function (g, idx) {
      if (g.code.indexOf("B-ROLL") === 0 || g.code.indexOf("STUDY") === 0) {
        list.push({
          uid: "broll_" + idx,
          type: "image",
          kind: "broll",
          kindLabel: (g.code.indexOf("STUDY") === 0 ? "🎨 Концепт-дослідження (" : "🎞️ Кінокадр B-Roll (") + g.code + ")",
          chipClass: g.code.indexOf("STUDY") === 0 ? "chip-purple" : "chip-amber",
          title: g.title,
          file: g.raw_path.split("/").pop(),
          tc: g.tc || "00:00",
          track: "Кінокадр / Дослідження • " + g.dims,
          desc: (g.badge || "") + " — " + g.title + ". Розмір: " + g.dims,
          src: "../" + g.web_preview,
          poster: "../" + g.web_preview,
          localPath: repoRoot + g.raw_path,
          githubUrl: "https://github.com/tfmshell-cloud/ai-titans-thoughtcast/blob/main/" + g.raw_path,
          externalUrl: "",
          prompt: ""
        });
      }
    });

    return list;
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
        ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" style=\"object-fit:cover;\">"
        : "<video class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" muted loop playsinline preload=\"metadata\"></video>";

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
      ? "<img id=\"modalStageImage\" class=\"cinema-stage-video\" src=\"" + esc(clip.src) + "\" style=\"object-fit:contain;background:#05070c;\">"
      : "<video id=\"modalStageVideo\" class=\"cinema-stage-video\" src=\"" + esc(clip.src) + "\" controls autoplay loop playsinline></video>";

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
        "  <div style=\"position:relative;cursor:pointer;\" data-play-pidx=\"" + pIdx + "\" title=\"Натисніть, щоб запустити відео-анімацію зуму в моніторі\">",
        "    <img src=\"../" + esc(d.web_preview) + "\" alt=\"" + esc(d.title) + "\" loading=\"lazy\" style=\"width:100%;border-radius:6px;border:1px solid var(--border);margin-bottom:8px;display:block;\">",
        "    <span style=\"position:absolute;bottom:14px;right:8px;background:rgba(12,14,19,0.88);color:var(--amber);border:1px solid rgba(251,191,36,0.45);padding:2px 8px;border-radius:6px;font-size:10.5px;font-weight:700;\">▶️ Дивитися 24fps Zoom</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(d.title) + "</h4>",
        "  <div style=\"font-size:11px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;\">" + esc(d.raw_4k_png) + "</div>",
        "  <div style=\"font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;\">«" + esc(d.highlight) + "»</div>",
        "  <div class=\"btn-group\">",
        "    <button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;\" data-play-pidx=\"" + pIdx + "\">▶️ У правий монітор</button>",
        "    <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;\" data-popup-pidx=\"" + pIdx + "\">🔍 Спливаюче вікно</button>",
        "    <button class=\"btn btn-emerald\" style=\"padding:4px 8px;font-size:11px;\" data-copy-dos-path=\"" + idx + "\">📋 Шлях 4K PNG</button>",
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
        "      <button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;\" data-popup-pidx=\"" + pIdx + "\">🔍 Спливаюче вікно</button>",
        "      <button class=\"btn btn-emerald\" style=\"padding:3px 7px;font-size:11px;\" data-copy-arch-path=\"" + idx + "\">Шлях MP4</button>",
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
          "<div style=\"position:relative;cursor:pointer;\" data-play-flow-kf=\"" + esc(fq.num) + "\" title=\"Клікніть для перегляду 2K концепт-кадру в моніторі\">",
          "  <img src=\"../" + esc(fq.keyframe_preview) + "\" alt=\"" + esc(fq.title) + "\" style=\"width:225px;aspect-ratio:16/9;object-fit:cover;border-radius:7px;border:1px solid rgba(56,189,248,0.45);display:block;\">",
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
        actionsHtml.push("<button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;\" data-play-flow-vid=\"" + esc(fq.num) + "\">▶️ У монітор</button>");
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;\" data-popup-flow-vid=\"" + esc(fq.num) + "\">🔍 Вікно</button>");
        actionsHtml.push("<button class=\"btn btn-emerald\" style=\"padding:3px 7px;font-size:11px;\" data-copy-flowq-vpath=\"" + idx + "\">Шлях MP4</button>");
      } else if (isImgReady) {
        actionsHtml.push("<button class=\"btn btn-cyan\" style=\"padding:4px 8px;font-size:11px;\" data-play-flow-kf=\"" + esc(fq.num) + "\">🖼️ 2K у монітор</button>");
        actionsHtml.push("<button class=\"btn btn-amber\" style=\"padding:4px 8px;font-size:11px;\" data-popup-flow-kf=\"" + esc(fq.num) + "\">🔍 2K у вікні</button>");
        actionsHtml.push("<button class=\"btn btn-emerald\" style=\"padding:3px 7px;font-size:11px;\" data-copy-flowq-ipath=\"" + idx + "\">Шлях JPG</button>");
      }
      actionsHtml.push("<button class=\"btn\" style=\"padding:3px 7px;font-size:11px;\" data-copy-flowq-p=\"" + idx + "\">Промпт</button>");

      return [
        "<tr" + (isVidReady ? " style=\"background:rgba(52,211,153,0.04);\"" : (isImgReady ? " style=\"background:rgba(56,189,248,0.03);\"" : "")) + ">",
        "  <td><input type=\"checkbox\" class=\"sop-checkbox\" data-flowq-check=\"" + esc(fq.num) + "\"" + (isDone ? " checked" : "") + "></td>",
        "  <td style=\"width:225px;\">" + previewCol + "</td>",
        "  <td>",
        "    <div style=\"font-weight:700;color:var(--text-primary);margin-bottom:3px;\">" + esc(fq.title || fq.file) + "</div>",
        "    <span class=\"filename-mono\">05_RAW_FOOTAGE/flow_renders/" + esc(fq.file) + "</span>",
        statusNote,
        "  </td>",
        "  <td style=\"font-family:var(--mono);font-size:11px;color:#e2e8f0;max-width:360px;\">" + esc(fq.prompt) + "</td>",
        "  <td><div class=\"btn-group\">" + actionsHtml.join("\n") + "</div></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

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

    var photoCardsHtml = (epMedia.archival_photos || []).map(function (ph, idx) {
      return [
        "<div class=\"node-box\" style=\"border-top-color:var(--amber);\">",
        "  <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:6px;\">",
        "    <span class=\"chip chip-amber\">" + esc(ph.code) + "</span>",
        "    <span class=\"chip chip-purple\">" + esc(ph.source) + "</span>",
        "  </div>",
        "  <a href=\"../" + esc(ph.web_preview) + "\" target=\"_blank\" rel=\"noopener\">",
        "    <img src=\"../" + esc(ph.web_preview) + "\" alt=\"" + esc(ph.title) + "\" style=\"width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:6px;border:1px solid var(--border);margin-bottom:7px;display:block;\">",
        "  </a>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(ph.title) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;\">" + esc(ph.raw_file) + "</div>",
        "  <div style=\"font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;\">" + esc(ph.desc) + "</div>",
        "  <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;width:100%;\" data-copy-text=\"" + esc(ph.raw_file) + "\">📋 Шлях файлу JPG</button>",
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

    var photoSectionHtml = photoCardsHtml ? [
      "<div class=\"panel-card\" style=\"border-color:rgba(251,191,36,0.45);\">",
      "  <div class=\"panel-head\">",
      "    <div>",
      "      <div class=\"panel-title\">📸 Автентичні Історичні Фото Спікера (" + (epMedia.archival_photos || []).length + " фото • Ера YC, WWDC 2008, Stanford)</div>",
      "      <div class=\"panel-desc\">Реальні історичні знімки з відкритого архіву Wikimedia Commons та Apple Keynote Archive.</div>",
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
        "  <div style=\"position:relative;cursor:pointer;\" data-play-gallery-idx=\"" + idx + "\" title=\"Клікніть для перегляду кадру у правому моніторі\">",
        "    <img src=\"../" + esc(g.web_preview) + "\" alt=\"" + esc(g.title) + "\" loading=\"lazy\" style=\"width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:6px;border:1px solid var(--border);display:block;margin-bottom:7px;\">",
        "    <span style=\"position:absolute;bottom:10px;right:6px;background:rgba(12,14,19,0.92);color:var(--cyan);padding:1px 6px;border-radius:4px;font-size:9.5px;font-family:var(--mono);font-weight:700;\">" + esc(g.dims) + "</span>",
        "  </div>",
        "  <h4 style=\"margin:2px 0 4px 0;\">" + esc(g.code) + " • " + esc(g.title) + "</h4>",
        "  <div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-bottom:6px;word-break:break-all;\">" + esc(g.raw_path) + "</div>",
        "  <div class=\"btn-group\">",
        "    <button class=\"btn btn-cyan\" style=\"padding:3px 8px;font-size:11px;\" data-play-gallery-idx=\"" + idx + "\">▶️ У монітор</button>",
        "    <button class=\"btn btn-amber\" style=\"padding:3px 8px;font-size:11px;\" data-popup-gallery-idx=\"" + idx + "\">🔍 У вікні</button>",
        "    <button class=\"btn btn-emerald\" style=\"padding:3px 8px;font-size:11px;\" data-copy-gallery-path=\"" + idx + "\">📋 Шлях файлу</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    var filteredReelHtml = playlist.map(function (item, idx) {
      if (state.mediaDockFilter !== "all" && item.kind !== state.mediaDockFilter) return "";
      var activeCls = idx === state.mediaActiveIndex ? " active" : "";
      var thumbHtml = item.type === "image"
        ? "<img class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" style=\"object-fit:cover;\">"
        : "<video class=\"reel-thumb-video\" src=\"" + esc(item.src) + "\" muted loop playsinline preload=\"metadata\"></video>";

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

    pane.innerHTML = [
      "<div class=\"media-split-layout\">",
      "  <div class=\"media-main-col\">",
      "    <div class=\"panel-card\" style=\"border-color:rgba(251,191,36,0.45);\">",
      "      <div class=\"panel-head\">",
      "        <div>",
      "          <div class=\"panel-title\">🎬 Візуальний Пул Епізоду (" + playlist.length + " готових медіа-елементів: 4 реал. відео Flow + 3 2K кадри Flow + 3 архіви B-Roll + 5 4K досьє + 3 B-Roll кадри)</div>",
      "          <div class=\"panel-desc\">Усі відео та зображення структуровано за окремими папками, синхронізовано між <strong>GitHub</strong>, <strong>GitHub Pages</strong> та <strong>Google Drive</strong>. Дивіться медіа в таблицях зліва, у <strong>Правому Відео-Моніторі</strong> або у <strong>Спливаючому Кінозалі</strong>.</div>",
      "        </div>",
      "        <div class=\"btn-group\">",
      "          <button class=\"btn btn-amber\" id=\"btnOpenFullCinemaHero\">🔍 Відкрити Спливаючий Кінозал (" + playlist.length + " медіа)</button>",
      "          <button class=\"btn btn-emerald\" id=\"btnDownloadEpSrt\">📥 Титри V3 (.srt)</button>",
      "        </div>",
      "      </div>",
      "      <div class=\"node-tree-grid\">",
      "        <div class=\"node-box\" style=\"border-top-color:var(--emerald);\"><h4>1. Готові Відео Flow (#01–#04)</h4><p style=\"font-size:11.8px;color:var(--text-secondary);\"><strong>4 кліпи 24fps</strong> зі стереозвуком (Macintosh, CRT Assembly, Silicon Laser, Exponential Curve) у <code>05_RAW_FOOTAGE/flow_renders/</code>.</p></div>",
      "        <div class=\"node-box\" style=\"border-top-color:var(--cyan);\"><h4>2. 2K Концепт-Кадри (#05–#07)</h4><p style=\"font-size:11.8px;color:var(--text-secondary);\"><strong>3 кадри 2752×1536</strong> (Neural Lattice, Servers Cold Hall, Boardroom Noir) готові до генерації відео у Flow.</p></div>",
      "        <div class=\"node-box\" style=\"border-top-color:var(--purple);\"><h4>3. Архіви B-Roll (3 MP4)</h4><p style=\"font-size:11.8px;color:var(--text-secondary);\">Реальні історичні плани (Сенат США 2023, Apple Mac 1992 CRT) у <code>05_RAW_FOOTAGE/archives/</code>.</p></div>",
      "        <div class=\"node-box\" style=\"border-top-color:var(--amber);\"><h4>4. 4K Досьє (5 пластин)</h4><p style=\"font-size:11.8px;color:var(--text-secondary);\">UHD 3840×2160 PNG + 24fps відеокліпи <code>Dynamic Zoom 1.00→1.06</code> для доріжки DaVinci V2.</p></div>",
      "      </div>",
      "    </div>",

      "    <div class=\"panel-card\" style=\"border-color:rgba(167,139,250,0.55);\">",
      "      <div class=\"panel-head\">",
      "        <div>",
      "          <div class=\"panel-title\">🚀 Пріоритетна Черга Google Flow / Veo (10 базових сцен) — Статус: 4 відео готові • 3 кадри 2K готові • 3 у розробці</div>",
      "          <div class=\"panel-desc\">Сцени <strong>#01–#04</strong> уже відтворюються через вбудовані плеєри. Сцени <strong>#05–#07</strong> мають готові концепт-кадри 2K (клікніть для збільшення).</div>",
      "        </div>",
      "      </div>",
      "      <div class=\"studio-table-wrap\">",
      "        <table class=\"studio-table\">",
      "          <thead><tr><th>✓</th><th>Медіа-прев'ю (Відео / 2K Кадр)</th><th>Цільовий файл у flow_renders/</th><th>Промпт для Google Flow / Veo 4K</th><th>Дії</th></tr></thead>",
      "          <tbody>" + flowRowsHtml + "</tbody>",
      "        </table>",
      "      </div>",
      "    </div>",

      "    <div class=\"panel-card\" style=\"border-color:rgba(56,189,248,0.45);\">",
      "      <div class=\"panel-head\">",
      "        <div>",
      "          <div class=\"panel-title\">🖼️ Галерея 2K Концепт-Кадрів та Кінокадрів B-Roll (#05, #06, #07 + Акт 1)</div>",
      "          <div class=\"panel-desc\">Усі зображення зберігаються окремо у <code>05_RAW_FOOTAGE/flow_images/EP01_Altman/</code>. Клікніть на будь-який кадр для відкриття у моніторі або спливаючому вікні.</div>",
      "        </div>",
      "      </div>",
      "      <div class=\"node-tree-grid\">" + galleryCardsHtml + "</div>",
      "    </div>",

      "    <div class=\"panel-card\" style=\"border-color:rgba(52,211,153,0.45);\">",
      "      <div class=\"panel-head\">",
      "        <div>",
      "          <div class=\"panel-title\">📼 Реальні Історичні Відеоархіви B-Roll (05_RAW_FOOTAGE/archives/)</div>",
      "          <div class=\"panel-desc\">Натисніть Play прямо у рядку або кнопку <strong>«▶️ У монітор»</strong> / <strong>«🔍 Спливаюче вікно»</strong> для перегляду зі звуком.</div>",
      "        </div>",
      "        <button class=\"btn btn-cyan\" id=\"btnCopyFetchEpCmd\">💻 Команда fetch_archives.sh --ep EP" + esc(epData.ep) + "</button>",
      "      </div>",
      "      <div class=\"studio-table-wrap\">",
      "        <table class=\"studio-table\">",
      "          <thead><tr><th>Живий прев'ю-плеєр</th><th>Назва та файл Smart Bin</th><th>Першоджерело & Синхронізація</th><th>Дії</th></tr></thead>",
      "          <tbody>" + archiveRowsHtml + "</tbody>",
      "        </table>",
      "      </div>",
      "    </div>",

      "    <div class=\"panel-card\">",
      photoSectionHtml,
      audioSectionHtml,
      nbHtml,
      "      <div class=\"panel-head\">",
      "        <div>",
      "          <div class=\"panel-title\">🗂️ Згенеровані 4K Документальні Артефакти («Досьє» • 3840×2160 PNG + 24fps Zoom MP4)</div>",
      "          <div class=\"panel-desc\">Клікніть по зображенню досьє, щоб переглянути його анімований кінематографічний наїзд камери (1.00→1.06) у правому моніторі.</div>",
      "        </div>",
      "      </div>",
      "      <div class=\"node-tree-grid\">" + dossiersHtml + portraitCardHtml + "</div>",
      "    </div>",
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
      "          <button class=\"btn\" style=\"padding:3px 8px;font-size:11px;\" id=\"btnDockNext\">Наступне ▶</button>",
      "        </div>",
      "      </div>",
      "    </div>",

      "    <div class=\"dock-filter-row\">",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "all" ? " active" : "") + "\" data-dock-filter=\"all\">Усі (" + playlist.length + ")</button>",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "flow_video" ? " active" : "") + "\" data-dock-filter=\"flow_video\">🚀 Flow Відео (4)</button>",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "flow_image" ? " active" : "") + "\" data-dock-filter=\"flow_image\">🖼️ 2K Кадри (3)</button>",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "archive" ? " active" : "") + "\" data-dock-filter=\"archive\">📼 Архіви (" + nArch + ")</button>",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "dossier" ? " active" : "") + "\" data-dock-filter=\"dossier\">🗂️ Досьє (" + nDos + ")</button>",
      "      <button class=\"dock-pill" + (state.mediaDockFilter === "broll" ? " active" : "") + "\" data-dock-filter=\"broll\">🎞️ B-Roll (3)</button>",
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
    if (mainVid && activeClip.type === "video") {
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

    setupReelAnimationObserver();
  }

  function init() {
    document.title = "EP" + epData.ep + " — " + epData.name + " | Мастер-Досьє та Студія Cinematic Thoughtcast";
    renderShell();
    renderSOP();
    renderBio();
    renderScript();
    renderPrompts();
    renderQuotes();
    renderAudio();
    renderMedia();
    renderDaVinci();
    updateTopProgress();

    var hash = (window.location.hash || "").replace(/^#/, "");
    if (hash) switchTab(hash, false);

    window.addEventListener("hashchange", function () {
      var h = (window.location.hash || "").replace(/^#/, "");
      if (h) switchTab(h, false);
    });
  }

  init();
})();
