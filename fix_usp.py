import os
import glob
import re

for filepath in glob.glob('templates/product*.json'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '.tp-usp{' in content:
        # Check if already added to avoid duplication
        if 'margin-bottom:24px;' not in content and 'margin-bottom: 24px;' not in content:
            new_content = content.replace('.tp-usp{', '.tp-usp{margin-bottom:24px;')
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")

