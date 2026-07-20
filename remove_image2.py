import re

with open('sections/header.liquid', 'r') as f:
    content = f.read()

# Define the pattern to match the "Image 2" header and all fields associated with it.
# The schema for image_2 is at the end of the mega_menu block.
# We want to remove from `{ "type": "header", "content": "Image 2" }` 
# up to the end of the image_2_link block.
pattern = r'\{\s*"type":\s*"header",\s*"content":\s*"Image 2"\s*\}.*?\{\s*"type":\s*"url",\s*"id":\s*"image_2_link",\s*"label":\s*"Link"\s*\}'

new_content = re.sub(pattern, '', content, flags=re.DOTALL)

# Cleanup any trailing commas before closing braces
new_content = re.sub(r',\s*\}', '\n}', new_content)
new_content = re.sub(r',\s*\]', '\n]', new_content)

with open('sections/header.liquid', 'w') as f:
    f.write(new_content)

print("Done updating header.liquid")
