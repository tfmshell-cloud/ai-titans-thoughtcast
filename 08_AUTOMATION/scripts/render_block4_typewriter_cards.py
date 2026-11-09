#!/usr/bin/env python3
"""
Render 4K (3840x2160 24fps) English Master Typewriter Thought Cards for Block 4 (Act 4)
Cards 14, 15, 16, 17
"""
import os, sys, subprocess, shutil
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
        "EP01_CARD_14_Physicality_Of_Compute.mp4",
        "THE PHYSICALITY OF INTELLIGENCE // STARGATE AMBITION",
        "“Artificial general intelligence is no longer abstract software. It is gigawatts of fusion plasma, subterranean cooling rivers, and millions of etched silicon transistors.”",
        "— THE STARGATE HYPOTHESIS (100-BILLION-DOLLAR CLUSTERS)",
        (100, 220, 255) # Electric Cyan / Fusion
    ),
    (
        "EP01_CARD_15_Seven_Trillion_Equation.mp4",
        "THE SEVEN TRILLION GAMBIT // SEMICONDUCTOR SOVEREIGNTY",
        "“Whoever controls the physical foundries of extreme ultraviolet light commands the sovereign operating system of global civilization.”",
        "— GLOBAL CHIP INITIATIVE (2024)",
        (255, 140, 60) # Foundry Amber
    ),
    (
        "EP01_CARD_16_Builders_Code_Three_Rules.mp4",
        "THE BUILDER’S CODE // THREE AXIOMS OF EXPONENTIAL LIFE",
        "“1. Irrational self-belief. 2. Treat crises as debugging algorithms. 3. Bet exclusively on ideas that compound.”",
        "— SAM ALTMAN, ESSAYS & PRINCIPLES",
        (120, 255, 180) # Emerald Mint
    ),
    (
        "EP01_CARD_17_Plastic_Reality_Finale.mp4",
        "THE PLASTIC REALITY // HORIZON OF AGI",
        "“The world is far more malleable than you were taught. Its rules are not etched in stone—they were written by people no smarter than you. The future does not happen to us; we build it.”",
        "— SAM ALTMAN // EPISODE 01 FINALE",
        (255, 215, 0) # Solar Gold
    ),
]

def render_card_video(filename, category, quote, author, accent_color, duration_sec=10, fps=24):
    out_path = os.path.join(out_dir, filename)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100000:
        print(f"  ✓ Already exists: {filename}")
        return

    print(f"Rendering: {filename}...")
    total_frames = duration_sec * fps
    type_duration_frames = int(3.5 * fps)
    
    # Calculate text wrap
    max_w = 2600
    words = quote.split(' ')
    lines = []
    cur_line = ""
    for w in words:
        test_line = f"{cur_line} {w}".strip()
        bbox = font_quote.getbbox(test_line)
        if (bbox[2] - bbox[0]) <= max_w:
            cur_line = test_line
        else:
            if cur_line: lines.append(cur_line)
            cur_line = w
    if cur_line: lines.append(cur_line)

    full_text = " ".join(lines)
    total_chars = len(full_text)

    tmp_dir = os.path.join(out_dir, f"tmp_{filename[:-4]}")
    os.makedirs(tmp_dir, exist_ok=True)

    try:
        for f_idx in range(total_frames):
            img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Draw card plate
            card_w, card_h = 2800, 1100
            card_x = (W - card_w) // 2
            card_y = (H - card_h) // 2

            # Semi-translucent dark slate plate
            draw.rounded_rectangle(
                [card_x, card_y, card_x + card_w, card_y + card_h],
                radius=32,
                fill=(12, 16, 24, 230),
                outline=(accent_color[0], accent_color[1], accent_color[2], 180),
                width=3
            )

            # Category Header
            draw.text((card_x + 80, card_y + 70), category, font=font_cat, fill=accent_color)
            draw.line([(card_x + 80, card_y + 130), (card_x + card_w - 80, card_y + 130)], fill=(accent_color[0], accent_color[1], accent_color[2], 80), width=2)

            # Typing progress
            if f_idx < type_duration_frames:
                chars_visible = int((f_idx / type_duration_frames) * total_chars)
                show_cursor = (f_idx // 4) % 2 == 0
            else:
                chars_visible = total_chars
                show_cursor = ((f_idx - type_duration_frames) // 12) % 2 == 0 and (f_idx < total_frames - 24)

            # Render visible quote text
            chars_drawn = 0
            y_offset = card_y + 180
            for line in lines:
                if chars_drawn >= chars_visible:
                    break
                line_len = len(line) + 1
                if chars_drawn + line_len <= chars_visible:
                    draw.text((card_x + 80, y_offset), line, font=font_quote, fill=(245, 245, 250, 255))
                    chars_drawn += line_len
                else:
                    visible_slice = chars_visible - chars_drawn
                    partial = line[:visible_slice]
                    draw.text((card_x + 80, y_offset), partial, font=font_quote, fill=(245, 245, 250, 255))
                    if show_cursor:
                        p_bbox = font_quote.getbbox(partial)
                        cx = card_x + 80 + (p_bbox[2] - p_bbox[0]) + 4
                        draw.rectangle([cx, y_offset + 8, cx + 18, y_offset + 64], fill=accent_color)
                    chars_drawn = chars_visible
                    break
                y_offset += 95

            # Render author
            if f_idx >= int(type_duration_frames * 0.8):
                draw.text((card_x + 80, card_y + card_h - 100), author, font=font_author, fill=(180, 185, 195, 220))

            frame_path = os.path.join(tmp_dir, f"frame_{f_idx:04d}.png")
            img.save(frame_path)

        # Encode with ffmpeg
        cmd = [
            ffmpeg_bin, "-y", "-r", str(fps),
            "-i", os.path.join(tmp_dir, "frame_%04d.png"),
            "-c:v", "libx264", "-pix_fmt", "yuva420p",
            "-preset", "fast", "-crf", "18",
            out_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  ✓ Finished: {filename}")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

for c in cards:
    render_card_video(c[0], c[1], c[2], c[3], c[4], duration_sec=10, fps=24)
