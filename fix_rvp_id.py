with open('sections/recently-viewed-paired.liquid', 'r') as f:
    content = f.read()

# Replace all occurrences of {{ ai_gen_id }} with rvp
content = content.replace('{{ ai_gen_id }}', 'rvp')

# Also remove the assign ai_gen_id line
content = content.replace("{% assign ai_gen_id = section.id | replace: '_', '' | downcase %}", '')

# Update the fetch URL to use the static filename
content = content.replace('section_id={{ section.id }}', 'section_id=recently-viewed-paired')

with open('sections/recently-viewed-paired.liquid', 'w') as f:
    f.write(content)
print("Replaced successfully")
