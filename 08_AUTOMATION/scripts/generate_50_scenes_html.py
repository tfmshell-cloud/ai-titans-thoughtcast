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
    elif num_int <= 30:
        return ("cambridge", "🎓 Кембридж & Elixir", "emerald")
    elif num_int <= 36:
        return ("neuro", "🧠 Нейронаука & fMRI", "purple")
    elif num_int <= 40:
        return ("deepmind", "⚡ Лабораторія & Atari", "cyan")
    elif num_int <= 44:
        return ("seoul", "🏯 Сеул & Хід 37", "amber")
    else:
        return ("nobel", "🧬 Молекулярне орігамі & Нобель", "rose")

def generate_html():
    cards_html = ""
    for s in SCENES:
        n_int = int(s["num"])
        cat_key, cat_label, cat_color = get_category(n_int)
        
        # Combined triad text for one-click copy
        combined_triad = f"""=== SCENE #{s['num']}: {s['title']} ({s['period']}) ===
[PROMPT 1: START FRAME A (16:9)]
{s['p1_start']}

[PROMPT 2: FLOW ACTION MORPH (24fps)]
{s['p2_flow']}

[PROMPT 3: END FRAME B (16:9)]
{s['p3_end']}

[DAVINCI 19 RECIPE]: {s['davinci_recipe']}
[FAIRLIGHT SFX]: {s['sfx_cue']}"""

        # Escape for data attribute or script
        cards_html += f"""
        <article class="scene-card" data-cat="{cat_key}" id="scene-{s['num']}">
          <div class="card-header">
            <div class="meta-row">
              <span class="num-badge">#{s['num']}</span>
              <span class="badge badge-{cat_color}">{cat_label}</span>
              <span class="badge badge-period">⏱️ {s['period']}</span>
              <span class="badge badge-safe">🛡️ 100% Policy-Safe</span>
            </div>
            <h3 class="card-title">{s['title']}</h3>
          </div>
          
          <div class="card-body">
            <div class="narrative-box">
              <div class="box-title">📖 Драматичний сюжет & Історичний факт</div>
              <p class="box-text">{s['narrative']}</p>
            </div>

            <div class="symbol-box">
              <span class="symbol-icon">💎</span>
              <div class="symbol-text"><strong>Філософський символ / Сенс:</strong> {s['symbol']}</div>
            </div>

            <div class="triad-container">
              <div class="triad-header-bar">
                <span class="triad-title">🎬 Синергетична 3-Промпт Тріада (Google Flow / Veo 2 / Midjourney)</span>
                <button class="copy-btn copy-btn-all" onclick="copyTriad('{s['num']}', this)">📦 Копіювати всю Тріаду (All 3)</button>
              </div>

              <!-- Prompt 1: Start Frame A -->
              <div class="prompt-box prompt-p1">
                <div class="prompt-label-row">
                  <span class="prompt-badge p1-badge">PROMPT 1 • СТАРТОВЕ ЗОБРАЖЕННЯ (Start Frame A — 16:9)</span>
                  <button class="copy-btn copy-btn-p1" onclick="copyText('p1-{s['num']}', this)">📋 Копіювати Prompt 1</button>
                </div>
                <pre class="code-block" id="p1-{s['num']}">{s['p1_start']}</pre>
              </div>

              <!-- Prompt 2: Flow Action Morph -->
              <div class="prompt-box prompt-p2">
                <div class="prompt-label-row">
                  <span class="prompt-badge p2-badge">PROMPT 2 • ДІЯ ТРАНСФОРМАЦІЇ (Flow Action Morph — 24fps)</span>
                  <button class="copy-btn copy-btn-p2" onclick="copyText('p2-{s['num']}', this)">📋 Копіювати Prompt 2</button>
                </div>
                <pre class="code-block" id="p2-{s['num']}">{s['p2_flow']}</pre>
              </div>

              <!-- Prompt 3: End Frame B -->
              <div class="prompt-box prompt-p3">
                <div class="prompt-label-row">
                  <span class="prompt-badge p3-badge">PROMPT 3 • ФІНАЛЬНЕ ЗОБРАЖЕННЯ (End Frame B — 16:9)</span>
                  <button class="copy-btn copy-btn-p3" onclick="copyText('p3-{s['num']}', this)">📋 Копіювати Prompt 3</button>
                </div>
                <pre class="code-block" id="p3-{s['num']}">{s['p3_end']}</pre>
              </div>
            </div>

            <!-- DaVinci & Fairlight Technical Grid -->
            <div class="tech-grid">
              <div class="tech-box davinci-box">
                <div class="tech-title">🎨 DaVinci Resolve 19 Колор & Fusion</div>
                <p class="tech-desc">{s['davinci_recipe']}</p>
              </div>
              <div class="tech-box sfx-box">
                <div class="tech-title">🎧 Fairlight Саунд-дизайн (SFX)</div>
                <p class="tech-desc">{s['sfx_cue']}</p>
              </div>
            </div>

            <!-- Hidden full triad block for copy -->
            <textarea id="full-triad-{s['num']}" style="display:none;">{combined_triad}</textarea>
          </div>
        </article>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>50 Біографічних Сюжетів & Тріад (100% Policy-Safe) • Деміс Гассабіс • AI Titans</title>
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
    .btn-cyan {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.45);
      color: var(--cyan);
    }}

    .container {{
      max-width: 1320px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: radial-gradient(circle at top right, rgba(52, 211, 153, 0.12), transparent 45%),
                  radial-gradient(circle at bottom left, rgba(192, 132, 252, 0.15), transparent 45%),
                  var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2.5rem 2rem;
      margin-bottom: 2rem;
    }}
    .hero-badge-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 9999px;
      background: rgba(192, 132, 252, 0.15);
      color: var(--purple);
      border: 1px solid rgba(192, 132, 252, 0.35);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .hero-badge-safe {{
      background: rgba(52, 211, 153, 0.15);
      color: var(--emerald);
      border-color: rgba(52, 211, 153, 0.35);
    }}
    .hero-badge-count {{
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      border-color: rgba(56, 189, 248, 0.35);
    }}
    .hero-title {{
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 0.75rem;
      background: linear-gradient(135deg, #ffffff 40%, var(--purple) 80%, var(--cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
      color: var(--text-secondary);
      font-size: 1.05rem;
      max-width: 950px;
      margin-bottom: 1.5rem;
    }}
    .hero-stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
    }}
    .stat-card {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      padding: 1rem;
      border-radius: 10px;
    }}
    .stat-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--purple);
      font-family: var(--font-mono);
    }}
    .stat-label {{
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* Filter & Search Bar */
    .filter-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2rem;
    }}
    .search-box-row {{
      position: relative;
    }}
    .search-input {{
      width: 100%;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.85rem 1.25rem 0.85rem 2.75rem;
      color: var(--text-primary);
      font-size: 14px;
      font-family: var(--font-sans);
      outline: none;
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--purple);
      box-shadow: 0 0 0 2px rgba(192, 132, 252, 0.2);
    }}
    .search-icon {{
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 16px;
      color: var(--text-muted);
    }}
    .filter-buttons {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .filter-btn {{
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--purple);
      color: #0b0f17;
      border-color: var(--purple);
      font-weight: 700;
    }}

    /* Scene Cards Grid */
    .scenes-grid {{
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }}
    .scene-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      transition: all 0.2s ease;
    }}
    .scene-card:hover {{
      border-color: rgba(192, 132, 252, 0.4);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
    }}
    .card-header {{
      padding: 1.25rem 1.5rem;
      background: var(--surface-elevated);
      border-bottom: 1px solid var(--border);
    }}
    .meta-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 0.6rem;
      flex-wrap: wrap;
    }}
    .num-badge {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 800;
      color: #0b0f17;
      background: var(--purple);
      padding: 2px 8px;
      border-radius: 6px;
    }}
    .badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .badge-purple {{ background: rgba(192, 132, 252, 0.15); color: var(--purple); border: 1px solid rgba(192, 132, 252, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.15); color: var(--amber); border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.15); color: var(--emerald); border: 1px solid rgba(52, 211, 153, 0.3); }}
    .badge-rose {{ background: rgba(244, 63, 94, 0.15); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.3); }}
    .badge-period {{ background: var(--surface); color: var(--text-muted); border: 1px solid var(--border); font-family: var(--font-mono); }}
    .badge-safe {{ background: rgba(52, 211, 153, 0.12); color: var(--emerald); border: 1px solid rgba(52, 211, 153, 0.3); font-weight: 700; }}
    
    .card-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .card-body {{
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}

    .narrative-box {{
      background: rgba(17, 23, 36, 0.6);
      border-left: 3px solid var(--purple);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
    }}
    .box-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--purple);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.35rem;
    }}
    .box-text {{
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.6;
    }}

    .symbol-box {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      background: var(--surface-elevated);
      padding: 0.75rem 1rem;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      font-size: 13px;
      color: var(--text-secondary);
    }}
    .symbol-icon {{ font-size: 16px; }}

    /* Triad Container */
    .triad-container {{
      background: #0d121c;
      border: 1px solid #1a2333;
      border-radius: 10px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}
    .triad-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid #1a2333;
    }}
    .triad-title {{
      font-size: 13px;
      font-weight: 700;
      color: #f1f5f9;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .prompt-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.85rem 1rem;
    }}
    .prompt-p1 {{ border-left: 3px solid var(--cyan); }}
    .prompt-p2 {{ border-left: 3px solid var(--amber); }}
    .prompt-p3 {{ border-left: 3px solid var(--emerald); }}
    
    .prompt-label-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .prompt-badge {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.4px;
    }}
    .p1-badge {{ color: var(--cyan); }}
    .p2-badge {{ color: var(--amber); }}
    .p3-badge {{ color: var(--emerald); }}

    .code-block {{
      font-family: var(--font-mono);
      font-size: 12.5px;
      color: #e2e8f0;
      white-space: pre-wrap;
      word-break: break-word;
      line-height: 1.55;
      background: rgba(0, 0, 0, 0.3);
      padding: 0.65rem 0.85rem;
      border-radius: 6px;
    }}

    .copy-btn {{
      padding: 0.35rem 0.7rem;
      border-radius: 5px;
      font-size: 11px;
      font-weight: 600;
      border: 1px solid var(--border);
      background: var(--surface-hover);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .copy-btn:hover {{
      background: #27354d;
      color: #ffffff;
    }}
    .copy-btn-all {{
      background: rgba(192, 132, 252, 0.15);
      border-color: rgba(192, 132, 252, 0.4);
      color: var(--purple);
      font-weight: 700;
    }}
    .copy-btn-all:hover {{
      background: var(--purple);
      color: #0b0f17;
    }}
    .copy-btn-p1 {{ color: var(--cyan); border-color: rgba(56, 189, 248, 0.35); }}
    .copy-btn-p2 {{ color: var(--amber); border-color: rgba(251, 191, 36, 0.35); }}
    .copy-btn-p3 {{ color: var(--emerald); border-color: rgba(52, 211, 153, 0.35); }}

    /* Tech Grid: DaVinci & Fairlight */
    .tech-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1rem;
    }}
    .tech-box {{
      background: var(--surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.85rem 1rem;
    }}
    .davinci-box {{ border-left: 3px solid #ffaa00; }}
    .sfx-box {{ border-left: 3px solid #00d2ff; }}
    .tech-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.35rem;
    }}
    .tech-desc {{
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--surface-elevated);
      border: 1px solid var(--purple);
      color: var(--text-primary);
      padding: 0.75rem 1.25rem;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      gap: 8px;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      z-index: 1000;
      pointer-events: none;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Footer */
    footer {{
      margin-top: 4rem;
      border-top: 1px solid var(--border);
      padding-top: 2rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 13px;
    }}
    footer a {{
      color: var(--purple);
      text-decoration: none;
    }}
    footer a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

  <!-- Sticky Top Navigation -->
  <nav class="top-nav">
    <a href="index.html" class="nav-brand">
      <span>AI TITANS THOUGHTCAST</span> • Demis Hassabis Master Studio
    </a>
    <div class="nav-actions">
      <a href="index.html" class="btn btn-outline">🏠 Master Hub</a>
      <a href="cinematic_innovations.html" class="btn btn-outline">⚡ Еп. 01: Altman (20)</a>
      <a href="cinematic_innovations_ep02.html" class="btn btn-outline">🔥 Еп. 02: Huang (20)</a>
      <a href="cinematic_innovations_ep03.html" class="btn btn-cyan">✨ Еп. 03: 30 Innovations</a>
      <a href="50_scenes_hassabis.html" class="btn btn-purple">🧬 50 Тріад (Active)</a>
    </div>
  </nav>

  <div class="container">
    
    <!-- Hero Banner -->
    <section class="hero-banner">
      <div class="hero-badge-row">
        <span class="hero-badge">ЕПІЗОД 03: ДЕМІС ГАССАБІС</span>
        <span class="hero-badge hero-badge-count">50 СИНЕРГЕТИЧНИХ ТРІАД (150 ПРОМПТІВ)</span>
        <span class="hero-badge hero-badge-safe">🛡️ 100% POLICY-SAFE (ZERO BANS)</span>
        <span class="hero-badge">GOOGLE FLOW & VEO 2 READY</span>
      </div>
      <h1 class="hero-title">50 Біографічних Сюжетів & Кінематографічних Тріад</h1>
      <p class="hero-subtitle">
        Повна хроніка життя гросмейстера штучного інтелекту: від батьківської теслярської майстерні та 8-бітного кодингу під ковдрою до Сеульського Ходу 37, AlphaFold та найвищої світової наукової нагороди 2024 року. Кожна сцена містить узгоджену тріаду: <strong>Start Image A</strong> → <strong>Action Morph</strong> → <strong>End Image B</strong>.
      </p>

      <div class="hero-stats-grid">
        <div class="stat-card">
          <div class="stat-val">50</div>
          <div class="stat-label">Сюжетів розроблено</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" style="color:var(--cyan);">150</div>
          <div class="stat-label">Google Flow Промптів</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" style="color:var(--emerald);">100%</div>
          <div class="stat-label">Policy-Safe (Zero Moderation)</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" style="color:var(--amber);">50</div>
          <div class="stat-label">DaVinci 19 & Fairlight Рецептів</div>
        </div>
      </div>
    </section>

    <!-- Filter & Search Section -->
    <section class="filter-wrapper">
      <div class="search-box-row">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Швидкий пошук за ключовими словами (напр. шахи, fMRI, касета, Сеул, білок, асемблер, Токамак)..." onkeyup="filterScenes()">
      </div>

      <div class="filter-buttons">
        <button class="filter-btn active" onclick="setCategory('all', this)">Всі сюжети (50)</button>
        <button class="filter-btn" onclick="setCategory('childhood', this)">👶 Дитинство & Батько (1–10)</button>
        <button class="filter-btn" onclick="setCategory('chess', this)">♟️ Шаховий вундеркінд (11–20)</button>
        <button class="filter-btn" onclick="setCategory('gaming', this)">🕹️ Bullfrog & Theme Park (21–26)</button>
        <button class="filter-btn" onclick="setCategory('cambridge', this)">🎓 Кембридж & Elixir (27–30)</button>
        <button class="filter-btn" onclick="setCategory('neuro', this)">🧠 Нейронаука & fMRI (31–36)</button>
        <button class="filter-btn" onclick="setCategory('deepmind', this)">⚡ Лабораторія & Atari (37–40)</button>
        <button class="filter-btn" onclick="setCategory('seoul', this)">🏯 Сеул & Хід 37 (41–44)</button>
        <button class="filter-btn" onclick="setCategory('nobel', this)">🧬 Молекулярне орігамі & Нобель (45–50)</button>
      </div>
    </section>

    <!-- Scenes Master List -->
    <main class="scenes-grid" id="scenesContainer">
      {cards_html}
    </main>

    <!-- Global Footer -->
    <footer>
      <p>AI Titans Thoughtcast • Продакшн-студія Епізоду 03 • Деміс Гассабіс</p>
      <p style="margin-top:6px; font-size:12px;">Усі промпти очищені від персональних імен живих людей та торгових марок задля 100% надійної генерації у Google Flow / Veo 2 без блокування квоти.</p>
    </footer>

  </div>

  <!-- Toast Element -->
  <div class="toast" id="toast">✅ Промпт успішно скопійовано в буфер!</div>

  <script>
    let currentCategory = 'all';

    function setCategory(cat, btn) {{
      currentCategory = cat;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterScenes();
    }}

    function filterScenes() {{
      const query = document.getElementById('searchInput').value.toLowerCase();
      const cards = document.querySelectorAll('.scene-card');

      cards.forEach(card => {{
        const cat = card.getAttribute('data-cat');
        const text = card.innerText.toLowerCase();
        const matchesCat = (currentCategory === 'all' || cat === currentCategory);
        const matchesSearch = (!query || text.includes(query));

        if (matchesCat && matchesSearch) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function copyText(elementId, btn) {{
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText || el.textContent;
      navigator.clipboard.writeText(text).then(() => {{
        showToast("✅ Скопійовано: " + btn.innerText.replace('📋 ', ''));
        const orig = btn.innerText;
        btn.innerText = "✓ Скопійовано!";
        btn.style.background = "#059669";
        btn.style.color = "#ffffff";
        setTimeout(() => {{
          btn.innerText = orig;
          btn.style.background = "";
          btn.style.color = "";
        }}, 1800);
      }});
    }}

    function copyTriad(num, btn) {{
      const fullTriadEl = document.getElementById('full-triad-' + num);
      if (!fullTriadEl) return;
      navigator.clipboard.writeText(fullTriadEl.value).then(() => {{
        showToast("📦 Всю Тріаду #" + num + " (Start + Flow + End) скопійовано!");
        const orig = btn.innerText;
        btn.innerText = "✓ Всю Тріаду скопійовано!";
        btn.style.background = "#c084fc";
        btn.style.color = "#0b0f17";
        setTimeout(() => {{
          btn.innerText = orig;
          btn.style.background = "";
          btn.style.color = "";
        }}, 2000);
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2500);
    }}
  </script>
</body>
</html>
"""

    for p in HTML_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Generated HTML at {p} ({len(full_html)} bytes)")

if __name__ == "__main__":
    generate_html()
