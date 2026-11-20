# BUILD REPORT — News Image v4 entry (news-image-20261119)

**Status: LOCAL ONLY. Nothing submitted, nothing uploaded. Awaiting the user's personal approval of the image, per instructions.**

- Page: one 1024×1024 broadsheet, "Thursday 19 November 2026", cream paper, Times-style serif (Liberation Serif), red strapline naming the top 3 stories, region-count bar (ASIA 10 · EUROPE 7 · AFRICA 6 · AMERICAS 5 · MIDDLE EAST 3 · OCEANIA 2 · GLOBAL 2), six by-the-numbers, numbered dot-matrix world map, DATE CHECK exclusion audit.
- **Story count: 35** — 13 mains (3 large + 10 medium, every one a scene illustration whose scene carries facts) + 22 one-line ALSO briefs in two columns.

## Why v4 exists — the v3 heat autopsy (facts, not guesses)

v3 scored 0.982336 (11W-1D-0L, #602, 12 matches). It beat all 4 anchors (margins 4–5, including the 4-strong anchor) and 7 of 8 rung opponents (margins 2–4). The one draw was round 5 vs a clean 6-story rung entry: call 0 (opponent first) went to the opponent, margin 3; call 1 (us first) went to us, margin 3 — split 1–1, 10 points instead of 16–20. The judge's written reasons:

- Call 0 (lost): our page was too dense — "14 dense panels, 35 story cards and micro-text (stats, bylines, 'date check' footnote) are illegible and read as noise" at ~300px; the opponent was "one clean composition, legible small".
- Call 1 (won): our breadth dominated — "12+ scenes spanning diplomacy, justice, markets, climate, Gaza, Ukraine, sport and labour across every continent, with sources and a timeline" — but the judge still conceded the opponent "reads far better at 300px and looks cleaner".

Design conclusion: v4 must win breadth (criterion 2) WITHOUT losing readability/craft (criteria 3+5) against a clean page. That is the only path to 12–0–0 and top 20 (bar: #20 at 0.989920).

## What changed vs v3 (legibility rebuild — same 35 stories, same furniture)

### Micro-text cuts (the exact things the judge named)
1. **DATE CHECK 3 lines → 2 lines, 11px → 12px.** Reworded shorter ("Every story here happened, or was first reported, on 19 Nov 2026. LEFT OUT AS OTHER DAYS' NEWS (13): …") — all 13 exclusions still named verbatim (assert: 13/13), so the date-discipline signal is intact and the box is now two lines of readable type instead of a grey block.
2. **Bylines removed from the 10 medium decks** ("— Reuters" / "— AP" / … dropped). Top-3 mains keep their bylines (the judge praised "with sources" in call 1). Sources still appear in the ALSO briefs and the colophon.
3. **Number-strip captions 10px → 11px** (fit 11→10); the $81.3bn caption shortened to "Anthropic's record sale" so all six captions fit at 11px.
4. **Colophon shortened + 11px** (source list trimmed to 8 outlets; still names the wires).

### Looser cards (freed space → whitespace + bigger type, not new content)
5. **Headlines +1px max, decks +1px max** (large 30→31 / 14→15; medium 21→22 / 13→14; minima unchanged so the auto-fit never overflows). Tags 11→12 (large) / 9→10 (medium).
6. **Medium cards 147px → 152px tall, scenes 54px → 56px** — the extra height pays for the bigger type and slightly larger scenes.
7. **ALSO brief leading 13px → 14px** — the 22 one-line briefs stay one line each but the lines are now cleanly separated at 300px. Map caption and chip legend 9px → 10px.

### Kept from v3
35 stories (identical list), 13 mains (3 large + 10 medium), masthead 96px one line + NOV 19 badge, top-3 mains (Shenzhen/ICJ/GTA VI), chips REPORTED/CLAIM/FORECAST + legend, region bar, timeline strip, THE VERDICT box, kicker "35 STORIES · 13 SCENES · EVERY CONTINENT · ALL FROM THIS ONE DAY", Shenzhen + ICJ as resolved outcomes, DATE CHECK as audit (the five 18 Nov stories appear ONLY there), cream broadsheet, 2-column briefs, numbered map pins. main.py is byte-identical to v3 (copier logic untouched).

## Collision fix found by crop-zoom inspection (1 fixed)
Colombia's 3rd marcher: his head was clipped ~2px by the REPORTED chip (inherited v3 geometry, exposed by the 56px scene). Fixed by shortening that marcher 30→26px tall — he now reads as a naturally shorter figure in the crowd, head fully clear. Re-verified by crop.

## Layout budget
v4 spends: medium rows +10px (2× 152 vs 147), ALSO block +11px (14px leading). It saves: DATE CHECK −7px (2 lines at 12px vs 3 at 11px). Net +14px vs v3. Page content bottom: **1017 / 1024** (7px slack; 0 warnings).

## 300px verdict: PASS, visibly cleaner than v3
Masthead dominant and fully legible; strapline + 6 numbers + top-3 headlines legible; all 10 medium headlines now have a legible first line (v3's second-row medium headlines were half-blurred); ALSO lines stay distinct instead of merging; DATE CHECK reads as two lines of text rather than a grey block. Medium decks still blur at 300px (they are 11–14px at full size) — unavoidable at 35 stories — but they are shorter (no bylines) and sit in visibly airier cards, so they no longer read as "noise" blocks.

## Remaining weaknesses (honest)
- **Density is reduced, not eliminated.** 35 stories on one page is still dense by construction; a 6-story clean page will always read better at 300px. v4 bets that the judge weights breadth (criterion 2) above readability (criteria 3/5) when the page is no longer *illegible* — which is exactly what call 1 of the v3 draw said ("readability sits below selection in the criteria"). If a future judge weights the other way in both calls, we lose that matchup again. There is no way to remove this trade-off without cutting stories, which the brief forbids.
- **Win margins vs rung opponents were 2–4 in v3** (not 5s). Bigger type does not change the stories themselves; the rate gain depends on the judge finding the cleaner page more persuasive in close calls. Top-20 (0.989920) needs both the draw flipped to a win AND strong margins — plausible, not guaranteed.
- **Page bottom is tight** (1017/1024, 7px slack). Any further vertical addition needs a compensating cut.
- **In-scene 8px labels** (e.g. "THE HAGUE · PEACE PALACE", "100,000+ IN SHELTERS") remain — they carry facts at full size and the judge never named them, but they are still ~2px at 300px.

## Verification (all passed)
1. `draw.py` run 2× in fresh dirs → identical sha256, 0 warnings, bottom 1017/1024.
2. `main.py` copier test byte-identical (`cmp` clean); main.py diff vs v3 is empty.
3. PNG signature OK, 322,176 bytes ≤ 1 MiB, 1024×1024 RGB.
4. Story audit: 13 mains + 22 briefs = 35; kicker says 35; region bar sums to 35; DATE CHECK names 13/13 exclusions; forbidden-token assert passes (no 18 Nov story outside DATE CHECK).
5. Visual: full page + 300px + 17 crop-zooms (3 large + 10 medium cards + map + ALSO + VERDICT/DATE CHECK/colophon) read; no clipped/overlapping text remains; all 13 map pins visible and matching their mains; DATE CHECK is 2 lines at 12px.
6. Import audit: draw.py only hashlib/os/sys/math/PIL; main.py stdlib-only; no random/time/network (the two grep hits are docstring words).

## Files in this directory
- `entry.png` — the rendered page (1024×1024, 322,176 bytes, sha256 `be8c155259bebaf49e04c0ce080951cdd28dc82b51a724dfa7a730934d892f0c`)
- `entry-300.png` — 300px-wide downscale used for the legibility check
- `main.py` — the shipped entrypoint: stdlib-only copier, copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`) — no PIL, no re-render
- `draw.py` — the local build program (Python + PIL) that renders entry.png; NOT the entrypoint
- `README.md` — three LINKED make.fun badges for competition news-image-20261119, repo autocv-id/nov19-world-in-one-day
- `LICENSE` — MIT, Copyright (c) 2026 autocv-id
- `.makefun/owner.json` — `{"wallet": "9uafWyVTaY1eGdvsNChdRdcAvzZ4JWxeLULgXgYpGanu"}`
- `BUILD-REPORT.md` — this file
