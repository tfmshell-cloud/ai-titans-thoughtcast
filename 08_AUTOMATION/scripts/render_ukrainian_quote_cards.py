#!/usr/bin/env python3
"""
🎨 RENDER UKRAINIAN 4K MASTER TYPOGRAPHIC QUOTE CARDS
Dark Noir / Swiss Style with Frosted Obsidian Panel and Glow Accents
For Episode 01: Sam Altman
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards"
os.makedirs(out_dir, exist_ok=True)

W, H = 3840, 2160
font_title_path = "/System/Library/Fonts/HelveticaNeue.ttc"
font_code_path = "/System/Library/Fonts/Menlo.ttc"
font_serif_path = "/System/Library/Fonts/Supplemental/Georgia.ttf"

def draw_quote_card(filename, category, quote, author, accent_color=(245, 185, 65), font_size_quote=64, footer_tag="THOUGHTCAST 4K // AI TITANS // EP01: SAM ALTMAN"):
    # 1. Base dark obsidian canvas
    img = Image.new("RGBA", (W, H), (8, 10, 15, 255))
    draw = ImageDraw.Draw(img)

    # 2. Minimalist subtle background grid
    grid_color = (20, 26, 36, 255)
    for x in range(0, W, 120):
        draw.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 120):
        draw.line([(0, y), (W, y)], fill=grid_color, width=1)

    # 3. Main frosted container dimensions
    card_w, card_h = 2800, 1260
    cx1 = (W - card_w) // 2
    cy1 = (H - card_h) // 2
    cx2 = cx1 + card_w
    cy2 = cy1 + card_h

    # Subtle ambient glow behind card
    glow_box = [cx1 - 20, cy1 - 20, cx2 + 20, cy2 + 20]
    glow_col = (accent_color[0]//6, accent_color[1]//6, accent_color[2]//6, 80)
    draw.rounded_rectangle(glow_box, radius=40, fill=glow_col)

    # Frosted Obsidian Panel
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=32, fill=(14, 18, 25, 245), outline=(45, 55, 75, 255), width=2)

    # Top accent highlight line
    draw.rounded_rectangle([cx1, cy1, cx2, cy1 + 8], radius=4, fill=accent_color)

    # Decorative corner marks
    cross_size = 24
    for px, py in [(cx1 - 40, cy1 - 40), (cx2 + 40, cy1 - 40), (cx1 - 40, cy2 + 40), (cx2 + 40, cy2 + 40)]:
        draw.line([(px - cross_size, py), (px + cross_size, py)], fill=(60, 75, 95, 200), width=2)
        draw.line([(px, py - cross_size), (px, py + cross_size)], fill=(60, 75, 95, 200), width=2)

    # Fonts
    font_cat = ImageFont.truetype(font_code_path, 40)
    font_quote = ImageFont.truetype(font_title_path, font_size_quote)
    font_author = ImageFont.truetype(font_title_path, 48)
    font_meta = ImageFont.truetype(font_code_path, 32)
    font_large_quote_mark = ImageFont.truetype(font_serif_path, 180)

    # Category header
    cat_y = cy1 + 90
    draw.text((cx1 + 120, cat_y), f"// {category.upper()}", font=font_cat, fill=accent_color)

    # Divider line
    draw.line([(cx1 + 120, cat_y + 65), (cx2 - 120, cat_y + 65)], fill=(35, 45, 60, 255), width=2)

    # Large subtle quotation watermark
    draw.text((cx1 + 80, cat_y + 70), "“", font=font_large_quote_mark, fill=(accent_color[0]//4, accent_color[1]//4, accent_color[2]//4, 120))

    # Text wrapping logic
    # Clean explicit linebreaks first
    quote_paragraphs = quote.split("\n")
    lines = []
    max_line_width = card_w - 240

    for para in quote_paragraphs:
        words = para.split(" ")
        cur_line = []
        for w in words:
            test_line = " ".join(cur_line + [w])
            bbox = draw.textbbox((0, 0), test_line, font=font_quote)
            if bbox[2] - bbox[0] < max_line_width:
                cur_line.append(w)
            else:
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))

    # Render quote lines
    quote_y = cat_y + 160
    line_spacing = font_size_quote + 34
    for l in lines:
        draw.text((cx1 + 120, quote_y), l, font=font_quote, fill=(242, 246, 252, 255))
        quote_y += line_spacing

    # Author / Attribution
    author_y = cy2 - 150
    draw.text((cx1 + 120, author_y), author.upper(), font=font_author, fill=(180, 195, 215, 255))

    # Technical footer metadata
    meta_y = cy2 - 70
    draw.text((cx1 + 120, meta_y), footer_tag, font=font_meta, fill=(75, 90, 110, 255))
    draw.text((cx2 - 580, meta_y), "MASTER ARCHIVAL RECORD", font=font_meta, fill=(75, 90, 110, 255))

    out_path = os.path.join(out_dir, filename)
    img.save(out_path, "PNG")
    print(f"✓ Generated 4K Ukrainian Quote Card: {filename}")
    return out_path

cards_data = [
    (
        "EP01_UA_CARD_01_Extension_Of_Thought_Macintosh.png",
        "Інсайт дитинства // 1993 Macintosh LC II",
        "«Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю. Вона стала продовженням моєї думки».",
        "— Сем Альтман",
        (245, 185, 65), # Amber
        66
    ),
    (
        "EP01_UA_CARD_02_Psychological_Friction_Loopt.png",
        "Досвід Loopt // Інженерія волі",
        "«Більшість людей здаються не тому, що їхня ідея хибна. Вони здаються, тому що не здатні витримати психологічне тертя щоденних відмов».",
        "— Сем Альтман // 2012",
        (255, 170, 50), # Orange Amber
        64
    ),
    (
        "EP01_UA_CARD_03_Exponential_Risk_Manifesto.png",
        "Маніфест президента YC // 2014",
        "«Люди катастрофічно недооцінюють ризик того, що вони стоятимуть на місці у світі, який змінюється за експонентою».",
        "— Сем Альтман // Маніфест",
        (64, 224, 208), # Cyber Cyan
        64
    ),
    (
        "EP01_UA_CARD_04_Compute_Equations_Microsoft.png",
        "Реструктуризація OpenAI // 2019",
        "«Ми не зможемо врятувати світ, якщо у нас банально не вистачить обчислювальних потужностей перевірити власні рівняння».",
        "— Сем Альтман // Контракт з Microsoft",
        (50, 220, 150), # Emerald
        64
    ),
    (
        "EP01_UA_CARD_05_Guest_Badge_Nov2023.png",
        "Криза 17 листопада 2023 // 120 Годин",
        "«Перший і останній раз, коли я вдягаю цей бейдж».",
        "— Сем Альтман // Сан-Франциско, 19 листопада 2023",
        (255, 90, 95), # Crimson Rose
        70
    ),
    (
        "EP01_UA_CARD_06_730_Employees_Ultimatum.png",
        "Відкритий ультиматум // 20 листопада 2023",
        "«Або ви йдете у відставку і повертаєте Сема Альтмана, або ми всі негайно звільняємося слідом за ним».",
        "— 730 з 770 співробітників OpenAI",
        (255, 215, 0), # Pure Gold
        64
    ),
    (
        "EP01_UA_CARD_07_Three_Rules_Exponential_Life.png",
        "Уроки траєкторії // Три правила експоненти",
        "1. Не бійтеся ірраціональної віри в себе.\n2. Дивіться на проблеми як на код.\n3. Обирайте експоненту.",
        "— Закони побудови власного життя",
        (200, 225, 255), # Platinum Blue
        66
    ),
    (
        "EP01_UA_CARD_08_Plastic_Reality_Finale.png",
        "Фінал // Пластичність реальності",
        "«Світ набагато пластичніший, ніж вам здається з дитинства. Його правила не викарбувані на скрижалях — вони написані такими ж самими людьми, як ви».",
        "— Сем Альтман // Фінал епізоду",
        (255, 200, 80), # Golden Dawn
        64
    ),
]

if __name__ == "__main__":
    print("🎨 Generating 4K Ukrainian Typographic Quote Cards...")
    for fn, cat, q, a, col, fs in cards_data:
        draw_quote_card(fn, cat, q, a, col, fs)
    print("✓ All 8 Ukrainian Quote Cards successfully generated!")
