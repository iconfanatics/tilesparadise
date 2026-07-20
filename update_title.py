import json

with open('templates/product.tiles.json', 'r') as f:
    data = json.load(f)

# The file now does NOT have comments since I stripped them!
data['sections']['main']['blocks']['calculator_block']['settings']['title'] = ""

with open('templates/product.tiles.json', 'w') as f:
    json.dump(data, f, indent=2)

