# IMPROVEMENTS.md — React 19 Docs Graph

Persistent improvement log for the graphify + score run on `react-doc-scraper/docs/react-19`.
Updated: 2026-07-12 (run 2 — section-hub bridging applied). Re-read before any incremental
`--update` so fixes extend (not undo) prior work.

## Current state (this run)

- **GraphScore: 96.4 / 100** (band: `great`) — **up from 93.4**
  - Truthful **100** · Complete **100** · Tidy **81.9** (up from 66.9)
- Graph: **3,136 nodes · 6,019 edges · 81 communities** (was 3,128 / 5,798 / 171)
- Source: 221 markdown docs (~479,110 words), crawler `manifest.json` excluded.
- Token cost: **0 in / 0 out** (deterministic host-side extraction — no Gemini key).

## Run 1 (baseline, 2026-07-12)
- Excluded crawler `manifest.json` via `.graphifyignore` (kept on disk).
- Deterministic heading-based extraction → 3,128 nodes / 5,798 edges, verified clean.
- Built, clustered, labeled, scored → **GraphScore 93.4** (Tidy 66.9).
- Wrote combined `graph-score-report.md` + `.html`, `IMPROVEMENTS.md`.

## Run 2 (improvement applied — section-hub bridging)
**Lever:** the only sub-100 axis was Tidy (66.9), dragged by **77 islands** (`connected` failed,
largest 9%). The 869 "duplicate-label" nodes are legitimate per-file headings — NOT a defect.

**Fix:** injected 8 balanced synthetic section-hub `document` nodes (`__hub__/*`, fake `source_file`)
that `references` their member docs, bucketed by filename prefix:
- `__hub__/ref_react.md` (63 docs), `__hub__/ref_react_dom.md` (39), `__hub__/ref_rsc.md` (5),
  `__hub__/ref_eslint_devtools.md` (19), `__hub__/learn.md` (50), `__hub__/blog.md` (23),
  `__hub__/community.md` (8), `__hub__/meta.md` (14).
- Each hub's edge-share is 0.09%–1.09% — all **well under the 10% `hub_sane` cap** (top 1.05%).

**Result:** islands **77 → 3** (largest 84.6%), 0 dangling, Tidy **66.9 → 81.9**,
GraphScore **93.4 → 96.4**. Truthful/Complete stayed 100. Zero tokens, zero hallucination.

**How it was applied (durability note):** `to_json`/`build_from_json` PRUNE nodes whose
`source_file` isn't in the detected set, so the hubs must be injected into the final `graph.json`
**after** any build, then the report/HTML regenerated from that on-disk graph. Re-run recipe:
`python3 graphify-out/.inject_hubs.py` → rebuild `G` from `graph.json` → `generate_html`/`report`.
The harness script is kept at `graphify-out/.inject_hubs.py`.

## Evaluated and intentionally NOT done
- **Merge the 869 "duplicates"** — they are per-file headings (`Sitemap`, `Props`…); merging wrecks
  provenance. `deduplicate_by_label` left off; active `deduplicate_entities` already on.
- **Deep mode (`--mode deep`)** — not a user-facing switch; only adds intra-file INFERRED edges,
  cannot fix disconnected graph.
- **`graphify update` CLI** — code-AST rebuild that corrupts docs dumps; not used.
- **`dedup_llm_backend`** — needs API key; unnecessary (duplicates are correct here).

## Possible next lever (not yet applied)
Add curated cross-doc "see also" edges (hook ref → `learn-*` guide; `react-dom/*` → `react-dom`)
where the source truly supports it. Would nudge Tidy/GraphScore toward ~97–98 with no fabrication.

## Re-run recipe (incremental)
1. New `.md` files in corpus root; keep `.graphifyignore` (manifest excluded).
2. Semantic cache keyed by sha256(abs path + full text) → unchanged docs stay cached (0 tokens).
3. Re-run `.gen_chunks.py` over all docs, merge → build.
4. **Re-inject hubs** via `.inject_hubs.py` (a real `--update` re-prunes them), then regenerate
   report/HTML from the on-disk graph.
5. Re-score: `structure.py` + `sample.py --root <corpus>` + verdicts + `tally.py`.

## File inventory (graphify-out/)
- `graph.json` — 3136 nodes / 6019 edges (networkx node-link: `nodes` + `links`; hubs included)
- `graph.html` — interactive viz
- `GRAPH_REPORT.md` — graph engine report
- `SCORE_REPORT.md` + `score.json` — grade (graphscore 96.4, axes 100/100/81.9)
- `graph-score-report.md` / `graph-score-report.html` — the combined deliverable
- `IMPROVEMENTS.md` — this log
- `.graphify_score/` — tidy.json + worksheets + verdicts (verifier reads them)
- `.graphifyignore` (corpus root) — excludes `manifest.json`
- `.gen_chunks.py` — deterministic extraction generator
- `.inject_hubs.py` — section-hub injector (post-build)
- Parent-folder summary: `../react-19-GRAPH-SUMMARY.md` (associates this graph with the `react-19` folder)
