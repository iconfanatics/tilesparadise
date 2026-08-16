import json
import re

file_path = '/home/sany/sajedul/templates/index.json'

with open(file_path, 'r') as f:
    content = f.read()

# Remove C-style comments to parse valid JSON
content_no_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
data = json.loads(content_no_comments)

# 1. Update the AI block to stop using JS recommendations
ai_block = data['sections']['blocks_4HkYkr']['blocks']['ai_gen_block_477adb9_YEeeb6']
ai_block['settings']['use_recommendations'] = False
ai_block['settings']['products_limit'] = 6  # Reduce limit for better performance

# 2. Remove the temporary featured_collection_new
if 'featured_collection_new' in data['sections']:
    del data['sections']['featured_collection_new']

if 'featured_collection_new' in data['order']:
    data['order'].remove('featured_collection_new')

# Save changes
comment = "/*\n * ------------------------------------------------------------\n * IMPORTANT: The contents of this file are auto-generated.\n * ------------------------------------------------------------\n */\n"
with open(file_path, 'w') as f:
    f.write(comment + json.dumps(data, indent=2))

print("index.json successfully reverted and optimized")
