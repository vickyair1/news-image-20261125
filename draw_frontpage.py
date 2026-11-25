#!/usr/bin/env python3
"""news-image-20261125 round 2 — Wednesday 25 November 2026 in one image.

Draws a 1024x1024 broadsheet front page with PIL only. No network, no
randomness, no timestamps: the same input always writes the same bytes.
Writes /output/entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 230)
INK = (17, 17, 17)
RED = (163, 18, 18)
NAVY = (26, 42, 74)
GREY = (90, 86, 76)
LINE = (120, 112, 92)
OCEAN = (223, 232, 234)
LAND = (232, 221, 192)
LANDB = (138, 127, 95)

FD = "/usr/share/fonts/truetype/dejavu"
FL = "/usr/share/fonts/truetype/liberation"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF = f"{FD}/DejaVuSerif-Bold.ttf"
SERIF_R = f"{FD}/DejaVuSerif.ttf"
SANS = f"{FD}/DejaVuSans.ttf"
SANS_B = f"{FD}/DejaVuSans-Bold.ttf"


def wrap(d, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, fnt, fill, leading):
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories
# Illustrated stories 1-12. Region values feed the masthead tally.
LEADS = [
    dict(n=1, scene="rocket", tag="LIFTOFF", city="JIUQUAN, CHINA",
         region="Asia-Pacific", lon=100.3, lat=40.9,
         head="Shenzhou-24 lifts off with a Pakistani pilot aboard",
         deck="Long March 2F launches at 00:18 UTC; the crew docks "
              "at Tiangong 3 1/2 hours later.",
         src="REUTERS · XINHUA"),
    dict(n=2, scene="court", tag="GUILTY", city="BROOKLYN, US",
         region="Americas", lon=-74.0, lat=40.7,
         head="Huawei guilty on 10 of 12 counts, and it will appeal",
         deck="A jury convicts the telecom giant of bank fraud "
              "and stealing trade secrets.",
         src="REUTERS · BLOOMBERG · AP"),
    dict(n=3, scene="data", tag="LEAKED", city="MOSCOW, RUSSIA",
         region="Europe", lon=37.6, lat=55.8,
         head="Russia's own figures show nearly 500,000 war dead",
         deck="Leaked Rosstat records list about 490,000 military dead to "
              "Sep 2026. Researchers say the true toll may top 700,000.",
         src="MEDIAZONA · MEDUZA · REUTERS"),
]

SMALL = [
    dict(n=4, scene="tower", tag="MIDDLE EAST · CONFLICT", city="RIYADH",
         region="Middle East", lon=46.7, lat=24.7,
         head="The PIF tower is hit again, and 11 are wounded",
         deck="Second strike on the wealth fund's tower in days.",
         src="REUTERS · ARAB NEWS"),
    dict(n=5, scene="shop", tag="AMERICAS · SIEGE", city="CARTAGENA",
         region="Americas", lon=-75.5, lat=10.4,
         head="Hostages held in a supermarket are freed",
         deck="Forces storm the store; all hostages freed, one captor killed.",
         src="AFP · REUTERS"),
    dict(n=6, scene="treaty", tag="OCEANIA · DIPLOMACY", city="CANBERRA",
         region="Oceania", lon=149.1, lat=-35.3,
         head="Australia signs a sweeping pact with Solomon Islands",
         deck="Canberra is primary security partner; no foreign base.",
         src="REUTERS · ABC · AP"),
    dict(n=7, scene="shanghai", tag="ASIA · POLITICS", city="SHANGHAI",
         region="Asia-Pacific", lon=121.5, lat=31.2,
         head="Xi's anti-graft drive reaches Shanghai's party boss",
         deck="Chen Jining probed; the 4th Politburo member since 2025.",
         src="REUTERS · XINHUA"),
    dict(n=8, scene="chart", tag="ASIA · MARKETS", city="TOKYO",
         region="Asia-Pacific", lon=139.7, lat=35.7,
         head="Asia's AI stocks plunge again",
         deck="Kospi -5.9%, Nikkei -2.9%, SoftBank -15% on tariff fears.",
         src="REUTERS"),
    dict(n=9, scene="tariff", tag="AMERICAS · TRADE", city="WASHINGTON",
         region="Americas", lon=-77.0, lat=38.9,
         head="US readies new tariffs on 16 economies",
         deck="USTR probe covers China, the EU and 14 more, sources say.",
         src="REUTERS · WSJ"),
    dict(n=10, scene="port", tag="MIDDLE EAST · STRIKES", city="HODEIDAH",
         region="Middle East", lon=42.8, lat=14.8,
         head="Saudi-led strikes hit Hodeidah port",
         deck="Raids early Wednesday; Houthis threaten Jeddah.",
         src="ARAB NEWS · REUTERS"),
    dict(n=11, scene="ship", tag="EUROPE · DRONE WAR", city="GULF OF FINLAND",
         region="Europe", lon=27.0, lat=60.0,
         head="Zelenskyy claims the drone hit on a Russian cargo ship",
         deck="Kyiv takes responsibility for the Sparta II strike.",
         src="REUTERS · BBC"),
    dict(n=12, scene="football", tag="EUROPE · SPORT", city="MADRID",
         region="Europe", lon=-3.7, lat=40.4,
         head="Real Madrid rout PSV 5-1",
         deck="Mbappe scores twice in a second-half blitz.",
         src="REUTERS · TNT SPORTS"),
]

# Briefs 13-40: (n, city, headline, source, region)
BRIEFS = [
    (13, "SAN JUAN", "Barreto of Puerto Rico crowned Miss Universe 2026", "AP", "Americas"),
    (14, "GAZA CITY", "Strike on the Shati camp kills at least four", "AL JAZEERA", "Middle East"),
    (15, "RIYADH", "Saudi defences down two Houthi drones in the east", "REUTERS", "Middle East"),
    (16, "STRAIT OF HORMUZ", "Iran says two tankers hit by mines", "REUTERS", "Middle East"),
    (17, "KINSHASA", "Congo Ebola deaths reach 5,678; 11,613 cases counted", "ABC", "Africa"),
    (18, "SPACE", "Hera reaches the asteroid NASA struck; first images due", "BBC", "Global"),
    (19, "WINDSOR", "Two arrested on William and Kate's estate", "PA · BBC", "Europe"),
    (20, "NEW YORK", "Nvidia falls about 6% as the Huang rally fades", "REUTERS", "Americas"),
    (21, "LONDON", "UK sanctions Myanmar generals over the Rohingya", "BBC", "Europe"),
    (22, "LANGLEY", "CIA and spy agency hit by cyber breach", "REUTERS", "Americas"),
    (23, "CARACAS", "Venezuela puts its debt load at $237.5bn", "REUTERS", "Americas"),
    (24, "ZAPORIZHZHIA", "Russian strike kills 2, wounds dozens", "AP", "Europe"),
    (25, "ANTALYA", "COP31 chief blames the EU for failure", "BBC", "Europe"),
    (26, "JOHANNESBURG", "Zimbabwean convicted over Ukraine fight", "BBC", "Africa"),
    (27, "TAIPEI", "A US destroyer transits the Taiwan Strait", "REUTERS", "Asia-Pacific"),
    (28, "OSLO", "Norway urges restraint after the cargo-ship attack", "REUTERS", "Europe"),
    (29, "PORT-AU-PRINCE", "Gangs burn a police station", "REUTERS", "Americas"),
    (30, "SEOUL", "North Korea fires two missiles into the sea", "AP", "Asia-Pacific"),
    (31, "DAKAR", "Court restores Senegal as African champions", "CAS · AP", "Africa"),
    (32, "FORT HOOD", "Death-row shooter asks for a stay of execution", "AP", "Americas"),
    (33, "BEIJING", "Politburo meets to set the 2027 reshuffle", "REUTERS", "Asia-Pacific"),
    (34, "LOS ANGELES", "Markle's lawyers call the new count a pile-on", "AP", "Americas"),
    (35, "HELSINKI", "Finland opens a criminal case over the gulf strike", "YLE", "Europe"),
    (36, "WASHINGTON", "US inflation, Q3 GDP due; Fed hike seen", "REUTERS", "Americas"),
    (37, "NEW YORK", "Dell lifts forecasts after record quarter", "REUTERS", "Americas"),
    (38, "WASHINGTON", "Commanders beat Bengals 22-20", "AP", "Americas"),
    (39, "NEW YORK", "Gold eases after US data; Bitcoin $59,257", "REUTERS", "Global"),
    (40, "BEIJING", "China calls Huawei conviction economic coercion", "REUTERS", "Asia-Pacific"),
]

NUMBERS = [
    ("1st", "Pakistani in orbit on Shenzhou-24"),
    ("10/12", "counts Huawei was convicted on"),
    ("~490,000", "Russian war dead, by the state's own leaked data"),
    ("11", "wounded in the second strike on the PIF tower"),
    ("5-1", "Real Madrid rout PSV at the Bernabeu"),
    ("-15%", "SoftBank shares as Asia's AI stocks slide"),
]

TIMELINE = ("UTC  00:18 Shenzhou lifts off  ·  00:41 Solomons treaty signed  ·  "
            "03:56 Tiangong docking  ·  06:02 Asia stocks slide  ·  "
            "08:12 Zelenskyy claims Sparta II  ·  13:30 Cartagena rescue")

DATE_CHECK = ("DATE CHECK — Wires read to 06:40 UTC, Wednesday 25 November 2026. "
    "Every story here happened, or was first reported, on Wednesday 25 November 2026, "
    "as the named outlets reported it. Tuesday-evening events (the Huawei verdict, the "
    "Chen probe, Real Madrid 5-1, the Cartagena rescue) are in as Wednesday's morning "
    "news.  LEFT OUT — NOT 25 NOV: the Senegal boat (19 Nov) · the Sparta II strike "
    "(21 Nov; Zelenskyy's claim of it IS today's news) · COP31's failure (22 Nov) · "
    "the first PIF tower strike (19 Nov).")

# ---------------------------------------------------------------- scenes
# Every scene is drawn with flat vector shapes only: sky, ground, a few
# figures/objects, one accent colour. No photos, no text inside pictures.

def _sky(d, x, y, w, h, top, bot):
    for i in range(h):
        t = i / max(1, h - 1)
        d.line([(x, y + i), (x + w, y + i)],
               fill=tuple(int(top[c] + (bot[c] - top[c]) * t) for c in range(3)))


def _stars(d, x, y, w, h, n=14):
    pts = [(7, 9), (23, 20), (41, 6), (58, 16), (76, 8), (92, 22), (15, 30),
           (33, 28), (52, 32), (70, 28), (88, 34), (45, 12), (63, 24), (27, 14)]
    for i in range(min(n, len(pts))):
        px, py = pts[i]
        d.ellipse([x + px % w - 1, y + py % h - 1, x + px % w + 1, y + py % h + 1],
                  fill=(255, 255, 255))


def _person(d, x, y, s, shirt, skin=(214, 178, 138)):
    d.ellipse([x - 3 * s, y - 9 * s, x + 3 * s, y - 3 * s], fill=skin)
    d.polygon([(x - 5 * s, y - 3 * s), (x + 5 * s, y - 3 * s),
               (x + 6 * s, y + 8 * s), (x - 6 * s, y + 8 * s)], fill=shirt)


def scene_rocket(d, x, y, w, h):
    _sky(d, x, y, w, h, (10, 16, 42), (38, 62, 110))
    _stars(d, x, y, w, h)
    d.polygon([(x + w * 0.47, y + h * 0.08), (x + w * 0.53, y + h * 0.08),
               (x + w * 0.55, y + h * 0.55), (x + w * 0.45, y + h * 0.55)],
              fill=(235, 235, 228))
    d.polygon([(x + w * 0.47, y + h * 0.08), (x + w * 0.50, y + h * 0.02),
               (x + w * 0.53, y + h * 0.08)], fill=(163, 18, 18))
    d.rectangle([x + w * 0.485, y + h * 0.22, x + w * 0.515, y + h * 0.34],
                fill=(26, 42, 74))
    d.polygon([(x + w * 0.45, y + h * 0.55), (x + w * 0.42, y + h * 0.68),
               (x + w * 0.46, y + h * 0.62)], fill=(163, 18, 18))
    d.polygon([(x + w * 0.55, y + h * 0.55), (x + w * 0.58, y + h * 0.68),
               (x + w * 0.54, y + h * 0.62)], fill=(163, 18, 18))
    d.polygon([(x + w * 0.465, y + h * 0.55), (x + w * 0.535, y + h * 0.55),
               (x + w * 0.52, y + h * 0.82), (x + w * 0.48, y + h * 0.82)],
              fill=(245, 158, 11))
    d.rectangle([x, y + h * 0.88, x + w, y + h], fill=(52, 48, 40))
    d.rectangle([x + w * 0.12, y + h * 0.62, x + w * 0.18, y + h * 0.88],
                fill=(120, 116, 104))


def scene_court(d, x, y, w, h):
    _sky(d, x, y, w, h, (74, 58, 44), (120, 100, 76))
    d.rectangle([x, y + h * 0.55, x + w, y + h], fill=(88, 66, 44))
    d.rectangle([x + w * 0.30, y + h * 0.30, x + w * 0.70, y + h * 0.58],
                fill=(52, 38, 26))
    d.rectangle([x + w * 0.30, y + h * 0.30, x + w * 0.70, y + h * 0.36],
                fill=(26, 42, 74))
    for i in range(5):
        _person(d, x + w * (0.12 + i * 0.19), y + h * 0.78, 1.0,
                (40, 40, 40) if i % 2 else (90, 90, 96))
    d.rectangle([x + w * 0.08, y + h * 0.08, x + w * 0.14, y + h * 0.26],
                fill=(163, 18, 18))
    d.rectangle([x + w * 0.08, y + h * 0.08, x + w * 0.14, y + h * 0.13],
                fill=(255, 255, 255))


def scene_data(d, x, y, w, h):
    _sky(d, x, y, w, h, (30, 30, 34), (70, 66, 60))
    d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(38, 38, 34))
    for r in range(4):
        for c in range(9):
            cx = x + w * (0.06 + c * 0.105)
            cy = y + h * (0.30 + r * 0.11)
            d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(163, 18, 18))
    bars = [0.25, 0.45, 0.65, 0.9]
    for i, b in enumerate(bars):
        bx = x + w * (0.62 + i * 0.095)
        d.rectangle([bx, y + h * (0.75 - b * 0.55), bx + w * 0.06,
                     y + h * 0.75], fill=(245, 158, 11))
    d.line([(x + w * 0.58, y + h * 0.78), (x + w * 0.98, y + h * 0.78)],
           fill=(220, 220, 210), width=2)


def scene_tower(d, x, y, w, h):
    _sky(d, x, y, w, h, (16, 22, 48), (70, 80, 120))
    _stars(d, x, y, w, h, 8)
    for i, bx in enumerate([0.06, 0.20, 0.62, 0.78]):
        bh = [0.45, 0.60, 0.52, 0.38][i]
        d.rectangle([x + w * bx, y + h * (0.95 - bh), x + w * (bx + 0.12),
                     y + h * 0.95], fill=(40, 44, 62))
    d.polygon([(x + w * 0.42, y + h * 0.95), (x + w * 0.46, y + h * 0.05),
               (x + w * 0.54, y + h * 0.05), (x + w * 0.58, y + h * 0.95)],
              fill=(58, 64, 88))
    for r in range(6):
        for c in range(2):
            d.rectangle([x + w * (0.475 + c * 0.03), y + h * (0.16 + r * 0.11),
                         x + w * (0.495 + c * 0.03), y + h * (0.22 + r * 0.11)],
                        fill=(245, 200, 90))
    d.ellipse([x + w * 0.42, y + h * 0.02, x + w * 0.58, y + h * 0.20],
              fill=(245, 158, 11))
    d.ellipse([x + w * 0.45, y + h * 0.05, x + w * 0.55, y + h * 0.16],
              fill=(250, 120, 40))


def scene_shop(d, x, y, w, h):
    _sky(d, x, y, w, h, (120, 140, 170), (200, 205, 210))
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(90, 90, 88))
    d.rectangle([x + w * 0.08, y + h * 0.18, x + w * 0.92, y + h * 0.66],
                fill=(245, 200, 40))
    d.rectangle([x + w * 0.14, y + h * 0.34, x + w * 0.86, y + h * 0.66],
                fill=(70, 110, 150))
    d.line([(x, y + h * 0.60), (x + w, y + h * 0.52)], fill=(255, 255, 255),
           width=3)
    for i in range(4):
        _person(d, x + w * (0.16 + i * 0.22), y + h * 0.82, 0.9,
                (26, 42, 74) if i % 2 == 0 else (163, 18, 18))


def scene_treaty(d, x, y, w, h):
    _sky(d, x, y, w, h, (200, 210, 220), (235, 235, 230))
    d.rectangle([x, y + h * 0.68, x + w, y + h], fill=(120, 88, 52))
    d.rectangle([x + w * 0.10, y + h * 0.62, x + w * 0.90, y + h * 0.72],
                fill=(96, 66, 38))
    d.rectangle([x + w * 0.38, y + h * 0.52, x + w * 0.62, y + h * 0.64],
                fill=(255, 255, 255))
    d.line([(x + w * 0.42, y + h * 0.56), (x + w * 0.58, y + h * 0.56)],
           fill=(60, 60, 60), width=1)
    d.line([(x + w * 0.42, y + h * 0.60), (x + w * 0.58, y + h * 0.60)],
           fill=(60, 60, 60), width=1)
    # Australia flag (blue, union canton + stars) and Solomons flag (blue/green)
    d.rectangle([x + w * 0.08, y + h * 0.08, x + w * 0.30, y + h * 0.42],
                fill=(0, 40, 120))
    d.rectangle([x + w * 0.08, y + h * 0.08, x + w * 0.16, y + h * 0.20],
                fill=(200, 30, 30))
    d.rectangle([x + w * 0.70, y + h * 0.08, x + w * 0.92, y + h * 0.42],
                fill=(0, 90, 60))
    d.polygon([(x + w * 0.70, y + h * 0.42), (x + w * 0.92, y + h * 0.08),
               (x + w * 0.92, y + h * 0.42)], fill=(0, 40, 120))
    _person(d, x + w * 0.44, y + h * 0.50, 1.0, (26, 42, 74))
    _person(d, x + w * 0.56, y + h * 0.50, 1.0, (163, 18, 18))


def scene_shanghai(d, x, y, w, h):
    _sky(d, x, y, w, h, (210, 180, 120), (240, 220, 180))
    d.rectangle([x, y + h * 0.80, x + w, y + h], fill=(70, 70, 72))
    for i, (bx, bh) in enumerate([(0.05, 0.55), (0.20, 0.75), (0.38, 0.45),
                                  (0.55, 0.65), (0.72, 0.50), (0.86, 0.35)]):
        d.rectangle([x + w * bx, y + h * (0.82 - bh), x + w * (bx + 0.11),
                     y + h * 0.82], fill=(52, 58, 74))
    d.polygon([(x + w * 0.20, y + h * 0.07), (x + w * 0.255, y + h * 0.07),
               (x + w * 0.31, y + h * 0.07)], fill=(52, 58, 74))
    d.ellipse([x + w * 0.68, y + h * 0.10, x + w * 0.88, y + h * 0.32],
              outline=(163, 18, 18), width=4)
    d.rectangle([x + w * 0.72, y + h * 0.17, x + w * 0.84, y + h * 0.25],
                fill=(163, 18, 18))


def scene_chart(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 24, 40))
    for i in range(6):
        bx = x + w * (0.06 + i * 0.15)
        top = y + h * (0.20 + i * 0.08)
        d.rectangle([bx, top, bx + w * 0.07, top + h * 0.18],
                    fill=(220, 60, 50) if i % 2 == 0 else (60, 160, 90))
    pts = [(x + w * 0.05, y + h * 0.25), (x + w * 0.25, y + h * 0.35),
           (x + w * 0.45, y + h * 0.30), (x + w * 0.65, y + h * 0.55),
           (x + w * 0.85, y + h * 0.70), (x + w * 0.97, y + h * 0.85)]
    d.line(pts, fill=(245, 60, 40), width=4)
    d.polygon([(x + w * 0.90, y + h * 0.78), (x + w * 0.99, y + h * 0.86),
               (x + w * 0.88, y + h * 0.90)], fill=(245, 60, 40))
    d.rectangle([x + w * 0.60, y + h * 0.08, x + w * 0.94, y + h * 0.28],
                fill=(255, 255, 255))
    d.text((x + w * 0.64, y + h * 0.11), "-15%", font=font(SANS_B, 16),
           fill=(163, 18, 18))


def scene_tariff(d, x, y, w, h):
    _sky(d, x, y, w, h, (150, 180, 210), (210, 220, 230))
    d.rectangle([x, y + h * 0.70, x + w, y + h], fill=(60, 80, 110))
    d.polygon([(x + w * 0.10, y + h * 0.70), (x + w * 0.90, y + h * 0.70),
               (x + w * 0.80, y + h * 0.30), (x + w * 0.20, y + h * 0.30)],
              fill=(90, 100, 110))
    for r in range(3):
        for c in range(4):
            col = [(163, 18, 18), (26, 42, 74), (245, 158, 11), (40, 120, 80)][(r + c) % 4]
            d.rectangle([x + w * (0.24 + c * 0.14), y + h * (0.34 + r * 0.11),
                         x + w * (0.35 + c * 0.14), y + h * (0.42 + r * 0.11)],
                        fill=col)
    d.ellipse([x + w * 0.68, y + h * 0.02, x + w * 0.98, y + h * 0.34],
              fill=(163, 18, 18))
    d.text((x + w * 0.76, y + h * 0.07), "%", font=font(SANS_B, 26),
           fill=(255, 255, 255))


def scene_port(d, x, y, w, h):
    _sky(d, x, y, w, h, (200, 170, 120), (120, 110, 100))
    d.rectangle([x, y + h * 0.70, x + w, y + h], fill=(50, 70, 90))
    d.rectangle([x + w * 0.10, y + h * 0.45, x + w * 0.55, y + h * 0.70],
                fill=(70, 70, 76))
    for i in range(3):
        d.rectangle([x + w * (0.14 + i * 0.14), y + h * 0.50,
                     x + w * (0.22 + i * 0.14), y + h * 0.58],
                    fill=(245, 158, 11))
    d.line([(x + w * 0.62, y + h * 0.10), (x + w * 0.62, y + h * 0.70)],
           fill=(40, 40, 44), width=5)
    d.line([(x + w * 0.62, y + h * 0.12), (x + w * 0.92, y + h * 0.28)],
           fill=(40, 40, 44), width=4)
    d.ellipse([x + w * 0.30, y + h * 0.08, x + w * 0.48, y + h * 0.30],
              fill=(90, 85, 80))
    d.ellipse([x + w * 0.36, y + h * 0.14, x + w * 0.54, y + h * 0.36],
              fill=(245, 120, 40))


def scene_ship(d, x, y, w, h):
    _sky(d, x, y, w, h, (140, 180, 210), (210, 225, 235))
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(40, 90, 130))
    for i in range(3):
        d.arc([x + w * (0.05 + i * 0.3), y + h * 0.72, x + w * (0.25 + i * 0.3),
               y + h * 0.92], 0, 180, fill=(255, 255, 255), width=2)
    d.polygon([(x + w * 0.12, y + h * 0.62), (x + w * 0.88, y + h * 0.62),
               (x + w * 0.80, y + h * 0.48), (x + w * 0.20, y + h * 0.48)],
              fill=(30, 50, 70))
    for i, col in enumerate([(163, 18, 18), (245, 158, 11), (26, 42, 74)]):
        d.rectangle([x + w * (0.28 + i * 0.16), y + h * 0.30,
                     x + w * (0.40 + i * 0.16), y + h * 0.48], fill=col)
    d.ellipse([x + w * 0.60, y + h * 0.22, x + w * 0.72, y + h * 0.38],
              fill=(60, 60, 60))
    d.ellipse([x + w * 0.63, y + h * 0.25, x + w * 0.75, y + h * 0.41],
              fill=(245, 120, 40))
    d.line([(x + w * 0.66, y + h * 0.22), (x + w * 0.78, y + h * 0.06)],
           fill=(60, 60, 60), width=2)


def scene_football(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 120, 60))
    d.rectangle([x, y, x + w, y + h * 0.30], fill=(240, 240, 235))
    d.text((x + w * 0.08, y + h * 0.04), "REAL 5-1 PSV",
           font=font(SANS_B, 15), fill=(163, 18, 18))
    d.rectangle([x + w * 0.08, y + h * 0.55, x + w * 0.34, y + h * 0.92],
                outline=(255, 255, 255), width=3)
    d.ellipse([x + w * 0.60, y + h * 0.62, x + w * 0.72, y + h * 0.80],
              fill=(255, 255, 255))
    d.ellipse([x + w * 0.63, y + h * 0.66, x + w * 0.66, y + h * 0.70],
              fill=(17, 17, 17))
    _person(d, x + w * 0.48, y + h * 0.80, 1.0, (255, 255, 255))
    _person(d, x + w * 0.82, y + h * 0.78, 1.0, (163, 18, 18))


SCENES = {"rocket": scene_rocket, "court": scene_court, "data": scene_data,
          "tower": scene_tower, "shop": scene_shop, "treaty": scene_treaty,
          "shanghai": scene_shanghai, "chart": scene_chart,
          "tariff": scene_tariff, "port": scene_port, "ship": scene_ship,
          "football": scene_football}

# ---------------------------------------------------------------- map
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70),
     (-75, 62), (-60, 55), (-55, 47), (-70, 42), (-75, 35), (-80, 26),
     (-85, 20), (-90, 15), (-95, 18), (-105, 20), (-115, 28), (-125, 40),
     (-140, 60), (-165, 60)],
    [(-80, 10), (-75, 5), (-60, 0), (-50, -5), (-40, -10), (-35, -20),
     (-45, -30), (-55, -35), (-65, -45), (-70, -55), (-75, -40), (-80, -20),
     (-80, -5)],
    [(-10, 36), (-5, 44), (0, 48), (5, 55), (10, 58), (20, 60), (25, 65),
     (30, 70), (40, 68), (45, 60), (40, 50), (30, 45), (20, 40), (10, 38),
     (0, 36), (-10, 38)],
    [(-10, 35), (0, 35), (10, 37), (20, 32), (30, 31), (35, 28), (40, 15),
     (48, 11), (50, 5), (40, -5), (35, -15), (30, -25), (20, -35),
     (15, -30), (10, -15), (5, 0), (-5, 5), (-15, 10), (-17, 15)],
    [(40, 70), (60, 72), (80, 73), (100, 77), (120, 73), (140, 72),
     (160, 70), (170, 66), (160, 60), (140, 50), (130, 42), (120, 38),
     (110, 30), (105, 20), (100, 10), (95, 15), (90, 22), (80, 15),
     (75, 8), (70, 20), (60, 25), (50, 28), (45, 30), (40, 35), (35, 40),
     (30, 42)],
    [(113, -22), (114, -30), (120, -34), (130, -32), (140, -38), (150, -37),
     (153, -27), (146, -19), (142, -11), (135, -12), (130, -13), (122, -14),
     (114, -20)],
]


def draw_map(d, x, y, w, h, stories):
    d.rectangle([x, y, x + w, y + h], fill=OCEAN, outline=LINE)
    d.text((x + 6, y + 4), "WHERE IT HAPPENED — PINS = STORY NUMBERS",
           font=font(SANS_B, 9), fill=INK)

    def proj(lon, lat):
        return (x + (lon + 170) / 360.0 * w,
                y + 18 + (75 - lat) / 130.0 * (h - 40))

    for poly in CONTINENTS:
        d.polygon([proj(lon, lat) for lon, lat in poly], fill=LAND,
                  outline=LANDB)
    f_pin = font(SANS_B, 9)
    for s in stories:
        px, py = proj(s["lon"], s["lat"])
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255))
        t = str(s["n"])
        d.text((px - d.textlength(t, font=f_pin) / 2, py - 6), t,
               font=f_pin, fill=(255, 255, 255))
    return

# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    f_mast = font(SERIF, 56)
    f_stand = font(SERIF_R, 13)
    f_tally = font(SANS_B, 10)
    f_num = font(SERIF, 26)
    f_numlab = font(SANS, 9)
    f_label = font(SANS_B, 11)
    f_tag = font(SANS_B, 9)
    f_tag8 = font(SANS_B, 8)
    f_head = font(SERIF, 19)
    f_deck = font(SANS, 11)
    f_src = font(SANS_B, 9)
    f_shead = font(SANS_B, 12)
    f_sdeck = font(SANS, 10)
    f_brief = font(SANS, 9)
    f_briefb = font(SANS_B, 9)
    f_small = font(SANS, 9)
    f_foot = font(SANS_B, 9)

    # top bar
    d.rectangle([0, 0, W, 24], fill=(0, 0, 0))
    d.text((8, 6), "THE WORLD IN ONE DAY", font=f_label, fill=(255, 255, 255))
    r = "EVERY STORY DATED WEDNESDAY 25 NOV 2026"
    d.text((W - 8 - d.textlength(r, font=f_label), 6), r, font=f_label,
           fill=(255, 255, 255))

    # masthead
    title = "Wednesday 25 November 2026"
    d.text(((W - d.textlength(title, font=f_mast)) / 2, 30), title,
           font=f_mast, fill=INK)
    d.rectangle([0, 92, W, 95], fill=RED)
    stand = ("Shenzhou-24 lifts off with Pakistan's first astronaut  "
             "\u25c6  Huawei guilty on 10 of 12  \u25c6  "
             "Russia's leaked data: nearly 500,000 war dead")
    d.text(((W - d.textlength(stand, font=f_stand)) / 2, 100), stand,
           font=f_stand, fill=INK)

    # region tally, computed from the story data (40 stories)
    regions = {}
    for s in LEADS + SMALL:
        regions[s["region"]] = regions.get(s["region"], 0) + 1
    for _, _, _, _, rg in BRIEFS:
        regions[rg] = regions.get(rg, 0) + 1
    order = ["Americas", "Europe", "Asia-Pacific", "Middle East", "Oceania",
             "Africa", "Global"]
    tally = "40 STORIES  ·  " + "  ·  ".join(
        f"{r.upper()} {regions.get(r, 0)}" for r in order)
    d.text(((W - d.textlength(tally, font=f_tally)) / 2, 122), tally,
           font=f_tally, fill=GREY)

    # numbers strip
    y0, bw = 140, 164
    for i, (big, lab) in enumerate(NUMBERS):
        bx = 8 + i * (bw + 4)
        d.rectangle([bx, y0, bx + bw, y0 + 52], outline=LINE, width=1)
        d.text((bx + 8, y0 + 4), big, font=f_num, fill=RED)
        lab_lines = wrap(d, lab, f_numlab, bw - 16)
        text_block(d, bx + 8, y0 + 31, lab_lines[:2], f_numlab, INK, 10)

    # leads
    d.text((8, 200), "THE DAY'S THREE LEADS", font=f_label, fill=RED)
    d.line([(210, 206), (W - 8, 206)], fill=LINE, width=1)
    colw, gap = 328, 4
    for i, s in enumerate(LEADS):
        x = 8 + i * (colw + gap)
        y = 214
        SCENES[s["scene"]](d, x, y, colw, 96)
        d.rectangle([x, y, x + colw, y + 96], outline=LINE, width=1)
        d.text((x, y + 100), f"{s['n']}  {s['tag']}  ·  {s['city']}",
               font=f_tag, fill=RED)
        yy = text_block(d, x, y + 114,
                        wrap(d, s["head"], f_head, colw), f_head, INK, 20)
        yy = text_block(d, x, yy + 3,
                        wrap(d, s["deck"], f_deck, colw)[:2], f_deck, INK, 13)
        d.text((x, y + 192), s["src"], font=f_src, fill=GREY)

    # nine small panels
    d.text((8, 414), "THE DAY IN NINE", font=f_label, fill=RED)
    d.line([(150, 420), (W - 8, 420)], fill=LINE, width=1)
    for i, s in enumerate(SMALL):
        r, c = divmod(i, 3)
        x = 8 + c * (colw + gap)
        y = 428 + r * 104
        SCENES[s["scene"]](d, x, y, colw, 44)
        d.rectangle([x, y, x + colw, y + 44], outline=LINE, width=1)
        d.text((x, y + 48), f"{s['n']}  {s['tag']}  ·  {s['city']}  —  {s['src']}",
               font=f_tag8, fill=RED)
        yy = text_block(d, x, y + 60,
                        wrap(d, s["head"], f_shead, colw), f_shead, INK, 13)
        text_block(d, x, y + 88,
                   wrap(d, s["deck"], f_sdeck, colw)[:1], f_sdeck, INK, 12)

    # map + briefs
    d.text((8, 744), "ALSO ON WEDNESDAY — 28 MORE STORIES",
           font=f_label, fill=RED)
    d.line([(330, 750), (W - 8, 750)], fill=LINE, width=1)
    draw_map(d, 8, 760, 300, 176, LEADS + SMALL)
    # region tally under the map
    ty = 940
    d.text((8, ty), "AMERICAS %d · EUROPE %d · ASIA-PACIFIC %d" % (
        regions["Americas"], regions["Europe"], regions["Asia-Pacific"]),
        font=f_small, fill=GREY)
    d.text((8, ty + 12), "MIDDLE EAST %d · OCEANIA %d · AFRICA %d · GLOBAL %d" % (
        regions["Middle East"], regions["Oceania"], regions["Africa"],
        regions["Global"]), font=f_small, fill=GREY)

    for ci in range(2):
        bx = 320 + ci * 352
        for ri in range(14):
            b = BRIEFS[ci * 14 + ri]
            yy = 760 + ri * 14
            d.text((bx, yy), str(b[0]), font=f_briefb, fill=RED)
            d.text((bx + 22, yy), b[1] + " — ", font=f_briefb, fill=INK)
            rest = b[2] + "  ·  " + b[3]
            d.text((bx + 22 + d.textlength(b[1] + " — ", font=f_briefb), yy),
                   rest, font=f_brief, fill=INK)

    # timeline strip
    d.rectangle([0, 964, W, 964], fill=LINE)
    d.text((8, 970), TIMELINE, font=f_small, fill=INK)

    # date check
    d.rectangle([8, 984, W - 8, 1023], outline=RED, width=1)
    text_block(d, 14, 987, wrap(d, DATE_CHECK, f_small, W - 28),
               f_small, INK, 11)

    out = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    img.save(out, format="PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
