# GraphScore: 96.4 / 100  (great)

_Map: `graphify-out/graph.json` — 3136 dots, 6019 lines._

| Part | Score | Weight | What it means |
|------|------:|-------:|---------------|
| Truthful | 100/100 | 50% | 40 of 40 checked lines were real |
| Complete | 100/100 | 30% | caught 14 of 14 key facts |
| Tidy | 82/100 | 20% | structure health (see checks below) |

## Structure checks (Tidy)

- ✅ **connected** (0.85) — largest cluster holds 85% of dots (3 islands)
- ✅ **not_orphaned** (1.00) — 0 lonely dots (0%)
- ✅ **clean_edges** (1.00) — 0 self-loops, 0 broken lines
- ❌ **deduped** (0.00) — 869 duplicate dots (28%)
- ✅ **hub_sane** (1.00) — busiest dot touches 3% of lines
- ✅ **linked** (1.00) — avg 3.8 lines per dot, density 0.001
- ✅ **well_clustered** (1.00) — community separation (modularity) = 0.95

## How to improve the score

**Structural fixes:**

- 869 duplicate dots (28%) — the same thing named slightly differently. Use consistent naming/casing so entity-resolution merges them.

**General:** a doc that is a bare API index (just a list of names) makes graphify over-invent relationships — prefer prose that states real relationships. Very large files can get truncated during extraction — split them. Re-run the score after fixes to confirm it rose.

## Read this before trusting the number

- **Judge:** the Truthful/Complete scores were read by **tencent/hy3**. A weaker model gives a rougher grade; the Tidy score is a script and is identical everywhere.
- **Wobble:** the reading isn't perfectly steady — expect **± a few points** run to run. Big drops are real; tiny ones are noise.
- **Self-grading:** if this map was built by the same model that judged it, the Truthful score skews a little generous.
- **Reference-free:** no answer key — Truthful checks lines against their own source text; Complete checks a sample of files, not every file.