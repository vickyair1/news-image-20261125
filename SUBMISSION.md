# SUBMISSION — news-image-20261125 round 2 (Force_Last, replaces round 1)

- Slug: `news-image-20261125` · $100 pool, top 50 share prizes (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
- Deadline: 2026-11-27T00:00:00Z (07:00 WIB 27 Nov)
- Program: `main.py` (Python, PIL only, no network) → writes `/output/entry.png`, 1024×1024 PNG, 200,459 bytes (< 1 MiB)
- Code HEAD: `ec6d655c5354c6e140f5d14f672d51cba1491981` (this file added in a follow-up commit; final HEAD reported to the parent)
- Round 1 is live but ranks below 200 (score < 968,077; top-50 bar 980,385; top-10 bar 986,584) and is worth $0. Round 2 is a fresh build from this spec alone — round-1 code/data files were NOT read.

## The four fixes vs round 1

1. **Leads:** Shenzhou-24 (Pakistan's first astronaut, first foreign visitor to Tiangong) + Huawei guilty 10/12 + Russia ~500,000 war dead are the 3 large illustrated leads. Shenzhou-24 was completely missing from round 1.
2. **Illustrated panels:** 12 drawn vector scenes (3 large leads + 9 smaller), each with headline + deck + location/region tag + source tag. Round 1 had only 3 small illustrations.
3. **World map** with numbered pins matching story numbers 1–12, plus a region tally (Americas 13 · Europe 9 · Asia-Pacific 7 · Middle East 5 · Oceania 1 · Africa 3 · Global 2 = 40). Round 1 had no map.
4. **Per-story source tags on every story** (all 40, illustrated and briefs alike). Round 1 had none.

Kept from round 1: numbers strip, UTC timeline strip, DATE CHECK box, taxonomy tags, 35–50 stories (40 here), all dated 25 Nov 2026.

## Story list (all Wed 25 Nov 2026, as first reported that day)

Tuesday-evening events (Huawei verdict, Chen probe, Real Madrid 5–1, Cartagena rescue, Miss Universe crowning) are in as Wednesday's morning news — the convention the live top artifacts use. Two date corrections found by fresh research: Chen **Jining** (not "Jinging"); the Senegal boat capsized **19 Nov**, so it is NOT a story — it is listed in the DATE CHECK as left out.

| # | Story | Date / note | Source |
|---|-------|-------------|--------|
| 1 | Shenzhou-24 lifts off, Pakistani pilot aboard; docks Tiangong 03:56 UTC | 25 Nov 00:18 UTC | Reuters · Xinhua |
| 2 | Huawei guilty on 10 of 12 counts, Brooklyn jury; will appeal | Verdict Tue 24 Nov Brooklyn, reported worldwide Wed 25 Nov | Reuters · Bloomberg · AP |
| 3 | Leaked Rosstat data: ~490,000 Russian war dead to Sep 2026; true toll may top 700,000 | Leak analysis reported 23–24 Nov, read worldwide Wed 25 Nov | Mediazona · Meduza · Reuters |
| 4 | PIF tower hit again, 11 wounded | 2nd strike in days, reported 25 Nov | Reuters · Arab News |
| 5 | Cartagena supermarket hostages freed; 1 captor killed | Siege Tue, stormed Wed 13:30 | AFP · Reuters |
| 6 | Australia–Solomon Islands treaty signed, Canberra | 25 Nov | Reuters · ABC · AP |
| 7 | Xi's anti-graft drive reaches Shanghai party boss Chen Jining | Probe announced Tue; Shanghai pledges loyalty Wed 25 Nov | Reuters · Xinhua |
| 8 | Asia's AI stocks plunge (Kospi −5.9%, Nikkei −2.9%, SoftBank −15%) | 25 Nov | Reuters |
| 9 | US readies new tariffs on 16 economies | USTR probe, reported 25 Nov | Reuters · WSJ |
| 10 | Saudi-led strikes hit Hodeidah port | Early Wed 25 Nov | Arab News · Reuters |
| 11 | Zelenskyy claims the drone hit on Russian cargo ship Sparta II | Claim Wed 25 Nov (strike itself Sat 21 Nov) | Reuters · BBC |
| 12 | Real Madrid rout PSV 5–1 | Tue night, reported Wed 25 Nov | Reuters · TNT Sports |
| 13 | Jennifer Barreto (Puerto Rico) crowned Miss Universe 2026 | Tue night San Juan, reported Wed | AP |
| 14 | Strike on Gaza's Shati camp kills at least four | 25 Nov | Al Jazeera |
| 15 | Saudi defences down two Houthi drones in the east | 25 Nov | Reuters |
| 16 | Iran says two tankers hit by mines, Strait of Hormuz | 25 Nov (claim) | Reuters |
| 17 | Congo Ebola deaths reach 5,678; 11,613 cases | 25 Nov | ABC |
| 18 | Hera reaches the asteroid NASA struck; first images due | 25 Nov | BBC |
| 19 | Two arrested on William and Kate's Windsor estate | 25 Nov | PA · BBC |
| 20 | Nvidia falls ~6% as the Huang rally fades | 25 Nov | Reuters |
| 21 | UK sanctions Myanmar generals over the Rohingya | 25 Nov | BBC |
| 22 | CIA and spy agency hit by cyber breach | 25 Nov | Reuters |
| 23 | Venezuela puts its debt load at $237.5bn | 25 Nov | Reuters |
| 24 | Russian strike kills 2, wounds dozens, Zaporizhzhia | 25 Nov | AP |
| 25 | COP31 chief blames the EU for failure | 25 Nov | BBC |
| 26 | Zimbabwean convicted over Ukraine fight | 25 Nov | BBC |
| 27 | A US destroyer transits the Taiwan Strait | 25 Nov | Reuters |
| 28 | Norway urges restraint after the cargo-ship attack | 25 Nov | Reuters |
| 29 | Gangs burn a police station, Port-au-Prince | 25 Nov | Reuters |
| 30 | North Korea fires two missiles into the sea | 25 Nov | AP |
| 31 | Court restores Senegal as African champions | 25 Nov | CAS · AP |
| 32 | Death-row shooter asks for a stay of execution, Fort Hood | 25 Nov | AP |
| 33 | Politburo meets to set the 2027 reshuffle, Beijing | 25 Nov | Reuters |
| 34 | Markle's lawyers call the new count a pile-on, Los Angeles | 25 Nov | AP |
| 35 | Finland opens a criminal case over the gulf strike | 25 Nov | YLE |
| 36 | US inflation, Q3 GDP due; Fed hike seen | 25 Nov | Reuters |
| 37 | Dell lifts forecasts after record quarter | 25 Nov | Reuters |
| 38 | Commanders beat Bengals 22–20 | 25 Nov | AP |
| 39 | Gold eases after US data; Bitcoin $59,257 | 25 Nov | Reuters |
| 40 | China calls Huawei conviction economic coercion | 25 Nov | Reuters |

DATE CHECK (printed on the image): wires to 06:40 UTC Wed 25 Nov 2026; left out as not 25 Nov — Senegal boat (19 Nov) · Sparta II strike (21 Nov; Zelenskyy's claim IS today's news) · COP31 failure (22 Nov) · first PIF tower strike (19 Nov).

## Checker (fresh kit, pre-bundle)

`node news-image-20261125-kit/cli/makefun.mjs check --kit news-image-20261125-kit --repo .`
(run 2026-11-25 ~10:17 WIB; full output in `check-result.json`, untracked)

- **4 pass:** competition_open, snapshot, license_osi, entrypoint
- **14 skip:** strategy_note, committed_secret, transcripts_recorded, thinking_wellformed, thinking_in_window, thinking_committed, thinking_reproduces, thinking_on_task, thinking_turns, thinking_priced, thinking_revised, thinking_fresh, transcripts_run_record, thinking_own_work
- **1 FAIL:** transcripts_present (no transcripts uploaded yet — expected pre-bundle; parent bundles/submits)

## Determinism

Two runs of `python3 main.py`, byte-identical output:

- Run 1: `f20e090e8c1dd2cc3504dec96ffd73352ce13e3792cc8225672e52a25308eeb6`
- Run 2: `f20e090e8c1dd2cc3504dec96ffd73352ce13e3792cc8225672e52a25308eeb6`
- Size 200,459 bytes, 1024×1024 PNG. (An earlier draft hashed `d9c4b7de…` before the final brief fix; the hash above is the final program's.)

## Files to mirror

- `~/workspace/scratch/news-image-20261125/round2/main.py`
- `~/workspace/scratch/news-image-20261125/round2/README.md`
- `~/workspace/scratch/news-image-20261125/round2/LICENSE`
- `~/workspace/scratch/news-image-20261125/round2/SUBMISSION.md`

NOT mirrored: `news-image-20261125-kit/` and `kit.tar.gz` (fresh kit download, gitignored), `check-result.json` / `check-result.err` (local check logs, gitignored). Do NOT submit from here — parent mirrors to GitHub and submits.

## PACKAGING — 25 Nov 2026 ~17:21 WIB (user go-ahead "Gas news-25 round 2" 17:18)
- Kit verified 11/11 files vs kit.json (bundle sha 946c3b76…; tarball sha c8e85c0b…); competition.yaml + RULES.txt read fully.
- Bundle: `news-image-20261125-r2-bundle.tar.gz`, sha256 `d5fbb1af9e3e2a687d0b86052891a769c19c27cb4620be99dccd4fef2682e6f5` (191,621 bytes; builder session d1b75ded-eb5e-4246-a8c5-4282ced53576 + 1 real muse.db usage row, model ipnext/avocado-5.17-v2). Prompt file = builder's [Subagent Task] brief verbatim (prompt-origin other).
- Check vs commit eb8b957c3903551039c7b50f47ff3e18ff689db2: **14 pass / 0 fail / 5 skip** — reproduces 99.6% (636/638 authored, 0 copied/pasted/read), thinking_revised PASS (main.py final content from 7 messages), thinking_priced + run record PASS. No fixer needed.
- Quota: can_submit **TRUE** (entries_made 1, day cap 6 left 5, hard limit 40 left 39).
- Mirror target (EXISTING round-1 repo): https://github.com/vickyair1/news-image-20261125 (round-1 GitHub HEAD fe766b8f87e555c5a52b937758c6119938f5d4d1) — replace the 4 files with the round-2 versions, then signed submit with the NEW GitHub HEAD. Force_Last: round 2 replaces round 1.
