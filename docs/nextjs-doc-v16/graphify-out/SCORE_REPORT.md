# GraphScore: 98.2 / 100  (great)

_Map: `graphify-out/graph.json` — 1772 dots, 2148 lines._

| Part | Score | Weight | What it means |
|------|------:|-------:|---------------|
| Truthful | 100/100 | 50% | 40 of 40 checked lines were real |
| Complete | 100/100 | 30% | caught 21 of 21 key facts |
| Tidy | 91/100 | 20% | structure health (see checks below) |

## Structure checks (Tidy)

- ✅ **connected** (0.99) — largest cluster holds 99% of dots (4 islands)
- ✅ **not_orphaned** (1.00) — 0 lonely dots (0%)
- ✅ **clean_edges** (1.00) — 0 self-loops, 0 broken lines
- ⚠️ **deduped** (0.50) — 133 duplicate dots (8%)
- ✅ **hub_sane** (1.00) — busiest dot touches 3% of lines
- ⚠️ **linked** (0.71) — avg 2.4 lines per dot, density 0.001
- ✅ **well_clustered** (1.00) — community separation (modularity) = 0.80

## Read this before trusting the number

- **Judge:** the Truthful/Complete scores were read by **Hermes (tencent/hy3)**. A weaker model gives a rougher grade; the Tidy score is a script and is identical everywhere.
- **Wobble:** the reading isn't perfectly steady — expect **± a few points** run to run. Big drops are real; tiny ones are noise.
- **Self-grading:** if this map was built by the same model that judged it, the Truthful score skews a little generous.
- **Reference-free:** no answer key — Truthful checks lines against their own source text; Complete checks a sample of files, not every file.