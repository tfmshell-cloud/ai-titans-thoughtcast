# Технічний аудіо-паспорт (Ep 01: Altman) — Fairlight & Suno Pro
**Проєкт:** Cinematic Thoughtcast: AI Titans  
**Хронометраж епізоду:** 20:30  
**Базовий темпоритм музики:** 92 BPM  
**Формат виводу:** 48 kHz / 24-bit WAV

---

## 1. Карта аудіотреків у DaVinci Resolve Fairlight

- **A1 (Голос диктора):**
  - **Компресор:** Швидка атака (5ms), реліз 80ms.
  - **Параметричний EQ:** High-pass фільтр нижче 75Hz, м'який підйом +1.5 dB на 3.5kHz для кришталевої артикуляції.
  - **Сенд:** `Sidechain Out 1`.
- **A2 (Музика Suno Pro 92 BPM):**
  - **Штатний компресор DaVinci:** Активовано `Sidechain Listen` від A1.
  - **Ducking:** -3.2 dB, Attack 40ms, Release 350ms.
- **A3 (SFX / Атмосфера):**
  - Клацання реле CRT-монітора (0:00, 20:00).
  - Саб-дропи 40Hz на точках зламу драматургії:
    - `0:45` (Шкільний бунт)
    - `9:30` (Реліз ChatGPT)
    - `13:45` (Бунт 730 співробітників)
  - Аналогове вінілове зерно.

---

## 2. Модульні промпти для генерації музики в Suno Pro

### Акт 1 (0:00 - 4:45) — «Theme 1: Introspection»
```text
Instrumental ambient trip-hop, 92 bpm, dusty vinyl texture, warm vintage Rhodes chords, deep analog sub bass, nostalgic clean electric guitar harmonics, quiet contemplative mood, cinematic documentary soundtrack, high fidelity.
```

### Акти 2 та 3 (4:45 - 15:30) — «Theme 2: Tension»
```text
Instrumental dark industrial downtempo, 92 bpm, aggressive muted sub-bass pulse, clockwork metallic percussion, tension analog modular synth arpeggios, distant dark saxophone drone with reverb, brooding psychological focus, cinematic film score.
```

### Акт 4 (15:30 - 20:30) — «Theme 3: Triumph»
```text
Instrumental majestic sci-fi trip-hop, 92 bpm, soaring analog brass synths, deep resonant bass pulse, emotional celestial choir pad, slow triumphant groove, sense of cosmic scale, IMAX resolution soundtrack.
```
