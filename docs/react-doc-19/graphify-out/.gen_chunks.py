#!/usr/bin/env python3
"""Deterministic heading-based graphify chunk generator for the React 19 docs dump.

- one `document` node per .md file
- one `concept` node per heading (slugified)
- EXTRACTED 1.0 edges: file -> section
- INFERRED 0.75 edges: intra-file section sequence
- EXTRACTED 1.0 edges: cross-file .md links (resolved by real path compare)
- ids always match ^[a-z0-9_]+$
"""
import json
import re
from pathlib import Path

CORPUS_DIR = Path("/Users/mrp/Documents/1-Projects/webscraping/react-doc-scraper/docs/react-19")
OUT = CORPUS_DIR / "graphify-out"
CHUNK_SIZE = 22
# ancestor of CORPUS_DIR whose path becomes the stem prefix: react-19/learn-foo.md -> "learn_foo"
STEM_RELATIVE_TO = CORPUS_DIR

ID_RE = re.compile(r"^[a-z0-9_]+$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
BARE_MD_RE = re.compile(r"(?<![\(\[\]])(\b[a-z0-9_\-/]+\.md)(#[a-z0-9_\-]*)?", re.IGNORECASE)


def slugify(text: str) -> str:
    text = text.lower().strip().replace("`", "")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")[:60]


def file_stem(abspath: str) -> str:
    p = Path(abspath)
    rel = p.relative_to(STEM_RELATIVE_TO)
    return "_".join(slugify(s) for s in rel.with_suffix("").parts)


def clean_heading(raw: str) -> str:
    return re.sub(r"[`*_]", "", raw).strip()


def main():
    md_files = sorted([p for p in CORPUS_DIR.glob("*.md") if p.is_file()])
    print(f"Found {len(md_files)} markdown files")

    stems = {file_stem(str(p)): p for p in md_files}
    total = (len(md_files) + CHUNK_SIZE - 1) // CHUNK_SIZE
    chunks = [md_files[i * CHUNK_SIZE:(i + 1) * CHUNK_SIZE] for i in range(total)]
    chunks = [c for c in chunks if c]

    for ci, files in enumerate(chunks):
        nodes, edges = {}, []
        seen_links = set()

        def add_node(nid, label, ftype, src):
            if nid in nodes or not ID_RE.match(nid):
                return
            nodes[nid] = {
                "id": nid, "label": label[:160], "file_type": ftype,
                "source_file": src, "source_location": None,
                "source_url": None, "captured_at": None,
                "author": None, "contributor": None,
            }

        def add_edge(s, t, rel, conf, score, src):
            if s in nodes and t in nodes:
                edges.append({"source": s, "target": t, "relation": rel,
                              "confidence": conf, "confidence_score": score,
                              "source_file": src, "source_location": None, "weight": 1.0})

        for p in files:
            abs_p, stem = str(p), file_stem(str(p))
            text = p.read_text(encoding="utf-8", errors="replace")
            if text.startswith("---"):
                end = text.find("\n---", 3)
                if end != -1:
                    text = text[end + 4:]

            add_node(stem, p.stem.replace("-", " ").title(), "document", abs_p)
            headings, prev = [], stem
            for m in HEADING_RE.finditer(text):
                level, raw = len(m.group(1)), clean_heading(m.group(2))
                ent = slugify(raw)
                if not ent or raw.lower() == "table of contents":
                    continue
                nid = f"{stem}_{ent}"
                if nid == stem:
                    nid = f"{stem}_{ent}_h{level}"
                add_node(nid, raw, "concept", abs_p)
                headings.append(nid)
                add_edge(stem, nid, "references", "EXTRACTED", 1.0, abs_p)

            seq = [stem] + headings
            for a, b in zip(seq, seq[1:]):
                add_edge(a, b, "conceptually_related_to", "INFERRED", 0.75, abs_p)

            # markdown-link resolver: strip ONE trailing .md if present (defensive)
            def resolve_target(target):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    return None
                base = target.split("#", 1)[0]
                if not base.endswith(".md"):
                    return None
                # strip a single redundant trailing ".md" (Expo/Vite-style double ext)
                if base.lower().endswith(".md.md"):
                    base = base[:-3]
                cand = (p.parent / base).resolve()
                return next((s for s, pp in stems.items() if pp.resolve() == cand), None)

            for lm in LINK_RE.finditer(text):
                cstem = resolve_target(lm.group(1).strip())
                if cstem and cstem != stem:
                    if (stem, cstem) not in seen_links:
                        seen_links.add((stem, cstem))
                        add_edge(stem, cstem, "references", "EXTRACTED", 1.0, abs_p)
                    if "#" in lm.group(1):
                        tgt = f"{cstem}_{slugify(lm.group(1).split('#', 1)[1])}"
                        if tgt in nodes:
                            add_edge(stem, tgt, "references", "EXTRACTED", 1.0, abs_p)

            for bm in BARE_MD_RE.finditer(text):
                cstem = resolve_target(bm.group(1))
                if cstem and cstem != stem and ("bare", stem, cstem) not in seen_links:
                    seen_links.add(("bare", stem, cstem))
                    add_edge(stem, cstem, "references", "EXTRACTED", 1.0, abs_p)

        chunk = {"nodes": list(nodes.values()), "edges": edges,
                 "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
        out_path = OUT / f".graphify_chunk_{ci:02d}.json"
        out_path.write_text(json.dumps(chunk, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"chunk {ci:02d}: {len(chunk['nodes'])} nodes, {len(edges)} edges -> {out_path.name}")

    print("DONE")


if __name__ == "__main__":
    main()
