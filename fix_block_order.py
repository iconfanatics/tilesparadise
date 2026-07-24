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
    
    data['sections']['main']['block_order'] = block_order
    
    order = data['order']
    
    if "calculator_section" in order:
        order.remove("calculator_section")
        if "calculator_section" in data['sections']:
            del data['sections']['calculator_section']

    calculator_section = {
      "type": "custom-liquid",
      "name": "Tile Calculator",
      "settings": {
        "title": "",
        "include_margins": True,
        "liquid": "{%- comment -%}\n  Liquid block (no title needed; set Display mode \"Show all\").\n  Banner linking to your standalone /pages/tile-calculator.\n{%- endcomment -%}\n<div class=\"tp-calcb\">\n  <div class=\"tp-calcb__txt\">\n    <h3>Doing a whole room?</h3>\n    <p>Use our free Tile Calculator &mdash; enter your wall and floor measurements, deduct doors and windows, and we'll work out exactly how many boxes you need, plus 10% for wastage.</p>\n  </div>\n  <a class=\"tp-calcb__btn\" href=\"/pages/tile-calculator\">Open the Tile Calculator &rarr;</a>\n</div>\n<div class=\"tp-usp-spacer\" style=\"height:40px; width:100%;\"></div>\n<style>\n  .tp-calcb{display:flex;align-items:center;justify-content:space-between;gap:22px;flex-wrap:wrap;\n    background:linear-gradient(120deg,#1a1d24,#2a3340);color:#fff;border-radius:14px;padding:24px 26px;\n    text-decoration:none;font-family:\"Open Sans\",sans-serif;}\n  .tp-calcb__txt h3{font-size:18px;font-weight:800;margin:0;color:#fff;}\n  .tp-calcb__txt p{font-size:13px;opacity:.85;margin:5px 0 0;max-width:560px;line-height:1.5;color:#fff;}\n  a.tp-calcb__btn{background:#fff;color:#1a1d24;font-weight:800;font-size:14px;padding:13px 22px;border-radius:10px;white-space:nowrap;\n    text-decoration:none !important; box-shadow:none !important; border:none !important; outline:none !important; background-image:none !important;}\n  .tp-calcb:hover a.tp-calcb__btn{background:#c8102e;color:#fff;}\n</style>"
      }
    }
    
    data['sections']['calculator_section'] = calculator_section
    
    if "product_tabs" in order:
        idx = order.index("product_tabs")
        order.insert(idx, "calculator_section")
    else:
        order.append("calculator_section")
        
    data['order'] = order

    new_json_str = json.dumps(data, indent=2)
    with open(filename, 'w') as f:
        f.write(comment_block + new_json_str + '\n')
    print("Successfully updated block order in", filename)

update_block_order()
