#!/usr/bin/env python3
"""
Render 4K (3840x2160 24fps) English Master Typewriter Thought Cards for Block 3 (Act 3)
Cards 10, 11, 12, 13
"""
import os, sys, time, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 3840, 2160
ffmpeg_bin = '/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg'
font_title_path = '/System/Library/Fonts/HelveticaNeue.ttc'
font_code_path = '/System/Library/Fonts/Supplemental/Courier New.ttf'

font_cat = ImageFont.truetype(font_code_path, 42)
font_quote = ImageFont.truetype(font_title_path, 68)
font_author = ImageFont.truetype(font_title_path, 48)

out_dir = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/dossiers_press'
os.makedirs(out_dir, exist_ok=True)

cards = [
    (
        "EP01_CARD_10_Exponential_Adoption.mp4",
        "CONSUMER VELOCITY // EXPONENTIAL ADOPTION",
        "“Within five days, one million users. Within two months, one hundred million. The fastest-growing consumer product in human history.”",
        "— CHATGPT LAUNCH (NOVEMBER 30, 2022)",
        (235, 175, 75) # Amber Gold
    ),
    (
        "EP01_CARD_11_Citadel_Paradox.mp4",
        "THE CITADEL PARADOX // INSTITUTIONAL FRAGILITY",
        "“The architect of the AI boom has been cast out of his own citadel. Without warning, the technology industry froze.”",
        "— FRIDAY BOARD COUP (NOVEMBER 17, 2023)",
        (240, 90, 80) # Warm Crimson
    ),
    (
        "EP01_CARD_12_Loyalty_Axiom.mp4",
        "THE LOYALTY AXIOM // THE NATURE OF POWER",
        "“First and last time I ever wear one of these.”",
        "— SAM ALTMAN, VISITOR BADGE (NOVEMBER 19, 2023)",
        (130, 180, 255) # Electric Blue
    ),
    (
        "EP01_CARD_13_Paradigm_Of_Power.mp4",
        "THE PARADIGM OF POWER // MISSION CONVICTION",
        "“Authority is not anchored in legal bylaws or corporate titles. It rests entirely on the shared faith of an elite team in the scale of the mission.”",
        "— TRIUMPHANT RETURN (NOVEMBER 22, 2023)",
        (212, 175, 55) # Emerald Gold
    ),
]

def render_card_video(filename, category, quote, author, accent_color, duration_sec=10, fps=24):
    out_path = os.path.join(out_dir, filename)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100000:
        print(f"  ✓ Already exists: {filename}")
        return

    print(f"Rendering: {filename}...")
    total_frames = duration_sec * fps
    type_duration_frames = int(3.5 * fps) # 3.5 seconds to type out

    # Pre-wrap quote
    card_w = 2800
    words = quote.split(' ')
    lines = []
    cur_line = []
    dummy_img = Image.new("RGBA", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_img)

    for w in words:
        test_line = ' '.join(cur_line + [w])
        bbox = dummy_draw.textbbox((0, 0), test_line, font=font_quote)
        if bbox[2] - bbox[0] < card_w - 240:
            cur_line.append(w)
        else:
            lines.append(' '.join(cur_line))
            cur_line = [w]
    if cur_line:
        lines.append(' '.join(cur_line))

    full_quote = '\n'.join(lines)
    total_chars = len(full_quote)

    cmd = [
        ffmpeg_bin, '-y',
        '-f', 'image2pipe',
        '-vcodec', 'png',
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-preset', 'veryfast',
        '-crf', '19',
        '-pix_fmt', 'yuv420p',
        out_path
    ]

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cx1 = (W - 2800) // 2
    cy1 = (H - 1200) // 2
    cx2 = cx1 + 2800
    cy2 = cy1 + 1200

    base_frame = Image.new("RGBA", (W, H), (10, 13, 18, 255))
    draw_base = ImageDraw.Draw(base_frame)

    grid_color = (25, 30, 40, 255)
    for x in range(0, W, 120):
        draw_base.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 120):
        draw_base.line([(0, y), (W, y)], fill=grid_color, width=1)

    draw_base.rounded_rectangle([cx1, cy1, cx2, cy2], radius=32, fill=(16, 20, 28, 240), outline=(50, 60, 80, 255), width=2)
    draw_base.rounded_rectangle([cx1, cy1, cx2, cy1 + 8], radius=4, fill=accent_color)

    cat_y = cy1 + 100
    draw_base.text((cx1 + 120, cat_y), category.upper(), font=font_cat, fill=accent_color)
    draw_base.line([(cx1 + 120, cat_y + 70), (cx2 - 120, cat_y + 70)], fill=(40, 50, 65, 255), width=2)

    author_y = cy2 - 140
    draw_base.text((cx1 + 120, author_y), author.upper(), font=font_author, fill=(160, 175, 195, 255))
    draw_base.text((cx1 + 120, cy2 - 70), "THOUGHTCAST // 4K CINEMATIC", font=font_cat, fill=(80, 95, 115, 255))

    for f_idx in range(total_frames):
        if f_idx < type_duration_frames:
            char_count = int((f_idx / float(type_duration_frames)) * total_chars)
        else:
            char_count = total_chars

        visible_text = full_quote[:char_count]

        frame = base_frame.copy()
        draw = ImageDraw.Draw(frame)

        quote_y = cat_y + 140
        line_h = 95
        cur_lines = visible_text.split('\n')
        for i, l in enumerate(cur_lines):
            draw.text((cx1 + 120, quote_y), l, font=font_quote, fill=(240, 244, 250, 255))
            if i == len(cur_lines) - 1:
                if (f_idx // 8) % 2 == 0:
                    bbox = draw.textbbox((cx1 + 120, quote_y), l, font=font_quote)
                    cursor_x = bbox[2] + 8
                    draw.text((cursor_x, quote_y), "|", font=font_quote, fill=accent_color)
            quote_y += line_h

        frame.save(p.stdin, 'PNG')

    p.stdin.close()
    p.wait()
    print(f"  ✓ Rendered {filename}")

for fn, cat, q, a, col in cards:
    render_card_video(fn, cat, q, a, col)

print("🎉 ALL 4 BLOCK 3 ENGLISH TYPEWRITER CARDS RENDERED!")
