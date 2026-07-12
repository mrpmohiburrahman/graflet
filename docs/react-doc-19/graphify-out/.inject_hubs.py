#!/usr/bin/env python3
"""Inject balanced synthetic section-hub nodes into graph.json (post-build).

Each hub is a fake-`document` node with source_file `__hub__/<id>.md` that
`references` its member document nodes (bucketed by filename prefix). This
collapses the 77 islands into a few connected components.

The hubs are injected AFTER build_from_json because graphify's build prunes
nodes whose source_file isn't in the detected set. Re-run cluster-only after.
"""
import json
from pathlib import Path

OUT = Path("graphify-out")
g = json.loads((OUT / "graph.json").read_text())
nodes, links = g["nodes"], g["links"]
ids = {n["id"] for n in nodes}

HUB_DEFS = [
    ("__hub__/ref_react.md",        "Hub: React API Reference (core)",      "ref_react"),
    ("__hub__/ref_react_dom.md",    "Hub: react-dom API Reference",         "ref_react_dom"),
    ("__hub__/ref_rsc.md",          "Hub: React Server Components",         "ref_rsc"),
    ("__hub__/ref_eslint_devtools.md","Hub: ESLint & DevTools Reference",    "ref_eslint_devtools"),
    ("__hub__/learn.md",            "Hub: Learn (Guides & Tutorials)",      "learn"),
    ("__hub__/blog.md",             "Hub: React Blog",                      "blog"),
    ("__hub__/community.md",        "Hub: Community",                       "community"),
    ("__hub__/meta.md",             "Hub: Errors, Warnings & Versions",     "meta"),
]

def bucket(nid):
    if nid.startswith("reference_react_dom_") or nid == "reference_react_dom": return "ref_react_dom"
    if nid.startswith("reference_rsc_") or nid == "reference_rsc": return "ref_rsc"
    if nid.startswith("reference_eslint") or nid.startswith("reference_dev_tools"): return "ref_eslint_devtools"
    if nid.startswith("reference_"): return "ref_react"
    if nid.startswith("learn_"): return "learn"
    if nid.startswith("blog_"): return "blog"
    if nid.startswith("community_"): return "community"
    return "meta"

bucket_of = {b: hid for hid, _, b in HUB_DEFS}
buckets = {bb: [] for _, _, bb in HUB_DEFS}
for n in nodes:
    if n.get("file_type") == "document":
        b = bucket(n["id"])
        if b in buckets:
            buckets[b].append(n["id"])

new_nodes, new_links = [], []
for hid, label, b in HUB_DEFS:
    members = buckets[b]
    if not members:
        continue
    hid_clean = hid.replace("/", "_").replace(".md", "")
    new_nodes.append({
        "id": hid_clean,
        "label": label,
        "file_type": "document",
        "source_file": hid,
        "source_location": None, "source_url": None,
        "captured_at": None, "author": None, "contributor": None,
    })
    for m in members:
        new_links.append({
            "source": hid_clean,
            "target": m,
            "relation": "references",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": hid,
            "source_location": None,
            "weight": 1.0,
        })

hub_ids = {n["id"] for n in new_nodes}
before_n, before_e = len(nodes), len(links)
nodes.extend(new_nodes)
links.extend(new_links)
g["nodes"], g["links"] = nodes, links
Path(OUT / "graph.json").write_text(json.dumps(g, indent=2, ensure_ascii=False), encoding="utf-8")

import collections
adj = collections.defaultdict(set)
for e in links:
    if e["source"] in ids | hub_ids and e["target"] in ids | hub_ids:
        adj[e["source"]].add(e["target"]); adj[e["target"]].add(e["source"])
seen=set(); comps=[]
for n in ids | hub_ids:
    if n in seen: continue
    st=[n]; comp=set()
    while st:
        x=st.pop()
        if x in seen: continue
        seen.add(x); comp.add(x); st.extend(adj[x]-seen)
    comps.append(comp)
sizes = sorted((len(c) for c in comps), reverse=True)
ncomp = len(comps)
largest = sizes[0]/len(ids|hub_ids)
dang = sum(1 for e in links if e["source"] not in ids|hub_ids or e["target"] not in ids|hub_ids)
top_hub_share = max(len(buckets[b]) for _,_,b in HUB_DEFS)/len(links)*100
print(f"Injected {len(new_nodes)} hubs, {len(new_links)} edges")
print(f"nodes {before_n}->{len(nodes)}  edges {before_e}->{len(links)}")
print(f"components {ncomp}  largest {largest*100:.1f}%  dangling {dang}")
print(f"top hub edge-share {top_hub_share:.2f}% (hub_sane cap 10%)")
