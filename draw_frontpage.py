#!/usr/bin/env python3
"""Draw the Wednesday 25 November 2026 world-news front page.

Reads nothing, fetches nothing: every story below was researched from the
morning wires (AP, Reuters, BBC, AFP, NYT, CNN, UEFA, RFE/RL) and is baked
into this file. Run: python3 draw_frontpage.py  ->  entry.png (1024x1024).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
FAINT = (96, 92, 84)
RED = (178, 32, 44)
NAVY = (28, 58, 94)
GREEN = (31, 110, 72)
AMBER = (166, 110, 12)
PURPLE = (98, 58, 140)
RULE = (18, 18, 18)
PANEL = (255, 255, 255)
SOFT = (238, 232, 219)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width`."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, width, fill=INK, leading=None, max_lines=None):
    """Draw wrapped text; return the y just below the last line."""
    x, y = xy
    leading = leading or int(fnt.size * 1.22)
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def chip(draw, x, y, label, colour):
    """Small coloured tier tag; returns the x just past it."""
    fnt = font(SANS_B, 11)
    tw = draw.textlength(label, font=fnt)
    draw.rounded_rectangle([x, y, x + tw + 12, y + 16], radius=3, fill=colour)
    draw.text((x + 6, y + 2), label, font=fnt, fill=(255, 255, 255))
    return x + tw + 12


# Tier colours for the five fields every story belongs to.
TIERS = {
    "WAR": RED,
    "POLITICS": NAVY,
    "MARKETS": GREEN,
    "DISASTER": AMBER,
    "SPORT": PURPLE,
}


def masthead(draw):
    draw.rectangle([0, 0, W, 118], fill=INK)
    draw.text((28, 14), "THE WORLD IN ONE IMAGE",
              font=font(SERIF, 46), fill=(247, 243, 234))
    draw.text((28, 72), "One day of world news, drawn as a newspaper front page",
              font=font(SERIF_REG, 20), fill=(205, 200, 188))
    date_f = font(SERIF, 40)
    draw.text((W - 28 - draw.textlength("WEDNESDAY", font=date_f), 12),
              "WEDNESDAY", font=date_f, fill=(247, 243, 234))
    draw.text((W - 28 - draw.textlength("25 NOVEMBER 2026", font=font(SANS_B, 22)), 62),
              "25 NOVEMBER 2026", font=font(SANS_B, 22), fill=(232, 196, 120))
    draw.line([0, 118, W, 118], fill=RED, width=4)
    fnt = font(SANS_B, 14)
    draw.text((28, 128), "35 STORIES  ·  SIX REGIONS  ·  WIRES AS OF 02:15 UTC, WED 25 NOV 2026",
              font=fnt, fill=FAINT)


def lead_icon(draw, box, kind):
    """A small drawn picture inside a lead column: pure geometry, no photo."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=SOFT, outline=RULE, width=1)
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    if kind == "tariff":
        # rising bars with an arrow climbing over them, all inside the box
        base = y1 - 14
        for i, h in enumerate((14, 20, 18, 30, 40)):
            bx = x0 + 26 + i * 52
            draw.rectangle([bx, base - h, bx + 34, base], fill=NAVY)
        draw.line([x0 + 22, base - 28, x1 - 34, base - 46], fill=RED, width=5)
        draw.polygon([(x1 - 40, base - 54), (x1 - 22, base - 46),
                      (x1 - 42, base - 38)], fill=RED)
    elif kind == "boat":
        # a hull on two wave lines with a small flag, all inside the box
        draw.polygon([(x0 + 60, y1 - 34), (x1 - 60, y1 - 34), (x1 - 78, y1 - 12),
                      (x0 + 78, y1 - 12)], fill=NAVY)
        draw.line([cx, y1 - 58, cx, y1 - 34], fill=INK, width=3)
        draw.polygon([(cx, y1 - 58), (cx + 26, y1 - 48), (cx, y1 - 38)], fill=RED)
        for wy in (y1 - 8,):
            for k in range(5):
                wx = x0 + 20 + k * 56
                draw.arc([wx, wy - 8, wx + 34, wy + 8], 0, 180, fill=NAVY, width=3)
        draw.text((x0 + 22, y0 + 8), "SENEGAL COAST", font=font(MONO, 15), fill=NAVY)
    else:
        # rows of small figures: a toll counted in dots, label on top
        draw.text((x0 + 22, y0 + 8), "MOSCOW'S OWN COUNT",
                  font=font(MONO, 15), fill=RED)
        for r in range(3):
            for c in range(9):
                px = x0 + 30 + c * 28
                py = y0 + 30 + r * 16
                draw.ellipse([px, py, px + 12, py + 12], fill=RED)


def leads(draw):
    cols = [(28, 356), (356, 684), (684, 996)]
    items = [
        ("01", "tariff", "US READIES NEW TARIFFS ON TRADING PARTNERS",
         "Washington is preparing fresh tariffs on several countries, the BBC understands. WED",
         "MARKETS"),
        ("02", "boat", "BOAT CAPSIZES OFF SENEGAL; DOZENS MISSING",
         "A migrant boat capsized off Yenne early on Wednesday; four dead, dozens missing. WED",
         "DISASTER"),
        ("03", "dots", "RUSSIA'S OWN FIGURES: 490,334 WAR DEAD",
         "At least 490,334 Russian soldiers have died since 2022, Moscow's own figures say. WED",
         "WAR"),
    ]
    for (x0, x1), (num, kind, head, deck, tier) in zip(cols, items):
        lead_icon(draw, (x0, 148, x1, 218), kind)
        draw.text((x0, 226), num, font=font(SERIF, 30), fill=RED)
        chip(draw, x0 + 52, 234, tier, TIERS[tier])
        y = para(draw, (x0, 258), head, font(SANS_B, 19), x1 - x0, leading=22,
                 max_lines=2)
        para(draw, (x0, y + 2), deck, font(SANS, 14), x1 - x0, leading=17,
             max_lines=2)
    draw.line([28, 344, 996, 344], fill=RULE, width=2)


def timeline(draw):
    y = 356
    draw.text((28, y), "THE DAY IN ORDER", font=font(SANS_B, 15), fill=INK)
    draw.text((W - 28 - draw.textlength("TUE EVENING  →  WED MORNING (UTC)",
              font=font(SANS, 13)), y + 1),
              "TUE EVENING  →  WED MORNING (UTC)", font=font(SANS, 13), fill=FAINT)
    ty = y + 34
    draw.line([40, ty, 984, ty], fill=INK, width=2)
    stops = [
        ("TUE EVE", "Huawei guilty\non 10 of 12 counts"),
        ("TUE EVE", "Houthis hit\nRiyadh tower"),
        ("22:27 UTC", "CIA hack\nfirst reported"),
        ("TUE NIGHT", "Real Madrid\n5–1 PSV"),
        ("WED 00:00", "Boat capsizes\noff Senegal"),
        ("WED ~02:00", "US tariffs\nplan reported"),
    ]
    step = 944 / 6
    for i, (when, what) in enumerate(stops):
        cx = 40 + step * i + step / 2
        draw.ellipse([cx - 6, ty - 6, cx + 6, ty + 6], fill=RED, outline=INK, width=1)
        wf = font(SANS_B, 12)
        draw.text((cx - draw.textlength(when, font=wf) / 2, ty + 10), when,
                  font=wf, fill=RED)
        tf = font(SANS, 12)
        lines = what.split("\n")
        ly = ty + 27
        for line in lines:
            draw.text((cx - draw.textlength(line, font=tf) / 2, ly), line,
                      font=tf, fill=INK)
            ly += 14
    draw.line([28, 448, 996, 448], fill=RULE, width=1)


def numbers_strip(draw):
    y = 458
    draw.text((28, y), "THE DAY IN NUMBERS", font=font(SANS_B, 15), fill=INK)
    stats = [
        ("490,334", "Russian soldiers dead\nsince 2022, Moscow's count"),
        ("11", "wounded as Houthis\nstrike Riyadh tower"),
        ("4+", "dead, dozens missing\nas boat sinks off Senegal"),
        ("$4.71bn", "pulled from US Bitcoin\nETFs in November"),
        ("10 of 12", "counts Huawei found\nguilty on in New York"),
        ("5–1", "Real Madrid rout\nPSV at the Bernabéu"),
    ]
    bw = (996 - 28 - 5 * 10) / 6
    for i, (big, small) in enumerate(stats):
        x0 = 28 + i * (bw + 10)
        draw.rectangle([x0, y + 22, x0 + bw, y + 78], fill=PANEL, outline=RULE, width=1)
        bf = font(SERIF, 24)
        draw.text((x0 + (bw - draw.textlength(big, font=bf)) / 2, y + 24), big,
                  font=bf, fill=RED)
        sf = font(SANS, 10)
        ly = y + 52
        for line in small.split("\n"):
            draw.text((x0 + (bw - draw.textlength(line, font=sf)) / 2, ly), line,
                      font=sf, fill=INK)
            ly += 11


def features(draw):
    y0 = 544
    draw.text((28, y0), "FEATURES", font=font(SANS_B, 15), fill=INK)
    draw.line([28, y0 + 20, 996, y0 + 20], fill=RULE, width=1)
    items = [
        ("04", "WAR", "SPY AGENCIES HACKED — BUT NO SECRETS LOST",
         "The CIA and the director of national intelligence found a breach of an "
         "unclassified network for open-source analysis. No classified systems hit. TUE"),
        ("05", "MARKETS", "HUAWEI GUILTY OF STEALING TRADE SECRETS",
         "A Brooklyn jury convicted the Chinese telecoms giant on 10 of 12 criminal "
         "counts after a three-month trial. Huawei rejects the verdicts. TUE"),
        ("06", "WAR", "HOUTHIS STRIKE RIYADH'S TALLEST TOWER",
         "Yemen's Houthi rebels hit the PIF Tower in the Saudi capital for the second "
         "time in under a week, wounding at least 11 people. TUE"),
        ("07", "WAR", "UKRAINE SANK A RUSSIAN WARSHIP OFF LIBYA",
         "Kyiv confirmed it struck two Russian vessels off Libya, sinking one in "
         "Benghazi harbour, and hit a cargo ship in the Gulf of Finland. TUE"),
        ("08", "DISASTER", "WHO PULLS STAFF FROM EBOLA HOSPITAL",
         "Health workers left a hospital in Akwe, Ituri province, after sheltering "
         "there for three days from fierce fighting in the Ebola zone. WED"),
        ("09", "POLITICS", "TRUMP MEETS NATO CHIEF RUTTE TODAY",
         "The president holds talks with Mark Rutte as his envoy says he is 'not "
         "certain' US military aid to Israel will end this year. WED"),
        ("10", "SPORT", "REAL MADRID 5–1 PSV; ARSENAL HELD",
         "Mbappé scored twice and Bellingham volleyed home as Real stayed perfect; "
         "Arsenal drew 1–1 and Manchester City 2–2 with Napoli. TUE"),
        ("11", "SPORT", "ENGLAND LEVEL THE T20 SERIES IN AUSTRALIA",
         "England chased 185 to beat Australia by eight wickets in the second T20 "
         "international, levelling the five-match series at 1–1. TUE"),
        ("12", "POLITICS", "BJP AND AKALI DAL REUNITE FOR PUNJAB 2027",
         "India's ruling BJP and the Shiromani Akali Dal announced an alliance for "
         "the 2027 Punjab assembly elections, ending a six-year split. TUE"),
        ("13", "WAR", "NATO TO FLY EARLY-WARNING JETS OVER POLAND",
         "The alliance will deploy early-warning aircraft in Poland after missiles "
         "landed there during an attack on Ukraine. TUE"),
    ]
    col_w = 474
    row_h = 44
    for i, (num, tier, head, deck) in enumerate(items):
        col = i % 2
        row = i // 2
        x = 28 + col * (col_w + 20)
        y = y0 + 28 + row * row_h
        draw.text((x, y), num, font=font(SERIF, 22), fill=RED)
        hx = x + 44
        after_chip = chip(draw, hx, y + 4, tier, TIERS[tier])
        para(draw, (after_chip + 8, y + 1), head, font(SANS_B, 14),
             col_w - 44 - (after_chip - hx) - 8, leading=16, max_lines=1)
        para(draw, (hx, y + 17), deck, font(SANS, 12), col_w - 44, leading=14,
             max_lines=2)


def briefs(draw):
    y0 = 800
    draw.text((28, y0), "BRIEFS — THE REST OF THE DAY", font=font(SANS_B, 15), fill=INK)
    draw.line([28, y0 + 20, 996, y0 + 20], fill=RULE, width=1)
    items = [
        ("14", "Iran says three oil tankers were hit by naval mines in the Strait of Hormuz. TUE"),
        ("15", "Sarkozy corruption case ordered to trial; first pre-trial hearing 1 April 2027. TUE"),
        ("16", "Fort Hood gunman Hasan seeks a stay of execution set for next week. TUE"),
        ("17", "Trump pardons turkeys; Giuliani awarded the Medal of Freedom. TUE"),
        ("18", "Radar fault delays flights at Chicago O'Hare, the FAA says. TUE"),
        ("19", "US Bitcoin ETFs set a November outflow record: $4.71bn and counting. TUE"),
        ("20", "India's food inflation climbs again; factory PMI hits a nine-month high. WED"),
        ("21", "UK papers lead on a review finding disability benefit PIP 'not fit for purpose'. WED"),
        ("22", "Vaibhav Sooryavanshi, 15, smashes a 28-ball century with 22 sixes for India A. TUE"),
        ("23", "India's women beat Thailand 7–0 to reach the Champions Trophy semis. TUE"),
        ("24", "UCL tonight, FORECAST: PSG–Roma, Sporting–Man Utd, Lille–Bayern. WED"),
        ("25", "Court clears the Army to detonate 10,000 lb of degrading explosive in Iowa. TUE"),
        ("26", "US envoy 'not certain' military aid to Israel ends this year as promised. WED"),
        ("27", "NATO vows to defend space amid reports of a Russian nuclear-armed satellite. TUE"),
        ("28", "Iran braces for winter gas shortages as war damage deepens its energy crisis. TUE"),
        ("29", "UN flags continuing humanitarian hardship for civilians in Gaza. TUE"),
        ("30", "EU announces further sanctions against Russia over the war in Ukraine. TUE"),
        ("31", "US and Qatar hold talks on strategic cooperation and the region. TUE"),
        ("32", "Bake Off winner crowned after a high-stakes final. TUE"),
        ("33", "Pochettino leads Manchester United fury at Yoro red-card ruling. TUE"),
        ("34", "United's Yoro has his Anfield red card overturned on appeal. TUE"),
        ("35", "Lewis Pugh swims the Strait of Hormuz to mark the war's sea damage. TUE"),
    ]
    col_w = 474
    for i, (num, text) in enumerate(items):
        col = i % 2
        row = i // 2
        x = 28 + col * (col_w + 20)
        y = y0 + 28 + row * 12
        draw.text((x, y), num, font=font(SANS_B, 11), fill=RED)
        para(draw, (x + 26, y), text, font(SANS, 12), col_w - 26, leading=14,
             max_lines=1)


def region_bar(draw):
    y0 = 964
    draw.text((28, y0),
              "WHERE THE NEWS CAME FROM — Europe 13  ·  N. America 8  ·  Middle East 7  ·  "
              "Asia-Pacific 4  ·  Africa 2  ·  Oceania 1",
              font=font(SANS_B, 12), fill=INK)
    regions = [
        (13, NAVY), (8, RED), (7, AMBER), (4, GREEN), (2, (120, 90, 40)), (1, PURPLE),
    ]
    total = sum(n for n, _ in regions)
    x = 28
    for n, colour in regions:
        w = 968 * n / total
        draw.rectangle([x, y0 + 16, x + w, y0 + 26], fill=colour)
        x += w


def footer(draw):
    draw.text((28, 996),
              "KEPT OUT — NOT 25 NOV: ICJ Myanmar ruling (19 Nov) · COP31 no-deal close (23 Nov) · "
              "Huang back at Nvidia (23 Nov) · GTA 6 release (19 Nov)",
              font=font(SANS_B, 11), fill=RED)
    draw.text((28, 1011),
              "Sources: AP · Reuters · BBC · AFP · NYT · CNN · UEFA · RFE/RL — drawn illustrations only, no photographs",
              font=font(SANS, 11), fill=FAINT)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    leads(draw)
    timeline(draw)
    numbers_strip(draw)
    features(draw)
    briefs(draw)
    region_bar(draw)
    footer(draw)
    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
