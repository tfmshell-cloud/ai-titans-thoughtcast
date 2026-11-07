#!/usr/bin/env python3
"""
Builds Web-Ready MP4 Video Previews & Animated Pre-Vis Loops for AI Titans Studio:
1. 14 Real Archival B-Roll MP4s -> 07_DASHBOARD/assets/video_previews/archives/*.mp4
2. 14 Animated 4K Dossier Dynamic Zoom (1.00->1.06) MP4s -> 07_DASHBOARD/assets/video_previews/dossiers/*.mp4
3. 19 Animated Google Flow / Veo Pre-Vis ("Майбутні футажі") MP4s (10 for EP01 + 9 for EP02-EP10)
   -> 05_RAW_FOOTAGE/flow_renders/*.mp4 AND 07_DASHBOARD/assets/video_previews/flow/*.mp4
"""

import math
import os
import random
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
if not os.path.exists(FFMPEG):
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

ARCH_SRC = ROOT / "05_RAW_FOOTAGE" / "archives"
DOSS_SRC = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
FLOW_RAW_DIR = ROOT / "05_RAW_FOOTAGE" / "flow_renders"

WEB_VID_ROOT = ROOT / "07_DASHBOARD" / "assets" / "video_previews"
WEB_ARCH_DIR = WEB_VID_ROOT / "archives"
WEB_DOSS_DIR = WEB_VID_ROOT / "dossiers"
WEB_FLOW_DIR = WEB_VID_ROOT / "flow"

for d in [FLOW_RAW_DIR, WEB_ARCH_DIR, WEB_DOSS_DIR, WEB_FLOW_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def load_font(size: int, mono: bool = False):
    candidates = (
        [
            "/System/Library/Fonts/SFNSMono.ttf",
            "/System/Library/Fonts/Menlo.ttc",
            "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
        ]
        if mono
        else [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNS.ttf",
        ]
    )
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def step1_transcode_archives():
    print("=== [1/3] Transcoding 14 Real Archival MP4 Clips for Web Streaming ===")
    mp4s = sorted(ARCH_SRC.glob("*.mp4"))
    for src in mp4s:
        dst = WEB_ARCH_DIR / src.name
        cmd = [
            FFMPEG, "-y", "-i", str(src),
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:black,fps=24",
            "-c:v", "libx264", "-preset", "fast", "-crf", "26",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "96k",
            "-movflags", "+faststart",
            str(dst)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        size_kb = dst.stat().st_size // 1024
        print(f"  [OK] {dst.name} ({size_kb} KB)")


DOSSIER_MAP = {
    "EP01_DOC_01": "EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png",
    "EP01_DOC_02": "EP01_DOC_02_ACT2_OpenAI_Introducing_Dec11_2015.png",
    "EP01_DOC_03": "EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023.png",
    "EP01_DOC_04": "EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023.png",
    "EP01_DOC_05": "EP01_DOC_05_ACT3_730_Employees_Open_Letter.png",
    "EP02_DOC_01": "EP02_DOC_01_ACT2_NVIDIA_RIVA128_SEC_1999_IPO.png",
    "EP03_DOC_01": "EP03_DOC_01_ACT3_AlphaGo_Move37_Nature_2016.png",
    "EP04_DOC_01": "EP04_DOC_01_ACT2_Hinton_Backprop_Nature_1986.png",
    "EP05_DOC_01": "EP05_DOC_01_ACT2_LeCun_LeNet5_IEEE_1998.png",
    "EP06_DOC_01": "EP06_DOC_01_ACT2_Sutskever_AlexNet_NIPS_2012.png",
    "EP07_DOC_01": "EP07_DOC_01_ACT3_Amodei_Constitutional_AI_2022.png",
    "EP08_DOC_01": "EP08_DOC_01_ACT2_FeiFeiLi_ImageNet_CVPR_2009.png",
    "EP09_DOC_01": "EP09_DOC_01_ACT2_Bengio_Attention_Bahdanau_2014.png",
    "EP10_DOC_01": "EP10_DOC_01_ACT2_AndrewNg_GoogleBrain_Coursera_2011.png",
}


def step2_render_dossier_zoom_videos():
    print("=== [2/3] Rendering 14 Animated 24fps Dynamic Zoom (1.00->1.06) Dossier Videos ===")
    for doc_id, png_name in DOSSIER_MAP.items():
        src_png = DOSS_SRC / png_name
        if not src_png.exists():
            print(f"  [WARN] Missing {src_png}")
            continue
        dst_mp4 = WEB_DOSS_DIR / f"{doc_id}.mp4"
        # Use ffmpeg zoompan for smooth 24fps Ken Burns Dynamic Zoom 1.00 -> 1.06 over 5 seconds (120 frames)
        vf = (
            "scale=2560:1440,"
            "zoompan=z='min(zoom+0.0005,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1280x720:fps=24,"
            "format=yuv420p"
        )
        cmd = [
            FFMPEG, "-y", "-loop", "1", "-i", str(src_png),
            "-vf", vf,
            "-t", "5",
            "-c:v", "libx264", "-preset", "fast", "-crf", "26",
            "-movflags", "+faststart",
            str(dst_mp4)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        size_kb = dst_mp4.stat().st_size // 1024
        print(f"  [OK] {dst_mp4.name} ({size_kb} KB)")


FLOW_SCENES = [
    # EP01 (10 Priority Shots)
    {
        "ep": "01", "num": "01", "file": "ep01_flow_01_mac_chassis.mp4", "tc": "0:00–0:15",
        "title": "1993 Macintosh LC II • Amber Dust Motes",
        "mode": "mac_chassis", "accent": (251, 191, 36), "sub": "DaVinci V1 • Speed 60% • Optical Flow"
    },
    {
        "ep": "01", "num": "02", "file": "ep01_flow_02_crt_code.mp4", "tc": "0:15–0:45",
        "title": "Green Phosphor CRT • Scrolling Assembly Code",
        "mode": "crt_code", "accent": (52, 211, 153), "sub": "Macro Phosphor Scanlines • 24fps"
    },
    {
        "ep": "01", "num": "03", "file": "ep01_flow_03_silicon_laser.mp4", "tc": "1:30–2:30",
        "title": "Silicon Wafer Circuitry • Coherent Cyan Laser",
        "mode": "silicon_laser", "accent": (56, 189, 248), "sub": "Microscopic Copper Traces • 8K Style"
    },
    {
        "ep": "01", "num": "04", "file": "ep01_flow_04_exponential_line.mp4", "tc": "3:30–4:45",
        "title": "The Exponential Curve • Golden Trajectory",
        "mode": "exponential_line", "accent": (251, 191, 36), "sub": "Moore's Law & Compute Scaling Visualization"
    },
    {
        "ep": "01", "num": "05", "file": "ep01_flow_05_neural_lattice.mp4", "tc": "7:00–8:15",
        "title": "Obsidian Neural Lattice • Synchronized Pulses",
        "mode": "neural_lattice", "accent": (56, 189, 248), "sub": "GPT Transformer Attention Nodes Firing"
    },
    {
        "ep": "01", "num": "06", "file": "ep01_flow_06_server_monolith.mp4", "tc": "8:15–9:30",
        "title": "Monolithic Server Racks • Blue LED & Cold Vapor",
        "mode": "server_monolith", "accent": (56, 189, 248), "sub": "Hyperscale AI Datacenter Corridor"
    },
    {
        "ep": "01", "num": "07", "file": "ep01_flow_07_boardroom_noir.mp4", "tc": "10:45–12:15",
        "title": "Boardroom Noir • Smartphone Alert in Rain",
        "mode": "boardroom_noir", "accent": (251, 113, 133), "sub": "Nov 17, 2023 • Google Meet Coup Atmosphere"
    },
    {
        "ep": "01", "num": "08", "file": "ep01_flow_08_golden_signatures.mp4", "tc": "13:45–15:30",
        "title": "730 Golden Light Threads • Convergence Core",
        "mode": "golden_signatures", "accent": (251, 191, 36), "sub": "OpenAI Employees Unity Simulation"
    },
    {
        "ep": "01", "num": "09", "file": "ep01_flow_09_fusion_torus.mp4", "tc": "15:30–17:00",
        "title": "Helion Magnetic Fusion Torus • Violet-Gold Plasma",
        "mode": "fusion_torus", "accent": (167, 139, 250), "sub": "Magnetic Field Containment • Hard Sci-Fi"
    },
    {
        "ep": "01", "num": "10", "file": "ep01_flow_10_earth_horizon.mp4", "tc": "18:30–20:00",
        "title": "Orbital Earth Horizon • Golden Planetary Grid",
        "mode": "earth_horizon", "accent": (251, 191, 36), "sub": "Planetary Intelligence Network • IMAX Finale"
    },
    # EP02 - EP10 Signature Flow Pre-Vis Clips
    {
        "ep": "02", "num": "01", "file": "ep02_flow_01_blackwell_wafer_matrix.mp4", "tc": "04:15–05:30",
        "title": "NVIDIA Blackwell 208B Transistor Silicon Matrix",
        "mode": "silicon_laser", "accent": (52, 211, 153), "sub": "Extreme Macro Photolithography • EP02 Jensen Huang"
    },
    {
        "ep": "03", "num": "01", "file": "ep03_flow_01_alphafold_protein_cosmos.mp4", "tc": "12:30–14:00",
        "title": "AlphaFold 3D Protein Folding Ribbon Cosmos",
        "mode": "neural_lattice", "accent": (56, 189, 248), "sub": "200M Molecular Structures • EP03 Demis Hassabis"
    },
    {
        "ep": "04", "num": "01", "file": "ep04_flow_01_backprop_synapse_storm.mp4", "tc": "06:00–07:30",
        "title": "Backpropagation Error Signal Reversal Storm",
        "mode": "golden_signatures", "accent": (251, 191, 36), "sub": "Biological vs Silicon Neural Weights • EP04 Hinton"
    },
    {
        "ep": "05", "num": "01", "file": "ep05_flow_01_jepa_world_model_grid.mp4", "tc": "11:00–12:30",
        "title": "LeNet Convolution & JEPA 3D Physics World Model",
        "mode": "crt_code", "accent": (56, 189, 248), "sub": "Convolutional Feature Maps • EP05 Yann LeCun"
    },
    {
        "ep": "06", "num": "01", "file": "ep06_flow_01_ssi_obsidian_monolith.mp4", "tc": "14:00–15:30",
        "title": "Safe Superintelligence (SSI) Obsidian Monolith",
        "mode": "server_monolith", "accent": (167, 139, 250), "sub": "Pure Alignment Architecture • EP06 Ilya Sutskever"
    },
    {
        "ep": "07", "num": "01", "file": "ep07_flow_01_constitutional_prism.mp4", "tc": "09:00–10:30",
        "title": "Constitutional AI Optical Prism & Interpretability",
        "mode": "fusion_torus", "accent": (251, 191, 36), "sub": "Mechanistic Interpretability • EP07 Dario Amodei"
    },
    {
        "ep": "08", "num": "01", "file": "ep08_flow_01_spatial_intelligence_dome.mp4", "tc": "07:30–09:00",
        "title": "ImageNet 14M Mosaic & Spatial Intelligence Dome",
        "mode": "earth_horizon", "accent": (52, 211, 153), "sub": "Visual & 3D World Perception • EP08 Fei-Fei Li"
    },
    {
        "ep": "09", "num": "01", "file": "ep09_flow_01_attention_vector_threads.mp4", "tc": "06:30–08:00",
        "title": "Soft Attention Alignment Threads & Safety Shield",
        "mode": "golden_signatures", "accent": (251, 113, 133), "sub": "Bahdanau Attention Mechanism • EP09 Yoshua Bengio"
    },
    {
        "ep": "10", "num": "01", "file": "ep10_flow_01_global_neural_classroom.mp4", "tc": "13:00–14:30",
        "title": "Global Planetary AI Democratization Network",
        "mode": "exponential_line", "accent": (56, 189, 248), "sub": "Coursera & Stanford CS229 Wave • EP10 Andrew Ng"
    },
]


def render_flow_clip(scene: dict):
    W, H = 1280, 720
    FPS = 24
    DURATION = 5
    TOTAL_FRAMES = FPS * DURATION
    mode = scene["mode"]
    acc = scene["accent"]

    font_title = load_font(24, mono=False)
    font_mono = load_font(15, mono=True)
    font_small = load_font(13, mono=True)

    dst_web = WEB_FLOW_DIR / scene["file"]
    dst_raw = FLOW_RAW_DIR / scene["file"]

    cmd = [
        FFMPEG, "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "25",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(dst_web)
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    rng = random.Random(hash(scene["file"]))
    particles = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.6, 2.8), rng.uniform(0, 6.28)) for _ in range(95)]

    for f in range(TOTAL_FRAMES):
        t = f / float(TOTAL_FRAMES)
        img = Image.new("RGB", (W, H), (9, 11, 16))
        draw = ImageDraw.Draw(img)

        # Subtle cinematic background grid
        for gx in range(0, W, 80):
            draw.line([(gx, 0), (gx, H)], fill=(16, 20, 30), width=1)
        for gy in range(0, H, 80):
            draw.line([(0, gy), (W, gy)], fill=(16, 20, 30), width=1)

        cx, cy = W // 2, H // 2

        if mode == "mac_chassis":
            # Vintage 1993 Macintosh chassis & amber volumetric rays + floating dust motes
            for r_i in range(8):
                spread = r_i * 38
                draw.polygon([(0, 80 + spread), (W, 240 + spread * 2), (W, 310 + spread * 2), (0, 120 + spread)],
                             fill=(32 + r_i * 2, 24 + r_i, 12))
            box_x = int(390 - t * 24)
            draw.rounded_rectangle([box_x, 150, box_x + 480, 560], radius=18, fill=(38, 34, 28), outline=acc, width=3)
            draw.rounded_rectangle([box_x + 55, 195, box_x + 425, 435], radius=12, fill=(14, 24, 18), outline=(90, 82, 68), width=2)
            # Floppy drive slot
            draw.rectangle([box_x + 280, 480, box_x + 410, 492], fill=(15, 15, 18), outline=acc, width=1)
            # Blinking cursor inside screen
            if (f // 8) % 2 == 0:
                draw.rectangle([box_x + 85, 230, box_x + 102, 254], fill=(52, 211, 153))
            for px, py, pr, ph in particles:
                nx = (px + f * pr * 1.2) % W
                ny = (py - f * pr * 0.6 + math.sin(t * 6.28 + ph) * 12) % H
                r_int = int(pr * 2.2)
                draw.ellipse([nx - r_int, ny - r_int, nx + r_int, ny + r_int], fill=acc)

        elif mode == "crt_code":
            # Scrolling green phosphor assembly lines + scanlines
            asm_lines = [
                "0x00401000  MOV EAX, [EBP+0x08]      ; Load neural weight tensor",
                "0x00401004  FMUL DWORD PTR [ESI+0x10] ; Backprop gradient step",
                "0x0040100A  FADD ST(0), ST(1)        ; Accumulate activation",
                "0x0040100E  CMP ECX, 0x00010000      ; Epoch convergence check",
                "0x00401014  JNZ 0x00401000           ; Loop next synapse layer",
                "0x00401018  CALL _attention_matrix   ; Softmax context align",
                "0x0040101D  MOV [EDI], EAX           ; Store latent representation",
                "0x00401020  RET                      ; Complete forward pass",
            ]
            scroll_y = int(t * 240)
            for idx_l in range(18):
                yy = 110 + ((idx_l * 34 - scroll_y) % 520)
                line_txt = asm_lines[idx_l % len(asm_lines)]
                bright = max(60, min(255, int(255 - abs(yy - cy) * 0.5)))
                draw.text((140, yy), line_txt, font=font_mono, fill=(int(acc[0]*bright/255), int(acc[1]*bright/255), int(acc[2]*bright/255)))
            for sy in range(80, H - 80, 6):
                draw.line([(90, sy), (W - 90, sy)], fill=(8, 18, 14), width=1)

        elif mode == "silicon_laser":
            # Perspective silicon wafer traces with moving laser pulses
            for i in range(-10, 11):
                x_top = cx + i * 32
                x_bot = cx + i * 115
                draw.line([(x_top, 140), (x_bot, H - 90)], fill=(25, 55, 78), width=2)
                pulse_p = (t * 2.0 + (i + 10) * 0.13) % 1.0
                px = x_top + (x_bot - x_top) * pulse_p
                py = 140 + (H - 230) * pulse_p
                draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=acc)
            for j in range(1, 10):
                yy = 140 + int((j / 10.0) ** 1.4 * (H - 230))
                draw.line([(120, yy), (W - 120, yy)], fill=(22, 48, 68), width=2)

        elif mode == "exponential_line":
            # Glowing exponential curve rising sharply
            pts = []
            max_x = int(160 + (W - 320) * min(1.0, t * 1.25))
            for x in range(160, max_x, 8):
                norm_x = (x - 160) / float(W - 320)
                y = (H - 140) - (norm_x ** 3.4) * (H - 280)
                pts.append((x, y))
            if len(pts) > 1:
                for w_glow, col_div in [(10, 4), (5, 2), (3, 1)]:
                    c_use = (acc[0] // col_div, acc[1] // col_div, acc[2] // col_div)
                    draw.line(pts, fill=c_use, width=w_glow)
                hx, hy = pts[-1]
                draw.ellipse([hx - 10, hy - 10, hx + 10, hy + 10], fill=(255, 255, 255), outline=acc, width=3)

        elif mode == "neural_lattice":
            # 3D-like rotating neural nodes & firing connections
            nodes = []
            for idx_n, (px, py, pr, ph) in enumerate(particles[:42]):
                angle = ph + t * 2.2
                rx = cx + math.cos(angle) * (140 + (idx_n % 7) * 55)
                ry = cy + math.sin(angle * 1.3) * (80 + (idx_n % 5) * 42)
                nodes.append((rx, ry))
            for i_n in range(len(nodes)):
                for j_n in range(i_n + 1, min(i_n + 5, len(nodes))):
                    x1, y1 = nodes[i_n]
                    x2, y2 = nodes[j_n]
                    if math.hypot(x2 - x1, y2 - y1) < 230:
                        draw.line([(x1, y1), (x2, y2)], fill=(28, 64, 92), width=1)
                        p_pos = (t * 3 + i_n * 0.2) % 1.0
                        mx = x1 + (x2 - x1) * p_pos
                        my = y1 + (y2 - y1) * p_pos
                        draw.ellipse([mx - 3, my - 3, mx + 3, my + 3], fill=acc)
            for rx, ry in nodes:
                draw.ellipse([rx - 5, ry - 5, rx + 5, ry + 5], fill=acc)

        elif mode == "server_monolith":
            # Endless supercomputer server corridor with pulsing LEDs
            for side in [-1, 1]:
                for depth in range(1, 9):
                    d_scale = (depth + (t * 2.0) % 1.0) / 9.0
                    x_pos = cx + side * int(70 + d_scale * 480)
                    top_y = cy - int(40 + d_scale * 240)
                    bot_y = cy + int(40 + d_scale * 240)
                    w_rack = int(18 + d_scale * 48)
                    draw.rectangle([x_pos - w_rack, top_y, x_pos + w_rack, bot_y], fill=(15, 19, 28), outline=(38, 52, 74), width=2)
                    for led_y in range(top_y + 16, bot_y - 16, 22):
                        if (led_y + f + depth) % 3 != 0:
                            draw.rectangle([x_pos - w_rack + 6, led_y, x_pos - w_rack + 18, led_y + 4], fill=acc)

        elif mode == "boardroom_noir":
            # Moody conference table + glowing smartphone notification + rain streaks
            for rx, ry, pr, ph in particles:
                ry_now = (ry + f * 9 * pr) % H
                draw.line([(rx, ry_now), (rx - 6, ry_now + 26)], fill=(38, 48, 68), width=1)
            # Dark perspective table
            draw.polygon([(220, H - 90), (W - 220, H - 90), (W - 430, 380), (430, 380)], fill=(18, 16, 22), outline=(48, 42, 56), width=2)
            # Glowing phone on table
            pulse = int(140 + 110 * math.sin(t * 6.28 * 2))
            draw.polygon([(cx - 42, 470), (cx + 42, 470), (cx + 32, 435), (cx - 32, 435)],
                         fill=(pulse, pulse // 2, pulse // 2), outline=acc, width=2)
            draw.ellipse([cx - 140, 400, cx + 140, 520], outline=(acc[0] // 2, acc[1] // 3, acc[2] // 3), width=2)

        elif mode == "golden_signatures":
            # 730 golden threads converging into central energy core
            core_r = int(28 + 14 * math.sin(t * 6.28 * 2))
            for idx_p, (px, py, pr, ph) in enumerate(particles):
                ang = ph + idx_p * 0.08 + t * 0.9
                dist = (1.0 - ((t + (idx_p % 20) / 20.0) % 1.0)) * 540 + 30
                x1 = cx + math.cos(ang) * dist
                y1 = cy + math.sin(ang) * (dist * 0.6)
                x2 = cx + math.cos(ang) * max(15, dist - 55)
                y2 = cy + math.sin(ang) * (max(15, dist - 55) * 0.6)
                draw.line([(x1, y1), (x2, y2)], fill=acc, width=2)
            draw.ellipse([cx - core_r * 2, cy - core_r * 2, cx + core_r * 2, cy + core_r * 2], outline=acc, width=2)
            draw.ellipse([cx - core_r, cy - core_r, cx + core_r, cy + core_r], fill=acc)

        elif mode == "fusion_torus":
            # Magnetic fusion torus rings
            for ring in range(14):
                ang = (ring / 14.0) * math.pi * 2 + t * math.pi * 2
                rx = cx + math.cos(ang) * 190
                ry = cy + math.sin(ang) * 75
                rad_x = 120 + int(30 * math.sin(ang))
                rad_y = 95
                draw.ellipse([rx - rad_x, ry - rad_y, rx + rad_x, ry + rad_y], outline=acc, width=2)
            draw.ellipse([cx - 85, cy - 38, cx + 85, cy + 38], fill=(24, 16, 36), outline=(251, 191, 36), width=3)

        elif mode == "earth_horizon":
            # Curved orbital horizon + neural city grid arcs
            earth_y = int(H + 420 - t * 25)
            draw.ellipse([cx - 980, earth_y - 680, cx + 980, earth_y + 680], fill=(12, 20, 34), outline=acc, width=4)
            for arc_i in range(-6, 7):
                ax = cx + arc_i * 85
                ay = earth_y - 650 + abs(arc_i) * 18
                draw.ellipse([ax - 4, ay - 4, ax + 4, ay + 4], fill=acc)
                if arc_i < 6:
                    nx = cx + (arc_i + 1) * 85
                    ny = earth_y - 650 + abs(arc_i + 1) * 18
                    draw.line([(ax, ay), ((ax + nx) // 2, min(ay, ny) - 35), (nx, ny)], fill=acc, width=2)

        # HUD Cinema Frame & Metadata Overlay
        draw.rectangle([24, 20, W - 24, H - 20], outline=(42, 50, 68), width=1)
        draw.rectangle([24, 20, W - 24, 68], fill=(12, 15, 22))
        draw.text((42, 32), f"FLOW / VEO 4K PRE-VIS • EP{scene['ep']} #{scene['num']} • TC {scene['tc']}", font=font_mono, fill=acc)
        draw.text((W - 350, 32), f"24.000 FPS • FRAME {f+1:03d}/{TOTAL_FRAMES:03d}", font=font_mono, fill=(148, 163, 184))

        draw.rectangle([24, H - 82, W - 24, H - 20], fill=(12, 15, 22))
        draw.text((42, H - 72), scene["title"], font=font_title, fill=(230, 237, 243))
        draw.text((42, H - 42), f"{scene['file']}  |  {scene['sub']}", font=font_small, fill=(148, 163, 184))

        proc.stdin.write(img.tobytes())

    proc.stdin.close()
    proc.wait()
    shutil.copy2(dst_web, dst_raw)
    size_kb = dst_web.stat().st_size // 1024
    print(f"  [OK] {scene['file']} ({size_kb} KB) -> web & flow_renders/")


def step3_render_flow_previs():
    print("=== [3/3] Rendering 19 Animated 24fps Flow/Veo Pre-Vis Videos ('Майбутні футажі') ===")
    for sc in FLOW_SCENES:
        render_flow_clip(sc)


if __name__ == "__main__":
    step1_transcode_archives()
    step2_render_dossier_zoom_videos()
    step3_render_flow_previs()
    print("=== ALL WEB VIDEO PREVIEWS & FLOW ANIMATICS GENERATED SUCCESSFULLY ===")
