import json
import re

file_path = '/home/sany/sajedul/templates/index.json'

with open(file_path, 'r') as f:
    content = f.read()

# Remove C-style comments to parse valid JSON
content_no_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
data = json.loads(content_no_comments)

new_section = {
  'type': 'featured-collection',
  'settings': {
    'collection': '60x120cm-rectangular-large-tiles',
    'title': 'Luxury Porcelain Tiles (Lightweight Version)',
    'layout': 'vertical',
    'products_count': 6,
    'stack_products': False,
    'show_quick_buy': True,
    'show_view_button': False,
    'show_shop_button': True,
    'enable_sample_button': True,
    'custom_css_class': 'lightweight-carousel'
  }
}

data['sections']['featured_collection_new'] = new_section

order = data['order']
if 'blocks_4HkYkr' in order:
    idx = order.index('blocks_4HkYkr')
    order.insert(idx + 1, 'featured_collection_new')
else:
    order.append('featured_collection_new')

comment = "/*\n * ------------------------------------------------------------\n * IMPORTANT: The contents of this file are auto-generated.\n * ------------------------------------------------------------\n */\n"
with open(file_path, 'w') as f:
    f.write(comment + json.dumps(data, indent=2))

print("index.json updated successfully")
