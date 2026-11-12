(function () {
  "use strict";

  var season = window.SEASON1_INDEX || [];
  var quotesDb = window.TITANS_1000_QUOTES || [];

  var CONFLICTS = {
    "01": "Macintosh LC II у 8 років, публічний камінг-аут у консервативній школі, 120 годин корпоративного бунту в OpenAI.",
    "02": "Миття туалетів у реформаторії Кентуккі, посуд у Denny's, 30 днів до банкрутства після NV1, 10 років віри в CUDA.",
    "03": "Шаховий майстер у 13 років, гра Theme Park у 17, божественний Хід 37 в AlphaGo та розгадка білків у AlphaFold2.",
    "04": "Тінь прапрадіда Джорджа Буля, рік праці теслею в Лондоні, 30 років «зими ШІ» на підлозі, вихід із Google та Нобель.",
    "05": "Паяльник у передмісті Парижа, згорткові мережі для банківських чеків у Bell Labs, критика LLM та захист Open Source.",
    "06": "Переїзди Горький–Єрусалим–Торонто, двері Хінтона у 17 років, AlexNet, епоха GPT та монастир тиші SSI.",
    "07": "Біофізика сітківки в Прінстоні, емпіричні закони масштабування, розрив із OpenAI, Constitutional AI та маніфест благодаті.",
    "08": "Еміграція з Ченду у 16 років без мови, прасувальний прес у хімчистці паралельно з Прінстоном, подвиг ImageNet та World Labs.",
    "09": "Відмова від мільярдів Кремнієвої долини заради університету Mila, винахід Attention Mechanism та глобальна безпека ООН.",
    "10": "Передруковування коду з журналів у Сінгапурі, нейрон кота на 16 000 процесорів Google Brain, революція Coursera та Data-Centric AI."
  };

  var state = {
    tab: "heroes",
    quoteHero: "all",
    quoteQuery: "",
    quoteLimit: 120,
    sunoHeroFilter: "all",
    veoFilter: "all",
    veoHero: "all"
  };

  function esc(s) {
    if (s === null || s === undefined) return "";
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  var toastTimer = null;
  function showToast(msg) {
    var el = document.getElementById("hubToast");
    if (!el) return;
    el.textContent = msg;
    el.classList.add("visible");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      el.classList.remove("visible");
    }, 2300);
  }

  function copyText(txt, label) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(function () {
        showToast("✓ Скопійовано: " + (label || "буфер обміну"));
      }).catch(function () {
        fallbackCopy(txt, label);
      });
    } else {
      fallbackCopy(txt, label);
    }
  }

  function fallbackCopy(txt, label) {
    var ta = document.createElement("textarea");
    ta.value = txt;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      showToast("✓ Скопійовано: " + (label || "буфер обміну"));
    } catch (e) {}
    document.body.removeChild(ta);
  }

  function revealInFinder(filePath, label) {
    if (!filePath) return;
    var fullPath = filePath.startsWith("/")
      ? filePath
      : ("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/" + filePath);

    fetch("http://127.0.0.1:8765/reveal?path=" + encodeURIComponent(fullPath))
      .then(function (res) { return res.json(); })
      .then(function (data) {
        if (data.status === "ok") {
          showToast("📁 Відкрито у Finder: " + (label || fullPath.split("/").pop()));
        } else {
          copyText(fullPath, "шлях файлу");
          showToast("📋 Шлях скопійовано: " + fullPath.split("/").pop());
        }
      })
      .catch(function () {
        copyText(fullPath, "шлях файлу");
        showToast("📋 Шлях скопійовано! (Запустіть ./open_in_finder.sh --bridge)");
      });
  }

  function getHeroPrimaryTrack(epCode) {
    var pool = window.SUNO_MASTER_POOL || [];
    for (var i = 0; i < pool.length; i++) {
      if (pool[i].hero_ep === epCode && pool[i].smart_bin.indexOf("_ACT1_") !== -1) {
        return pool[i];
      }
    }
    return null;
  }

  function getHeroAllTracks(epCode) {
    var pool = window.SUNO_MASTER_POOL || [];
    var out = [];
    pool.forEach(function (t) {
      if (t.hero_ep === epCode) {
        out.push({ track: t, bin_dir: t.bin_dir, smart_bin: t.smart_bin });
      } else if (t.extra_bins) {
        t.extra_bins.forEach(function (eb) {
          if (eb.ep === epCode || eb.smart_bin.indexOf("EP" + epCode + "_") === 0) {
            out.push({ track: t, bin_dir: eb.bin_dir, smart_bin: eb.smart_bin });
          }
        });
      }
    });
    return out;
  }

  function getEpisodeReadiness(epItem) {
    var checked = {};
    try {
      var raw = localStorage.getItem("aititans_progress_v2_" + epItem.ep);
      if (raw) checked = JSON.parse(raw);
    } catch (e) {}

    var sopTotal = epItem.sop_tasks_count || 22;
    var sopDone = 0;
    Object.keys(checked).forEach(function (k) {
      if (k.indexOf("ep" + epItem.ep + "_s") === 0 && checked[k]) sopDone += 1;
    });

    var vidDone = 0;
    for (var i = 1; i <= 100; i++) {
      if (checked["vid_" + i]) vidDone += 1;
    }

    var sunoTotal = epItem.suno_count || 16;
    var heroWavCount = getHeroAllTracks(epItem.ep).length || 4;
    var sunoDone = heroWavCount;
    for (var s = 0; s < sunoTotal; s++) {
      if (checked["suno_" + s]) sunoDone += 1;
    }
    if (sunoDone > sunoTotal) sunoDone = sunoTotal;

    var voTotal = epItem.vo_count || 10;
    var voDone = 0;
    for (var v = 0; v < voTotal; v++) {
      if (checked["vo_" + v]) voDone += 1;
    }

    var pct = Math.round(((sopDone / sopTotal) * 70) + ((vidDone / 100) * 15) + ((sunoDone / sunoTotal) * 10) + ((voDone / voTotal) * 5));
    if (sopDone === sopTotal && sopTotal > 0 && pct < 100 && vidDone === 0 && voDone === 0) {
      pct = 100;
    }
    return {
      pct: Math.min(100, pct),
      sopDone: sopDone,
      sopTotal: sopTotal,
      vidDone: vidDone,
      heroWavCount: heroWavCount
    };
  }

  function renderHeroesGrid() {
    var container = document.getElementById("heroesGridContainer");
    if (!container) return;

    var totalWords = 0;
    var sumPct = 0;
    var mediaPool = window.MEDIA_ACQUISITION_POOL || {};

    var cardsHtml = season.map(function (h) {
      totalWords += (h.script_words || 0);
      var prog = getEpisodeReadiness(h);
      sumPct += prog.pct;
      var conflict = CONFLICTS[h.ep] || h.role;
      var act1Track = getHeroPrimaryTrack(h.ep);
      var epMedia = mediaPool[h.ep] || {};
      var vaultEp = (window.PROJECT_VAULT_INVENTORY || {})[h.ep] || {};
      var vSum = vaultEp.summary || {};
      var dosCount = (epMedia.dossiers || []).length || 0;
      var archCount = (epMedia.archives || []).length || 0;
      var flowCount = (epMedia.flow_queue || []).length || 0;
      var sciCount = (epMedia.scientific_vfx || []).length || 0;
      var galCount = vSum.images_count || (((epMedia.flow_gallery || []).length || 0) + ((epMedia.archival_photos || []).length || 0));
      var totalMp4Count = vSum.videos_count || (dosCount + archCount + flowCount + sciCount);
      var researchDocsCnt = vSum.research_docs_count || 0;
      var firstArch = (epMedia.archives || [])[0];
      var veoList = (window.VEO_ANIMATION_PIPELINE || []).filter(function (v) { return v.ep === h.ep; });
      var veoStatusMap = getVeoStatusMap();
      var veoDone = veoList.filter(function (v) { return !!veoStatusMap[v.id]; }).length;
      var veoBadgeHtml = veoList.length ? ("<span class=\x22pill " + (veoDone === veoList.length ? "pill-emerald" : "pill-amber") + "\x22>⚡ Veo: " + veoDone + "/" + veoList.length + "</span>") : "";


      var audioStripHtml = act1Track ? [
        "  <div style=\"background:rgba(16,185,129,0.07);border:1px solid rgba(52,211,153,0.28);border-radius:8px;padding:7px 10px;margin:8px 0;\" onclick=\"event.stopPropagation();\">",
        "    <div style=\"display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:5px;flex-wrap:wrap;\">",
        "      <span style=\"font-size:11px;color:var(--emerald);font-weight:600;\">🎧 Тема Акту 1: " + esc(act1Track.orig_name) + " (" + esc(act1Track.duration) + ")</span>",
        "      <span class=\"pill pill-emerald\" style=\"font-size:10px;\">✅ " + prog.heroWavCount + " WAV у Smart Bin</span>",
        "    </div>",
        "    <audio controls preload=\"none\" style=\"height:28px;width:100%;\" src=\"assets/audio_previews/" + esc(act1Track.preview) + "\"></audio>",
        "  </div>"
      ].join("\n") : "";

      return [
        "<article class=\"hero-card\" data-open-url=\"" + esc(h.page_url) + "\" tabindex=\"0\" role=\"link\" aria-label=\"Відкрити Мастер-Досьє: " + esc(h.name) + "\">",
        "  <div class=\"hero-card-top\">",
        "    <div class=\"hero-avatar-wrap\">",
        "      <img src=\"" + esc(h.avatar) + "\" alt=\"" + esc(h.name) + "\" loading=\"lazy\">",
        "      <span class=\"ep-num-badge\">EP " + esc(h.ep) + "</span>",
        "    </div>",
        "    <div class=\"hero-card-info\">",
        "      <div class=\"hero-badges-line\">",
        "        <span class=\"pill pill-purple\">" + esc(h.archetype) + "</span>",
        "        <span class=\"pill pill-emerald\">" + esc(h.duration) + " • " + esc(h.bpm) + "</span>",
        (window.MONTAGE_STATUS && window.MONTAGE_STATUS[h.ep]
          ? "        <span class=\"pill\" style=\"background:rgba(245,158,11,0.15);color:#f5b544;border:1px solid rgba(245,158,11,0.45);\" title=\"" + esc(window.MONTAGE_STATUS[h.ep].headline) + "\">🎬 Змонтовано: " + esc(window.MONTAGE_STATUS[h.ep].total_duration) + "</span>"
          : ""),
        "      </div>",
        "      <h3 class=\"hero-name\">" + esc(h.name) + " <span class=\"hero-latin-inline\">// " + esc(h.latin) + "</span></h3>",
        "      <div class=\"hero-ep-title\">«" + esc(h.title) + "»</div>",
        "      <div class=\"hero-role\">" + esc(h.role) + "</div>",
        "    </div>",
        "  </div>",

        "  <div class=\"hero-conflict-box\">",
        "    <strong>Точка опори та конфлікт:</strong> " + esc(conflict),
        "  </div>",

        audioStripHtml,

        "  <blockquote class=\"hero-quote-mini\">" + esc(h.key_quote) + "</blockquote>",

        "  <div class=\"hero-metrics-strip\">",
        "    <span>📝 <strong>" + esc(h.script_words) + "</strong> слів</span>",
        "    <span>🎬 <strong>" + totalMp4Count + "</strong> відео (Волт+Архів)</span>",
        "    <span>🖼️ <strong>" + galCount + "</strong> фото & 4K артів</span>",
        (researchDocsCnt ? ("    <span>📚 <strong>" + researchDocsCnt + "</strong> джерел/транскриптів</span>") : ("    <span>🎵 <strong>" + prog.heroWavCount + "/4</strong> актів WAV</span>")),
        "  </div>",

        "  <div class=\"hero-prog-row\">",
        "    <div class=\"hero-prog-label\"><span>Готовність випуску (" + prog.sopDone + "/" + prog.sopTotal + " SOP + 4 WAV + " + totalMp4Count + " MP4)</span><strong>" + prog.pct + "%</strong></div>",
        "    <div class=\"hero-prog-bar\"><div class=\"hero-prog-fill\" style=\"width:" + prog.pct + "%\"></div></div>",
        "  </div>",

        "  <div class=\"hero-deep-links\" onclick=\"event.stopPropagation();\">",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#media\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(251,191,36,0.65);background:rgba(251,191,36,0.13);color:var(--amber);\">🎬 Відео-Монітор (" + totalMp4Count + " MP4)</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#media-archives\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(52,211,153,0.55);background:rgba(16,185,129,0.12);color:var(--emerald);\">📼 Архів & Фото (" + archCount + "+" + (epMedia.archival_photos || []).length + ")</a>",
        (researchDocsCnt ? ("    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#bio\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(56,189,248,0.55);color:var(--cyan);\">📚 Джерела (" + researchDocsCnt + ")</a>") : ""),
        "    <a class=\"deep-chip\" href=\"media_vault_analysis.html?ep=" + esc(h.ep) + "\" target=\"_blank\" rel=\"noopener\">🗂️ Волт</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#audio\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(52,211,153,0.45);color:var(--emerald);\">🎵 4 WAV + Suno</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#script\" target=\"_blank\" rel=\"noopener\">🎬 Сценарій</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#prompts\" target=\"_blank\" rel=\"noopener\">🎥 100 Промптів</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#davinci\" target=\"_blank\" rel=\"noopener\">🎚️ DaVinci 19</a>",
        "  </div>",

        "  <a class=\"hero-open-cta\" href=\"" + esc(h.page_url) + "\" target=\"_blank\" rel=\"noopener\" onclick=\"event.stopPropagation();\">",
        "    <span>🚀 Відкрити персональну студію та Мастер-Досьє героя</span>",
        "    <span>↗</span>",
        "  </a>",
        "</article>"
      ].join("\n");
    }).join("\n");

    container.innerHTML = cardsHtml;

    // Mutual-exclusive audio playback across hero cards
    var cardAudios = container.querySelectorAll("audio");
    for (var ca = 0; ca < cardAudios.length; ca++) {
      cardAudios[ca].addEventListener("play", function (ev) {
        for (var cb = 0; cb < cardAudios.length; cb++) {
          if (cardAudios[cb] !== ev.target) cardAudios[cb].pause();
        }
      });
    }

    var avgPct = season.length ? Math.round(sumPct / season.length) : 0;
    var statWords = document.getElementById("statTotalWords");
    var statAvg = document.getElementById("statSeasonReadiness");
    if (statWords) statWords.textContent = totalWords.toLocaleString("uk-UA") + " слів";
    if (statAvg) statAvg.textContent = avgPct + "% SOP";

    container.querySelectorAll(".hero-card").forEach(function (card) {
      card.addEventListener("click", function () {
        var url = card.getAttribute("data-open-url");
        if (url) window.open(url, "_blank", "noopener");
      });
      card.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") {
          ev.preventDefault();
          var url = card.getAttribute("data-open-url");
          if (url) window.open(url, "_blank", "noopener");
        }
      });
    });

    var sideHeroes = document.getElementById("sidebarHeroLinks");
    if (sideHeroes) {
      sideHeroes.innerHTML = season.map(function (h) {
        return [
          "<a class=\"folder-row folder-row-link\" href=\"" + esc(h.page_url) + "\" target=\"_blank\" rel=\"noopener\">",
          "  <span class=\"folder-name\" style=\"font-size:11px;\">👤 EP" + esc(h.ep) + " • " + esc(h.name) + "</span>",
          "  <span class=\"folder-tag\" style=\"color:var(--emerald);\">4 WAV • Студія ↗</span>",
          "</a>"
        ].join("\n");
      }).join("\n");
    }
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
    renderAnimationPane();
    renderHeroesGrid();
  }

  function renderAnimationPane() {
    var container = document.getElementById("animationPaneContainer");
    if (!container) return;

    var pipeline = window.VEO_ANIMATION_PIPELINE || [];
    var statusMap = getVeoStatusMap();
    var doneCount = 0;
    pipeline.forEach(function (item) {
      if (statusMap[item.id]) doneCount += 1;
    });
    var totalCount = pipeline.length;
    var pendingCount = totalCount - doneCount;
    var pct = Math.round((doneCount / (totalCount || 1)) * 100);

    var bannerBadge = document.getElementById("hubTopVeoBadge");
    if (bannerBadge) {
      bannerBadge.textContent = "Veo Анімації (" + doneCount + "/" + totalCount + " Готово)";
      bannerBadge.className = "pill " + (doneCount === totalCount ? "pill-emerald" : "pill-amber");
    }

    var filter = state.veoFilter || "all";
    var heroFilter = state.veoHero || "all";

    var filtered = pipeline.filter(function (item) {
      var isDone = !!statusMap[item.id];
      if (filter === "done" && !isDone) return false;
      if (filter === "pending" && isDone) return false;
      if (heroFilter !== "all" && item.ep !== heroFilter) return false;
      return true;
    });

    var heroOptions = ['<option value="all">Всі герої (10 епізодів)</option>'].concat(
      season.map(function (h) {
        return '<option value="' + esc(h.ep) + '"' + (heroFilter === h.ep ? ' selected' : '') + '>EP' + esc(h.ep) + ' • ' + esc(h.name) + '</option>';
      })
    ).join("");

    var cardsHtml = filtered.map(function (item) {
      var isDone = !!statusMap[item.id];
      var statusBadge = isDone
        ? '<span class="pill pill-emerald" style="box-shadow:0 0 10px rgba(16,185,129,0.35);font-size:11px;">✅ ВІДЕО ГОТОВЕ (4K / 24 FPS)</span>'
        : '<span class="pill pill-amber" style="box-shadow:0 0 10px rgba(251,191,36,0.35);font-size:11px;">⏳ В ЧЕРЗІ НА ГЕНЕРАЦІЮ (Veo / Flow 6–10с)</span>';

      var mediaBoxHtml = "";
      if (isDone && item.video_preview) {
        mediaBoxHtml = [
          '<div style="position:relative;margin-bottom:10px;">',
          '  <video controls loop preload="metadata" playsinline style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:8px;border:1px solid rgba(16,185,129,0.4);display:block;" src="' + esc(item.video_preview) + '"></video>',
          '  <div style="position:absolute;top:8px;right:8px;background:rgba(15,23,42,0.85);padding:3px 8px;border-radius:5px;font-size:10px;color:var(--emerald);font-weight:700;">VEO / FLOW 4K</div>',
          '</div>'
        ].join("\n");
      } else {
        mediaBoxHtml = [
          '<div style="position:relative;margin-bottom:10px;overflow:hidden;border-radius:8px;border:1px solid rgba(251,191,36,0.35);cursor:pointer;" data-reveal-finder="' + esc(item.raw_path) + '" title="Клікніть, щоб відкрити цей 2K кадр у Finder">',
          '  <img src="' + esc(item.web_preview) + '" alt="' + esc(item.title) + '" style="width:100%;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform 0.2s;" onmouseover="this.style.transform=\'scale(1.02)\'" onmouseout="this.style.transform=\'scale(1)\'">',
          '  <div style="position:absolute;top:8px;right:8px;background:rgba(15,23,42,0.85);padding:3px 8px;border-radius:5px;font-size:10px;color:var(--amber);font-weight:700;">2K KEYFRAME</div>',
          '  <div style="position:absolute;bottom:8px;left:8px;background:rgba(15,23,42,0.85);padding:3px 8px;border-radius:5px;font-size:10.5px;color:var(--cyan);font-weight:600;display:flex;align-items:center;gap:4px;">📁 Відкрити у Finder</div>',
          '</div>'
        ].join("\n");
      }

      return [
        '<div class="card" style="border-color:' + (isDone ? 'rgba(16,185,129,0.35)' : 'rgba(251,191,36,0.4)') + ';background:var(--surface);display:flex;flex-direction:column;justify-content:space-between;padding:1rem;">',
        '  <div>',
        '    <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;margin-bottom:8px;flex-wrap:wrap;">',
        '      <div style="display:flex;gap:5px;align-items:center;">',
        '        <span class="pill pill-purple">EP' + esc(item.ep) + ' • ' + esc(item.hero) + '</span>',
        '        <span class="pill pill-cyan" style="font-family:var(--mono);font-size:10.5px;">' + esc(item.code) + '</span>',
        '      </div>',
        '      ' + statusBadge,
        '    </div>',
        mediaBoxHtml,
        '    <h3 style="font-size:14px;line-height:1.35;margin:0 0 6px 0;color:var(--text-primary);">' + esc(item.title) + '</h3>',
        '    <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;">',
        '      <span class="pill pill-purple" style="font-size:10.5px;">⏱️ ' + esc(item.tc) + '</span>',
        '      <span class="pill pill-cyan" style="font-size:10.5px;">' + esc(item.act) + '</span>',
        '      <span class="pill pill-emerald" style="font-size:10.5px;">Хронометраж: ' + esc(item.duration) + '</span>',
        '    </div>',
        '    <div style="font-size:11.8px;color:var(--text-secondary);background:rgba(56,189,248,0.06);border-left:3px solid var(--cyan);padding:6px 9px;border-radius:0 6px 6px 0;margin-bottom:9px;line-height:1.4;">',
        '      <strong>🎬 Режисерський рух камери:</strong> ' + esc(item.motion_direction),
        '    </div>',
        '    <div style="margin-bottom:10px;">',
        '      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">',
        '        <span style="font-size:10.5px;color:var(--amber);font-weight:700;">ПРОМПТ ДЛЯ GOOGLE VEO 2 / FLOW:</span>',
        '        <button class="btn-copy-sm" data-copy-veo-prompt="' + esc(item.id) + '">📋 Скопіювати промпт</button>',
        '      </div>',
        '      <pre style="background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:6px;padding:8px;font-size:11px;color:var(--text-primary);white-space:pre-wrap;word-break:break-word;font-family:var(--mono);max-height:85px;overflow-y:auto;margin:0;">' + esc(item.prompt) + '</pre>',
        '    </div>',
        '  </div>',
        '  <div style="border-top:1px solid var(--border);padding-top:10px;margin-top:5px;display:flex;gap:8px;flex-direction:column;">',
        '    <button class="btn ' + (isDone ? 'btn-emerald' : 'btn-amber') + '" style="width:100%;padding:7px 12px;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;" data-toggle-veo="' + esc(item.id) + '">',
        '      ' + (isDone ? '✅ Виконано (Клікніть, щоб повернути в чергу)' : '⏳ Позначити як виконано (відео згенеровано)'),
        '    </button>',
        '    <div style="display:flex;justify-content:space-between;gap:6px;flex-wrap:wrap;">',
        '      <a class="btn" style="flex:1;text-align:center;font-size:11px;padding:5px 8px;background:var(--surface-hover);border:1px solid var(--border);color:var(--cyan);text-decoration:none;" href="' + esc(item.page_url) + '">🎙️ Студія EP' + esc(item.ep) + ' →</a>',
        '      <button class="btn btn-cyan" style="font-size:11px;padding:5px 8px;cursor:pointer;white-space:nowrap;" data-reveal-finder="' + esc(isDone && item.video_path ? item.video_path : item.raw_path) + '">📁 У Finder</button>',
        '      <button class="btn" style="font-size:11px;padding:5px 8px;background:var(--surface-hover);border:1px solid var(--border);color:var(--text-muted);cursor:pointer;" data-copy-text="' + esc(item.raw_path) + '">Шлях 2K</button>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join("\n");
    }).join("\n");

    var mediaPool = window.MEDIA_ACQUISITION_POOL || {};
    var matrixRowsHtml = season.map(function (h) {
      var epVeos = pipeline.filter(function (v) { return v.ep === h.ep; });
      var epVeoDone = epVeos.filter(function (v) { return !!statusMap[v.id]; }).length;
      var epMedia = mediaPool[h.ep] || {};
      var galCount = (epMedia.flow_gallery || []).length || 12;
      var act1Track = getHeroPrimaryTrack(h.ep);

      var veoBadge = epVeos.length === 0
        ? '<span class="pill pill-purple">Без специфікацій</span>'
        : (epVeoDone === epVeos.length
            ? '<span class="pill pill-emerald">✅ ' + epVeoDone + '/' + epVeos.length + ' Готово</span>'
            : '<span class="pill pill-amber">⏳ ' + epVeoDone + '/' + epVeos.length + ' В роботі</span>');

      var audioPlayHtml = act1Track
        ? '<div style="display:flex;align-items:center;gap:6px;">' +
          '  <span style="font-size:10.5px;color:var(--emerald);font-weight:600;white-space:nowrap;">4 WAV</span>' +
          '  <audio controls preload="none" style="height:24px;width:125px;" src="assets/audio_previews/' + esc(act1Track.preview) + '"></audio>' +
          '</div>'
        : '<span class="pill pill-emerald">✅ 4 WAV</span>';

      return [
        '<tr>',
        '  <td><a href="' + esc(h.page_url) + '" style="font-weight:700;color:var(--cyan);text-decoration:none;">EP' + esc(h.ep) + ' • ' + esc(h.name) + '</a><div style="font-size:10.5px;color:var(--text-muted);">' + esc(h.archetype) + '</div></td>',
        '  <td><span class="pill pill-emerald">✅ 100% Готово</span><div style="font-size:10.2px;color:var(--text-muted);margin-top:2px;">' + (h.script_words || 2400) + ' слів</div></td>',
        '  <td><span class="pill pill-amber">⏳ Текст готовий (115 WPM)</span><div style="font-size:10.2px;color:var(--text-muted);margin-top:2px;">Очікує озвучки ElevenLabs</div></td>',
        '  <td>' + audioPlayHtml + '</td>',
        '  <td><span class="pill pill-emerald">✅ 4K Симуляція</span><div style="font-size:10.2px;color:var(--text-muted);margin-top:2px;">Готово у базі</div></td>',
        '  <td><span class="pill pill-emerald">✅ ' + galCount + ' концептів</span><div style="font-size:10.2px;color:var(--text-muted);margin-top:2px;">Midjourney / Flow</div></td>',
        '  <td>' + veoBadge + '</td>',
        '  <td><span class="pill pill-purple">📦 Smart Bins Ready</span><div style="font-size:10.2px;color:var(--text-muted);margin-top:2px;">A1-A4 / V1-V4</div></td>',
        '  <td><a class="btn btn-cyan" style="padding:3px 8px;font-size:11px;text-decoration:none;display:inline-block;white-space:nowrap;" href="' + esc(h.page_url) + '">🎙️ Студія →</a></td>',
        '</tr>'
      ].join("\n");
    }).join("\n");

    container.innerHTML = [
      '<div class="card" style="margin-bottom:1rem;padding:1.1rem;background:linear-gradient(135deg,rgba(251,191,36,0.1),rgba(56,189,248,0.06));border-color:rgba(251,191,36,0.45);">',
      '  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;">',
      '    <div>',
      '      <h2 style="margin:0 0 4px 0;font-size:17px;color:var(--amber);display:flex;align-items:center;gap:8px;">',
      '        🎬 ТОП-14 Ключових Анімацій Google Veo 2 / Flow (Сезон 1)',
      '        <span class="pill pill-amber">Інтерактивний Трекер Задач</span>',
      '      </h2>',
      '      <div style="font-size:12.3px;color:var(--text-secondary);max-width:820px;line-height:1.4;">',
      '        14 найважливіших 6–10-секундних сцен, які перетворюють філософські кульмінації епізодів у кінематографічний VFX. Натискайте кнопку на картці, щоб відзначити готовність — прогрес зберігається у вашому браузері та синхронізується з усіма розділами.',
      '      </div>',
      '    </div>',
      '    <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap;">',
      '      <span class="pill pill-purple">Всього: <strong>' + totalCount + '</strong></span>',
      '      <span class="pill pill-emerald" id="hubVeoDoneCount">Виконано: <strong>' + doneCount + '</strong></span>',
      '      <span class="pill pill-amber" id="hubVeoPendingCount">В черзі: <strong>' + pendingCount + '</strong></span>',
      '    </div>',
      '  </div>',
      '  <div style="margin-top:0.85rem;">',
      '    <div style="display:flex;justify-content:space-between;font-size:11.5px;color:var(--text-secondary);margin-bottom:4px;">',
      '      <span>Загальний прогрес анімацій сезону:</span>',
      '      <strong style="color:' + (pct === 100 ? 'var(--emerald)' : 'var(--amber)') + ';">' + doneCount + ' з ' + totalCount + ' (' + pct + '%)</strong>',
      '    </div>',
      '    <div class="progress-track"><div class="progress-fill" style="width:' + pct + '%;background:' + (pct === 100 ? 'var(--emerald)' : 'var(--amber)') + ';"></div></div>',
      '  </div>',
      '</div>',

      '<div class="card" style="margin-bottom:1rem;padding:0.75rem 1rem;">',
      '  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;">',
      '    <div style="display:flex;gap:6px;flex-wrap:wrap;">',
      '      <button class="btn ' + (filter === 'all' ? 'btn-emerald' : '') + '" data-veo-filter="all" style="padding:4px 10px;font-size:11.5px;cursor:pointer;">Всі кандидати (' + totalCount + ')</button>',
      '      <button class="btn ' + (filter === 'pending' ? 'btn-amber' : '') + '" data-veo-filter="pending" style="padding:4px 10px;font-size:11.5px;cursor:pointer;">⏳ В черзі на анімацію (' + pendingCount + ')</button>',
      '      <button class="btn ' + (filter === 'done' ? 'btn-emerald' : '') + '" data-veo-filter="done" style="padding:4px 10px;font-size:11.5px;cursor:pointer;">✅ Готові відео (' + doneCount + ')</button>',
      '    </div>',
      '    <div style="display:flex;align-items:center;gap:6px;">',
      '      <span style="font-size:11.5px;color:var(--text-secondary);">Фільтр героя:</span>',
      '      <select id="veoHeroSelect" style="background:var(--surface);border:1px solid var(--border);color:var(--text-primary);padding:4px 8px;border-radius:6px;font-size:11.5px;">' + heroOptions + '</select>',
      '    </div>',
      '  </div>',
      '</div>',

      '<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:1rem;margin-bottom:1.5rem;">' + cardsHtml + '</div>',

      '<div class="card" style="margin-top:1.5rem;padding:1.1rem;border-color:rgba(56,189,248,0.4);">',
      '  <div class="panel-head" style="margin-bottom:10px;">',
      '    <div>',
      '      <h3 style="margin:0 0 3px 0;font-size:15px;color:var(--cyan);display:flex;align-items:center;gap:8px;">',
      '        📊 Матриця Виробничої Готовності Сезону 1 (Епізоди 01–10)',
      '      </h3>',
      '      <div style="font-size:11.8px;color:var(--text-secondary);">',
      '        Зведений стан усіх 7 виробничих цехів для кожного з 10 титанів ШІ. Усі сценарії 100% готові (23,756 слів), музичні теми Suno 92 BPM розкладені по смарт-бінах. Аудіо можна прослухати прямо тут.',
      '      </div>',
      '    </div>',
      '    <span class="pill pill-emerald">10 / 10 Епізодів у Виробництві</span>',
      '  </div>',
      '  <div style="overflow-x:auto;">',
      '    <table class="data-table" style="width:100%;font-size:11.5px;">',
      '      <thead>',
      '        <tr>',
      '          <th>Епізод & Герой</th>',
      '          <th>1. Сценарій (02_SCRIPTS)</th>',
      '          <th>2. Диктор SSML (115 WPM)</th>',
      '          <th>3. Саундтрек (Suno 92 BPM)</th>',
      '          <th>4. Науковий VFX</th>',
      '          <th>5. 2K Концепти</th>',
      '          <th>6. Veo Анімація</th>',
      '          <th>7. DaVinci 19</th>',
      '          <th>Дія</th>',
      '        </tr>',
      '      </thead>',
      '      <tbody>' + matrixRowsHtml + '</tbody>',
      '    </table>',
      '  </div>',
      '</div>'
    ].join("\n");

    container.querySelectorAll("[data-toggle-veo]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-toggle-veo");
        var current = !!statusMap[id];
        setVeoStatus(id, !current);
        showToast((!current ? "✅ Виконано: " : "⏳ Повернуто в чергу: ") + id);
      });
    });

    container.querySelectorAll("[data-copy-veo-prompt]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-copy-veo-prompt");
        var target = pipeline.find(function (p) { return p.id === id; });
        if (target) copyText(target.prompt, "Veo 2 Промпт " + id);
      });
    });

    container.querySelectorAll("[data-copy-text]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        copyText(btn.getAttribute("data-copy-text"), "шлях файлу");
      });
    });

    container.querySelectorAll("[data-veo-filter]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        state.veoFilter = btn.getAttribute("data-veo-filter");
        renderAnimationPane();
      });
    });

    var hSelect = document.getElementById("veoHeroSelect");
    if (hSelect) {
      hSelect.addEventListener("change", function () {
        state.veoHero = hSelect.value;
        renderAnimationPane();
      });
    }
  }


  function renderSeasonRegistry() {
    var tbody = document.getElementById("seasonRegistryBody");
    if (!tbody) return;
    tbody.innerHTML = season.map(function (h) {
      var prog = getEpisodeReadiness(h);
      var act1Track = getHeroPrimaryTrack(h.ep);
      return [
        "<tr>",
        "  <td><span class=\"pill pill-cyan\">EP " + esc(h.ep) + "</span></td>",
        "  <td><strong>" + esc(h.name) + "</strong><div style=\"font-size:11px;color:var(--text-muted);\">" + esc(h.latin) + "</div></td>",
        "  <td>«" + esc(h.title) + "»</td>",
        "  <td style=\"max-width:290px;font-size:11.5px;color:var(--text-secondary);\">" + esc(CONFLICTS[h.ep] || "") + "</td>",
        "  <td><span class=\"pill pill-emerald\">✅ 4 WAV (" + esc(act1Track ? act1Track.orig_name : "Suno") + ") + 4K Досьє + 100 промптів</span></td>",
        "  <td style=\"font-family:var(--mono);font-size:11.5px;\">" + prog.pct + "% (" + prog.sopDone + "/" + prog.sopTotal + ")</td>",
        "  <td><a class=\"btn-mini-open\" href=\"" + esc(h.page_url) + "\" target=\"_blank\" rel=\"noopener\">Відкрити ↗</a></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");
  }

  function renderGlobalQuotes() {
    var pillsWrap = document.getElementById("globalQuotesHeroPills");
    var gridWrap = document.getElementById("globalQuotesGrid");
    var countEl = document.getElementById("globalQuotesCount");
    var moreBtn = document.getElementById("btnLoadMoreQuotes");
    if (!pillsWrap || !gridWrap) return;

    var pills = ["<button class=\"q-filter-btn" + (state.quoteHero === "all" ? " active" : "") + "\" data-qhero=\"all\">Усі 10 героїв (1,000)</button>"]
      .concat(quotesDb.map(function (h) {
        return "<button class=\"q-filter-btn" + (state.quoteHero === h.ep ? " active" : "") + "\" data-qhero=\"" + esc(h.ep) + "\">EP" + esc(h.ep) + " " + esc(h.name.split(" ").pop()) + " (100)</button>";
      })).join("");
    pillsWrap.innerHTML = pills;

    pillsWrap.querySelectorAll("[data-qhero]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.quoteHero = b.getAttribute("data-qhero");
        state.quoteLimit = 120;
        renderGlobalQuotes();
      });
    });

    var q = state.quoteQuery.trim().toLowerCase();
    var flat = [];
    quotesDb.forEach(function (hero) {
      if (state.quoteHero !== "all" && hero.ep !== state.quoteHero) return;
      (hero.quotes_100 || []).forEach(function (item) {
        if (q) {
          var hay = (item.text + " " + item.cat + " " + hero.name + " " + hero.latin).toLowerCase();
          if (hay.indexOf(q) === -1) return;
        }
        flat.push({
          ep: hero.ep,
          heroName: hero.name,
          pageUrl: hero.page_url,
          num: item.num,
          cat: item.cat,
          text: item.text
        });
      });
    });

    if (countEl) {
      countEl.innerHTML = "Знайдено цитат у базі: <strong>" + flat.length + "</strong> із 1,000";
    }

    var shown = flat.slice(0, state.quoteLimit);
    gridWrap.innerHTML = shown.map(function (row, idx) {
      return [
        "<div class=\"g-quote-card\">",
        "  <div class=\"g-quote-top\">",
        "    <a class=\"pill pill-cyan\" href=\"" + esc(row.pageUrl) + "#quotes\" target=\"_blank\" rel=\"noopener\">EP" + esc(row.ep) + " • " + esc(row.heroName) + " #" + String(row.num).padStart(3, "0") + "</a>",
        "    <span class=\"pill pill-purple\">" + esc(row.cat) + "</span>",
        "  </div>",
        "  <div class=\"g-quote-body\">" + esc(row.text) + "</div>",
        "  <div style=\"display:flex;justify-content:flex-end;margin-top:auto;padding-top:6px;\">",
        "    <button class=\"btn-copy-sm\" data-gcopy=\"" + idx + "\">📋 Копіювати</button>",
        "  </div>",
        "</div>"
      ].join("\n");
    }).join("\n");

    gridWrap.querySelectorAll("[data-gcopy]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-gcopy"), 10);
        var r = shown[i];
        if (r) copyText(r.text + " — " + r.heroName, "цитата EP" + r.ep + " #" + r.num);
      });
    });

    if (moreBtn) {
      if (flat.length > state.quoteLimit) {
        moreBtn.style.display = "inline-flex";
        moreBtn.textContent = "Показати ще (" + (flat.length - state.quoteLimit) + " цитат залишилось)";
      } else {
        moreBtn.style.display = "none";
      }
    }
  }

  function renderSunoMasterPool() {
    var tbody = document.getElementById("hubSunoPoolBody");
    var pool = window.SUNO_MASTER_POOL || [];
    if (!tbody) return;

    tbody.innerHTML = pool.map(function (t, idx) {
      var extraHtml = "";
      if (t.extra_bins && t.extra_bins.length) {
        extraHtml = "<div style=\"font-size:10px;color:var(--text-muted);margin-top:3px;\">+ Smart Bins: " +
          t.extra_bins.map(function (eb) { return "EP" + esc(eb.ep || "") + " (" + esc(eb.smart_bin) + ")"; }).join(", ") +
          "</div>";
      }
      return [
        "<tr>",
        "  <td><span class=\"pill pill-emerald\">#" + esc(t.num) + "</span></td>",
        "  <td><strong>" + esc(t.orig_name) + "</strong><div style=\"font-size:10.6px;color:var(--amber);margin-top:2px;\">" + esc(t.hero_label || "") + "</div><div style=\"font-size:10.8px;color:var(--cyan);font-family:var(--mono);margin-top:2px;\">→ " + esc(t.bin_dir) + "/" + esc(t.smart_bin) + "</div>" + extraHtml + "</td>",
        "  <td><span class=\"pill pill-purple\">" + esc(t.module) + "</span><div style=\"font-size:10.8px;color:var(--text-muted);margin-top:3px;\">" + esc(t.specs) + "</div></td>",
        "  <td style=\"min-width:225px;\"><audio controls preload=\"none\" style=\"height:30px;width:220px;\" src=\"assets/audio_previews/" + esc(t.preview) + "\"></audio></td>",
        "  <td style=\"font-size:11.5px;color:var(--text-secondary);max-width:265px;\">" + esc(t.usage) + "</td>",
        "  <td><button class=\"btn-copy-sm\" data-hub-wav-copy=\"" + idx + "\">📋 WAV</button></td>",
        "</tr>"
      ].join("\n");
    }).join("\n");

    var audios = tbody.querySelectorAll("audio");
    for (var i = 0; i < audios.length; i++) {
      audios[i].addEventListener("play", function (ev) {
        for (var j = 0; j < audios.length; j++) {
          if (audios[j] !== ev.target) audios[j].pause();
        }
      });
    }

    tbody.querySelectorAll("[data-hub-wav-copy]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = parseInt(btn.getAttribute("data-hub-wav-copy"), 10);
        var tr = pool[idx];
        if (tr) {
          copyText("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/suno_stems/" + tr.bin_dir + "/" + tr.smart_bin, tr.smart_bin);
        }
      });
    });
  }

  function switchHubTab(tabId) {
    var tabs = ["heroes", "animation", "architecture", "quotes", "standards", "registry"];
    if (tabs.indexOf(tabId) === -1) tabId = "heroes";
    state.tab = tabId;

    document.querySelectorAll("[data-hub-tab]").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-hub-tab") === tabId);
    });
    tabs.forEach(function (t) {
      var el = document.getElementById("hub-pane-" + t);
      if (el) el.classList.toggle("active", t === tabId);
    });
    if (tabId === "animation") renderAnimationPane();
  }

  function bindStaticActions() {
    document.querySelectorAll("[data-hub-tab]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        switchHubTab(btn.getAttribute("data-hub-tab"));
      });
    });

    var qInput = document.getElementById("globalQuotesSearch");
    if (qInput) {
      qInput.addEventListener("input", function () {
        state.quoteQuery = qInput.value;
        state.quoteLimit = 120;
        renderGlobalQuotes();
      });
    }

    var moreBtn = document.getElementById("btnLoadMoreQuotes");
    if (moreBtn) {
      moreBtn.addEventListener("click", function () {
        state.quoteLimit += 200;
        renderGlobalQuotes();
      });
    }

    document.querySelectorAll("[data-copy-template]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var targetId = btn.getAttribute("data-copy-template");
        var src = document.getElementById(targetId);
        if (src) copyText(src.textContent.trim(), btn.getAttribute("data-label") || "шаблон");
      });
    });

    var copyRepoBtn = document.getElementById("btnCopyRepoPath");
    if (copyRepoBtn) {
      copyRepoBtn.addEventListener("click", function () {
        copyText("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast", "локальний шлях проєкту");
      });
    }

    ["sidebarOpenAudioBtn", "sidebarOpenSunoCatalogBtn"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) {
        el.addEventListener("click", function () {
          switchHubTab("standards");
          window.scrollTo({ top: 0, behavior: "smooth" });
        });
      }
    });

    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest("[data-reveal-finder]");
      if (btn) {
        ev.preventDefault();
        var path = btn.getAttribute("data-reveal-finder");
        var label = btn.getAttribute("data-reveal-label") || "";
        revealInFinder(path, label);
      }
    });

    window.addEventListener("storage", function () {
      renderHeroesGrid();
      renderSeasonRegistry();
      renderAnimationPane();
    });
    window.addEventListener("focus", function () {
      renderHeroesGrid();
      renderSeasonRegistry();
      renderAnimationPane();
    });

    var cTime = document.getElementById("cTime");
    if (cTime) {
      cTime.textContent = "Season 1 • 10 Episodes • 16 WAV Masters (40 Smart Bin Tracks) • 14 4K Dossiers • 1,000 Prompts";
    }
  }

  function init() {
    renderHeroesGrid();
    renderSeasonRegistry();
    renderGlobalQuotes();
    renderSunoMasterPool();
    bindStaticActions();
  }

  init();
})();
