# BUILD REPORT — News Image v3 entry (news-image-20261119)

**Status: LOCAL ONLY. Nothing submitted, nothing uploaded. Awaiting the user's personal approval of the image, per instructions.**

- Page: one 1024×1024 broadsheet, "Thursday 19 November 2026", cream paper, Times-style serif (Liberation Serif), red strapline naming the top 3 stories, region-count bar (ASIA 10 · EUROPE 7 · AFRICA 6 · AMERICAS 5 · MIDDLE EAST 3 · OCEANIA 2 · GLOBAL 2), six by-the-numbers, numbered dot-matrix world map, DATE CHECK exclusion audit.
- **Story count: 35** — 13 mains (3 large + 10 medium, every one a scene illustration whose scene carries facts) + 22 one-line ALSO briefs in two columns.

## What changed vs v2 (top-10 judge-rate research, 20 Nov 2026)

The research (leaderboard + top-10 artifacts) found v2 already led the field on story count, illustrated people (12/13 mains), status chips, DATE CHECK depth and resolved top-2 stories — but trailed #1/#2 on masthead size, scene quality, and information furniture (timeline, verdict box). "People" alone is not a lever: four of the top six have zero illustrated people. v3 closes the measured gaps:

### P0
1. **Masthead 79px → 96px, one line.** No condensed serif is installed (Liberation Serif Bold at 96px is 1,185px wide), so the masthead is rendered at 96px and squeezed horizontally to 916px with LANCZOS (`condensed_line`) — the deterministic equivalent of a condensed display face; glyph height stays full 96px. Date untouched.
2. **THE DAY BY HOURS timeline strip** (one line, under the strapline): 00:00 NZ GTA VI unlocks · MORNING Shenzhen summit · MORNING ICJ verdict 9–6 · AFTERNOON Anthropic debuts · 16:00 KST Korea clears Han · EVENING COP31 drops fossil fuels. Only verified clock times are used (GTA VI midnight NZ, Korea ruling 16:00 KST); the rest are day-part labels. No new stories.
3. **Top-3 scene quality.** Shenzhen trio now has distinct hair (Trump blond swoop, Xi black flat, Putin grey). The ICJ judge was rebuilt (neck, wide shoulders, white jabot with collar tabs, grey wig framing the face, chunky gavel) — it reads as a robed judge, not a pawn. Medium scenes simplified to 1–2 dominant elements each: COP31 lost its delegates (document + CUT stamp only), Anthropic lost the bell-ringer (chart + $81.3bn only), Gaza lost smoke, Korea lost its flag, Cyclone lost the shelter sign, Denmark lost the speaker desk, Australia lost the clipboard.
4. **Kicker** now sells the edge: "35 STORIES · 13 SCENES · EVERY CONTINENT · ALL FROM THIS ONE DAY".

### P1
5. **THE VERDICT box** (one dark line above DATE CHECK): "THE VERDICT — Myanmar committed genocide, 9–6. First state ever found liable."
6. **Number strip:** $120bn → **551,864** (Seoul exam sitters — a distinctive number; $120bn still appears in the COP31 deck). Kept: 3 / 9–6 / $81.3bn / 109–0 / 4.9%.
7. **Marathon promoted to main #12** (NAIROBI · SPORT, medal + BANNED stamp, deck from brief v2 #17); **Berlin demoted to brief #17** ("40 nations back Europe's seat in talks." — Reuters). Australia moved to main #6 to keep 13 mains. Total stays 35; region bar unchanged; map pin #12 moved Berlin → Nairobi (29,12), pin #6 moved to Canberra (42,19).

### P2
8. **DATE CHECK 11 → 13 exclusions** (added: first COP31 draft, Mon 16 Nov; Fed minutes, 18 Nov).
9. **NOV 19 calendar badge** beside the masthead.

### Kept from v2
35 stories, 13 mains (3 large + 10 medium), chips REPORTED/CLAIM/FORECAST + legend, Shenzhen + ICJ stated as resolved outcomes, DATE CHECK as audit (the five 18 Nov stories appear ONLY there), cream broadsheet, top-3 mains, 2-column briefs, numbered map pins.

## Collision fixes found by crop-zoom inspection (15 fixed)
Round 1: Shenzhen doc's 5th line clipped + seal overlap; ICJ 9–6 badge covering the judge + "9 VOTES TO 6" clipped at the scene bottom; COP31 CUT stamp over its text line; marathon BANNED stamp under the REPORTED chip; Korea judge's head + OVERTURNED stamp under the chip; Denmark "ARCTIC PACT" label over a member dot; map pin 4 hidden behind pin 8 (Kerch pin moved 28,5 → 30,4). Round 2: Anthropic "IPO $83" over the bars; Australia "JOBLESS RATE" over "4.9%" + worker's head under the chip; Gaza medic's helmet under the CLAIM chip; Kerch explosion burst under the chip + arch clipped at the scene top; Cyclone spiral striking through "100,000+ IN SHELTERS"; Colombia's 3rd/4th placards under the chip (3 marchers now, placards lowered to side height); GTA "VICE CITY" hidden behind the controller (moved to the street band).

## Layout budget
v3 adds a 96px masthead (+15px), the timeline strip (+22px) and the VERDICT box (+23px). Paid for by compacting: large cards 228→220 (scene 102→96), medium cards 154→147 (scene 59→54), brief line-height 14→13, numbers strip 42→38, region bar 21→19, and smaller gaps throughout. Page content bottom: **1003 / 1024**.

## Verification (all passed)
1. `draw.py` run 2× → identical sha256, 0 warnings.
2. `main.py` with `MAKEFUN_OUTPUT_DIR=/tmp/v3cop` → byte-identical copy (`cmp` clean).
3. PNG signature OK, 320,213 bytes ≤ 1 MiB, 1024×1024 RGB.
4. Story audit: 13 mains + 22 briefs = 35; kicker says 35; region bar sums to 35; DATE CHECK names 13 exclusions; forbidden-token assert passes (no 18 Nov story outside DATE CHECK).
5. Visual: full page + 300px + 14 crop-zooms (all 13 scenes + map) read; no clipped/overlapping text remains; masthead one full line; timeline legible; all 13 map pins visible and matching their mains.
6. Import audit: draw.py only hashlib/os/sys/math/PIL; main.py stdlib-only; no random/time/network.

## Files in this directory
- `entry.png` — the rendered page (1024×1024, 320,213 bytes, sha256 `498c10baa0a2f8b60a7a053dd5f22acb77bfc879d81ac76f04f9341214be9505`)
- `entry-300.png` — 300px-wide downscale used for the legibility check
- `main.py` — the shipped entrypoint: stdlib-only copier, copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`) — no PIL, no re-render
- `draw.py` — the local build program (Python + PIL) that renders entry.png; NOT the entrypoint
- `README.md` — three LINKED make.fun badges for competition news-image-20261119, repo autocv-id/nov19-world-in-one-day
- `LICENSE` — MIT, Copyright (c) 2026 autocv-id
- `.makefun/owner.json` — `{"wallet": "9uafWyVTaY1eGdvsNChdRdcAvzZ4JWxeLULgXgYpGanu"}`
- `BUILD-REPORT.md` — this file
