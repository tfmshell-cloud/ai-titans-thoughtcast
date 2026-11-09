#!/usr/bin/env python3
"""
Render 4K (3840x2160 24fps) English Master Typewriter Thought Cards for Block 2
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
        "EP01_CARD_06_Risk_Of_Standing_Still.mp4",
        "AXIOM OF VELOCITY // DYNAMICS OF EXPONENTIAL SCALING",
        "“People catastrophically underestimate the risk of standing still in an exponential world.”",
        "— SAM ALTMAN, Y COMBINATOR (2014)",
        (255, 176, 32) # Amber Gold
    ),
    (
        "EP01_CARD_07_Linear_Blind_Spot.mp4",
        "THE VENTURE PARADOX // COMPOUNDING HORIZONS",
        "“In an exponential regime, incremental progress is mathematically indistinguishable from failure.”",
        "— THE ROSEWOOD THESIS (JULY 2015)",
        (0, 229, 255) # Neon Cyan
    ),
    (
        "EP01_CARD_08_Scaling_Hypothesis.mp4",
        "FOUNDATIONAL HYPOTHESIS // THE ARCHITECTURE OF AGI",
        "“Compute and data do not merely optimize algorithms; they fundamentally transmute them into intelligence.”",
        "— OPENAI GENESIS AXIOM (2015–2018)",
        (255, 51, 102) # Deep Crimson
    ),
    (
        "EP01_CARD_09_Compute_Equation.mp4",
        "ECONOMIC REALITY // THE INDUSTRIAL ALLIANCE",
        "“We cannot save the world if we cannot afford the compute to verify our own equations.”",
        "— THE 2019 RESTRUCTURING THESIS",
        (0, 136, 255) # Royal Electric Blue
    ),
]

def render_card(filename, category, quote, author, accent_color):
    dst = os.path.join(out_dir, filename)
    print(f"Rendering: {filename}...")
    
    fps = 24
    total_seconds = 10.0
    total_frames = int(total_seconds * fps) # 240 frames
    type_duration_sec = 3.5 # typing duration
    type_frames = int(type_duration_sec * fps)
    
    # Pre-render card background
    card_w, card_h = 2800, 1100
    card_x = (W - card_w) // 2
    card_y = (H - card_h) // 2
    
    bg = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    
    # Draw translucent glass card
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + card_h],
        radius=32,
        fill=(10, 14, 22, 230),
        outline=accent_color,
        width=3
    )
    # Accent top border
    draw.line([card_x + 60, card_y, card_x + card_w - 60, card_y], fill=accent_color, width=8)
    
    # Draw static category text
    draw.text((card_x + 120, card_y + 110), category, font=font_cat, fill=accent_color)
    # Draw static author/subtitle text
    draw.text((card_x + 120, card_y + card_h - 150), author, font=font_author, fill=(160, 175, 195, 230))
    # Footer tag
    draw.text((card_x + card_w - 560, card_y + card_h - 150), "THOUGHTCAST // 4K CINEMATIC", font=font_cat, fill=(100, 115, 135, 180))

    # Text wrapping for quote
    max_quote_w = card_w - 240
    words = quote.split(' ')
    lines = []
    cur_line = []
    for w in words:
        test_line = ' '.join(cur_line + [w])
        bbox = draw.textbbox((0, 0), test_line, font=font_quote)
        if bbox[2] - bbox[0] > max_quote_w and cur_line:
            lines.append(' '.join(cur_line))
            cur_line = [w]
        else:
            cur_line.append(w)
    if cur_line:
        lines.append(' '.join(cur_line))
    
    full_text = '\n'.join(lines)
    total_chars = len(full_text)
    
    cmd = [
        ffmpeg_bin, '-y',
        '-f', 'image2pipe',
        '-vcodec', 'png',
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuva420p',
        '-r', str(fps),
        dst
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    
    quote_y_start = card_y + 240
    line_h = 100
    
    for f in range(total_frames):
        frame = bg.copy()
        f_draw = ImageDraw.Draw(frame)
        
        # Calculate chars visible
        if f < type_frames:
            char_count = int((f / type_frames) * total_chars)
        else:
            char_count = total_chars
            
        cur_chars = full_text[:char_count]
        
        # Draw visible lines
        drawn_chars = 0
        last_x, last_y = card_x + 120, quote_y_start
        for i, line in enumerate(lines):
            line_y = quote_y_start + i * line_h
            if drawn_chars + len(line) <= char_count:
                f_draw.text((card_x + 120, line_y), line, font=font_quote, fill=(245, 248, 255, 255))
                drawn_chars += len(line) + 1
                last_x = card_x + 120 + f_draw.textbbox((0, 0), line, font=font_quote)[2]
                last_y = line_y
            elif drawn_chars < char_count:
                sub_len = char_count - drawn_chars
                sub_line = line[:sub_len]
                f_draw.text((card_x + 120, line_y), sub_line, font=font_quote, fill=(245, 248, 255, 255))
                last_x = card_x + 120 + f_draw.textbbox((0, 0), sub_line, font=font_quote)[2]
                last_y = line_y
                drawn_chars += len(line) + 1
                break
            else:
                break
                
        # Pulsing cursor
        cursor_visible = (f % 12 < 8)
        if cursor_visible:
            f_draw.line([last_x + 6, last_y + 8, last_x + 6, last_y + 72], fill=accent_color, width=6)
            
        frame.save(proc.stdin, 'PNG')
        
    proc.stdin.close()
    proc.wait()
    print(f"✓ Created {dst} ({total_seconds}s, 4K)")

for name, cat, q, auth, col in cards:
    render_card(name, cat, q, auth, col)
print("\n🎉 ALL 4 BLOCK 2 ENGLISH TYPEWRITER CARDS RENDERED IN 4K!")
