#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/08_AUTOMATION/scripts")
from generate_50_scenes_hassabis import SCENES

HTML_PATHS = [
    "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/50_scenes_hassabis.html",
    "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/docs/50_scenes_hassabis.html"
]

def get_category(num_int):
    if num_int <= 10:
        return ("childhood", "👶 Дитинство & Батько", "purple")
    elif num_int <= 20:
        return ("chess", "♟️ Шаховий вундеркінд", "amber")
    elif num_int <= 26:
        return ("gaming", "🕹️ Bullfrog & Theme Park", "cyan")
    elif num_int <= 32:
        return ("cambridge", "🎓 Кембридж & Elixir", "emerald")
    elif num_int <= 36:
        return ("neuro", "🧠 Нейронаука & fMRI", "purple")
    elif num_int <= 40:
        return ("deepmind", "⚡ DeepMind & Atari", "cyan")
    elif num_int <= 44:
        return ("seoul", "🏯 Сеул & Хід 37", "amber")
    else:
        return ("nobel", "🧬 AlphaFold & Нобель", "rose")

def generate_html():
    cards_html = ""
    for s in SCENES:
        n_int = int(s["num"])
        cat_key, cat_label, cat_color = get_category(n_int)
        cards_html += f"""
        <article class="scene-card" data-cat="{cat_key}" id="scene-{s['num']}">
          <div class="card-header">
            <div class="meta-row">
              <span class="num-badge">#{s['num']}</span>
              <span class="badge badge-{cat_color}">{cat_label}</span>
              <span class="badge badge-period">⏱️ {s['period']}</span>
            </div>
            <h3 class="card-title">{s['title']}</h3>
          </div>
          
          <div class="card-body">
            <div class="narrative-box">
              <div class="box-title">📖 Драматичний сюжет & Історичний факт</div>
              <p class="box-text">{s['narrative']}</p>
            </div>

            <div class="visual-box">
              <div class="box-header-flex">
                <div class="box-title" style="color:var(--cyan);">🎬 Режисерська художньо-документальна візуалізація</div>
                <button class="copy-btn" onclick="copyScene('vis-{s['num']}', this)">📋 Копіювати візуал</button>
              </div>
              <p class="visual-text" id="vis-{s['num']}">{s['visual']}</p>
            </div>

            <div class="symbol-box">
              <span class="symbol-icon">💡</span>
              <div class="symbol-text"><strong>Символізм & Художній сенс:</strong> {s['symbol']}</div>
            </div>
          </div>
        </article>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>50 Біографічних Сюжетів: Деміс Гассабіс | Режисерський Візуальний Гід</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0b0f17;
      --surface: #111724;
      --surface-elevated: #161e2e;
      --surface-hover: #1c273c;
      --border: #1e293b;
      --border-subtle: #172132;
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --cyan: #38bdf8;
      --emerald: #34d399;
      --amber: #fbbf24;
      --purple: #c084fc;
      --rose: #f43f5e;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text-primary);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 5rem;
    }}

    /* Sticky Navigation */
    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 15, 23, 0.94);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 14px;
      color: var(--text-primary);
      text-decoration: none;
    }}
    .nav-brand span {{
      background: linear-gradient(135deg, var(--purple), var(--rose));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .nav-actions {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn {{
      padding: 0.45rem 0.9rem;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .btn-outline {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-secondary);
    }}
    .btn-outline:hover {{
      background: var(--surface-hover);
      color: var(--text-primary);
    }}
    .btn-purple {{
      background: rgba(192, 132, 252, 0.15);
      border: 1px solid rgba(192, 132, 252, 0.45);
      color: var(--purple);
    }}

    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: radial-gradient(circle at top right, rgba(192, 132, 252, 0.15), transparent 45%),
                  radial-gradient(circle at bottom left, rgba(244, 63, 94, 0.1), transparent 45%),
                  var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2.5rem 2rem;
      margin-bottom: 2rem;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      background: rgba(192, 132, 252, 0.16);
      border: 1px solid rgba(192, 132, 252, 0.45);
      color: var(--purple);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 28px;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 0.75rem;
      background: linear-gradient(135deg, #ffffff 40%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      font-size: 15px;
      color: var(--text-secondary);
      max-width: 950px;
      margin-bottom: 1.5rem;
    }}

    /* Filter Bar */
    .filter-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}
    .filter-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .filter-pill {{
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .filter-pill:hover {{
      background: var(--surface-hover);
      color: var(--text-primary);
    }}
    .filter-pill.active {{
      background: var(--purple);
      color: #0b0f17;
      border-color: var(--purple);
      font-weight: 700;
    }}
    .search-input {{
      padding: 0.45rem 1rem;
      border-radius: 8px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-primary);
      font-size: 13px;
      width: 280px;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--purple);
    }}

    /* Cards Grid */
    .cards-grid {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}
    .scene-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      transition: all 0.2s ease;
    }}
    .scene-card:hover {{
      border-color: rgba(192, 132, 252, 0.4);
    }}
    .card-header {{
      padding: 1.25rem 1.5rem 0.85rem;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .meta-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 0.5rem;
      flex-wrap: wrap;
    }}
    .num-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--purple);
      background: rgba(192, 132, 252, 0.12);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }}
    .badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 999px;
    }}
    .badge-purple {{ background: rgba(192, 132, 252, 0.12); color: var(--purple); border: 1px solid rgba(192, 132, 252, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.12); color: var(--amber); border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.12); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.12); color: var(--emerald); border: 1px solid rgba(52, 211, 153, 0.3); }}
    .badge-rose {{ background: rgba(244, 63, 94, 0.12); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.3); }}
    .badge-period {{ font-family: var(--font-mono); background: var(--surface-elevated); color: var(--text-muted); border: 1px solid var(--border-subtle); }}

    .card-title {{
      font-size: 18px;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .card-body {{
      padding: 1.25rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}
    .narrative-box {{
      background: var(--surface-elevated);
      border-radius: 8px;
      padding: 0.85rem 1rem;
      border-left: 3px solid var(--text-muted);
    }}
    .box-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 0.35rem;
    }}
    .box-text {{
      font-size: 13.5px;
      color: var(--text-secondary);
      line-height: 1.55;
    }}

    .visual-box {{
      background: #080c14;
      border: 1px solid var(--border-subtle);
      border-left: 3px solid var(--cyan);
      border-radius: 8px;
      padding: 1rem;
    }}
    .box-header-flex {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
      gap: 8px;
    }}
    .visual-text {{
      font-size: 13.5px;
      color: #e2e8f0;
      line-height: 1.6;
    }}

    .symbol-box {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      background: rgba(192, 132, 252, 0.08);
      border: 1px solid rgba(192, 132, 252, 0.2);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-size: 13px;
      color: #cbd5e1;
    }}
    .symbol-icon {{
      font-size: 16px;
      line-height: 1;
    }}

    .copy-btn {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      font-size: 11px;
      font-weight: 600;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .copy-btn:hover {{
      background: var(--purple);
      color: #0b0f17;
      border-color: var(--purple);
    }}

    .toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--purple);
      color: #0b0f17;
      font-weight: 700;
      font-size: 13px;
      padding: 0.75rem 1.25rem;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      z-index: 1000;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.25s ease;
      pointer-events: none;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Bar -->
  <nav class="top-nav">
    <a href="../index.html" class="nav-brand">
      <span>AI Titans</span> Thoughtcast Director Hub
    </a>
    <div class="nav-actions">
      <a href="index.html" class="btn btn-outline">← Головний Дашборд</a>
      <a href="cinematic_innovations_ep03.html" class="btn btn-outline">♟️ 30 Тріад Еп. 03</a>
      <a href="50_scenes_hassabis.html" class="btn btn-purple">🎬 50 Біографічних Сюжетів</a>
      <a href="episodes/ep03_hassabis.html" class="btn btn-outline">🎙️ Студія Еп. 03</a>
    </div>
  </nav>

  <main class="container">
    <section class="hero-banner">
      <span class="hero-badge">🎬 50 Режисерських Візуалізацій • Деміс Гассабіс</span>
      <h1 class="hero-title">50 Біографічних Сюжетів: Від Батьківської Майстерні до Нобелівського Олімпу</h1>
      <p class="hero-desc">
        Повний авторський каталог 50 коротких сюжетів із життя Деміса Гассабіса для художньо-документального втілення. Кожен сюжет містить точний історичний факт, детальну режисерську візуалізацію (світло, камера, фактури, анімація) та глибинний філософський символізм.
      </p>
    </section>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <div class="filter-pills">
        <button class="filter-pill active" data-filter="all">Всі 50 сюжетів</button>
        <button class="filter-pill" data-filter="childhood">👶 Дитинство & Батько (1–10)</button>
        <button class="filter-pill" data-filter="chess">♟️ Шаховий вундеркінд (11–20)</button>
        <button class="filter-pill" data-filter="gaming">🕹️ Bullfrog & Theme Park (21–26)</button>
        <button class="filter-pill" data-filter="cambridge">🎓 Кембридж & Elixir (27–32)</button>
        <button class="filter-pill" data-filter="neuro">🧠 Нейронаука & fMRI (33–36)</button>
        <button class="filter-pill" data-filter="deepmind">⚡ DeepMind & Atari (37–40)</button>
        <button class="filter-pill" data-filter="seoul">🏯 Сеул & Хід 37 (41–44)</button>
        <button class="filter-pill" data-filter="nobel">🧬 AlphaFold & Нобель (45–50)</button>
      </div>
      <input type="text" id="searchInput" class="search-input" placeholder="Пошук по 50 сюжетах (напр. батько, тесля, стружка, Spectrum)...">
    </div>

    <!-- Cards Grid -->
    <div class="cards-grid" id="cardsGrid">
      {cards_html}
    </div>
  </main>

  <div class="toast" id="toast">✓ Скопійовано!</div>

  <script>
    function copyScene(elemId, btn) {{
      var text = document.getElementById(elemId).innerText;
      navigator.clipboard.writeText(text).then(function() {{
        showToast("✓ Візуальний опис скопійовано!");
        var orig = btn.innerText;
        btn.innerText = "✓ Скопійовано!";
        btn.style.background = "#c084fc";
        btn.style.color = "#000";
        setTimeout(function() {{
          btn.innerText = orig;
          btn.style.background = "";
          btn.style.color = "";
        }}, 2000);
      }});
    }}

    function showToast(msg) {{
      var t = document.getElementById("toast");
      t.innerText = msg;
      t.classList.add("show");
      setTimeout(function() {{ t.classList.remove("show"); }}, 2500);
    }}

    var pills = document.querySelectorAll(".filter-pill");
    pills.forEach(function(pill) {{
      pill.addEventListener("click", function() {{
        pills.forEach(function(p) {{ p.classList.remove("active"); }});
        pill.classList.add("active");
        var cat = pill.getAttribute("data-filter");
        filterCards(cat, document.getElementById("searchInput").value);
      }});
    }});

    document.getElementById("searchInput").addEventListener("input", function(e) {{
      var activePill = document.querySelector(".filter-pill.active");
      var cat = activePill ? activePill.getAttribute("data-filter") : "all";
      filterCards(cat, e.target.value);
    }});

    function filterCards(cat, searchStr) {{
      var q = searchStr.toLowerCase().trim();
      var cards = document.querySelectorAll(".scene-card");
      cards.forEach(function(card) {{
        var cardCat = card.getAttribute("data-cat");
        var text = card.innerText.toLowerCase();
        var matchCat = (cat === "all" || cardCat === cat);
        var matchSearch = (!q || text.indexOf(q) !== -1);
        if (matchCat && matchSearch) {{
          card.style.display = "";
        }} else {{
          card.style.display = "none";
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    for p in HTML_PATHS:
        with open(p, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"✓ Generated {p} ({len(full_html)} bytes)")

if __name__ == "__main__":
    generate_html()
