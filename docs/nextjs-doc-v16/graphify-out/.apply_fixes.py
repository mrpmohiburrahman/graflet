import json, re
from pathlib import Path
from collections import Counter, defaultdict

g = json.loads(Path('graphify-out/graph.json').read_text())
nodes = g['nodes']
links = g.get('links', g.get('edges', []))

# --------- FIX 1: canonical-merge duplicate CONCEPT nodes by normalized label ---------
def norm(l): return ' '.join(str(l).lower().split())
byid = {n['id']: n for n in nodes}
concept_groups = defaultdict(list)
for n in nodes:
    if n.get('file_type') == 'concept':
        concept_groups[norm(n['label'])].append(n['id'])

remap = {}          # old_id -> canonical_id
drop = set()
for lab, ids in concept_groups.items():
    if len(ids) > 1:
        canon = min(ids, key=len)     # shortest id = canonical
        for i in ids:
            if i != canon:
                remap[i] = canon
                drop.add(i)

# drop redundant nodes
nodes2 = [n for n in nodes if n['id'] not in drop]
# redirect edges
for e in links:
    e['source'] = remap.get(e['source'], e['source'])
    e['target'] = remap.get(e['target'], e['target'])
# dedup edges + remove self-loops introduced by merge
seen_e = set(); links2 = []
for e in links:
    if e['source'] == e['target']:
        continue
    key = (e['source'], e['target'], e.get('relation'))
    if key in seen_e:
        continue
    seen_e.add(key); links2.append(e)

merged_concepts = len(drop)

# --------- FIX 2: inject balanced synthetic section hubs ---------
existing_ids = {n['id'] for n in nodes2}
docs = [n for n in nodes2 if n.get('file_type') == 'document']

def bucket(sf):
    p = sf.split('/docs/v16/')[-1].split('/')
    if len(p) >= 2 and p[1] in ('03-api-reference', '04-api-reference'):
        b = '/'.join(p[:3]) if len(p) >= 3 and not p[2].endswith('.mdx') else '/'.join(p[:2])
    else:
        b = '/'.join(p[:2]) if len(p) >= 2 and not p[1].endswith('.mdx') else p[0]
    return b

# assign, fold small buckets (<3) into their level-1 segment
raw = defaultdict(list)
for n in docs:
    raw[bucket(n['source_file'])].append(n['id'])
counts = {k: len(v) for k, v in raw.items()}
final_buckets = defaultdict(list)
for b, ids in raw.items():
    if counts[b] < 3:
        lvl1 = b.split('/')[0].replace('.mdx', '')
        final_buckets[f'section:{lvl1}'].extend(ids)
    else:
        final_buckets[f'section:{b}'].extend(ids)

def slug(s): return re.sub(r'[^a-z0-9]', '_', s).lower().strip('_')

hub_nodes = []; hub_edges = []
for b, member_ids in final_buckets.items():
    hid = 'hub_' + slug(b)
    if hid in existing_ids:
        hid = hid + '_h'
    hub_nodes.append({
        'id': hid, 'label': 'Section: ' + b.split(':',1)[1],
        'file_type': 'document',
        'source_file': f'__hub__/{hid}.mdx',
        'source_location': None, 'source_url': None,
        'captured_at': None, 'author': None, 'contributor': None,
    })
    for m in member_ids:
        hub_edges.append({'source': hid, 'target': m, 'relation': 'references',
                          'confidence': 'INFERRED', 'confidence_score': 0.75,
                          'source_file': f'__hub__/{hid}.mdx',
                          'source_location': None, 'weight': 1.0})

nodes3 = nodes2 + hub_nodes
links3 = links2 + hub_edges

g['nodes'] = nodes3
if 'links' in g: g['links'] = links3
else: g['edges'] = links3

Path('graphify-out/.graphify_extract_fixed.json').write_text(json.dumps(
    {'nodes': nodes3, 'edges': links3, 'hyperedges': [], 'input_tokens': 0, 'output_tokens': 0},
    ensure_ascii=False))

print(f"merged concept dups: {merged_concepts}")
print(f"hubs created: {len(hub_nodes)}  hub edges: {len(hub_edges)}")
print(f"nodes {len(nodes)} -> {len(nodes3)}   edges {len(links)} -> {len(links3)}")
# hub edge share
top = max(len(v) for v in final_buckets.values())
print(f"top hub fan-out {top}  edge-share {100*top/len(links3):.1f}%")
