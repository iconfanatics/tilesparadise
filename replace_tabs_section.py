import json

def process_json_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    if start_idx == -1: return
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return

    updated = False
    
    sections = data.get('sections', {})
    if 'custom_liquid_tabs' in sections:
        # Delete old custom liquid tabs section
        del sections['custom_liquid_tabs']
        
        # Insert new product-tabs section
        sections['product_tabs'] = {
            "type": "product-tabs",
            "settings": {
                "tab_1_title": "Product Information",
                "tab_2_title": "Product Details"
            }
        }
        
        # Replace in order
        order = data.get('order', [])
        for i, val in enumerate(order):
            if val == 'custom_liquid_tabs':
                order[i] = 'product_tabs'
                
        updated = True
            
    if updated:
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"No update needed for {filename}")

process_json_file('templates/product.tiles.json')
process_json_file('templates/product.toilets.json')
process_json_file('templates/product.json')
process_json_file('templates/product.new-draft.json')
