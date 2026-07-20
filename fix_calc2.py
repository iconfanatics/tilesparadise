import json

with open('templates/product.tiles.json', 'r') as f:
    data = json.load(f)

liquid_content = data['sections']['main']['blocks']['calculator_block']['settings']['liquid']

# Update the style to include box-shadow as well
liquid_content = liquid_content.replace(
    "background-image: none !important; border: none !important; }",
    "background-image: none !important; border: none !important; box-shadow: none !important; outline: none !important; }"
)

data['sections']['main']['blocks']['calculator_block']['settings']['liquid'] = liquid_content

with open('templates/product.tiles.json', 'w') as f:
    json.dump(data, f, indent=2)

