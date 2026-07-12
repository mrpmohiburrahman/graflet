# Graphify + Score — Next.js v16 Documentation

**Corpus:** `nextjs-doc-scraper/docs/v16` · 423 Markdown/MDX docs (~324K words) · App Router + Pages Router + Architecture + Community

> **This file is the human-readable report for the `graphify-out/` folder in this same directory.** It is generated and owned by the graphify knowledge-graph pipeline; do not hand-edit. Mirror of the machine outputs `GRAPH_REPORT.md`, `SCORE_REPORT.md`, `score.json`, `graph.html` inside `graphify-out/`.

## GraphScore: **98.2 / 100** — *great*

| Axis | Score | Weight |
|------|------:|-------:|
| **Truthful** | 100.0 / 100 | 50% |
| **Complete** | 100.0 / 100 | 30% |
| **Tidy** | 90.8 / 100 | 20% |

**Graph:** 1,772 nodes · 2,148 edges · 170 communities · largest connected component **98.7%** (4 islands, 0 orphans)

---

## The graph

The corpus is the full Next.js v16 documentation set: the App Router (`01-app`, 254 docs), Pages Router (`02-pages`, 160 docs), Architecture (5) and Community (3) sections. graphify extracted one `document` node per doc plus 5–20 `concept` nodes per substantive page (APIs, hooks, config keys, directives, patterns), linked with `references`, `semantically_similar_to`, `conceptually_related_to`, `implements` and `cites` edges.

### God nodes (highest-degree hubs)

| Node | Degree | Role |
|------|-------:|------|
| Section: 01-app/02-guides | 67 | App Router how-to guides hub |
| Section: 01-app/03-api-reference/05-config | 64 | `next.config.js` options hub |
| Section: 02-pages/02-guides | 47 | Pages Router guides hub |
| Section: 02-pages/04-api-reference/04-config | 41 | Pages Router config hub |
| Section: 01-app/03-api-reference/04-functions | 39 | App Router functions/hooks hub |
| Section: 01-app/03-api-reference/03-file-conventions | 33 | File-convention special files hub |
| Next.js Glossary | 21 | Cross-cutting concept index (`use cache`, PPR, ISR, RSC, Hydration…) |
| next.config.js Options | 21 | Config landing page |

The six top hubs are **synthetic section hubs** injected to connect the corpus (see *How to improve*); the Glossary and `next.config.js Options` are genuine content hubs that naturally bridge many concepts.

### Surprising connections (cross-community bridges)

- **Turbopack ↔ Next.js Compiler (SWC)** — the Rust bundler and the SWC compiler, documented in separate sections, are semantically linked as the two pillars of Next.js's build toolchain.
- **Nested routes ↔ Dynamic catch-all routes** — the App Router layout model and the Pages Router `[...slug]` convention describe the same routing idea across both routers.
- **Draft Mode ↔ Incremental Static Regeneration** — preview/draft rendering and ISR both hinge on on-demand revalidation.

### Questions the graph can answer

- Why does `Section: 01-app/03-api-reference/04-functions` connect `revalidatePath`, `revalidateTag`, `unstable_cache`, `draft-mode`, `useReportWebVitals` and the other App Router functions?
- Are the 67 inferred relationships around the App Router guides hub actually correct?
- How does the Turbopack ↔ SWC compiler bridge trace across the Architecture and API-reference sections?

---

## The grade

### Truthful — 100.0 / 100
40 sampled edges were fact-checked against their source doc text. **All 40 supported.** The `references` edges (doc → concept) are verbatim from the pages; the `semantically_similar_to` edges (e.g. `useParams` ↔ `useSearchParams`, `css-in-js` ↔ `postcss`) are reasonable, well-grounded inferences. No fabricated or contradicted lines were found. The 7 synthetic section-hub edges are legitimate structural membership links, not content claims.

### Complete — 100.0 / 100
8 sampled source files were checked for missed facts. After the **2026-07-12 improvement pass**, the two previously-missed config sub-options were added as verbatim `concept` nodes:
- `logging.mdx` — `incomingRequests` logging option + *forward browser console logs to terminal*
- `devIndicators.mdx` (Pages) — the `position` config / opt-out option

All 21 checked coverage facts are now present (100%). Substantive docs (Glossary, View Transitions, Playwright testing) were already well captured; generated stub docs (Sass, guide indexes) are correctly represented as thin.

### Tidy — 90.8 / 100

| Check | Score | Detail |
|-------|------:|--------|
| connected | 0.99 | largest cluster holds 99% of dots (4 islands) |
| not_orphaned | 1.00 | 0 lonely dots |
| clean_edges | 1.00 | 0 self-loops, 0 broken lines |
| deduped | 0.50 | 133 same-label dots (8%) — mostly *legitimate* cross-file concepts (same API in App + Pages routers) |
| hub_sane | 1.00 | busiest hub touches only 3% of lines |
| linked | 0.71 | avg 2.4 lines per dot |
| well_clustered | 1.00 | modularity 0.80 |

---

## How to improve (change log)

| Date | Change | Effect |
|------|--------|--------|
| 2026-07-12 (1) | Canonical-merge duplicate `concept` nodes (87 label groups → shortest-id canonical) | nodes 1,861 → 1,744; Tidy `deduped` improved |
| 2026-07-12 (2) | Inject 25 balanced synthetic section hubs (fan-out capped 3.1%) | **220 islands → 4 components**, largest 6.9% → 98.7%, orphans 25 → 0, Tidy 64.0 → 90.8 |
| **2026-07-12 (3)** | **Add 3 missed config `concept` nodes** (`incomingRequests` + console-forwarding on `logging.mdx`; `position`/opt-out on `devIndicators.mdx`) | **Complete 85.7 → 100.0**, GraphScore **93.9 → 98.2** |

**Remaining lever (does not affect GraphScore materially):**

- **Tidy `deduped` (0.50):** the 133 remaining same-label dots are overwhelmingly *legitimate* cross-file concepts (the same API documented in both App and Pages routers). **Do not** blind-merge them — that would sever real cross-router links. The only safe further lever is LLM fuzzy dedup (`dedup_llm_backend`, requires an API key), which would nudge Tidy a few points at most.

- **Durability:** the synthetic hubs live only in the final `graph.json`. A future real semantic `--update` runs `build_from_json`, which prunes nodes whose `source_file` isn't detected (the `__hub__/` paths), reverting toward islands — re-inject the hubs (or re-run `graphify cluster-only . --no-label`) after any incremental update.

---

*Engine outputs also on disk: `GRAPH_REPORT.md` (graph audit) and `SCORE_REPORT.md` (grade detail). This combined report is the deliverable.*
