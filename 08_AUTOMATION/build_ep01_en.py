#!/usr/bin/env python3
"""
EP01 «Sam Altman: Anatomy of the Exponent» — англійська версія режисерського монтажу.

Береться той самий монтажний план, що й для української (build_ep01_acts.ACTS), і «перекладається в часі»:
  * кожен блок озвучки UA замінюється англійським дублем (03_AUDIO/voiceover/EP01_ALTMAN/EP01_VO_EN_NN_*.wav);
  * усередині блоку всі склейки, титри, SFX і наплави масштабуються пропорційно довжині англійського дубля
    (кадр стоїть на тій самій репліці), паузи між блоками зберігаються, початок блоку — на сітці 92 BPM;
  * мовна графіка (титри, назви актів, правила, картки-цитати, плашки) — англійські пари з make_ep01_en_graphics.py;
  * музика акту зводиться заново з даккінгом під англійський голос.

Запуск:
  python3 08_AUTOMATION/build_ep01_en.py            # мікси + FCPXML
  python3 08_AUTOMATION/build_ep01_en.py --resolve  # + імпорт у SEM: таймлайн EP01_FULL_EN_Claude_DirectorsCut
"""
import argparse
import bisect
import math
import os
import sys
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "scripts"))
import ep01_engine as E                 # noqa: E402
import build_ep01_acts as B             # noqa: E402
import ep01_resync as RS                # noqa: E402
from make_ep01_en_graphics import UA_TO_EN, CARDS   # noqa: E402

F = E.FPS
EN_DIR = os.path.join(E.BASE, "03_AUDIO", "voiceover", "EP01_ALTMAN")
TIMELINE = "EP01_FULL_EN_Claude_DirectorsCut"


def en_vo(n):
    f = next(x for x in sorted(os.listdir(EN_DIR)) if x.startswith(f"EP01_VO_EN_{n:02d}_") and x.endswith(".wav"))
    w = wave.open(os.path.join(EN_DIR, f))
    return f, w.getnframes() / w.getframerate()


def warp_act(act):
    """Повертає англійський акт і функцію перерахунку кадрів UA → EN."""
    items = sorted(act["vo"].items(), key=lambda kv: kv[1][1])
    ua, en = [0], [0]
    vo, prev_ua, prev_en = {}, 0, 0
    for n, (_, f0, secs) in items:
        gap = f0 - prev_ua
        start = prev_en + gap
        if abs(f0 / E.BAR_F - round(f0 / E.BAR_F)) < 0.02 and prev_en:   # UA-блок стоїть на такті — і EN теж
            q = int(round(round(start / E.BAR_F) * E.BAR_F))
            if q < prev_en + min(gap, 12):          # пауза не коротша за 0,5 с
                q = int(round((round(start / E.BAR_F) + 1) * E.BAR_F))
            start = q
        name, en_secs = en_vo(n)
        ua_len, en_len = int(secs * F), int(en_secs * F)
        ua += [f0, f0 + ua_len]
        en += [start, start + en_len]
        vo[n] = (name, start, en_secs)
        prev_ua, prev_en = f0 + ua_len, start + en_len
    end = prev_en + (act["end_f"] - prev_ua)
    ua.append(act["end_f"])
    en.append(end)

    def M(f):
        if f <= 0:
            return int(f)
        i = min(bisect.bisect_right(ua, f), len(ua) - 1)
        a0, a1, b0, b1 = ua[i - 1], ua[i], en[i - 1], en[i]
        return int(round(b0 + (f - a0) * (b1 - b0) / (a1 - a0))) if a1 > a0 else b0

    ua_starts = {f0: vo[n][1] for n, (_, f0, _) in items}

    def music_end(f1):
        """Обрив музики перед блоком — з тим самим відступом до голосу, що й в українській."""
        for s0, e0 in ua_starts.items():
            if 0 < s0 - f1 <= 48:
                return e0 - (s0 - f1)
        return M(f1)

    tr = lambda name: UA_TO_EN.get(name, name)
    v1 = [(M(f0), tr(n), si, db, note) for f0, n, si, db, note in act["v1"]]
    for i in range(1, len(v1)):                        # склейки строго по черзі
        if v1[i][0] <= v1[i - 1][0]:
            v1[i] = (v1[i - 1][0] + 1,) + v1[i][1:]
    # кадр не може тривати довше за своє джерело: пізніше починаємо, попередній кадр трохи довшає
    idx = E.index_files()
    diss = {M(c): h for c, h in (act.get("dissolves") or {}).items()}
    for i in range(1, len(v1)):
        f0, n, si, db, note = v1[i]
        f1 = v1[i + 1][0] if i + 1 < len(v1) else end
        if n.lower().endswith(E.STILL_EXT):
            continue
        ln = E.media_frames(E.find(idx, n) or "") or 10 ** 6
        avail = ln - int(round(si * F)) - 8                  # 8 кадрів запасу на наплав
        if f1 - f0 > avail:
            nf0 = f1 - avail
            if f0 in diss:
                diss[nf0] = diss.pop(f0)
            v1[i] = (nf0, n, si, db, note)
    out = dict(act, name=act["name"] + " EN", end_f=end, vo=vo, v1=v1,
               v2=[(M(f0), tr(n), M(f0 + d) - M(f0)) for f0, n, d in act.get("v2", [])],
               v3=[(M(f0), tr(n), (M(f0 + int(s * F)) - M(f0)) / F) for f0, n, s in act.get("v3", [])],
               sfx=[(M(f0), n, s, db) for f0, n, s, db in act.get("sfx", [])],
               music=[(n, si, M(f0), music_end(f1), fd) for n, si, f0, f1, fd in act["music"]],
               dissolves=diss,
               markers=[(M(f), c, nm, note) for f, c, nm, note in act.get("markers", []) if not nm.startswith("Д")]
               + [(f0, "Blue", f"EN{n:02d}", name) for n, (name, f0, s) in vo.items()])
    return out, M


# Правки лише англійського Акту III (рядок плану → новий файл, точка входу, звук)
ACT_III_EN = {
    12: ("Mouse_click_triggers_flash_42a0e76f_1080p.mp4", "EP01_CLAUDE_Mouse_Click_Laptop_part.mp4", 0.0),      # без чорної паузи
    15: ("EP06_CLIP_STILL_Sutskever_TAU_2023_6s.mp4",
         "EP06_VID_ARCH_13_ACT3_24FPS_Sutskever_Superalignment_Safety_NoPriors.mp4", 18.0),                     # лише Ілля
    30: ("Mouse_click_triggers_flash_42a0e76f_1080p.mp4", "EP01_CLAUDE_Mouse_Click_Badge_Walk_part.mp4", 0.0),  # одразу з бейджем
}


def act_iii_en_fixes(act):
    v1 = list(act["v1"])
    for i, (old, new, si) in ACT_III_EN.items():
        f0, name, _, _, note = v1[i]
        assert name == old, f"Акт III EN, план {i}: очікував {old}, а стоїть {name}"
        v1[i] = (f0, new, si, None, note + " [EN-правка]")
    act["v1"] = v1


# Правки лише англійського Акту II: Суцкевер з No Priors — вирізки без ведучої (0–3,75 с і 16,55–25,45 с джерела)
ACT_II_EN = {
    18: ("EP06_VID_ARCH_07_ACT2_24FPS_Sutskever_OpenAI_Origins_NoPriors.mp4", "EP01_CLAUDE_Ilya_NoPriors_A_only.mp4", 0.0),
    32: ("EP06_VID_ARCH_07_ACT2_24FPS_Sutskever_OpenAI_Origins_NoPriors.mp4", "EP01_CLAUDE_Ilya_NoPriors_B_only.mp4", 0.35),
}


def act_ii_en_fixes(act):
    v1 = list(act["v1"])
    for i, (old, new, si) in ACT_II_EN.items():
        f0, name, _, db, note = v1[i]
        assert name == old, f"Акт II EN, план {i}: очікував {old}, а стоїть {name}"
        v1[i] = (f0, new, si, db, note + " [EN-правка: лише Ілля]")
    act["v1"] = v1


def act_iii_en_music(act):
    """Блок 12 (звільнення): замість 42 с тиші — тиха напружена підкладка між двома треками."""
    mus = sorted(act["music"], key=lambda m: m[2])
    a, b = mus[0], mus[1]
    if b[2] - a[3] > 5 * F:
        act["music"] = mus[:1] + [("EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension.wav", 20.0, a[3], b[2], 1.5, 2.5)] + mus[1:]


def mix_path(key):
    return os.path.join(E.BASE, "03_AUDIO", "claude_mix", f"EP01_MUS_Act{key}_ducked_EN.wav")


def import_bins(paths):
    """Нові файли — у біни медіапулу за стандартом SEM (до імпорту таймлайну)."""
    sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules")
    import DaVinciResolveScript as bmd
    pm = bmd.scriptapp("Resolve").GetProjectManager()
    p = pm.GetCurrentProject()
    if p.GetName() != "SEM":
        p = pm.LoadProject("SEM")
    mp = p.GetMediaPool()
    root = mp.GetRootFolder()
    have = set()

    def walk(f):
        for c in f.GetClipList() or []:
            have.add(c.GetClipProperty("File Path"))
        for s in f.GetSubFolderList() or []:
            walk(s)
    walk(root)
    groups = {"10_VO_EN": [], "17_QUOTE_CARDS_EN": [], "28_EN_TITLES_GRAPHICS": [], "29_EN_MUSIC_MIX": []}
    for x in paths:
        if x in have:
            continue
        b = os.path.basename(x)
        if "_VO_EN_" in b:
            groups["10_VO_EN"].append(x)
        elif "_EN_CLIP_CARD_" in b or "_EN_CARD_" in b:
            groups["17_QUOTE_CARDS_EN"].append(x)
        elif b.endswith("_EN.png") or b.endswith("_EN.mov"):
            groups["28_EN_TITLES_GRAPHICS"].append(x)
        elif "_EN.wav" in b:
            groups["29_EN_MUSIC_MIX"].append(x)
    for bin_name, files in groups.items():
        if not files:
            continue
        b = next((s for s in root.GetSubFolderList() if s.GetName() == bin_name), None) or mp.AddSubFolder(root, bin_name)
        mp.SetCurrentFolder(b)
        mp.ImportMedia(files)
        print(f"  медіапул: {bin_name} +{len(files)}")
    mp.SetCurrentFolder(root)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--skip-mix", action="store_true")
    a_ = ap.parse_args()
    E.VO_LABEL = "VO_EN"
    idx = E.index_files()
    seq, off, bounds, markers = [], 0, [], []
    for key in ("I", "II", "III", "IV"):
        ua, _ = B.ACTS[key]
        act, M = warp_act(ua)
        RS.resync(act, lang="EN")              # усі акти
        if key == "II":
            act_ii_en_fixes(act)
        if key == "III":
            act_iii_en_fixes(act)
            act_iii_en_music(act)
        if False:
            pass              # склейки — за реальним англійським мовленням
        print(f"{act['name']}: {len(act['v1'])} планів, UA {ua['end_f'] / F:.1f} с → EN {act['end_f'] / F:.1f} с")
        if not (a_.skip_mix and os.path.exists(mix_path(key))):
            E.mix_music(act, idx, mix_path(key))
        seq.append((act, off, mix_path(key)))
        markers += [(f + off, c, n, note) for f, c, n, note in act["markers"]]
        if off:
            bounds.append(off)
        off += act["end_f"]
    idx = E.index_files()
    bridges = [(b - 4 * F, f"EP01_BRIDGE_Act{i + 1}_to_Act{i + 2}.wav", 8.0) for i, b in enumerate(bounds)]
    xml, probs, paths = E.build_fcpxml(seq, idx, TIMELINE, extra_dissolves={b: 16 for b in bounds},
                                       fade_in=12, fade_out=24, extra_sfx=bridges)
    p = os.path.join(E.BASE, "06_DAVINCI_PROJECTS", f"{TIMELINE}.fcpxml")
    open(p, "w", encoding="utf-8").write(xml)
    left_ua = [x for x in paths if "_UA_" in os.path.basename(x) or "VO_UA" in x]
    print(f"Англійська версія: {int(off / F // 60)} хв {off / F % 60:.0f} с, наплавів {len(E.build_fcpxml.transitions)}")
    print("  українських файлів у збірці:", left_ua or "немає")
    for pr in probs:
        print("  УВАГА:", pr)
    if a_.resolve:
        import_bins(paths)
        E.to_resolve(p, paths, TIMELINE, markers, replace=True)


if __name__ == "__main__":
    main()
