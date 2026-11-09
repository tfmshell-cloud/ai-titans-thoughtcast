#!/usr/bin/env python3
"""
Render 4K (3840x2160 24fps) Primary Source Dossier plates for Act 4:
- EP01_DOC_06: $100 Billion Stargate Supercomputer (Microsoft & OpenAI)
- EP01_DOC_07: $7 Trillion Semiconductor Foundry Sovereign Initiative
"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 3840, 2160
ffmpeg_bin = '/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg'
font_title_path = '/System/Library/Fonts/HelveticaNeue.ttc'
font_code_path = '/System/Library/Fonts/Supplemental/Courier New.ttf'

font_stamp = ImageFont.truetype(font_code_path, 34)
font_h1 = ImageFont.truetype(font_title_path, 68)
font_meta = ImageFont.truetype(font_title_path, 40)
font_body = ImageFont.truetype(font_title_path, 46)
font_callout = ImageFont.truetype(font_title_path, 54)
font_foot = ImageFont.truetype(font_code_path, 32)

doc_dir = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/dossiers_press'

dossiers = [
    {
        "id": "EP01_DOC_06",
        "png": "EP01_DOC_06_ACT4_Stargate_100B_Supercluster.png",
        "mp4": "EP01_DOC_06_Stargate_100B_Report_10s.mp4",
        "stamp": "GLOBAL INFRASTRUCTURE DOSSIER // MARCH 2024 • 5GW ROADMAP",
        "url": "https://theinformation.com/articles/microsoft-openai-stargate-100b-supercomputer",
        "title": "Microsoft and OpenAI Plot $100 Billion ‘Stargate’ AI Supercomputer",
        "meta": "Project Phase 5 • Anticipated 2028 Deployment • 5 Gigawatt Energy Requirement",
        "body_before": "Executives at Microsoft and OpenAI have formulated blueprints for an unprecedented data center project containing an AI supercomputer dubbed ‘Stargate’. The effort could cost more than $100 billion—100 times more expensive than the biggest operational clusters.",
        "highlight": "The cluster represents an existential pivot from software to physical reality: requiring millions of specialized AI accelerator chips and dedicated gigawatts from advanced nuclear fission and Helion fusion reactors.",
        "footer_left": "EXHIBIT 01-F // THE PHYSICAL COMPUTE EMPIRE",
        "footer_right": "PHASE 5 SUPERCLUSTER • 5,000,000 TRANSISTOR ARRAYS",
        "accent": (60, 160, 255) # Stargate Cyan
    },
    {
        "id": "EP01_DOC_07",
        "png": "EP01_DOC_07_ACT4_Seven_Trillion_Chip_Network.png",
        "mp4": "EP01_DOC_07_7_Trillion_Chip_Network_10s.mp4",
        "stamp": "SEMICONDUCTOR SOVEREIGNTY REPORT // FEBRUARY 2024",
        "url": "https://wsj.com/tech/ai/sam-altman-seeks-trillions-for-global-semiconductor-fabrication",
        "title": "Sam Altman Seeks Up to $7 Trillion to Reshape Global Chip Industry",
        "meta": "Sovereign Wealth Funds & Advanced EUV Foundries Initiative • Middle East & US",
        "body_before": "OpenAI Chief Executive Sam Altman is in discussions with global investors, including the United Arab Emirates government, to raise between $5 trillion and $7 trillion to overhaul the world's semiconductor fabrication capacity and energy grid.",
        "highlight": "“Compute is the currency of the future. The physical world is the only bottleneck to artificial general intelligence—we must build the foundries to break the constraint.”",
        "footer_left": "EXHIBIT 01-G // THE SEVEN TRILLION RESTRUCTURING",
        "footer_right": "EXTREME ULTRAVIOLET LITHOGRAPHY • GLOBAL FOUNDRY MATRIX",
        "accent": (240, 150, 40) # Foundry Gold
    }
]

for d in dossiers:
    png_path = os.path.join(doc_dir, d["png"])
    mp4_path = os.path.join(doc_dir, d["mp4"])

    # Render PNG plate
    img = Image.new("RGBA", (W, H), (10, 12, 18, 255))
    draw = ImageDraw.Draw(img)

    # Frame
    pad = 120
    draw.rectangle([pad, pad, W - pad, H - pad], outline=(60, 70, 90, 180), width=3)
    
    # Stamp & URL bar
    draw.text((pad + 40, pad + 40), d["stamp"], font=font_stamp, fill=d["accent"])
    draw.line([(pad + 40, pad + 90), (W - pad - 40, pad + 90)], fill=(60, 70, 90, 120), width=2)
    draw.text((pad + 40, pad + 115), f"SOURCE: {d['url']}", font=font_stamp, fill=(160, 170, 185, 200))

    # Paper Plate Container
    plate_x = pad + 180
    plate_y = pad + 190
    plate_w = W - 2 * (pad + 180)
    plate_h = 1350
    draw.rounded_rectangle([plate_x, plate_y, plate_x + plate_w, plate_y + plate_h], radius=24, fill=(245, 246, 248, 255))

    # Title
    draw.text((plate_x + 80, plate_y + 80), d["title"], font=font_h1, fill=(20, 25, 35, 255))
    draw.text((plate_x + 80, plate_y + 170), d["meta"], font=font_meta, fill=(100, 110, 130, 255))
    draw.line([(plate_x + 80, plate_y + 230), (plate_x + plate_w - 80, plate_y + 230)], fill=(210, 215, 225, 255), width=3)

    # Body before
    # Text wrap function
    def wrap_text(txt, font, max_width):
        words = txt.split(' ')
        lines, cur = [], ""
        for w in words:
            t = f"{cur} {w}".strip()
            bbox = font.getbbox(t)
            if bbox[2] - bbox[0] <= max_width: cur = t
            else:
                if cur: lines.append(cur)
                cur = w
        if cur: lines.append(cur)
        return lines

    cur_y = plate_y + 270
    for line in wrap_text(d["body_before"], font_body, plate_w - 160):
        draw.text((plate_x + 80, cur_y), line, font=font_body, fill=(40, 45, 55, 255))
        cur_y += 65

    # Highlight box
    cur_y += 30
    hl_lines = wrap_text(d["highlight"], font_callout, plate_w - 200)
    box_h = len(hl_lines) * 75 + 50
    draw.rounded_rectangle([plate_x + 60, cur_y, plate_x + plate_w - 60, cur_y + box_h], radius=16, fill=(235, 240, 250, 255), outline=d["accent"], width=3)
    hl_y = cur_y + 25
    for line in hl_lines:
        draw.text((plate_x + 100, hl_y), line, font=font_callout, fill=(15, 20, 30, 255))
        hl_y += 75

    # Footers
    draw.text((pad + 40, H - pad - 60), d["footer_left"], font=font_foot, fill=(150, 160, 175, 220))
    r_bbox = font_foot.getbbox(d["footer_right"])
    r_w = r_bbox[2] - r_bbox[0]
    draw.text((W - pad - 40 - r_w, H - pad - 60), d["footer_right"], font=font_foot, fill=d["accent"])

    img.save(png_path)
    print(f"  ✓ Saved PNG: {os.path.basename(png_path)}")

    # Render slow Ken-Burns motion video with ffmpeg
    dur = 10
    total_frames = dur * 24
    vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.00015,1.03)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"
    cmd = [
        ffmpeg_bin, "-y", "-loop", "1", "-i", png_path,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-t", str(dur),
        "-pix_fmt", "yuv420p", "-r", "24", mp4_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Rendered motion clip: {os.path.basename(mp4_path)} (10s 4K)")

print("All Block 4 Press Dossiers rendered!")
