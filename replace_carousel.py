import json
import re

def process_json_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Shopify JSON files often start with a comment block.
    # We can separate it by finding the first '{'
    start_idx = content.find('{')
    comment_block = content[:start_idx]
    json_str = content[start_idx:]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return

    # Look for custom_liquid_xki7ez
    if 'custom_liquid_xki7ez' in data.get('sections', {}):
        # We will replace it with the new block structure
        data['sections']['custom_liquid_xki7ez'] = {
            "type": "_blocks",
            "blocks": {
                "ai_gen_block_477adb9_new": {
                    "type": "ai_gen_block_477adb9",
                    "settings": {
                        "collection": "tile-sale",
                        "products_limit": 12,
                        "title": "Not quite the right look? Browse similar tiles",
                        "products_per_row_desktop": 5,
                        "products_per_row_mobile": "2",
                        "product_gap": 20,
                        "section_padding": 20,
                        "desktop_width_percent": 100,
                        "container_width": 1200,
                        "side_padding": 22,
                        "section_bg": "#f1eee8",
                        "title_size": 24,
                        "title_spacing": 15,
                        "title_color": "#000000",
                        "nav_button_bg": "#f5f5f5",
                        "nav_button_hover_bg": "#e8e8e8",
                        "nav_button_color": "#3b3337",
                        "nav_button_hover_color": "#000000",
                        "nav_right_offset": 4,
                        "card_bg": "#ffffff",
                        "image_bg": "#f4f4f4",
                        "card_border_radius": 2,
                        "card_padding": 10,
                        "product_title_size": 15,
                        "product_title_color": "#151515",
                        "price_size": 19,
                        "price_color": "#e40012",
                        "sale_price_color": "#e40012",
                        "compare_price_color": "#6f6f6f",
                        "accent_color": "#3070b7",
                        "badge_bg": "#e40012",
                        "badge_text_color": "#ffffff",
                        "badge_size": 13,
                        "vendor_bg": "#171717",
                        "vendor_text_color": "#ffffff",
                        "review_star_color": "#ff9d00",
                        "stock_text_color": "#111111",
                        "stock_size": 14,
                        "stock_icon_bg": "#31ad45",
                        "stock_icon_color": "#ffffff",
                        "out_of_stock_color": "#cf0e0e",
                        "wishlist_color": "#2e8f3d",
                        "button_text": "View product",
                        "button_bg": "#df3653",
                        "button_hover_bg": "#c72e47",
                        "button_text_color": "#ffffff",
                        "button_border_radius": 4
                    }
                }
            },
            "block_order": [
                "ai_gen_block_477adb9_new"
            ],
            "name": "Product carousel",
            "settings": {}
        }
        
        # Write back
        new_json_str = json.dumps(data, indent=2)
        with open(filename, 'w') as f:
            f.write(comment_block + new_json_str + '\n')
        print(f"Successfully updated {filename}")
    else:
        print(f"Could not find custom_liquid_xki7ez in {filename}")

process_json_file('templates/product.tiles.json')
