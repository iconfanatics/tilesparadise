import json

def process_json_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return

    updated = False
    
    if 'main' in data.get('sections', {}):
        blocks = data['sections']['main'].get('blocks', {})
        if 'custom_liquid_tabs' in blocks:
            if blocks['custom_liquid_tabs']['type'] == 'custom-liquid':
                blocks['custom_liquid_tabs']['type'] = 'liquid'
                updated = True
            
    if updated:
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"No matching blocks found in {filename}")

process_json_file('templates/product.tiles.json')
process_json_file('templates/product.toilets.json')
process_json_file('templates/product.json')
process_json_file('templates/product.new-draft.json')
