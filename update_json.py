import json
import glob

for filename in glob.glob('templates/product*.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        changed = False
        for section_id, section in data.get('sections', {}).items():
            for block_id, block in section.get('blocks', {}).items():
                if block.get('type') == 'delivery_options':
                    if 'settings' not in block:
                        block['settings'] = {}
                    
                    if 'delivery_drawer_content' not in block['settings']:
                        block['settings']['delivery_drawer_content'] = "<h3>Standard Delivery</h3><p>We deliver using a pallet network. Delivery takes 2-7 working days.</p><h3>Next Day Delivery</h3><p>Available on orders placed before 12pm.</p><h3>Returns</h3><p>We accept returns within 30 days of purchase.</p>"
                        changed = True
                    
                    if 'faq_drawer_content' not in block['settings']:
                        block['settings']['faq_drawer_content'] = "<h3>Frequently Asked Questions</h3><p><strong>How long does delivery take?</strong><br>Delivery typically takes between 2 to 7 working days depending on your location.</p><p><strong>Do you offer next day delivery?</strong><br>Yes, we offer next day pallet service for £39.95 if ordered before noon.</p><p><strong>What is your return policy?</strong><br>You can return items within 30 days in their original condition.</p>"
                        changed = True
                        
        if changed:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Updated {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
