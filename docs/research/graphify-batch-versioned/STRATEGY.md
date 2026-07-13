# Graphifying the context7-docs tree — batch strategy

**Verdict: one graph per `<owner>/<library>/<version>` directory. 50,855 units,
each an independent `graphify extract` run producing one `graph.json` for that
version's whole nested doc tree. No flattening, no merging, no reliance on the
root `.graphifyignore`. Drive it as an embarrassingly-parallel loop keyed by the
version dir; the only real cost knob is the LLM semantic pass.**

Grounded in two primary-source reads of the graphify source (installed CLI,
package `graphify/`) and the prior FLATTENING note. Source citations are
`file:line` throughout.

## TL;DR (the strategy in 6 bullets)

- **Unit = the version dir.** Point `graphify extract` at
  `<owner>/<library>/<version>/`; it recursively walks that whole nested tree
  and emits exactly **one** `graph.json`. One folder → one graph, always
  (`cli.py:2112`, `detect.py:1132`, `build.py:762`, `cli.py:2429`).
- **Versions and `default` are peers.** Each version dir (`default`, `v3.24.2`,
  `testnet-v1.65.2`, …) is a **separate full snapshot** → its own independent
  graph. `default` is just a folder name meaning "current/unversioned". **Never
  merge** version snapshots. Map identity = `(owner, library, version)`.
- **Do not flatten.** Node IDs are the full repo-relative path; nesting keeps
  same-named files distinct and clustering is path-blind. Verbatim paths are
  strictly better (`base.py:39-62`, `cluster.py:22-77`; prior
  `research/graphify-input-structure/FLATTENING.md`, GraphScore 98.2 nested).
- **Ignore is a non-issue at this unit — but not via the root file.** The
  library's `.ctx7.json`/`LICENSE`/`NOTICE` sit **one level above** the version
  dir, so a version-dir run never sees them. And the root
  `context7-docs/.graphifyignore` is **not read** for a deep run anyway
  (`_load_graphifyignore` ceiling = nearest VCS root or the scan root itself —
  `detect.py`, `ceiling = _find_vcs_root(root) or root`). Belt-and-suspenders:
  `--exclude` per run for any stray in-scope non-markdown.
- **Redirect output off the SSD source tree** with `--out`, mirroring the tree,
  so you don't scribble `graphify-out/` into 50k source dirs and you get a
  per-unit semantic cache for free resumability (`cli.py:2071-2072, 2112, 2260`).
- **Run it as a `find | xargs -P` loop**, skip units whose `graph.json` already
  exists (resumable), and drive the semantic pass with a keyed batch backend
  (the `gfy`/graphify-site free-Mistral path), **not** the interactive
  `/graphify` host-session path — 50k units is unattended, not attended.

---

## 1. The unit of graphify: one graph per version dir

graphify's ingestion unit is **one root folder → one graph**. There is no
sub-graph mode and no multi-root mode within a single invocation:

- `graphify extract <path>` reads exactly **one** positional path
  (`cli.py:1919-1923`); a second positional folder is silently dropped by the
  arg loop's `else: i += 1` fallthrough (`cli.py:2042-2043`). You cannot pass two
  roots.
- That single target goes to `detect()` (`cli.py:2112`), which runs **one**
  recursive `os.walk` from the root and appends every surviving file at every
  depth into one flat list (`detect.py:1130-1176`). Depth is irrelevant — a
  12-level `.md` lands in the same list as a top-level `README`.
- Code and semantic node/edge lists are concatenated into one `merged` dict
  (`cli.py:2421-2427`), `build_from_json` builds **one** `nx` graph
  (`build.py:383, 490`, returns single `G` at `762`), written to one
  `graphify-out/graph.json` (`cli.py:2429`).
- The other folder commands (`watch`, `update`) are also single-path
  (`watch.py:821`). Combining graphs is only possible **post-hoc** via
  `merge-graphs` / `global add`, which take already-built `graph.json` files, not
  source folders (`cli.py:1423, 1845, 2516`).

**Therefore:** pointing graphify at one `<owner>/<library>/<version>/` dir
produces exactly one `graph.json` covering that version's entire nested doc
tree — precisely the "per-version-KG bundle" the delivery plan wants. **Exact
invocation:**

```
graphify extract /Volumes/ExtSSD/context7-docs/<owner>/<library>/<version> \
  --out /Volumes/ExtSSD/context7-kg/<owner>/<library>/<version>
```

Do **not** point graphify at an owner dir or the context7-docs root expecting
sub-graphs — you would get one giant merged graph plus a non-fatal "Consider
running on a subfolder" print (`detect.py:1255-1260`), and pay O(n²)
`cohesion_score` per community (`cluster.py:257-265`) over the whole corpus.

---

## 2. Versions and `default`: independent graphs, never merged

Each version dir is a separate full doc snapshot. A single library commonly
holds several (`colinhacks/zod`: `default`, `v3.24.2`, `v3.25.29`, `v4.0.1`) —
that is 4 distinct units → 4 independent graphs. Because node IDs are full-path
stems (§3), sibling version dirs are already distinct strings and get distinct
IDs with no collision handling needed. `default` carries no special meaning to
graphify; it is a folder name that your catalog treats as the
current/unversioned snapshot.

**Map identity is `(owner, library, version)`** — the natural key for the
catalog and the mirrored output tree. This ties directly into the CLI
split-delivery design:

- The `.ctx7.json` in each **library** dir carries `commit_sha` — the **exact
  immutable pin** the delivery lockfile is built around
  (`{owner, repo, commit_sha, path, git_blob_hash}`). That commit hash is both
  the build provenance for the map and the upstream fetch address the buyer's
  CLI uses. See `handoffs/2026-07-13_09-34AM-docs-kg-cli-split-delivery-handoff.md`
  (Part 1 steps 3-4) and memory `docs-kg-cli-split-delivery`.
- One `graph.json` per `(owner, library, version)` is the sellable unit; store
  it gzipped in the private maps repo keyed by that same triple. The version
  string in the path is the version in the catalog — no extra bookkeeping.

Consequence for provenance: a `default` snapshot and a `v3.24.2` snapshot of the
same library are pinned to (potentially) different commits in their respective
`.ctx7.json`; keep them as separate rows/maps. Never fold them together.

---

## 3. Deep nesting (12-18 levels): keep verbatim, do not flatten

Directory depth and numbered/dotted/dashed version names are safe. Confirmed by
running graphify's real ID functions:

- **File node ID = full repo-relative path, extension dropped, normalized.**
  `_file_stem` keeps **every** segment (`base.py:39-62`,
  `path.with_suffix("").as_posix()`), then `normalize_id` NFKC-normalizes,
  collapses every non-word run to `_`, and casefolds (`ids.py:32-50`). So
  `colinhacks/zod/v3.24.2/README.md → colinhacks_zod_v3_24_2_readme`; a 12-level
  path just yields a longer underscore string. Digits survive (`\w`), so
  `v3.24.2 → v3_24_2`, `testnet-v1.65.2 → testnet_v1_65_2` — no per-segment
  parsing a number or dot can break.
- **Separator-collision is auto-resolved.** Because `/ . - _` all normalize to a
  single `_`, two on-disk paths differing only in separators can map to one ID;
  `_disambiguate_colliding_node_ids` appends a 6-char SHA1 of the raw path to
  split them, run unconditionally over all nodes (`resolution.py:578-640`,
  `extract.py:4517`). Distinct sibling version dirs never trigger it.
- **Clustering never reads paths.** Leiden/Louvain run purely on edges; node IDs
  are opaque sort keys (`cluster.py:22-77, 134-236`). Depth and numbered top dirs
  carry **zero** clustering signal. The only path-structure logic
  (`paths.py:55-210`, test-path + call-proximity) affects cross-file **code**
  call resolution only — inert on a pure-markdown tree (no calls).

This matches the prior finding: `research/graphify-input-structure/FLATTENING.md`
(GraphScore 98.2 on a fully-nested tree; flattening only *creates* the ID
collisions nesting avoids and breaks `source_location` citations).

**Real risk at depth 12-18:** essentially none for correctness. The only edge is
that node IDs have **no length cap** (`ids.py` never truncates) — an ~18-segment
path yields a very long ID string. That is a memory/readability cost in the JSON,
not a correctness bug. No action needed; do not truncate (truncation would
reintroduce collisions).

---

## 4. `.graphifyignore`: exactly how it resolves, and what to do

**How graphify resolves it (the highest-uncertainty item — get this right):**
`_load_graphifyignore(root)` (`detect.py`, the `_load_graphifyignore` function)
sets `ceiling = _find_vcs_root(root) or root`, then collects `.gitignore` +
`.graphifyignore` from **every dir from `ceiling` down to `root`** (outer→inner,
last-match-wins). It walks **up only to the nearest VCS root**; with no
`.git`/`.hg` at or above the scan root, **ceiling == the scan root**, so only
ignore files **inside the scan root** are read.

**The consequence for this tree:** `/Volumes/ExtSSD/context7-docs` is a plain
data tree on an external SSD, not a git repo. When you scan a deep version dir,
ceiling collapses to that version dir — so the **root
`context7-docs/.graphifyignore` is never read** for a per-version run. Do **not**
rely on it.

**But you don't need it, because the version-dir unit sidesteps the problem:**

- `.ctx7.json`, `LICENSE`, `NOTICE` live in the **library** dir — one level
  **above** the version dir — so a version-dir run never has them in scope. (The
  `progress.db*` / `status.txt` / `progress.log` files the root ignore targets
  live at the context7-docs **root**, also out of scope.)
- Even if a stray `LICENSE`/`NOTICE`/`COPYING` did appear inside a version dir,
  it is extensionless → `classify_file` returns `None` → skipped as unclassified
  regardless of any ignore rule.
- Version dirs contain **only markdown** (per the verified layout), and `.md` /
  `.mdx` are the doc extensions that feed the semantic pass (`detect.py:30-31`).

**Concrete action:** do **not** copy a `.graphifyignore` into 50k dirs, and do
**not** count on the root one. Nothing noisy is in scope at the version-dir unit.
As a cheap belt-and-suspenders against any stray in-scope non-markdown (e.g. a
per-version `.ctx7.json` if the layout ever varies, since `.json ∈
CODE_EXTENSIONS` and would be AST-parsed as minor noise), pass it per run:

```
--exclude '.ctx7.json'
```

`--exclude <pattern>` appends to `extra_excludes` and is honored by `detect`
(`cli.py:2029-2032`, wired at `cli.py:2100`/`2112`). This is the correct
mechanism at scale — a per-run flag, not 50k copied files. If a spot-audit finds
other stray in-scope files, add more `--exclude` patterns; never restructure the
tree.

---

## 5. Running it at scale (50,855 units)

The build is embarrassingly parallel — no cross-dir coordination — so the whole
job is a `find | xargs -P` loop keyed by version dir.

**Enumerate version dirs** (owner=1, library=2, version=3 → depth 3):

```bash
SRC=/Volumes/ExtSSD/context7-docs
OUT=/Volumes/ExtSSD/context7-kg

find "$SRC" -mindepth 3 -maxdepth 3 -type d -print0 |
  xargs -0 -P 8 -I{} bash -c '
    src="$1"; SRC="'"$SRC"'"; OUT="'"$OUT"'"
    rel="${src#$SRC/}"; out="$OUT/$rel"
    [ -f "$out/graphify-out/graph.json" ] && exit 0     # resumable: skip done units
    mkdir -p "$out"
    graphify extract "$src" --out "$out" --exclude ".ctx7.json"
  ' _ {}
```

Why this shape:

- **`--out` mirrors the tree off the SSD source.** `out_root = --out or target`
  and `graphify-out/graph.json` is written under it (`cli.py:2071-2072`,
  `cli.py:2429`); output never touches the read-only source tree.
- **Resumable for free, two ways.** (a) The `[ -f .../graph.json ] && exit 0`
  guard skips finished units, so re-running the loop after a crash resumes where
  it stopped. (b) `cache_root = out_root` (`cli.py:2112, 2260, 2286`), so a
  partially-completed unit keeps its semantic cache under its own out dir and a
  re-run reuses it instead of re-calling the LLM. Give **each unit its own
  `--out`** (mirrored path) — a single shared out dir would make all 50k runs
  collide on one `graph.json`/cache.
- **Parallelism.** `-P 8` is a starting point; the ceiling is **not** CPU, it is
  the LLM backend's rate limit (below). Graph construction/clustering is cheap
  per unit because each unit is small (per-version, not whole-tree).

**The bottleneck is the semantic pass, not graphify.** Every `.md`/`.mdx` feeds
the LLM semantic extractor — 2.86M files across the corpus. Large single units
(e.g. `mystenlabs/sui`, nested to ~18 path components) trip the "expensive"
warning (≥500 files or ≥500k words, `detect.py` `CORPUS_UPPER`/`FILE_COUNT_UPPER`)
and cost many tokens; most `default` units are tiny. Throughput is therefore
gated by LLM tokens/min, so:

- **Drive the semantic pass with a keyed batch backend** — the `gfy`/
  graphify-site free-Mistral path (see `graphify-site` skill and
  `research/graphify-kg-structure/ARCHITECTURE.md`), **not** the interactive
  `/graphify` host-session path. 50k units is an **unattended** batch; the
  host-session path is attended and cannot scale to 50k. The one-folder-one-graph
  unit and every ID/cluster property in §1-3 are **identical** regardless of which
  LLM drives the semantic pass — the backend choice is purely a throughput/cost
  decision.
- Tune `-P` down if the backend rate-limits (429s); the resumable guard means an
  aborted run costs nothing to restart.

**Single-README units: graphify them anyway, do not add a skip threshold.** Many
`default` dirs are one `README.md`. graphify will emit a valid (small) graph and
a "corpus fits in one context window, you may not need a graph" note
(`detect.py:1145-1149`) — a hint, not an error. Skipping them would leave holes
in the catalog keyed by `(owner, library, version)`; a one-node map is still the
sellable unit for that pin and costs almost nothing to build. Uniformity beats a
threshold. (If cost ever forces it, the only defensible skip is "zero markdown
files in the dir", not "small".)

---

## 6. Open decisions / risks

1. **LLM backend + budget.** The one genuinely unresolved lever: which keyed
   backend drives 50k semantic passes and at what tokens/min. This sets wall-clock
   and cost, not correctness. Decide the `gfy` backend and `-P` before launch;
   the resumable loop de-risks a wrong first guess.
2. **`.ctx7.json` placement assumption.** This strategy relies on the verified
   layout (`.ctx7.json`/`LICENSE`/`NOTICE` in the **library** dir, above the
   version dir). If any library instead drops `.ctx7.json` **inside** a version
   dir, it would be AST-parsed as minor code noise — the `--exclude '.ctx7.json'`
   in the loop already covers this, so it is guarded, not open. Confirm with one
   `find "$SRC" -mindepth 4 -name '.ctx7.json'` spot check before the full run.
3. **Node-ID length is unbounded** at depth 18. Cosmetic only (JSON size); flagged
   so no one "fixes" it by truncating and reintroduces collisions.
4. **ID prefix is set by the invocation root — keep it fixed.** Running per-version
   yields IDs prefixed with the version stem; if you ever re-run at a different
   root (per-library, whole-tree) every ID changes (`build.py:257-304, 126-150`).
   Standardize on the version-dir root across the whole batch so IDs stay stable
   across rebuilds.
5. **Whole-tree runtime trap (rejected path).** Naming it so it is not
   re-litigated: graphifying the whole tree or per-owner in one run merges into
   one giant graph and pays O(n²) `cohesion_score` per community
   (`cluster.py:257-265`) plus heavy Leiden — never do it. Per-version is both the
   sellable unit and the cheap unit.
6. **Verification gap (from the readers).** ID mechanics were confirmed on the
   pure functions, not via a full markdown extraction end-to-end; the collision
   salt exempts `type=module/namespace` nodes (`resolution.py`), which markdown is
   not expected to produce. Run a full extraction on **one** representative unit
   (e.g. `colinhacks/zod/default`) and eyeball the graph before firing all 50k.
