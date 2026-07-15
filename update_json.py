import json
import re

with open('templates/product.tiles.json', 'r') as f:
    text = f.read()

# Strip JS style comments (only block comments at top)
text_no_comments = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

data = json.loads(text_no_comments)

# Get the calculator block
calc = data['sections']['custom_liquid_6YVggk']

# Format it as a block for main
new_block = {
    "type": "liquid",
    "settings": {
        "title": "Calculator",
        "liquid": calc['settings']['liquid'],
        "display_mode": "show_all"
    }
}

# Add to main blocks
data['sections']['main']['blocks']['calculator_block'] = new_block

# Add to main block_order (at the top so it's right under the slider)
data['sections']['main']['block_order'].insert(0, "calculator_block")

# Delete old section
del data['sections']['custom_liquid_6YVggk']
data['order'].remove('custom_liquid_6YVggk')

with open('templates/product.tiles.json', 'w') as f:
    json.dump(data, f, indent=2)

