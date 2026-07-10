import json

filename = 'templates/product.tiles.json'
with open(filename, 'r') as f:
    content = f.read()

start_idx = content.find('{')
comment_block = content[:start_idx]
json_str = content[start_idx:]
data = json.loads(json_str)

paired_id = None
for sec_id, sec_data in data.get('sections', {}).items():
    if sec_data.get('name') == 'Paired With Carousel':
        paired_id = sec_id
        break

if paired_id and 'related_categories_new' not in data['sections']:
    data['sections']['related_categories_new'] = {
      "type": "related-categories",
      "blocks": {
        "cat1": { "type": "category_link", "settings": { "title": "Bathroom Wall Tiles" } },
        "cat2": { "type": "category_link", "settings": { "title": "Kitchen Wall Tiles" } },
        "cat3": { "type": "category_link", "settings": { "title": "Kitchen Splash Back Tiles" } },
        "cat4": { "type": "category_link", "settings": { "title": "Country Tiles" } },
        "cat5": { "type": "category_link", "settings": { "title": "Rustic Tiles" } },
        "cat6": { "type": "category_link", "settings": { "title": "Ceramic Tiles" } },
        "cat7": { "type": "category_link", "settings": { "title": "White Wall Tiles" } },
        "cat8": { "type": "category_link", "settings": { "title": "White Bathroom Tiles" } },
        "cat9": { "type": "category_link", "settings": { "title": "White Kitchen Tiles" } },
        "cat10": { "type": "category_link", "settings": { "title": "Zellige Effect Tiles" } },
        "cat11": { "type": "category_link", "settings": { "title": "Gloss Tiles" } },
        "cat12": { "type": "category_link", "settings": { "title": "Metro Tiles" } }
      },
      "block_order": [
        "cat1", "cat2", "cat3", "cat4", "cat5", "cat6",
        "cat7", "cat8", "cat9", "cat10", "cat11", "cat12"
      ],
      "settings": {
        "title": "Related Popular Categories",
        "bg_color": "#f8f7f5"
      }
    }
    
    order = data.get('order', [])
    if paired_id in order:
        idx = order.index(paired_id)
        order.insert(idx + 1, 'related_categories_new')
    
    with open(filename, 'w') as f:
        f.write(comment_block)
        json.dump(data, f, indent=2)
    print("Injected successfully.")
else:
    print("Paired With Carousel not found or already injected.")
