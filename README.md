# news-image-20261125 — round 2

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun · rank](https://make.fun/badge/news-image-20261125/vickyair1/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun · reward](https://make.fun/badge/news-image-20261125/vickyair1/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Sum up the world's news of **Wednesday 25 November 2026** in one image:
a broadsheet front page, drawn entirely in code (PIL, no photos, no network).

## The image

- **Masthead:** Wednesday 25 November 2026, with the three leads in the standfirst.
- **Numbers strip:** 1st Pakistani in orbit · 10/12 Huawei counts · ~490,000 Russian war dead · 11 wounded at the PIF tower · 5–1 Real Madrid · −15% SoftBank.
- **3 large illustrated leads:** Shenzhou-24 lifts off with Pakistan's first astronaut (00:18 UTC, docks at Tiangong 03:56 UTC) · Huawei guilty on 10 of 12 counts in Brooklyn · Russia's own leaked Rosstat data shows nearly 500,000 war dead.
- **9 more illustrated panels:** PIF tower hit again · Cartagena hostages freed · Australia–Solomon Islands treaty · Chen Jining probed · Asia's AI stocks plunge · US tariffs on 16 economies · Hodeidah strikes · Zelenskyy claims the Sparta II drone hit · Real Madrid 5–1 PSV.
- **World map** with numbered pins matching story numbers, plus a region tally.
- **28 more briefs** (40 stories total), a UTC timeline strip, and a **DATE CHECK** box: every story happened, or was first reported, on Wednesday 25 November 2026; Tuesday-evening events are in as Wednesday's morning news, and stale stories (Senegal boat 19 Nov, Sparta II strike 21 Nov, COP31 failure 22 Nov, first PIF strike 19 Nov) are listed as left out.
- Every story carries a per-story source tag (Reuters, AP, BBC, Xinhua, AFP, Bloomberg, Mediazona, Meduza, and more).

## Run it

```sh
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

Deterministic: no network, no timestamps, no randomness — two runs write
byte-identical output (verified, see SUBMISSION.md).

## Files

- `main.py` — the whole entry: story data, 12 vector illustrations, map, layout.
- `SUBMISSION.md` — story list with dates/sources, fixes vs round 1, checker result, determinism hashes, HEAD.
- `LICENSE` — MIT.
