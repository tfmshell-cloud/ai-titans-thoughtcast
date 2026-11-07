# DaVinci Resolve Studio — Специфікація проєкту для Епізоду 01
**Назва таймлайну:** `AI_TITANS_EP01_ALTMAN_MASTER`  
**Роздільна здатність:** 3840 x 2160 (4K UHD) або DCI 4K Scope (2.39:1)  
**Частота кадрів:** 24.000 fps  
**Колірний простір проєкту:** DaVinci YRGB Color Managed (Color Science: DaVinci Wide Gamut / Intermediate)

---

## 1. Архітектура нодного дерева на Color Page

```text
[Source Renders / Archives] 
   └── [Node 1: Exposure & Contrast] 
         └── [Node 2: Color Temp & Balance] 
               └── [Node 3: Film Look Kodak 2383 D60] 
                     └── [Node 4: OFX 35mm Film Grain] 
                           └── [Rec.709 Output]
```

- **Нода 1 (Exposure & Contrast Balancing):**
  - Баланс чорної точки на рівні 0.02.
  - М'який логарифмічний спад у тінях (toe rolloff) для уникнення цифрового кліппінгу.
- **Нода 2 (Color Temperature & Gamut Tint):**
  - Легкий ціановий відтінок у тінях (тіні холодного графіту).
  - Теплі нейтральні хайлайти для органічного тону шкіри та ламп розжарювання.
- **Нода 3 (CST / LUT):**
  - Вбудований плівковий профіль DaVinci: `Film Looks -> Rec.709 Kodak 2383 D60`.
- **Нода 4 (OFX Film Grain Engine):**
  - Профіль: `35mm film grain`.
  - Grain Size: `1.1`.
  - Grain Strength: `0.35`.
  - Призначення: безшовне об'єднання згенерованих відеофрагментів (Veo 2 / Flow) та архівних фотоматеріалів в єдине плівкове полотно.

---

## 2. Fairlight Audio Routing
- `A1 (VO)` &rarr; `Main 1` + `Send to Sidechain 1`.
- `A2 (Music)` &rarr; `Main 1` (Ducking -3.2 dB driven by `Sidechain 1`).
- `A3 (SFX)` &rarr; `Main 1`.
- `Main 1 (Stereo Bus)` &rarr; True Peak Limiter -1.0 dBFS, Integrated LUFS target: -14.0 LUFS (YouTube Standard).
