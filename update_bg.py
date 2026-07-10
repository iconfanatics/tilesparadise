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
    
    if 'custom_liquid_xki7ez' in data.get('sections', {}):
        blocks = data['sections']['custom_liquid_xki7ez'].get('blocks', {})
        if 'ai_gen_block_477adb9_new' in blocks:
            blocks['ai_gen_block_477adb9_new']['settings']['section_bg'] = '#f1eee8'
            updated = True
            
    if 'custom_liquid_t77pJf' in data.get('sections', {}):
        blocks = data['sections']['custom_liquid_t77pJf'].get('blocks', {})
        if 'ai_gen_block_paired_new' in blocks:
            blocks['ai_gen_block_paired_new']['settings']['section_bg'] = '#f1eee8'
            updated = True
            
    if updated:
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"No matching blocks found in {filename}")

process_json_file('templates/product.tiles.json')
