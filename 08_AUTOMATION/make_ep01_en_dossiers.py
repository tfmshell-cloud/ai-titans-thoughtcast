#!/usr/bin/env python3
"""Англійські версії досьє з інших епізодів, що стоять в EP01 і мають український текст.
Той самий HTML-шаблон і рендер, що й в оригіналі (08_AUTOMATION/scripts/render_ep07_dossiers_and_cards.py).
Вихід: 05_RAW_FOOTAGE/dossiers_press/<назва>_EN.png і _EN.mp4 (10 с, 4K)."""
import copy
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "scripts"))
import render_ep07_dossiers_and_cards as R07                       # noqa: E402
from render_ep03_dossiers_and_cards import build_dossier_html, render_4k_still_video, CHROME   # noqa: E402

DOSSIER_DIR = R07.DOSSIER_DIR
EN = {
    "EP07_DOC_03": dict(
        headline="Scaling Laws (2020): A Straight Line Across Seven Orders of Magnitude",
        meta=[("BAIDU & GOOGLE BRAIN", "Deep Speech 2 (2014) ➔ Concrete Problems in AI Safety (2016)"),
              ("OPENAI VP RESEARCH", "Led GPT-2 and GPT-3 and shaped the RLHF approach"),
              ("LAW L(N, D, C)", "Precise power-law loss curves across 7 orders of compute"),
              ("PARADIGM SHIFT", "Deep learning becomes the statistical physics of the mind")],
        paragraphs=["The paper by Kaplan, McCandlish and Amodei (January 2020) showed that the cross-entropy loss of language "
                    "models falls not in random jumps, but along a perfectly straight line on a log scale across seven orders of magnitude.",
                    "The discovery gave Amodei mathematical confidence that AGI-level systems would arrive within years — "
                    "and that safety had to be built before superpowerful intelligence appeared."]),
}


def main():
    specs = {s["id"]: s for s in R07.DOSSIERS_SPEC}
    tmp = HERE / "scratch"
    tmp.mkdir(exist_ok=True)
    for did, tr in EN.items():
        spec = copy.deepcopy(specs[did])
        spec.update(tr)
        png = DOSSIER_DIR / spec["raw_png"].replace(".png", "_EN.png")
        mp4 = DOSSIER_DIR / spec["master_mp4"].replace(".mp4", "_EN.mp4")
        html = tmp / f"{did}_EN.html"
        html.write_text(build_dossier_html(spec), encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        "--window-size=3840,2160", "--force-device-scale-factor=1", f"--screenshot={png}", html.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        render_4k_still_video(png, mp4, 10.0, zoom_drift=0.05)
        print("✓", mp4.name)


if __name__ == "__main__":
    main()
