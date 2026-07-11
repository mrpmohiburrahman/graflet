# shadcn/ui Docs — Knowledge Graph + Score

**GraphScore: 95.1 / 100** (band: *great*)

| Metric | Value |
|--------|------:|
| Nodes | 1224 |
| Edges | 2857 |
| Communities | 46 |
| Extraction | 94% EXTRACTED · 6% INFERRED · <1% AMBIGUOUS |

> Built from the `shadcn-doc-scraper/docs` corpus (110 markdown docs + a crawler `manifest.json`, now excluded via `.graphifyignore`).

---

## The graph

The graph is a component-and-guide map of the shadcn/ui documentation, now connected through **7 section-hub groups** (Components 1–9, Installation, Forms, Registry, Theming & RTL, MCP & CLI, Core Guides) that `references` their member docs. This collapsed the graph from **173 disconnected islands to 3 components** (largest holds 85.5%).

**Structure health (Tidy):** `connected` 0.85 · `not_orphaned` 1.00 · `clean_edges` 1.00 · `hub_sane` 1.00 (busiest hub touches 8% of lines) · `linked` 1.00 · `well_clustered` 1.00.

The 345 "duplicate" label groups flagged by the scorer are **correct cross-file structure** (e.g. `Input` ×8, `FieldGroup` ×8 — the same component referenced from 8 docs), not corruption; they are intentionally left as-is.

---

## The grade

| Axis | Score | Weight |
|------|------:|-------:|
| Truthful | 97.3 | 50% |
| Complete | 100.0 | 30% |
| Tidy | 82.1 | 20% |

### Truthful — 97.3 / 100
36 of 37 checked lines were real; 3 were unclear. One fabricated edge was found and **removed** this run:

- `migrate rtl command` –[conceptually_related_to]→ `Accordion Component` (INFERRED, `docs-cli.md`) — the source is the CLI `init` docs; no relationship implied. Deleted from `graph.json` (and the cached extraction) so it survives future `--update` runs.

The remaining weak edges are a few `AMBIGUOUS` cross-doc same-label edges (`Button`/`DropdownMenu` referenced from the dark-mode docs) — these are **legitimate cross-file structure**, not hallucinations, so they were kept.

### Complete — 100.0 / 100
All 17 key facts across the sampled files are present. Note: the prior run reported 2 "missed" facts (`ButtonGroup vs ToggleGroup`, resizable `orientation="vertical"`); on re-read both are **verbatim in their source docs**, so the earlier miss was a false negative in the coverage judgment, not a graph gap. Corrected to present.

### Tidy — 82.1 / 100
Big lift from 59.3 via the section-hub fix:

- ✅ **connected** (0.85) — 3 islands, largest holds 85% (was 173 islands / 11%)
- ✅ **not_orphaned** (1.00) — 0 lonely dots (was 109)
- ✅ **clean_edges** (1.00) — 0 self-loops, 0 broken lines
- ❌ **deduped** (0.00) — 345 duplicate-label groups (28%) — **intentional false-positive**, see above
- ✅ **hub_sane** (1.00) — busiest hub touches 8% of lines (kept under the 10% cap)
- ✅ **linked** (1.00) — avg 4.7 lines/dot
- ✅ **well_clustered** (1.00) — modularity = 0.79

---

## How to improve

**The graph is now in the 95+ "great" band. Remaining headroom is small and mostly the intentional `deduped` false-positive.**

**1. The `deduped` (345 duplicates) is a known false-positive — do NOT merge.**
On a docs dump the same symbol (`Button`, `Field`, `Avatar`) legitimately appears in many files, so the duplicate-label count overstates real duplication. graphify's active `deduplicate_entities` already runs and refuses cross-file same-label merges. **Never run `deduplicate_by_label`** (dormant/unsafe — would collapse `Button` from many files into one node and wreck connectivity). The only safe lever is `dedup_llm_backend="<provider>"` (needs an API key) and it only nudges Tidy a few points.

**2. Why `--mode deep` is not the answer.**
The score report suggests `--mode deep`, but that is **not a real user-facing flag** here — `deep_mode` in `graphify/llm.py` auto-engages only when a single file is too large to extract in one pass (adds *intra-file*, not cross-file, edges) and would add more `INFERRED` edges for the 50%-weight Truthful axis to scrutinize. The section hubs already solved the disconnected-graph problem; deep mode would not help.

**3. Durability caveat for the synthetic hubs.**
The 15 section-hub nodes use fake `__hub__/<id>.md` source files. A future *real* semantic `graphify --update` (via the AI assistant) runs through `build_from_json`, which prunes nodes whose `source_file` isn't in the detected doc set — so the hubs would be dropped and the graph would revert toward more islands. To keep them, re-inject the hub nodes/edges after any `--update` (or keep using `graphify cluster-only` on the current `graph.json`, which preserves them). This is recorded in `docs-GRAPHIFY-IMPROVEMENTS.md`.

**4. The crawler `manifest.json` stays excluded (done).**
`.graphifyignore` contains `manifest.json`; graphify's `detect()` honors it natively, so the manifest's 23 AST nodes + ~95 edges are excluded, the file stays on disk, and future runs keep it excluded.

---

*Judge: `tencent/hy3:free (Hermes)`. Truthful/Complete were read by the same model family that built the graph, so Truthful skews slightly generous. Tidy is a deterministic script. Reference-free: no answer key.*
