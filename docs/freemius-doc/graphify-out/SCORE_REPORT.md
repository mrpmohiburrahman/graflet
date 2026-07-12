# GraphScore: 92.4 / 100  (great)

_Map: `graphify-out/graph.json` — 570 dots, 1974 lines._

| Part | Score | Weight | What it means |
|------|------:|-------:|---------------|
| Truthful | 100/100 | 50% | 40 of 40 checked lines were real |
| Complete | 79/100 | 30% | caught 23 of 29 key facts |
| Tidy | 93/100 | 20% | structure health (see checks below) |

## Important facts the map missed

- Founding / team context  _(from about.md)_
- EU/UK VAT obligations  _(from blog-taxes-cheat-sheet-wordpress-developers.md)_
- Tax registration thresholds  _(from blog-taxes-cheat-sheet-wordpress-developers.md)_
- Commission / payout structure  _(from affiliate-program.md)_
- Affiliate coupon & referral links  _(from affiliate-program.md)_
- Embed / magic-login  _(from customer-portal.md)_

## Structure checks (Tidy)

- ✅ **connected** (0.93) — largest cluster holds 93% of dots (39 islands)
- ⚠️ **not_orphaned** (0.73) — 38 lonely dots (7%)
- ✅ **clean_edges** (1.00) — 0 self-loops, 0 broken lines
- ✅ **deduped** (0.98) — 2 duplicate dots (0%)
- ✅ **hub_sane** (1.00) — busiest dot touches 2% of lines
- ✅ **linked** (1.00) — avg 6.9 lines per dot, density 0.012
- ✅ **well_clustered** (1.00) — community separation (modularity) = 0.55

## How to improve the score

**Files dragging the score down** (fix these first):

| File | Made-up lines | Missed facts |
|------|--------------:|-------------:|
| `blog-taxes-cheat-sheet-wordpress-developers.md` | 0 | 2 |
| `affiliate-program.md` | 0 | 2 |
| `about.md` | 0 | 1 |
| `customer-portal.md` | 0 | 1 |

**General:** a doc that is a bare API index (just a list of names) makes graphify over-invent relationships — prefer prose that states real relationships. Very large files can get truncated during extraction — split them. Re-run the score after fixes to confirm it rose.

## Read this before trusting the number

- **Judge:** the Truthful/Complete scores were read by **Claude Sonnet (host agent, also built the graph)**. A weaker model gives a rougher grade; the Tidy score is a script and is identical everywhere.
- **Wobble:** the reading isn't perfectly steady — expect **± a few points** run to run. Big drops are real; tiny ones are noise.
- **Self-grading:** if this map was built by the same model that judged it, the Truthful score skews a little generous.
- **Reference-free:** no answer key — Truthful checks lines against their own source text; Complete checks a sample of files, not every file.