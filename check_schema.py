import json

with open('sections/recently-viewed-paired.liquid', 'r') as f:
    content = f.read()

schema_start = content.find('{% schema %}')
schema_end = content.find('{% endschema %}')

if schema_start != -1 and schema_end != -1:
    schema_str = content[schema_start+12:schema_end]
    try:
        data = json.loads(schema_str)
        print("Schema is valid JSON.")
    except Exception as e:
        print("Schema JSON error:", e)
else:
    print("Schema not found.")
