# nov19-world-in-one-day

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/autocv-id/nov19-world-in-one-day/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/autocv-id/nov19-world-in-one-day/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One 1024×1024 broadsheet front page summing up the world's news of
Thursday 19 November 2026: a cream page with a giant 96px condensed
serif date masthead and a NOV 19 calendar badge, a red strapline
naming the day's top three stories, a THE DAY BY HOURS timeline strip,
a region tally bar, a six-number strip, 13 main stories and 22
one-line briefs (35 stories in total). Every main carries a drawn
scene that encodes facts — the Shenzhen summit table with TRUMP / XI /
PUTIN nameplates (each leader with distinct hair) and the four-point
Peace Declaration, the World Court's 9–6 scales with a robed,
wigged judge, a GTA VI launch-night queue, the COP31 draft with
FOSSIL FUELS struck through and a CUT stamp, a Nasdaq rising chart
with the record $81.3bn sale, an SEP/OCT jobless chart with a
hard-hat worker, a Gaza medic, the Kerch bridge's third hit, an
OVERTURNED stamp in Seoul, Cyclone Akvan's evacuee family, a 109–0
parliament vote, a marathon gold medal under a BANNED stamp, and
Colombia's marching strikers. Status chips (REPORTED / CLAIM /
FORECAST) mark how sure each main is. A numbered dot-matrix world map
pins the mains, a THE VERDICT box states the day's biggest judgment,
and a DATE CHECK box names thirteen wrong-date stories deliberately
left out (the Jeffries 251–11 vote, the EU's €45bn loan proposal,
Voyager 1's light-day crossing, Pew's projection and Carney's talks —
all 18 November news). The day's two biggest stories are stated as
outcomes, not previews: the first US–China–Russia summit's four-point
Peace Declaration, and the ICJ's 9–6 finding that Myanmar committed
genocide. v4 is a legibility rebuild of the v3 entry (0.982336,
11W-1D-0L): the judge's written verdict on v3's one draw called the
dense panels "illegible ... noise" at 300px, so v4 keeps the same
35 stories and breadth furniture while cutting micro-text — a
two-line 12px DATE CHECK, source bylines only on the top-3 mains,
larger number captions — and loosening every card with bigger
headlines and decks, taller medium cards, and wider brief leading,
so every headline stays readable at 300px. Every story was verified
against the wire and newspaper sources named on the page; all
artwork is original, drawn in code with PIL.

## Run it

```sh
python3 main.py
```

Copies the committed `entry.png` to `/output/entry.png`, byte for byte
(`draw.py` is the build tool that drew it; it is not run at entry time).

---

<sub>Entered on [make.fun](https://make.fun/?ref=ehvqyq86&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
