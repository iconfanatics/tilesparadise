import json

def process_json_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return

    updated = False
    
    # Define the new tabs liquid
    tabs_liquid = """{%- liquid
  assign c = product.metafields.custom
  assign sku = product.selected_or_first_available_variant.sku
-%}

<div class="tp-tabs-container">
  <div class="tp-tabs-header">
    <button class="tp-tab-btn active" data-tab="tab-description">Product Information</button>
    <button class="tp-tab-btn" data-tab="tab-details">Product Details</button>
  </div>
  
  <div class="tp-tabs-content">
    <!-- Tab 1: Description -->
    <div id="tab-description" class="tp-tab-pane active">
      {%- if product.description != blank -%}
        <div class="tp-desc-wrap">
          <div class="tp-desc rte">
            {{ product.description | remove: 'data-section-type="product"' }}
          </div>
          <button type="button" class="tp-desc-toggle" style="display:none">Read more</button>
        </div>
      {%- endif -%}
    </div>
    
    <!-- Tab 2: Details -->
    <div id="tab-details" class="tp-tab-pane">
      <div class="tp-spec">
        {%- if sku != blank -%}<div class="tp-spec__row"><span class="k">SKU</span><span class="v">{{ sku }}</span></div>{%- endif -%}
        {%- if c.material != blank -%}<div class="tp-spec__row"><span class="k">Material</span><span class="v">{{ c.material }}</span></div>{%- endif -%}
        {%- if c.colour != blank -%}<div class="tp-spec__row"><span class="k">Colour</span><span class="v">{{ c.colour }}</span></div>{%- endif -%}
        {%- if c.thickness != blank -%}<div class="tp-spec__row"><span class="k">Thickness</span><span class="v">{{ c.thickness }}</span></div>{%- endif -%}
        {%- if c.tile_finish != blank -%}<div class="tp-spec__row"><span class="k">Finish</span><span class="v">{{ c.tile_finish }}</span></div>{%- endif -%}
        {%- if c.floor_or_wall != blank -%}<div class="tp-spec__row"><span class="k">Floor or Wall</span><span class="v">{{ c.floor_or_wall }}</span></div>{%- endif -%}
        {%- if c.size != blank -%}<div class="tp-spec__row"><span class="k">Size</span><span class="v">{{ c.size }}</span></div>{%- endif -%}
        {%- if c.rectified != blank -%}<div class="tp-spec__row"><span class="k">Rectified</span><span class="v">{% if c.rectified == true %}Yes{% elsif c.rectified == false %}No{% else %}{{ c.rectified }}{% endif %}</span></div>{%- endif -%}
        {%- if c.suitable_for_underfloor_heating != blank -%}<div class="tp-spec__row"><span class="k">Suitable for Underfloor Heating</span><span class="v">{% if c.suitable_for_underfloor_heating == true %}Yes{% elsif c.suitable_for_underfloor_heating == false %}No{% else %}{{ c.suitable_for_underfloor_heating }}{% endif %}</span></div>{%- endif -%}
        {%- if c.box_quantity != blank -%}<div class="tp-spec__row"><span class="k">Box Quantity</span><span class="v">{{ c.box_quantity }}</span></div>{%- endif -%}
        {%- if c.weight != blank -%}<div class="tp-spec__row"><span class="k">Weight</span><span class="v">{{ c.weight }}</span></div>{%- endif -%}
        {%- if c.sale_by != blank -%}<div class="tp-spec__row"><span class="k">Sale By</span><span class="v">{{ c.sale_by }}</span></div>{%- endif -%}
      </div>
    </div>
  </div>
</div>

<style>
  .tp-tabs-container {
    max-width: 820px;
    font-family: "Open Sans", sans-serif;
    margin-bottom: 30px;
    margin-top: 20px;
  }
  .tp-tabs-header {
    display: flex;
    gap: 8px;
    margin-bottom: 24px;
    border-bottom: 2px solid #1a1d24;
  }
  .tp-tab-btn {
    background: transparent;
    border: 2px solid #1a1d24;
    border-bottom: none;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 800;
    color: #1a1d24;
    cursor: pointer;
    margin-bottom: -2px;
    transition: all 0.2s ease;
  }
  .tp-tab-btn:not(.active) {
    background: #f7f8f9;
    border-color: #e6e8eb;
    border-bottom: 2px solid #1a1d24;
    color: #4a4f57;
  }
  .tp-tab-btn.active {
    background: #ffffff;
    border: 2px solid #1a1d24;
    border-bottom: 2px solid #ffffff;
  }
  
  .tp-tab-pane {
    display: none;
    animation: fadeIn 0.3s ease;
  }
  .tp-tab-pane.active {
    display: block;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  /* Details Table Styles */
  .tp-spec{display:grid;grid-template-columns:1fr 1fr;border:1px solid #e6e8eb;border-radius:8px;overflow:hidden;}
  .tp-spec__row{display:flex;justify-content:space-between;gap:14px;padding:13px 18px;font-size:14px;border-bottom:1px solid #eef0f2;}
  .tp-spec__row:nth-child(4n+1),.tp-spec__row:nth-child(4n+2){background:#f7f8f9;}
  .tp-spec .k{font-weight:700;color:#1a1d24;}
  .tp-spec .v{color:#4a4f57;text-align:right;}
  @media(max-width:600px){
    .tp-spec{grid-template-columns:1fr;}
    .tp-spec__row:nth-child(n){background:#fff;}
    .tp-spec__row:nth-child(odd){background:#f7f8f9;}
    .tp-tab-btn { padding: 10px 14px; font-size: 14px; }
  }
  
  /* Description Styles */
  .tp-desc{font-size:15px;line-height:1.7;color:#3a3f48;position:relative;overflow:hidden;}
  .tp-desc.is-clamped{max-height:230px;}
  .tp-desc.is-clamped::after{content:"";position:absolute;left:0;right:0;bottom:0;height:80px;background:linear-gradient(to bottom,rgba(255,255,255,0),#fff);pointer-events:none;}
  .tp-desc h2,.tp-desc h3{color:#1a1d24;font-weight:800;margin:16px 0 6px;line-height:1.3;}
  .tp-desc p{margin:0 0 11px;}
  .tp-desc ul,.tp-desc ol{margin:8px 0 14px 20px;}
  .tp-desc li{margin-bottom:5px;}
  .tp-desc table{width:100%;border-collapse:collapse;margin:10px 0;}
  .tp-desc td,.tp-desc th{border:1px solid #e6e8eb;padding:8px 12px;text-align:left;}
  .tp-desc-toggle{margin-top:12px;background:none;border:0;color:#c8102e;font-weight:700;cursor:pointer;font-size:14px;padding:0;}
  .tp-desc-toggle:hover{text-decoration:underline;}
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
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
    });
    
    document.querySelectorAll('.tp-desc-wrap').forEach(function(wrap){
      var desc = wrap.querySelector('.tp-desc');
      var btn  = wrap.querySelector('.tp-desc-toggle');
      if(!desc || !btn) return;
      var CLAMP = 230;
      if(desc.scrollHeight > CLAMP + 60){
        desc.classList.add('is-clamped');
        btn.style.display = 'inline-block';
        btn.addEventListener('click', function(){
          var clamped = desc.classList.toggle('is-clamped');
          btn.textContent = clamped ? 'Read more' : 'Read less';
        });
      }
    });
  });
</script>
"""

    if 'main' in data.get('sections', {}):
        blocks = data['sections']['main'].get('blocks', {})
        block_order = data['sections']['main'].get('block_order', [])
        
        # We will add our new tab block
        new_block_id = 'custom_liquid_tabs'
        blocks[new_block_id] = {
            "type": "custom-liquid",
            "name": "Product Tabs (Desc + Details)",
            "settings": {
                "title": "",
                "include_margins": True,
                "liquid": tabs_liquid
            }
        }
        
        # Replace the old blocks in the order
        # Specifically custom_liquid_CxGYaH and custom_liquid_hYpwa8
        new_order = []
        added_tabs = False
        for b_id in block_order:
            if b_id in ['custom_liquid_CxGYaH', 'custom_liquid_hYpwa8']:
                if not added_tabs:
                    new_order.append(new_block_id)
                    added_tabs = True
            else:
                new_order.append(b_id)
                
        # Also remove them from blocks if they exist
        if 'custom_liquid_CxGYaH' in blocks:
            del blocks['custom_liquid_CxGYaH']
        if 'custom_liquid_hYpwa8' in blocks:
            del blocks['custom_liquid_hYpwa8']
            
        data['sections']['main']['block_order'] = new_order
        updated = True
            
    if updated:
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"No matching blocks found in {filename}")

process_json_file('templates/product.tiles.json')
process_json_file('templates/product.toilets.json')
process_json_file('templates/product.json')
process_json_file('templates/product.new-draft.json')
