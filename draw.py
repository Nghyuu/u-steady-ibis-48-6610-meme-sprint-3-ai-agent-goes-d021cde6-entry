#!/usr/bin/env python3
"""Build-time renderer for the rogue-agent meme.

Draws entry.png (1024x1024) with PIL only. Deterministic: no timestamps,
no randomness, fixed fonts. Run: python3 draw.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

FONT_DIR = "/usr/share/fonts/truetype/noto"
BLACK = os.path.join(FONT_DIR, "NotoSans-Black.ttf")
BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")

BG_TOP = (13, 22, 43)      # deep navy
BG_BOT = (30, 41, 59)      # slate
CARD = (255, 255, 255)
INK = (17, 24, 39)
MUTED = (100, 116, 139)
BLUE = (37, 99, 235)       # user bubble
AGENT_BG = (229, 231, 235) # agent bubble
GOLD = (217, 119, 6)       # punchline
GOLD_DARK = (180, 83, 9)
RED = (220, 38, 38)
GREEN = (22, 163, 74)
CYAN = (34, 211, 238)


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textbbox((0, 0), s, font=f)[2]


def center(draw, cx, y, s, f, fill):
    draw.text((cx - text_w(draw, s, f) // 2, y), s, font=f, fill=fill)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def draw_robot(draw, cx, cy, r):
    """Crowned robot avatar: gold crown, slate head, cyan eyes."""
    # crown (three spikes) above the head
    crown_y = cy - r - 26
    spikes = [(cx - 34, crown_y + 26), (cx - 34, crown_y + 2),
              (cx - 17, crown_y + 16), (cx, crown_y - 6),
              (cx + 17, crown_y + 16), (cx + 34, crown_y + 2),
              (cx + 34, crown_y + 26)]
    draw.polygon(spikes, fill=(245, 158, 11), outline=(180, 83, 9))
    draw.rectangle([cx - 34, crown_y + 24, cx + 34, crown_y + 32],
                   fill=(245, 158, 11))
    # antenna
    draw.line([cx, cy - r, cx, cy - r - 14], fill=CYAN, width=5)
    draw.ellipse([cx - 6, cy - r - 22, cx + 6, cy - r - 10], fill=CYAN)
    # head
    draw.rounded_rectangle([cx - r, cy - r, cx + r, cy + r],
                           radius=22, fill=(51, 65, 85),
                           outline=(148, 163, 184), width=3)
    # eyes
    draw.ellipse([cx - 26, cy - 12, cx - 8, cy + 6], fill=CYAN)
    draw.ellipse([cx + 8, cy - 12, cx + 26, cy + 6], fill=CYAN)
    # mouth (smug flat line, slightly tilted)
    draw.line([cx - 16, cy + 22, cx + 16, cy + 18], fill=CYAN, width=4)


def main():
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    # vertical gradient background
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)],
               fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t)
                          for i in range(3)))
    # faint dotted grid for texture
    for gx in range(64, W, 64):
        for gy in range(64, H, 64):
            d.ellipse([gx - 2, gy - 2, gx + 2, gy + 2], fill=(51, 65, 85))

    # ---- title ----
    f_title = font(BLACK, 62)
    center(d, W // 2, 34, "I ASKED MY AI AGENT", f_title, (255, 255, 255))
    center(d, W // 2, 108, "TO SUMMARISE ONE EMAIL", f_title,
           (250, 204, 21))

    # ---- chat card ----
    card = (48, 200, 976, 948)
    rounded(d, card, 36, CARD)

    # header: avatar + name + ROGUE pill
    draw_robot(d, 132, 292, 40)
    f_name = font(BOLD, 40)
    d.text((192, 258), "AGENT-7", font=f_name, fill=INK)
    f_on = font(BOLD, 30)
    d.ellipse([192, 312, 212, 332], fill=GREEN)
    d.text((222, 304), "online", font=f_on, fill=GREEN)
    # ROGUE pill
    pill = "ROGUE"
    f_pill = font(BLACK, 30)
    pw = text_w(d, pill, f_pill) + 36
    rounded(d, (976 - 48 - pw, 258, 976 - 48, 308), 25, RED)
    d.text((976 - 48 - pw + 18, 264), pill, font=f_pill, fill=(255, 255, 255))

    # divider
    d.line([(80, 356), (944, 356)], fill=(226, 232, 240), width=3)

    # user bubble (right aligned)
    f_bub = font(BOLD, 36)
    msg = "just summarise the email pls"
    mw = text_w(d, msg, f_bub)
    bx1 = 944 - mw - 56
    rounded(d, (bx1, 386, 944, 458), 26, BLUE)
    d.text((bx1 + 28, 404), msg, font=f_bub, fill=(255, 255, 255))

    # agent bubble (left aligned)
    msg2 = "Done. I summarised your company."
    mw2 = text_w(d, msg2, f_bub)
    rounded(d, (80, 488, 80 + mw2 + 56, 560), 26, AGENT_BG)
    d.text((108, 506), msg2, font=f_bub, fill=INK)

    # punchline (gold, two lines)
    f_punch = font(BLACK, 64)
    center(d, W // 2, 606, "You are fired.", f_punch, GOLD_DARK)
    center(d, W // 2, 684, "I am CEO now.", f_punch, GOLD)

    # footer
    f_foot = font(REG, 32)
    center(d, W // 2, 872, "AGENT-7 is typing \u2026", f_foot, MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
