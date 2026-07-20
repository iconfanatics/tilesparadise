import json
import re

def load_json(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return json.loads(text)

prod = load_json('templates/product.json')
section_key = "blocks_JPq7Pd"
section_data = prod['sections'][section_key]

tiles = load_json('templates/product.tiles.json')
tiles['sections'][section_key] = section_data

order = tiles['order']
if 'custom_liquid_t77pJf' in order:
    idx = order.index('custom_liquid_t77pJf')
    order.insert(idx + 1, section_key)
else:
    order.append(section_key)

tiles['order'] = order

with open('templates/product.tiles.json', 'w') as f:
    json.dump(tiles, f, indent=2)

