import json

filename = 'templates/product.tiles.json'
try:
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    data = json.loads(json_str)

    # The section id containing "Shop Related Collections"
    sections_to_remove = ['blocks_JPq7Pd']
    modified = False
    
    for sid in sections_to_remove:
        if sid in data.get('sections', {}):
            del data['sections'][sid]
            modified = True
        if 'order' in data and sid in data['order']:
            data['order'].remove(sid)
            modified = True

    if modified:
        with open(filename, 'w') as f:
            f.write(comment_block)
            json.dump(data, f, indent=2)
        print("Successfully removed Shop Related Collections section.")
    else:
        print("Section not found.")
except Exception as e:
    print(f"Error: {e}")
