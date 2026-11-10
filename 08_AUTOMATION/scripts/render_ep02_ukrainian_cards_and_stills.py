#!/usr/bin/env python3
"""
Renders EP02 (Jensen Huang) 4K Ukrainian Quote Cards, Animated Dossier Zoom Previews,
Ken Burns 4K Archival Motion Clips, and Web Archival Photo Previews.
"""
import os
import subprocess
from pathlib import Path
from PIL import Image, ImageOps
from render_ukrainian_quote_cards import draw_quote_card

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
UA_CARDS_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards"
DOSS_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
WEB_DOSS_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "dossiers"
WEB_ARCH_PHOTO = ROOT / "07_DASHBOARD" / "assets" / "archival_photos"
STILLS_4K_DIR = ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k"
YOUNG_HUANG_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_huang"

for d in [UA_CARDS_DIR, WEB_DOSS_VID, WEB_ARCH_PHOTO, STILLS_4K_DIR]:
    d.mkdir(parents=True, exist_ok=True)

EP02_CARDS = [
    (
        "EP02_UA_CARD_01_No_Task_Is_Beneath_Me.png",
        "EP02_UA_CLIP_CARD_01_No_Task_Beneath_10s.mp4",
        10.0,
        "Акт 1 // Інтернат Oneida, Кентуккі (1972)",
        "«Для мене не буває низької праці. Я вимив більше туалетів, ніж усі ви, разом узяті».",
        "— Дженсен Хуанг // Стенфордська лекція",
        (64, 224, 208),
        66,
    ),
    (
        "EP02_UA_CARD_02_Dennys_Best_Dishwasher.png",
        "EP02_UA_CLIP_CARD_02_Dennys_Dishwasher_10s.mp4",
        10.0,
        "Акт 1 // Посудомийник у Denny's (Орегон, 15 років)",
        "«Я планував свою роботу ще до того, як тарілки потрапляли на кухню. Я став найкращим посудомийником в історії Denny's».",
        "— Дженсен Хуанг // Етика конвеєра",
        (245, 185, 65),
        62,
    ),
    (
        "EP02_UA_CARD_03_Honesty_With_Sega_Irimajiri.png",
        "EP02_UA_CLIP_CARD_03_Sega_Lifeline_12s.mp4",
        12.0,
        "Акт 2 // Вибір між брехнею та $5M (Токіо, 1997)",
        "«Наш чип не спрацює. Вам варто знайти іншого партнера. Але залиште нам фінансування — інакше ми зникнемо».",
        "— Дженсен Хуанг до CEO Sega Сьоїтіро Ірімадзірі",
        (255, 90, 95),
        62,
    ),
    (
        "EP02_UA_CARD_04_Thirty_Days_From_Bankruptcy.png",
        "EP02_UA_CLIP_CARD_04_Thirty_Days_8s.mp4",
        8.0,
        "Акт 2 // Мантра виживання (1997 → дотепер)",
        "«До банкрутства нашої компанії завжди залишається рівно тридцять днів».",
        "— Дженсен Хуанг // Кожна нарада NVIDIA",
        (255, 170, 50),
        68,
    ),
    (
        "EP02_UA_CARD_05_Zero_Billion_Dollar_Market.png",
        "EP02_UA_CLIP_CARD_05_Zero_Market_CUDA_10s.mp4",
        10.0,
        "Акт 3 // Архітектура CUDA та провал акцій (2006–2008)",
        "«Ми свідомо будуємо інфраструктуру для ринку, обсяг якого сьогодні дорівнює нулю мільярдів доларів».",
        "— Дженсен Хуанг // Ставка на паралельні обчислення",
        (34, 197, 94),
        64,
    ),
    (
        "EP02_UA_CARD_06_Truth_Dies_On_Hierarchy_Floors.png",
        "EP02_UA_CLIP_CARD_06_Flat_Org_55_Reports_10s.mp4",
        10.0,
        "Акт 4 // Плоска ієрархія (55 прямих підлеглих)",
        "«Інформація — це паливо компанії. Як тільки правда проходить через п'ять поверхів начальників, вона помирає».",
        "— Дженсен Хуанг // Без власного кабінету",
        (56, 189, 248),
        62,
    ),
    (
        "EP02_UA_CARD_07_Pain_And_Suffering_Resilience.png",
        "EP02_UA_CLIP_CARD_07_Pain_Suffering_10s.mp4",
        10.0,
        "Акт 4 // Стенфордський заклик (SIEPR 2024)",
        "«Велич народжується з характеру, а характер не кується зі зручності. Я бажаю вам великих порцій болю та страждань».",
        "— Дженсен Хуанг // Закон антикрихкості",
        (245, 185, 65),
        60,
    ),
    (
        "EP02_UA_CARD_08_Run_Dont_Walk_Finale.png",
        "EP02_UA_CLIP_CARD_08_Run_Dont_Walk_12s.mp4",
        12.0,
        "Акт 4 // Фінал • NTU Commencement 2023",
        "«Хай би чим ви займалися — біжіть, не йдіть. Або ви біжите за здобиччю, або тікаєте, щоб самому не стати здобиччю».",
        "— Дженсен Хуанг // Від мийки до трильйона",
        (74, 222, 128),
        60,
    ),
]

NEW_DOSSIER_VIDEOS = [
    ("EP02_DOC_02", "EP02_DOC_02_ACT2_Dennys_Founding_Charter_1993.png", "EP02_DOC_02_Dennys_Founding_10s.mp4"),
    ("EP02_DOC_03", "EP02_DOC_03_ACT2_Sega_NV2_Rescue_Memorandum_1997.png", "EP02_DOC_03_Sega_Rescue_10s.mp4"),
    ("EP02_DOC_04", "EP02_DOC_04_ACT2_RIVA128_GeForce256_First_GPU_1999.png", "EP02_DOC_04_RIVA_GeForce_10s.mp4"),
    ("EP02_DOC_05", "EP02_DOC_05_ACT3_AlexNet_GTX580_Turning_Point_2012.png", "EP02_DOC_05_AlexNet_GTX580_10s.mp4"),
    ("EP02_DOC_06", "EP02_DOC_06_ACT3_DGX1_OpenAI_Delivery_2016.png", "EP02_DOC_06_DGX1_OpenAI_10s.mp4"),
]

# Ken Burns animated 4K clips from verified archival photography
PHOTO_STILL_CLIPS = [
    ("EP02_IMG_ARCH_01_Taiwan_Tamsui_1970_Childhood_Era.jpg", "EP02_CLIP_STILL_Tamsui_1970_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_02_Oneida_Kentucky_Dorm_Farm_Campus.jpg", "EP02_CLIP_STILL_Oneida_Kentucky_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_03_Aloha_High_School_Oregon_1981.jpg", "EP02_CLIP_STILL_Aloha_High_5s.mp4", 5.0),
    ("EP02_IMG_ARCH_04_Oregon_State_University_Campus_1984.jpg", "EP02_CLIP_STILL_OSU_Campus_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_05_Dennys_2484_Berryessa_San_Jose_1993.jpg", "EP02_CLIP_STILL_Dennys_Berryessa_7s.mp4", 7.0),
    ("EP02_IMG_ARCH_06_NVIDIA_NV1_500nm_Silicon_Die_1995.jpg", "EP02_CLIP_STILL_NV1_Die_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_07_NVIDIA_RIVA_128_Chip_1997.jpg", "EP02_CLIP_STILL_RIVA_128_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_08_Morris_Chang_TSMC_Founder.jpg", "EP02_CLIP_STILL_Morris_Chang_5s.mp4", 5.0),
    ("EP02_IMG_ARCH_09_NVIDIA_GeForce_256_Worlds_First_GPU_1999.jpg", "EP02_CLIP_STILL_GeForce_256_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_10_EVGA_GeForce_GTX_580_AlexNet_2012.jpg", "EP02_CLIP_STILL_GF110_GTX580_Die_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_10B_EVGA_GeForce_GTX_580_Card_2012.jpg", "EP02_CLIP_STILL_EVGA_GTX580_Card_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_11_JenHsun_Huang_Engineering_Center_Stanford.jpg", "EP02_CLIP_STILL_Huang_Center_Stanford_5s.mp4", 5.0),
    ("EP02_IMG_ARCH_12_Huang_Early_Leather_Jacket_2014_Portrait.jpg", "EP02_CLIP_STILL_Huang_2014_Headshot_5s.mp4", 5.0),
    ("EP02_IMG_ARCH_13_Jensen_Huang_GTC_Keynote_2016.jpg", "EP02_CLIP_STILL_Huang_GTC_2016_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_15_NVIDIA_DGX_B200_HGX_System.jpg", "EP02_CLIP_STILL_DGX_B200_HGX_6s.mp4", 6.0),
    ("EP02_IMG_ARCH_16_NVIDIA_Endeavor_HQ_Santa_Clara.jpg", "EP02_CLIP_STILL_NVIDIA_Endeavor_HQ_6s.mp4", 6.0),
]


def render_4k_still_video(src_path: Path, dst_path: Path, dur_s: float, zoom_drift: float = 0.05):
    """Render a 16:9 24fps H.264 clip with gentle center Ken Burns drift (cover-cropped, zero distortion)."""
    frames = max(24, int(round(dur_s * 24.0)))
    step = zoom_drift / float(frames)
    vf = (
        f"scale=3840:2160:force_original_aspect_ratio=increase,"
        f"crop=3840:2160:(iw-3840)/2:(ih-2160)/2,"
        f"zoompan=z='min(zoom+{step:.6f},{1.0+zoom_drift:.3f})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps=24,"
        f"format=yuv420p"
    )
    subprocess.run([
        FFMPEG, "-y", "-loop", "1", "-i", str(src_path),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-vf", vf,
        "-t", f"{dur_s:.2f}", "-shortest",
        "-c:v", "libx264", "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        str(dst_path),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def make_web_photo_preview(src_path: Path, dst_path: Path, max_w: int = 1600):
    with Image.open(src_path) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        if im.width > max_w:
            im = im.resize((max_w, int(im.height * (max_w / float(im.width)))), Image.Resampling.LANCZOS)
        im.save(dst_path, "JPEG", quality=86, optimize=True)


def main():
    print("=== [1/4] Rendering 8 4K Ukrainian Quote Cards + Video Clips for EP02 ===")
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP02_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP02: JENSEN HUANG",
        ))
        mp4_path = STILLS_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)
        print(f"  [OK] {png_name} -> {mp4_name} ({mp4_path.stat().st_size//1024} KB)", flush=True)

    print("=== [2/4] Rendering 5 Animated Dossier Zoom MP4s (Web + 4K Master) ===")
    for doc_id, png_name, raw_mp4_name in NEW_DOSSIER_VIDEOS:
        src_png = DOSS_DIR / png_name
        if not src_png.exists():
            print(f"  [WARN] Missing {src_png}")
            continue
        web_dst = WEB_DOSS_VID / f"{doc_id}.mp4"
        raw_dst = DOSS_DIR / raw_mp4_name
        vf_web = (
            "scale=2560:1440,"
            "zoompan=z='min(zoom+0.0005,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1280x720:fps=24,"
            "format=yuv420p"
        )
        subprocess.run([
            FFMPEG, "-y", "-loop", "1", "-i", str(src_png), "-vf", vf_web,
            "-t", "5", "-c:v", "libx264", "-preset", "fast", "-crf", "26", "-movflags", "+faststart",
            str(web_dst),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        render_4k_still_video(src_png, raw_dst, 10.0, zoom_drift=0.05)
        print(f"  [OK] {doc_id}: web={web_dst.stat().st_size//1024}KB | master={raw_dst.stat().st_size//1024}KB", flush=True)

    print("=== [3/4] Publishing Web Previews for All EP02 Archival Photos ===")
    for img_path in sorted(YOUNG_HUANG_DIR.glob("EP02_IMG_ARCH_*.jpg")):
        web_dst = WEB_ARCH_PHOTO / img_path.name
        make_web_photo_preview(img_path, web_dst)
        print(f"  [OK] {web_dst.name} ({web_dst.stat().st_size//1024} KB)")

    print("=== [4/4] Rendering Ken Burns 4K Stills->Video Clips for EP02 ===")
    for src_name, clip_name, dur in PHOTO_STILL_CLIPS:
        src_p = YOUNG_HUANG_DIR / src_name
        if not src_p.exists():
            print(f"  [WARN] Missing still: {src_p}")
            continue
        dst_p = STILLS_4K_DIR / clip_name
        render_4k_still_video(src_p, dst_p, dur, zoom_drift=0.05)
        print(f"  [OK] {clip_name} ({dst_p.stat().st_size//1024} KB)", flush=True)


if __name__ == "__main__":
    main()
