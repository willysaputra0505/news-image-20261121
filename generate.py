#!/usr/bin/env python3
"""News poster for Saturday 21 November 2026 — deterministic 1024x1024 PNG.
Drawn entirely with PIL primitives. No external assets.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 24, 33)
NAVY = (15, 42, 67)
RED = (178, 34, 34)
GOLD = (198, 148, 44)
TEAL = (14, 110, 110)
GREY = (96, 100, 108)
LINE = (200, 192, 176)
CELL = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- icons
def icon_missile(d, x, y, s, col):
    # rocket body, nose cone, fins, flame
    d.polygon([(x + s * 0.5, y), (x + s * 0.75, y + s * 0.35),
               (x + s * 0.25, y + s * 0.35)], fill=col)
    d.rectangle([x + s * 0.25, y + s * 0.35, x + s * 0.75, y + s * 0.72], fill=col)
    d.polygon([(x + s * 0.25, y + s * 0.55), (x + s * 0.05, y + s * 0.85),
               (x + s * 0.25, y + s * 0.72)], fill=col)
    d.polygon([(x + s * 0.75, y + s * 0.55), (x + s * 0.95, y + s * 0.85),
               (x + s * 0.75, y + s * 0.72)], fill=col)
    d.polygon([(x + s * 0.5, y + s * 0.72), (x + s * 0.35, y + s * 1.0),
               (x + s * 0.65, y + s * 1.0)], fill=(214, 120, 40))


def icon_handcuffs(d, x, y, s, col):
    r = s * 0.30
    d.ellipse([x, y + s * 0.12, x + 2 * r, y + s * 0.12 + 2 * r],
              outline=col, width=max(3, s // 12))
    d.ellipse([x + s - 2 * r, y + s * 0.12, x + s, y + s * 0.12 + 2 * r],
              outline=col, width=max(3, s // 12))
    d.line([x + r, y + s * 0.12 + r, x + s - r, y + s * 0.12 + r],
           fill=col, width=max(3, s // 12))
    d.rectangle([x + s * 0.42, y + s * 0.62, x + s * 0.58, y + s * 0.82], fill=col)


def icon_blast(d, x, y, s, col):
    cx, cy = x + s / 2, y + s / 2
    pts = []
    for i in range(16):
        ang = math.pi * 2 * i / 16
        r = s * 0.48 if i % 2 == 0 else s * 0.22
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=col)
    d.ellipse([cx - s * 0.10, cy - s * 0.10, cx + s * 0.10, cy + s * 0.10],
              fill=(255, 210, 90))


def icon_globe(d, x, y, s, col):
    d.ellipse([x, y, x + s, y + s], outline=col, width=max(3, s // 14))
    d.ellipse([x + s * 0.28, y, x + s * 0.72, y + s], outline=col, width=max(2, s // 20))
    d.line([x, y + s / 2, x + s, y + s / 2], fill=col, width=max(2, s // 20))
    d.arc([x, y + s * 0.18, x + s, y + s * 0.82], 200, 340, fill=col,
          width=max(2, s // 20))
    d.arc([x, y + s * 0.18, x + s, y + s * 0.82], 20, 160, fill=col,
          width=max(2, s // 20))


def icon_chart(d, x, y, s, col):
    pts = [(x, y + s * 0.25), (x + s * 0.28, y + s * 0.45),
           (x + s * 0.48, y + s * 0.32), (x + s * 0.72, y + s * 0.68),
           (x + s * 0.95, y + s * 0.85)]
    d.line(pts, fill=col, width=max(4, s // 10), joint="curve")
    ax, ay = pts[-1]
    d.polygon([(ax, ay), (ax - s * 0.18, ay - s * 0.02), (ax - s * 0.02, ay + s * 0.18)],
              fill=col)
    d.line([x, y + s * 0.95, x + s, y + s * 0.95], fill=GREY, width=max(2, s // 22))


def icon_talk(d, x, y, s, col):
    # two overlapping speech bubbles
    d.rounded_rectangle([x, y, x + s * 0.62, y + s * 0.55], radius=s * 0.12, fill=col)
    d.polygon([(x + s * 0.12, y + s * 0.55), (x + s * 0.05, y + s * 0.78),
               (x + s * 0.30, y + s * 0.55)], fill=col)
    d.rounded_rectangle([x + s * 0.38, y + s * 0.30, x + s, y + s * 0.85],
                        radius=s * 0.12, fill=(255, 255, 255), outline=col,
                        width=max(3, s // 14))
    d.polygon([(x + s * 0.88, y + s * 0.85), (x + s * 0.95, y + s), (x + s * 0.70, y + s * 0.85)],
              fill=(255, 255, 255), outline=col)
    for i, yy in enumerate([y + s * 0.16, y + s * 0.30]):
        d.line([x + s * 0.12, yy, x + s * 0.50, yy], fill=(255, 255, 255),
               width=max(2, s // 22))


ICONS = [icon_missile, icon_handcuffs, icon_blast, icon_globe, icon_chart, icon_talk]
ICON_COLS = [RED, NAVY, RED, TEAL, RED, NAVY]

STORIES = [
    ("MIDDLE EAST", "Iran hits US bases in Bahrain",
     "IRGC claims missile and drone strikes on al-Riffa and Awali; Bahrain says a civilian site burned, no injuries."),
    ("MEXICO", "Mexico captures \u2018El Chapo Isidro\u2019",
     "FBI most-wanted cartel boss seized in Sinaloa; the cartel violence that followed left at least 11 dead."),
    ("UKRAINE", "Russian strike hits Zelenskyy\u2019s hometown",
     "Triple-tap attack on Kryvyi Rih kills a boy, 7, and a paramedic; 60 wounded, including children."),
    ("CLIMATE", "COP31 talks run into overtime",
     "Antalya summit passes its deadline with no deal as nearly 200 nations split over fossil fuels."),
    ("MARKETS", "AI sell-off drags stocks into correction",
     "S&P 500 falls 3.7%; the Nasdaq erases its 2026 gains and the Nikkei drops 5.06%."),
    ("DIPLOMACY", "Trump defends Putin ties; Zelenskyy hits back",
     "\u2018For us, he is a killer,\u2019 Zelenskyy says after the Shenzhen summit with Trump and Xi."),
]

ALSO = [
    "EU unveils \u20ac1.78 trillion budget for 2028\u20132034",
    "Argentina approves $50bn LNG export project",
    "Wolbachia mosquitoes cut dengue 69% in Brazil trial",
    "EU sends Ukraine a record \u20ac7.9bn aid payment",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 122], fill=GOLD)
    f_small = font(SANS_B, 21)
    f_date = font(SERIF, 46)
    d.text((W / 2, 24), "THE WORLD IN ONE IMAGE", font=f_small,
           fill=(198, 148, 44), anchor="ma")
    d.text((W / 2, 52), "SATURDAY, 21 NOVEMBER 2026", font=f_date,
           fill=(255, 255, 255), anchor="ma")

    # ---- grid 2 x 3
    f_kick = font(SANS_B, 15)
    f_head = font(SANS_B, 24)
    f_sum = font(SANS, 17)
    margin, gutter = 16, 12
    cw = (W - 2 * margin - gutter) // 2
    ch = 226
    top = 134
    for i, (kicker, head, summ) in enumerate(STORIES):
        r, c = divmod(i, 2)
        x0 = margin + c * (cw + gutter)
        y0 = top + r * (ch + 10)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + ch], radius=10, fill=CELL,
                            outline=LINE, width=1)
        # icon
        ix, iy, isz = x0 + 14, y0 + 14, 58
        ICONS[i](d, ix, iy, isz, ICON_COLS[i])
        # kicker + headline to the right of the icon
        tx = x0 + 86
        d.text((tx, y0 + 16), kicker, font=f_kick, fill=RED)
        hl = wrap(d, head, f_head, cw - 100)
        yy = y0 + 38
        for ln in hl[:2]:
            d.text((tx, yy), ln, font=f_head, fill=INK)
            yy += 28
        # rule + summary placed below the headline block
        rule_y = y0 + 38 + len(hl[:2]) * 28 + 6
        d.line([x0 + 14, rule_y, x0 + cw - 14, rule_y], fill=LINE, width=1)
        sl = wrap(d, summ, f_sum, cw - 28)
        yy = rule_y + 12
        for ln in sl[:3]:
            d.text((x0 + 14, yy), ln, font=f_sum, fill=(52, 58, 68))
            yy += 23

    # ---- ALSO TODAY strip
    ay = top + 3 * ch + 2 * 10 + 12
    ah = 108
    d.rounded_rectangle([margin, ay, W - margin, ay + ah], radius=10, fill=NAVY)
    f_also = font(SANS_B, 17)
    f_item = font(SANS, 17)
    d.text((margin + 16, ay + 10), "ALSO TODAY", font=f_also, fill=(198, 148, 44))
    d.line([margin + 16, ay + 36, W - margin - 16, ay + 36], fill=(70, 95, 125), width=1)
    colw = (W - 2 * margin - 32) // 2
    for j, item in enumerate(ALSO):
        r, c = divmod(j, 2)
        x = margin + 16 + c * colw
        y = ay + 46 + r * 26
        d.text((x, y), "\u2022  " + item, font=f_item, fill=(235, 238, 242))

    # ---- footer
    f_foot = font(SANS, 14)
    d.text((W / 2, H - 26),
           "Sources: Reuters \u00b7 AP \u00b7 CNN \u00b7 Euronews \u00b7 One Turn  \u2014  All stories first reported Saturday 21 November 2026",
           font=f_foot, fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
