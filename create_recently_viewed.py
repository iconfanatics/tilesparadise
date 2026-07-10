import re
import os

with open('blocks/ai_gen_block_paired.liquid', 'r') as f:
    content = f.read()

# Replace block.settings with section.settings
content = content.replace('block.settings.', 'section.settings.')
content = content.replace('block.id', 'section.id')
content = content.replace('block.shopify_attributes', 'section.shopify_attributes')

# Replace ai_gen_id logic to avoid collision
content = content.replace('{% assign ai_gen_id = section.id | replace: \'_\', \'\' | downcase %}', '{% assign ai_gen_id = section.id | replace: \'_\', \'\' | downcase %}')

# Find the track where products are rendered
track_start_str = '<div class="ai-product-carousel__track-{{ ai_gen_id }}">'
track_start = content.find(track_start_str)

# Find the end of the collection loop
track_end_str = '</div>\n    </div>\n  {% else %}'
track_end = content.find(track_end_str, track_start)

before_track = content[:track_start + len(track_start_str)]
after_track = content[track_end:]

# The product card logic starts with <div class="ai-product-carousel__item-
item_start = content.find('<div class="ai-product-carousel__item-{{ ai_gen_id }}">', track_start)
item_end = content.find('            {% endfor %}\n          {% endif %}\n        {% endfor %}', item_start)
product_item_html = content[item_start:item_end]

# We need to construct the search.results loop
new_loop = """
        {% assign parsed_terms = search.terms | split: ' OR ' %}
        {% for parsed_term in parsed_terms %}
          {% assign id = parsed_term | split: 'id:' | last | times: 1 %}
          {% for product in search.results %}
            {% if product.id == id %}
""" + product_item_html + """
              {% break %}
            {% endif %}
          {% endfor %}
        {% endfor %}
"""

# Now we need to wrap the whole <product-carousel-...> with the search condition
carousel_start_str = '<product-carousel-{{ ai_gen_id }}'
carousel_start = before_track.find(carousel_start_str)

# Before the carousel, we put the condition:
new_before = before_track[:carousel_start] + """
{% if request.page_type == 'search' and search.results_count > 0 %}
""" + before_track[carousel_start:]

# Instead of checking collection_handles, we check if search.results has items (which we already did)
new_before = new_before.replace('{% if section.settings.collection_handles != blank %}', '')

new_after = after_track.replace('{% else %}\n    <div class="ai-product-carousel__empty-{{ ai_gen_id }}">\n      <p>Select a collection to display products</p>\n    </div>\n  {% endif %}', '')

new_after = new_after.replace('</product-carousel-{{ ai_gen_id }}>', """</product-carousel-{{ ai_gen_id }}>
{% else %}
  <recently-viewed-paired data-product-id="{{ product.id }}"></recently-viewed-paired>
  <script>
    if (!customElements.get('recently-viewed-paired')) {
      class RecentlyViewedPaired extends HTMLElement {
        connectedCallback() {
          let items = JSON.parse(localStorage.getItem('recentlyViewedProducts') || '[]');
          const currentId = this.dataset.productId;
          let currentIdNum = parseInt(currentId);
          if (currentIdNum && items.includes(currentIdNum)) {
            items.splice(items.indexOf(currentIdNum), 1);
          }
          if (items.length === 0) {
            this.style.display = 'none';
            return;
          }
          items = items.slice(0, 10);
          const query = items.map(id => `id:${id}`).join(' OR ');
          
          let searchUrl = window.routes ? window.routes.searchUrl : '/search';
          fetch(`${searchUrl}?section_id={{ section.id }}&type=product&q=${query}`)
            .then(res => res.text())
            .then(html => {
              const parser = new DOMParser();
              const doc = parser.parseFromString(html, 'text/html');
              const content = doc.querySelector('product-carousel-{{ ai_gen_id }}');
              if (content) {
                this.innerHTML = content.outerHTML;
              } else {
                this.style.display = 'none';
              }
            });
        }
      }
      customElements.define('recently-viewed-paired', RecentlyViewedPaired);
    }
  </script>
{% endif %}
""")

final_content = new_before + new_loop + new_after

# Now replace the schema
schema_start = final_content.find('{% schema %}')
new_schema = """
{% schema %}
{
  "name": "Recently Viewed Paired",
  "settings": [
    {
      "type": "header",
      "content": "Layout"
    },
    {
      "type": "text",
      "id": "title",
      "label": "Heading",
      "default": "Recently Viewed"
    },
    {
      "type": "range",
      "id": "products_per_row_desktop",
      "label": "Products per row (desktop)",
      "min": 2,
      "max": 5,
      "step": 1,
      "default": 5
    },
    {
      "type": "select",
      "id": "products_per_row_mobile",
      "label": "Products per row (mobile)",
      "options": [
        { "value": "1", "label": "1" },
        { "value": "2", "label": "2" }
      ],
      "default": "2"
    },
    {
      "type": "range",
      "id": "product_gap",
      "label": "Gap between products",
      "min": 10,
      "max": 40,
      "step": 5,
      "unit": "px",
      "default": 20
    },
    {
      "type": "range",
      "id": "section_padding",
      "label": "Section padding",
      "min": 0,
      "max": 100,
      "step": 5,
      "unit": "px",
      "default": 20
    },
    {
      "type": "range",
      "id": "desktop_width_percent",
      "label": "Desktop width",
      "min": 50,
      "max": 100,
      "step": 5,
      "unit": "%",
      "default": 100
    },
    {
      "type": "range",
      "id": "container_width",
      "label": "Container width",
      "min": 900,
      "max": 1500,
      "step": 50,
      "unit": "px",
      "default": 1350
    },
    {
      "type": "range",
      "id": "side_padding",
      "label": "Side padding",
      "min": 0,
      "max": 60,
      "step": 2,
      "unit": "px",
      "default": 20
    },
    {
      "type": "color",
      "id": "section_bg",
      "label": "Section background",
      "default": "#f1eee8"
    },
    {
      "type": "header",
      "content": "Heading"
    },
    {
      "type": "range",
      "id": "title_size",
      "label": "Size",
      "min": 16,
      "max": 48,
      "step": 2,
      "unit": "px",
      "default": 28
    },
    {
      "type": "range",
      "id": "title_spacing",
      "label": "Bottom spacing",
      "min": 10,
      "max": 60,
      "step": 2,
      "unit": "px",
      "default": 24
    },
    {
      "type": "color",
      "id": "title_color",
      "label": "Color",
      "default": "#3b3337"
    },
    {
      "type": "header",
      "content": "Navigation Buttons"
    },
    {
      "type": "color",
      "id": "nav_button_bg",
      "label": "Background",
      "default": "#ffffff"
    },
    {
      "type": "color",
      "id": "nav_button_color",
      "label": "Color",
      "default": "#111111"
    },
    {
      "type": "color",
      "id": "nav_button_hover_bg",
      "label": "Hover background",
      "default": "#f1f1f1"
    },
    {
      "type": "color",
      "id": "nav_button_hover_color",
      "label": "Hover color",
      "default": "#111111"
    },
    {
      "type": "header",
      "content": "Product Card"
    },
    {
      "type": "color",
      "id": "card_bg",
      "label": "Background",
      "default": "#ffffff"
    },
    {
      "type": "color",
      "id": "image_bg",
      "label": "Image background",
      "default": "#f5f5f5"
    },
    {
      "type": "range",
      "id": "card_padding",
      "label": "Padding",
      "min": 10,
      "max": 30,
      "step": 1,
      "unit": "px",
      "default": 16
    },
    {
      "type": "range",
      "id": "card_border_radius",
      "label": "Border radius",
      "min": 0,
      "max": 20,
      "step": 1,
      "unit": "px",
      "default": 0
    },
    {
      "type": "header",
      "content": "Typography & Colors"
    },
    {
      "type": "range",
      "id": "product_title_size",
      "label": "Title size",
      "min": 12,
      "max": 24,
      "step": 1,
      "unit": "px",
      "default": 14
    },
    {
      "type": "color",
      "id": "product_title_color",
      "label": "Title color",
      "default": "#111111"
    },
    {
      "type": "range",
      "id": "price_size",
      "label": "Price size",
      "min": 12,
      "max": 24,
      "step": 1,
      "unit": "px",
      "default": 18
    },
    {
      "type": "color",
      "id": "price_color",
      "label": "Price color",
      "default": "#e40012"
    },
    {
      "type": "color",
      "id": "sale_price_color",
      "label": "Sale price color",
      "default": "#e40012"
    },
    {
      "type": "color",
      "id": "compare_price_color",
      "label": "Compare price color",
      "default": "#6f6f6f"
    },
    {
      "type": "color",
      "id": "accent_color",
      "label": "Accent color (hover)",
      "default": "#3070b7"
    },
    {
      "type": "header",
      "content": "Badges & Labels"
    },
    {
      "type": "color",
      "id": "badge_bg",
      "label": "Save badge background",
      "default": "#e40012"
    },
    {
      "type": "color",
      "id": "badge_text_color",
      "label": "Save badge text",
      "default": "#ffffff"
    },
    {
      "type": "range",
      "id": "badge_size",
      "label": "Badge font size",
      "min": 10,
      "max": 16,
      "step": 1,
      "unit": "px",
      "default": 13
    },
    {
      "type": "color",
      "id": "vendor_bg",
      "label": "Vendor background",
      "default": "#171717"
    },
    {
      "type": "color",
      "id": "vendor_text_color",
      "label": "Vendor text",
      "default": "#ffffff"
    },
    {
      "type": "color",
      "id": "review_star_color",
      "label": "Review star color",
      "default": "#ff9d00"
    },
    {
      "type": "header",
      "content": "Stock & Wishlist"
    },
    {
      "type": "color",
      "id": "stock_text_color",
      "label": "Stock text color",
      "default": "#111111"
    },
    {
      "type": "range",
      "id": "stock_size",
      "label": "Stock font size",
      "min": 10,
      "max": 16,
      "step": 1,
      "unit": "px",
      "default": 14
    },
    {
      "type": "color",
      "id": "stock_icon_bg",
      "label": "In-stock icon background",
      "default": "#31ad45"
    },
    {
      "type": "color",
      "id": "stock_icon_color",
      "label": "In-stock icon check",
      "default": "#ffffff"
    },
    {
      "type": "color",
      "id": "out_of_stock_color",
      "label": "Out of stock color",
      "default": "#cf0e0e"
    },
    {
      "type": "color",
      "id": "wishlist_color",
      "label": "Wishlist icon color",
      "default": "#2e8f3d"
    },
    {
      "type": "header",
      "content": "Button"
    },
    {
      "type": "text",
      "id": "button_text",
      "label": "Button text",
      "default": "View product"
    },
    {
      "type": "color",
      "id": "button_bg",
      "label": "Background",
      "default": "#df3653"
    },
    {
      "type": "color",
      "id": "button_hover_bg",
      "label": "Hover background",
      "default": "#c72e47"
    },
    {
      "type": "color",
      "id": "button_text_color",
      "label": "Text color",
      "default": "#ffffff"
    },
    {
      "type": "range",
      "id": "button_border_radius",
      "label": "Border radius",
      "min": 0,
      "max": 30,
      "step": 1,
      "unit": "px",
      "default": 4
    }
  ],
  "presets": [
    {
      "name": "Recently Viewed Paired"
    }
  ]
}
{% endschema %}
"""
final_content = final_content[:schema_start] + new_schema

# We need to make sure the web component JS handles multiple instances. It does, because we use customElements.get
with open('sections/recently-viewed-paired.liquid', 'w') as f:
    f.write(final_content)
