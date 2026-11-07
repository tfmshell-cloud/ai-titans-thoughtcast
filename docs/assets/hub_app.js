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
    sunoHeroFilter: "all"
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
      var dosCount = (epMedia.dossiers || []).length || 1;
      var archCount = (epMedia.archives || []).length || 1;

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
        "    <span>🎥 <strong>100</strong> промптів</span>",
        "    <span>🗂️ <strong>" + dosCount + "</strong> 4K досьє + <strong>" + archCount + "</strong> архів</span>",
        "    <span>🎵 <strong>" + prog.heroWavCount + "/4</strong> актів WAV</span>",
        "  </div>",

        "  <div class=\"hero-prog-row\">",
        "    <div class=\"hero-prog-label\"><span>Готовність випуску (" + prog.sopDone + "/" + prog.sopTotal + " SOP + 4 WAV)</span><strong>" + prog.pct + "%</strong></div>",
        "    <div class=\"hero-prog-bar\"><div class=\"hero-prog-fill\" style=\"width:" + prog.pct + "%\"></div></div>",
        "  </div>",

        "  <div class=\"hero-deep-links\" onclick=\"event.stopPropagation();\">",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#sop\" target=\"_blank\" rel=\"noopener\">🧭 Алгоритм</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#script\" target=\"_blank\" rel=\"noopener\">🎬 Сценарій</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#prompts\" target=\"_blank\" rel=\"noopener\">🎥 100 Промптів</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#audio\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(52,211,153,0.45);color:var(--emerald);\">🎵 4 WAV + Suno</a>",
        "    <a class=\"deep-chip\" href=\"" + esc(h.page_url) + "#media\" target=\"_blank\" rel=\"noopener\" style=\"border-color:rgba(251,191,36,0.45);color:var(--amber);\">🗂️ Досьє & Архіви</a>",
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
    var tabs = ["heroes", "architecture", "quotes", "standards", "registry"];
    if (tabs.indexOf(tabId) === -1) tabId = "heroes";
    state.tab = tabId;

    document.querySelectorAll("[data-hub-tab]").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-hub-tab") === tabId);
    });
    tabs.forEach(function (t) {
      var el = document.getElementById("hub-pane-" + t);
      if (el) el.classList.toggle("active", t === tabId);
    });
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

    window.addEventListener("storage", function () {
      renderHeroesGrid();
      renderSeasonRegistry();
    });
    window.addEventListener("focus", function () {
      renderHeroesGrid();
      renderSeasonRegistry();
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
