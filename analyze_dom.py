import urllib.request
import re

url = "https://tilesparadiseuk.com/"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # 1. Total DOM nodes (rough estimate by counting '<' followed by an alphanumeric char)
    total_elements = len(re.findall(r'<[a-zA-Z]', html))
    print(f"Total DOM Elements (Estimated): {total_elements}")
    
    # 2. Find sections
    # Split by shopify-section div
    sections = re.split(r'<div id="shopify-section-', html)[1:]
    
    print("\nTop 5 Heaviest Sections (by estimated DOM nodes):")
    section_counts = []
    
    for sec in sections:
        # get the section ID
        sec_id_match = re.match(r'([^"]+)"', sec)
        if not sec_id_match: continue
        sec_id = sec_id_match.group(1)
        
        # count elements in this section snippet
        nodes = len(re.findall(r'<[a-zA-Z]', sec))
        section_counts.append((sec_id, nodes))
        
    section_counts.sort(key=lambda x: x[1], reverse=True)
    for sec_id, nodes in section_counts[:5]:
        print(f"  - {sec_id}: {nodes} nodes")

except Exception as e:
    print(f"Error: {e}")
