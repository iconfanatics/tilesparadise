import json

with open('templates/product.tiles.json', 'r') as f:
    data = json.load(f)

# The liquid content
liquid_content = data['sections']['main']['blocks']['calculator_block']['settings']['liquid']

# Update the style to include text-decoration: none !important for everything inside
new_style_line = "  .tp-calcb, .tp-calcb * { text-decoration: none !important; background-image: none !important; border: none !important; }"
liquid_content = liquid_content.replace("<style>", "<style>\n" + new_style_line)

data['sections']['main']['blocks']['calculator_block']['settings']['liquid'] = liquid_content

with open('templates/product.tiles.json', 'w') as f:
    json.dump(data, f, indent=2)

