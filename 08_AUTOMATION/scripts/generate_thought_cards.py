#!/usr/bin/env python3
"""
Generate 4K (3840x2160) Master Graphic Thought Cards for Episode 01 Act 1
"""
import os
from PIL import Image, ImageDraw, ImageFont

out_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/dossiers_press"
os.makedirs(out_dir, exist_ok=True)

W, H = 3840, 2160
font_title_path = "/System/Library/Fonts/HelveticaNeue.ttc"
font_code_path = "/System/Library/Fonts/Supplemental/Courier New.ttf"

def draw_card(filename, category, quote, author, accent_color=(235, 175, 75)):
    # Create base dark obsidian image
    img = Image.new("RGBA", (W, H), (10, 13, 18, 255))
    draw = ImageDraw.Draw(img)

    # Subtle background vignette / grid
    grid_color = (25, 30, 40, 255)
    for x in range(0, W, 120):
        draw.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 120):
        draw.line([(0, y), (W, y)], fill=grid_color, width=1)

    # Center card container
    card_w, card_h = 2800, 1200
    cx1 = (W - card_w) // 2
    cy1 = (H - card_h) // 2
    cx2 = cx1 + card_w
    cy2 = cy1 + card_h

    # Card background (frosted obsidian panel)
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=32, fill=(16, 20, 28, 240), outline=(50, 60, 80, 255), width=2)
    # Accent top border
    draw.rounded_rectangle([cx1, cy1, cx2, cy1 + 8], radius=4, fill=accent_color)

    # Fonts
    font_cat = ImageFont.truetype(font_code_path, 42)
    font_quote = ImageFont.truetype(font_title_path, 68)
    font_author = ImageFont.truetype(font_title_path, 48)

    # Category badge
    cat_y = cy1 + 100
    draw.text((cx1 + 120, cat_y), category.upper(), font=font_cat, fill=accent_color)

    # Divider
    draw.line([(cx1 + 120, cat_y + 70), (cx2 - 120, cat_y + 70)], fill=(40, 50, 65, 255), width=2)

    # Word wrap quote
    words = quote.split(' ')
    lines = []
    cur_line = []
    for w in words:
        test_line = ' '.join(cur_line + [w])
        bbox = draw.textbbox((0, 0), test_line, font=font_quote)
        if bbox[2] - bbox[0] < card_w - 240:
            cur_line.append(w)
        else:
            lines.append(' '.join(cur_line))
            cur_line = [w]
    if cur_line:
        lines.append(' '.join(cur_line))

    # Draw quote lines
    quote_y = cat_y + 140
    line_h = 95
    for l in lines:
        draw.text((cx1 + 120, quote_y), l, font=font_quote, fill=(240, 244, 250, 255))
        quote_y += line_h

    # Author / Source
    author_y = cy2 - 140
    draw.text((cx1 + 120, author_y), author.upper(), font=font_author, fill=(160, 175, 195, 255))

    # Corner technical markings
    draw.text((cx1 + 120, cy2 - 70), "THOUGHTCAST // EP01: SAM ALTMAN // ARCHITECTS OF MIND", font=font_cat, fill=(80, 95, 115, 255))
    draw.text((cx2 - 500, cy2 - 70), "4K 24FPS CINEMATIC", font=font_cat, fill=(80, 95, 115, 255))

    out_path = os.path.join(out_dir, filename)
    img.save(out_path, "PNG")
    print(f"Generated 4K Thought Card: {filename}")

cards = [
    (
        "EP01_CARD_01_Extension_Of_Thought.png",
        "Інсайт дитинства // 1993 Macintosh LC II",
        "«Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю. Вона стала продовженням моєї думки».",
        "— Сем Альтман",
        (235, 175, 75) # Warm Amber
    ),
    (
        "EP01_CARD_02_Indifference_To_Authority.png",
        "Аксіома коду // Фундаментальний закон системи",
        "«Машина байдужа до авторитетів. Вона не знає образи. Вона карає не за спробу, а лише за синтаксичну помилку — баг, який можна переписати за п'ять хвилин».",
        "— Урок першого комп'ютера",
        (64, 224, 208) # Cyan Neon
    ),
    (
        "EP01_CARD_03_Autonomy_Equation.png",
        "Урок школи Burroughs // Формула автономії",
        "«Коли ти сам голосно вимовляєш свою найбільш вразливу правду — страх розсіюється, а в системи зникає важіль тиску на тебе».",
        "— Сент-Луїс, 16 років",
        (240, 90, 80) # Warm Crimson
    ),
    (
        "EP01_CARD_04_Linear_Vs_Exponential.png",
        "Стенфорд 2005 // Лінійний час проти експоненти",
        "«Лекції, семестрові цикли, іспити — це лінійний час. А кремнієвий світ за межами кампусу вже дихав експонентою».",
        "— Відхід зі Стенфорду у 19 років",
        (130, 180, 255) # Electric Blue
    ),
    (
        "EP01_CARD_05_Psychological_Friction.png",
        "Досвід Loopt // Інженерія волі",
        "«Більшість людей здаються не тому, що їхня ідея хибна. Вони здаються, тому що не здатні витримати психологічне тертя щоденних відмов».",
        "— Сем Альтман, 2012",
        (255, 215, 0) # Gold
    ),
]

for fn, cat, q, a, col in cards:
    draw_card(fn, cat, q, a, col)
