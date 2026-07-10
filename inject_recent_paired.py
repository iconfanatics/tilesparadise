import json

filename = 'templates/product.tiles.json'
with open(filename, 'r') as f:
    content = f.read()

start_idx = content.find('{')
comment_block = content[:start_idx]
json_str = content[start_idx:]
data = json.loads(json_str)

# 1. Remove old recently viewed carousel from sections and order
old_id = None
for sid, sdata in list(data.get('sections', {}).items()):
    if sdata.get('type') == 'recently-viewed-carousel':
        old_id = sid
        del data['sections'][sid]
if old_id and 'order' in data and old_id in data['order']:
    data['order'].remove(old_id)

# 2. Add the new recently-viewed-paired section
if 'recently_viewed_paired_new' not in data['sections']:
    data['sections']['recently_viewed_paired_new'] = {
      "type": "recently-viewed-paired",
      "settings": {
        "title": "Recently Viewed Products",
        "section_bg": "#f8f7f5"
      }
    }
    
    # Place it right after 'related_categories_new'
    order = data.get('order', [])
    if 'related_categories_new' in order:
        idx = order.index('related_categories_new')
        order.insert(idx + 1, 'recently_viewed_paired_new')
    else:
        order.append('recently_viewed_paired_new')
        
    with open(filename, 'w') as f:
        f.write(comment_block)
        json.dump(data, f, indent=2)
    print("Injected successfully.")
else:
    print("Already injected.")
