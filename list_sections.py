import json

file_path = '/home/sany/sajedul/templates/index.json'
with open(file_path, 'r') as f:
    lines = f.readlines()
    
# basic comment strip
clean_lines = [l for l in lines if not l.strip().startswith('/*') and not l.strip().startswith('*')]
content = ''.join(clean_lines)

try:
    data = json.loads(content)
    sections = data.get('sections', {})
    for k, v in sections.items():
        print(f"{k} -> {v.get('type')}")
except Exception as e:
    print("Error:", e)
