import json, re
from pathlib import Path
from collections import defaultdict

g = json.loads(Path('graphify-out/graph.json').read_text())
nodes = g['nodes']
key = 'links' if 'links' in g else 'edges'
links = g[key]

existing_ids = {n['id'] for n in nodes}
docs = [n for n in nodes if n.get('file_type') == 'document']

def bucket(sf):
    p = sf.split('/docs/v16/')[-1].split('/')
    if len(p) >= 2 and p[1] in ('03-api-reference', '04-api-reference'):
        b = '/'.join(p[:3]) if len(p) >= 3 and not p[2].endswith('.mdx') else '/'.join(p[:2])
    else:
        b = '/'.join(p[:2]) if len(p) >= 2 and not p[1].endswith('.mdx') else p[0]
    return b

raw = defaultdict(list)
for n in docs:
    raw[bucket(n['source_file'])].append(n['id'])
counts = {k: len(v) for k, v in raw.items()}
final = defaultdict(list)
for b, ids in raw.items():
    if counts[b] < 3:
        final[f'section:{b.split("/")[0].replace(".mdx","")}'].extend(ids)
    else:
        final[f'section:{b}'].extend(ids)

def slug(s): return re.sub(r'[^a-z0-9]', '_', s).lower().strip('_')

hub_nodes = []; hub_edges = []
for b, members in final.items():
    hid = 'hub_' + slug(b)
    while hid in existing_ids: hid += '_h'
    existing_ids.add(hid)
    hub_nodes.append({'id': hid, 'label': 'Section: ' + b.split(':',1)[1],
        'file_type': 'document', 'source_file': f'__hub__/{hid}.mdx',
        'source_location': None, 'source_url': None, 'captured_at': None,
        'author': None, 'contributor': None})
    for m in members:
        hub_edges.append({'source': hid, 'target': m, 'relation': 'references',
            'confidence': 'INFERRED', 'confidence_score': 0.75,
            'source_file': f'__hub__/{hid}.mdx', 'source_location': None, 'weight': 1.0})

g['nodes'] = nodes + hub_nodes
g[key] = links + hub_edges
Path('graphify-out/graph.json').write_text(json.dumps(g, ensure_ascii=False))
print(f"injected {len(hub_nodes)} hubs, {len(hub_edges)} edges")
print(f"total nodes {len(g['nodes'])} edges {len(g[key])}")
top = max(len(v) for v in final.values())
print(f"top hub fan-out {top} = {100*top/len(g[key]):.1f}% edge share")
