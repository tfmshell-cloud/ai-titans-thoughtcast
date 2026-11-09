#!/usr/bin/env python3
"""
Render 4K (3840x2160 24fps) English Master Typewriter Thought Cards
With Letter-by-Letter Animated Text Appearance & Blinking Accent Cursor
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
        "EP01_CARD_01_Extension_Of_Thought.mp4",
        "CHILDHOOD INSIGHT // 1993 MACINTOSH LC II",
        "“This machine blurred the line between my internal world and external reality. It became an extension of my thought.”",
        "— SAM ALTMAN",
        (235, 175, 75) # Amber Gold
    ),
    (
        "EP01_CARD_02_Indifference_To_Authority.mp4",
        "AXIOM OF CODE // FUNDAMENTAL LAW OF THE SYSTEM",
        "“The machine is indifferent to authority. It knows no grievance. It never punishes the attempt — only a syntax error, a bug you can fix in five minutes.”",
        "— LESSON OF THE FIRST COMPUTER",
        (64, 224, 208) # Cyan Neon
    ),
    (
        "EP01_CARD_03_Autonomy_Equation.mp4",
        "BURROUGHS SCHOOL // THE FORMULA OF AUTONOMY",
        "“When you state your most vulnerable truth out loud — fear evaporates, and the system loses its leverage over you.”",
        "— ST. LOUIS, AGE 16",
        (240, 90, 80) # Warm Crimson
    ),
    (
        "EP01_CARD_04_Linear_Vs_Exponential.mp4",
        "STANFORD 2005 // LINEAR TIME VS THE EXPONENTIAL",
        "“Lectures, semester cycles, exams — that is linear time. But the silicon world outside campus was already breathing the exponential.”",
        "— DROPPING OUT OF STANFORD AT 19",
        (130, 180, 255) # Electric Blue
    ),
    (
        "EP01_CARD_05_Psychological_Friction.mp4",
        "THE LOOPT ODYSSEY // THE ENGINEERING OF WILL",
        "“Most people don’t quit because their idea is wrong. They quit because they cannot endure the psychological friction of relentless daily rejection.”",
        "— SAM ALTMAN, 2012",
        (255, 215, 0) # Gold
    ),
]

def render_card(filename, category, quote, author, accent_color):
    dst = os.path.join(out_dir, filename)
    print(f"\nRendering {filename} in 4K with Typewriter Effect...")
    
    card_w, card_h = 2800, 1200
    cx1, cy1 = (W - card_w) // 2, (H - card_h) // 2
    cat_y = cy1 + 100
    quote_y = cat_y + 140
    line_h = 95
    max_text_w = card_w - 240

    # Wrap quote lines
    dummy = Image.new('RGB', (100, 100))
    draw_d = ImageDraw.Draw(dummy)
    words = quote.split(' ')
    lines = []
    cur_line = []
    for w in words:
        test_line = ' '.join(cur_line + [w])
        bbox = draw_d.textbbox((0, 0), test_line, font=font_quote)
        if bbox[2] - bbox[0] < max_text_w:
            cur_line.append(w)
        else:
            lines.append(' '.join(cur_line))
            cur_line = [w]
    if cur_line:
        lines.append(' '.join(cur_line))

    # Base background
    base_img = Image.new('RGB', (W, H), (10, 13, 18))
    draw = ImageDraw.Draw(base_img)
    for x in range(0, W, 120):
        draw.line([(x, 0), (x, H)], fill=(25, 30, 40), width=1)
    for y in range(0, H, 120):
        draw.line([(0, y), (W, y)], fill=(25, 30, 40), width=1)

    draw.rounded_rectangle([cx1, cy1, cx1 + card_w, cy1 + card_h], radius=32, fill=(16, 20, 28), outline=(50, 60, 80), width=2)
    draw.rounded_rectangle([cx1, cy1, cx1 + card_w, cy1 + 8], radius=4, fill=accent_color)
    draw.text((cx1 + 120, cat_y), category, font=font_cat, fill=accent_color)
    draw.line([(cx1 + 120, cat_y + 70), (cx1 + card_w - 120, cat_y + 70)], fill=(40, 50, 65), width=2)
    draw.text((cx1 + 120, cy1 + card_h - 140), author, font=font_author, fill=(160, 175, 195))
    draw.text((cx1 + 120, cy1 + card_h - 70), "THOUGHTCAST // EP01: SAM ALTMAN // ARCHITECTS OF MIND", font=font_cat, fill=(80, 95, 115))
    draw.text((cx1 + card_w - 500, cy1 + card_h - 70), "4K 24FPS CINEMATIC", font=font_cat, fill=(80, 95, 115))

    total_chars = sum(len(l) for l in lines)
    total_frames = 240 # 10s at 24fps
    type_frames = 96  # 4s typing

    cmd = [
        ffmpeg_bin, '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}',
        '-pix_fmt', 'rgb24',
        '-r', '24',
        '-i', '-',
        '-c:v', 'libx264',
        '-preset', 'veryfast',
        '-pix_fmt', 'yuv420p',
        '-r', '24',
        dst
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    t0 = time.time()
    for f in range(total_frames):
        frame_img = base_img.copy()
        fdraw = ImageDraw.Draw(frame_img)
        
        if f < type_frames:
            visible_count = int(total_chars * (f / float(type_frames)))
        else:
            visible_count = total_chars

        last_x, last_y = cx1 + 120, quote_y
        for l_idx, line in enumerate(lines):
            line_chars = len(line)
            prev_chars = sum(len(lines[i]) for i in range(l_idx))
            if visible_count <= prev_chars:
                break
            chars_to_draw = min(line_chars, visible_count - prev_chars)
            sub_str = line[:chars_to_draw]
            cur_y = quote_y + l_idx * line_h
            fdraw.text((cx1 + 120, cur_y), sub_str, font=font_quote, fill=(240, 244, 250))
            
            if chars_to_draw > 0:
                bbox = fdraw.textbbox((cx1 + 120, cur_y), sub_str, font=font_quote)
                last_x = bbox[2] + 4
                last_y = cur_y

        show_cursor = False
        if f < type_frames:
            show_cursor = True
        elif f < 144:
            show_cursor = (f // 8) % 2 == 0
        
        if show_cursor:
            fdraw.rectangle([last_x, last_y + 10, last_x + 6, last_y + 70], fill=accent_color)

        proc.stdin.write(frame_img.tobytes())

    proc.stdin.close()
    proc.wait()
    dur_render = time.time() - t0
    print(f"  ✓ Rendered {filename} in {dur_render:.2f}s ({os.path.getsize(dst)/1024/1024:.2f} MB)")

if __name__ == "__main__":
    t_start = time.time()
    for fn, cat, q, a, col in cards:
        render_card(fn, cat, q, a, col)
    print(f"\nAll 5 English Typewriter Cards rendered successfully in {time.time()-t_start:.2f}s!")
