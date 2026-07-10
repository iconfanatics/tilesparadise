import json

def process_json_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    if start_idx == -1: return
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return

    updated = False
    
    sections = data.get('sections', {})
    if 'custom_liquid_tabs' in sections:
        liquid_code = sections['custom_liquid_tabs']['settings']['liquid']
        
        # FIX CSS: Remove `border-color: #e6e8eb;` so inactive tab has black border too
        liquid_code = liquid_code.replace("border-color: #e6e8eb;", "")
        # Also let's make the background white for inactive like screenshot if we want, but #f7f8f9 is fine. 
        # Actually in screenshot, inactive tab is white! Let's make it white too.
        liquid_code = liquid_code.replace("background: #f7f8f9;", "background: #ffffff;")
        
        # FIX JS: Use event delegation or scope to container
        old_js = """<script>
  (function() {
    const tabs = document.querySelectorAll('.tp-tab-btn');
    const panes = document.querySelectorAll('.tp-tab-pane');
    
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        panes.forEach(p => p.classList.remove('active'));
        
        tab.classList.add('active');
        const targetPane = document.getElementById(tab.getAttribute('data-tab'));
        if (targetPane) targetPane.classList.add('active');
      });
    });"""
        
        new_js = """<script>
  (function() {
    // Select all tab containers on the page
    const containers = document.querySelectorAll('.tp-tabs-container');
    containers.forEach(container => {
      const tabs = container.querySelectorAll('.tp-tab-btn');
      const panes = container.querySelectorAll('.tp-tab-pane');
      
      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          tabs.forEach(t => t.classList.remove('active'));
          panes.forEach(p => p.classList.remove('active'));
          
          tab.classList.add('active');
          // Find the target pane inside this specific container
          const targetId = tab.getAttribute('data-tab');
          const targetPane = container.querySelector('#' + targetId) || document.getElementById(targetId);
          if (targetPane) targetPane.classList.add('active');
        });
      });
    });"""
        
        if old_js in liquid_code:
            liquid_code = liquid_code.replace(old_js, new_js)
            sections['custom_liquid_tabs']['settings']['liquid'] = liquid_code
            updated = True
        else:
            print("Could not find exact JS string to replace")
            
    if updated:
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"No update needed for {filename}")

process_json_file('templates/product.tiles.json')
process_json_file('templates/product.toilets.json')
process_json_file('templates/product.json')
process_json_file('templates/product.new-draft.json')
