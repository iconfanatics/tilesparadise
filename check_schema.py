import re
import json

with open('sections/header.liquid', 'r') as f:
    content = f.read()

match = re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', content, re.DOTALL)
if match:
    schema_text = match.group(1)
    try:
        json.loads(schema_text)
        print("Schema is valid JSON.")
    except Exception as e:
        print("Schema error:", e)
else:
    print("Schema block not found.")
