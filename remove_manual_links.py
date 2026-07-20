import re

with open('sections/header.liquid', 'r') as f:
    content = f.read()

# 1. Strip out the 'or child_promo_block.settings.manual... != blank'
content = re.sub(r'\s*or\s+child_promo_block\.settings\.manual\w*?_link_\w*?_text\s*!=\s*blank', '', content)

# 2. Strip out the manual links HTML generation blocks
# {%- if child_promo_block.settings.manual_link_1_text != blank -%} ... {%- endif -%}
content = re.sub(r'\{%- if child_promo_block\.settings\.manual.*?_link_.*?_text != blank -%\}.*?\{%- endif -%\}', '', content, flags=re.DOTALL)

# 3. Strip out the schema elements for manual links and their headers
# The headers: { "type": "header", "content": "OR Add Manual Links 1" },
content = re.sub(r'\{\s*"type":\s*"header",\s*"content":\s*"OR Add Manual Links \d+"\s*\},', '', content)

# The manual link text/url definitions
# We might match { "type": "url", "id": "manual2_link_5_url", "label": "Manual Link 5 URL" },
content = re.sub(r'\{\s*"type":\s*"(text|url)",\s*"id":\s*"manual\d*_link_\d+_(text|url)",\s*"label":\s*"[^"]+"\s*\},?', '', content)

# Remove any double commas left over
content = re.sub(r',\s*,', ',', content)
# Remove any hanging commas before a closing bracket
content = re.sub(r',\s*\}', '\n}', content)
content = re.sub(r',\s*\]', '\n]', content)

with open('sections/header.liquid', 'w') as f:
    f.write(content)

print("Done updating header.liquid")
