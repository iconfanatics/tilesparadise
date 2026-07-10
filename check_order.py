import json

with open('templates/product.tiles.json', 'r') as f:
    content = f.read()

start_idx = content.find('{')
json_str = content[start_idx:]
data = json.loads(json_str)

print("Section Order:")
for idx, sid in enumerate(data.get('order', [])):
    sec = data.get('sections', {}).get(sid, {})
    name = sec.get('name') or sec.get('type')
    title = sec.get('settings', {}).get('title', '')
    print(f"{idx}: {sid} -> Type/Name: {name} | Title: {title}")
