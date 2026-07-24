import json

def update_block_order():
    filename = 'templates/product.tiles.json'
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    data = json.loads(json_str)
    
    block_order = data['sections']['main']['block_order']
    
    if "calculator_block" in block_order:
        block_order.remove("calculator_block")
    
    if "description" in block_order:
        desc_idx = block_order.index("description")
        # insert calculator_block right AFTER description
        block_order.insert(desc_idx + 1, "calculator_block")
    else:
        print("Description block not found in order. Adding to end.")
        block_order.append("calculator_block")

    data['sections']['main']['block_order'] = block_order

    new_json_str = json.dumps(data, indent=2)
    with open(filename, 'w') as f:
        f.write(comment_block + new_json_str + '\n')
    print("Successfully updated block order in", filename)

update_block_order()
