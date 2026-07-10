import json

filename = 'templates/product.tiles.json'
try:
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    data = json.loads(json_str)

    modified = False
    if 'sections' in data:
        # Check inside main section blocks
        for sec_id, sec_data in data['sections'].items():
            if 'blocks' in sec_data:
                blocks_to_remove = []
                for block_id, block_data in sec_data['blocks'].items():
                    if block_data.get('type') in ['custom-liquid', 'liquid']:
                        settings = block_data.get('settings', {})
                        title = settings.get('title', '')
                        liquid = settings.get('liquid', '')
                        if title == 'Tile FAQs' or 'How many tiles do I need?' in liquid:
                            blocks_to_remove.append(block_id)
                
                for bid in blocks_to_remove:
                    del sec_data['blocks'][bid]
                    if 'block_order' in sec_data and bid in sec_data['block_order']:
                        sec_data['block_order'].remove(bid)
                    modified = True

        # Check top-level sections
        sections_to_remove = []
        for sec_id, sec_data in data['sections'].items():
            if sec_data.get('type') in ['custom-liquid', 'liquid']:
                settings = sec_data.get('settings', {})
                title = settings.get('title', '')
                liquid = settings.get('liquid', '')
                if title == 'Tile FAQs' or 'How many tiles do I need?' in liquid:
                    sections_to_remove.append(sec_id)
        
        for sid in sections_to_remove:
            del data['sections'][sid]
            if 'order' in data and sid in data['order']:
                data['order'].remove(sid)
            modified = True

    if modified:
        with open(filename, 'w') as f:
            f.write(comment_block)
            json.dump(data, f, indent=2)
        print("Successfully removed old Tile FAQs block.")
    else:
        print("Tile FAQs block not found.")
except Exception as e:
    print(f"Error: {e}")
