import os
import glob
import re

for filepath in glob.glob('templates/product*.json'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '.tp-usp{' in content:
        # Check if we already added a spacer div to prevent multiple additions
        if '<div class="tp-usp-spacer"' not in content:
            # We insert a spacer after the </div> that closes .tp-usp
            # Look for: </div>\n<style>
            # Replace with: </div>\n<div class="tp-usp-spacer" style="height:32px;"></div>\n<style>
            new_content = content.replace(
                '</div>\\n<style>',
                '</div>\\n<div class=\\"tp-usp-spacer\\" style=\\"height:40px; width:100%;\\">\u003c/div>\\n<style>'
            )
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

