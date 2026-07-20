import glob
import json
import re

for filepath in glob.glob('templates/product*.json'):
    with open(filepath, 'r') as f:
        text = f.read()
    
    has_comments = '/*' in text
    
    text_no_comments = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    
    try:
        data = json.loads(text_no_comments)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        continue
        
    if 'recently_viewed_paired_new' not in data['sections']:
        data['sections']['recently_viewed_paired_new'] = {
            "type": "recently-viewed-paired",
            "settings": {
                "title": "Recently Viewed Products",
                "section_bg": "#f8f7f5"
            }
        }
        
        if 'recently_viewed_paired_new' not in data['order']:
            # Put it right before product-recommendations or custom_liquid_kEaUUB or at the end
            inserted = False
            for target in ['product-recommendations', 'custom_liquid_kEaUUB']:
                if target in data['order']:
                    idx = data['order'].index(target)
                    data['order'].insert(idx, 'recently_viewed_paired_new')
                    inserted = True
                    break
            
            if not inserted:
                data['order'].append('recently_viewed_paired_new')
                
        with open(filepath, 'w') as f:
            if has_comments:
                f.write('/*\n * ------------------------------------------------------------\n * IMPORTANT: The contents of this file are auto-generated.\n * ------------------------------------------------------------\n */\n')
            json.dump(data, f, indent=2)
            f.write('\n')
        print(f"Added to {filepath}")

