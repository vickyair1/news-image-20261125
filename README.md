# The World in One Image — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/vickyair1/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/vickyair1/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

My entry for the [make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125): one packed newspaper front page for Wednesday 25 November 2026.

## What the page carries

35 stories from six regions, each dated WED or TUE so the day it sums up is unmistakable. The three leads are all genuinely from Wednesday: Washington preparing new tariffs on trading partners, a migrant boat capsizing off Senegal with dozens missing, and Moscow's own count putting Russian war dead at 490,334. Tuesday-evening stories carry their day in the text:

- **3 leads** — the US tariff plan, the Senegal boat sinking, and the 490,334 toll.
- **10 features** — the CIA and ODNI breach, Huawei's guilty verdict on 10 of 12 counts, the Houthi strike on Riyadh's tallest tower, Ukraine sinking a Russian warship off Libya, the WHO evacuation from the Ebola hospital in Congo, Trump meeting NATO chief Rutte, the Champions League results, England levelling the T20 series, the BJP–Akali Dal reunion, and NATO's early-warning deployment in Poland.
- **22 one-line briefs** (14–35), a timeline strip from Tuesday evening to Wednesday morning, a numbers strip, a region count, and a KEPT OUT box listing the famous stories deliberately left off because they are not 25 November (the ICJ Myanmar ruling of 19 Nov, the COP31 no-deal close, Huang's return to Nvidia, the GTA 6 release).

Every picture is a drawn illustration — no photographs, no generated images — so no text comes out garbled. The Champions League fixtures tonight are marked FORECAST. Wires as of about 02:15 UTC, Wednesday 25 November 2026.

## Contents

- `draw_frontpage.py` — draws `entry.png` from the researched stories (Python 3, Pillow; deterministic, so two runs write the same bytes).
- `entry.png` — the front page, a 1024×1024 PNG.
- `main.ts` — the entrypoint: copies `entry.png` into the output directory (Node 22 standard library only).
- `LICENSE` — MIT licence.

## How to run it

First redraw the page with `python3 draw_frontpage.py`, then run the entrypoint with `MAKEFUN_OUTPUT_DIR=out node main.ts` and find the finished page at `out/entry.png`.
