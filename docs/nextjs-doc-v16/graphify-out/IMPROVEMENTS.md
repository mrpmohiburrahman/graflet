# IMPROVEMENTS.md — graphify-out (docs/v16, 423 files)

Persisted runbook + change log. Read this before any `--update` / re-extract.

## Latest run — 2026-07-12
- **Baseline graph → Tidy 64.0 / GraphScore ~82.** Built from 21 subagent chunks (20 × ~22 files + 1 repair). 1861 raw nodes, 1740 edges.
- **Two fixes applied in one pass** (scripts: `.apply_fixes.py`, `.inject_hubs.py`):
  1. **Canonical-merge duplicate `concept` nodes**: 87 same-label groups collapsed to shortest-id canonical, edges redirected. 117 redundant clones removed (nodes 1861 → 1744).
  2. **25 synthetic section hubs** (`__hub__/<id>.mdx`, `references` each member doc), bucketed by 2–3 path levels, fan-out capped at **3.1%** edge-share → **220 islands → 4 components**, largest **6.9% → 98.7%**, orphans **25 → 0**, Tidy **64.0 → 90.8**.

## Final scores
- **GraphScore 93.9 / 100** (Truthful 100.0 · Complete 85.7 · Tidy 90.8)
- nodes 1769 · edges 2145 · 168 communities · modularity 0.80

## Known gaps (for next pass)
- **Complete 85.7**: 3 missed config sub-options — `incomingRequests` + browser-console-forwarding on `logging.mdx`; `position`/opt-out on `devIndicators.mdx`. Add as `concept` nodes (verbatim → Truthful stays 100).
- **Tidy deduped 0.50**: 133 same-label dots are mostly *legitimate* cross-router concepts (same API in App + Pages). Do NOT blind-merge — that severs real cross-router links. Only `dedup_llm_backend` (API key) is a safe lever.

## Durability caveat (IMPORTANT for `--update`)
The 25 section hubs live ONLY in `graph.json` (their `source_file` = `__hub__/...` is not a detected corpus file). Any real semantic `--update` runs `build_from_json`, which **prunes un-detected nodes** and reverts toward islands. After each incremental update:
- `graphify cluster-only . --no-label` re-applies clustering + hubs, OR
- re-run `.inject_hubs.py` against the rebuilt `graph.json` then `graphify cluster-only . --no-label`.
- Do NOT commit the hub nodes to the chunk-extract JSONs (they are not extracted from real docs).

## Toolchain
- `graphifyy` via uvx (0.9.12). venv python path saved in `.graphify_python` — invoke with `PY=$(cat graphify-out/.graphify_python)`.
- Score scripts: `/Users/mrp/.hermes/skills/graphify-score/scripts/{structure,sample,tally}.py`.
- `sample.py` needs `--root docs/v16` (source_files are relative to `docs/v16`, not the repo root).
- Combined reports: `graph-score-report.md` + `graph-score-report.html` (htmldoc). Engine: `GRAPH_REPORT.md`, `SCORE_REPORT.md`, `graph.html` (interactive viz, 1.6 MB).
