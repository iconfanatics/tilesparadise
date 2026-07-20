import re

with open('sections/header.liquid', 'r') as f:
    content = f.read()

# 1. Update the condition at line 348
condition_parts = []
for i in range(1, 8):
    prefix = "" if i == 1 else str(i)
    condition_parts.append(f"child_promo_block.settings.custom_linklist_{i} != blank or child_promo_block.settings.manual{prefix}_link_1_text != blank")

new_condition = "{%- if " + " or ".join(condition_parts) + " -%}"
# Replace the original condition
content = re.sub(r'\{%- if child_promo_block\.settings\.custom_linklist_1 != blank or child_promo_block\.settings\.custom_linklist_2 != blank or child_promo_block\.settings\.manual_link_1_text != blank or child_promo_block\.settings\.manual2_link_1_text != blank -%\}', new_condition, content)


# 2. Add HTML for columns 3 to 7
def generate_html_column(i):
    prefix = "" if i == 1 else str(i)
    return f"""                                    {{%- if child_promo_block != blank -%}}
                                      {{%- if child_promo_block.settings.custom_linklist_{i} != blank or child_promo_block.settings.manual{prefix}_link_1_text != blank -%}}
                                        <div class="tabbed-mega-nav__column">
                                        {{%- if child_promo_block.settings.custom_title_{i} != blank -%}}
                                          <span class="tabbed-mega-nav__column-title">{{{{ child_promo_block.settings.custom_title_{i} }}}}</span>
                                        {{%- endif -%}}
                                        <ul class="tabbed-mega-nav__link-grid list--unstyled" role="list">
                                          {{%- if child_promo_block.settings.custom_linklist_{i} != blank -%}}
                                            {{%- for custom_link in child_promo_block.settings.custom_linklist_{i}.links -%}}
                                              <li>
                                                <a href="{{{{ custom_link.url }}}}" class="tabbed-mega-nav__panel-link">
                                                  {{{{ custom_link.title }}}}
                                                </a>
                                              </li>
                                            {{%- endfor -%}}
                                          {{%- endif -%}}
                                          {{%- if child_promo_block.settings.manual{prefix}_link_1_text != blank -%}}
                                            <li><a href="{{{{ child_promo_block.settings.manual{prefix}_link_1_url }}}}" class="tabbed-mega-nav__panel-link">{{{{ child_promo_block.settings.manual{prefix}_link_1_text }}}}</a></li>
                                          {{%- endif -%}}
                                          {{%- if child_promo_block.settings.manual{prefix}_link_2_text != blank -%}}
                                            <li><a href="{{{{ child_promo_block.settings.manual{prefix}_link_2_url }}}}" class="tabbed-mega-nav__panel-link">{{{{ child_promo_block.settings.manual{prefix}_link_2_text }}}}</a></li>
                                          {{%- endif -%}}
                                          {{%- if child_promo_block.settings.manual{prefix}_link_3_text != blank -%}}
                                            <li><a href="{{{{ child_promo_block.settings.manual{prefix}_link_3_url }}}}" class="tabbed-mega-nav__panel-link">{{{{ child_promo_block.settings.manual{prefix}_link_3_text }}}}</a></li>
                                          {{%- endif -%}}
                                          {{%- if child_promo_block.settings.manual{prefix}_link_4_text != blank -%}}
                                            <li><a href="{{{{ child_promo_block.settings.manual{prefix}_link_4_url }}}}" class="tabbed-mega-nav__panel-link">{{{{ child_promo_block.settings.manual{prefix}_link_4_text }}}}</a></li>
                                          {{%- endif -%}}
                                          {{%- if child_promo_block.settings.manual{prefix}_link_5_text != blank -%}}
                                            <li><a href="{{{{ child_promo_block.settings.manual{prefix}_link_5_url }}}}" class="tabbed-mega-nav__panel-link">{{{{ child_promo_block.settings.manual{prefix}_link_5_text }}}}</a></li>
                                          {{%- endif -%}}
                                        </ul>
                                      </div>
                                      {{%- endif -%}}
                                    {{%- endif -%}}
"""

html_cols = "".join([generate_html_column(i) for i in range(3, 8)])

# find where column 2 ends
col_2_end = r"""                                          {%- if child_promo_block.settings.manual2_link_5_text != blank -%}
                                            <li><a href="{{ child_promo_block.settings.manual2_link_5_url }}" class="tabbed-mega-nav__panel-link">{{ child_promo_block.settings.manual2_link_5_text }}</a></li>
                                          {%- endif -%}
                                        </ul>
                                      </div>
                                      {%- endif -%}
                                    {%- endif -%}"""

content = content.replace(col_2_end, col_2_end + "\n" + html_cols)


# 3. Add Schema for 3 to 7
def generate_schema(i):
    prefix = "" if i == 1 else str(i)
    return f"""        {{
          "type": "header",
          "content": "Custom Linklist {i}"
        }},
        {{
          "type": "text",
          "id": "custom_title_{i}",
          "label": "Heading"
        }},
        {{
          "type": "link_list",
          "id": "custom_linklist_{i}",
          "label": "Select Menu (Optional)"
        }},
        {{
          "type": "header",
          "content": "OR Add Manual Links {i}"
        }},
        {{
          "type": "text",
          "id": "manual{prefix}_link_1_text",
          "label": "Manual Link 1 Text"
        }},
        {{
          "type": "url",
          "id": "manual{prefix}_link_1_url",
          "label": "Manual Link 1 URL"
        }},
        {{
          "type": "text",
          "id": "manual{prefix}_link_2_text",
          "label": "Manual Link 2 Text"
        }},
        {{
          "type": "url",
          "id": "manual{prefix}_link_2_url",
          "label": "Manual Link 2 URL"
        }},
        {{
          "type": "text",
          "id": "manual{prefix}_link_3_text",
          "label": "Manual Link 3 Text"
        }},
        {{
          "type": "url",
          "id": "manual{prefix}_link_3_url",
          "label": "Manual Link 3 URL"
        }},
        {{
          "type": "text",
          "id": "manual{prefix}_link_4_text",
          "label": "Manual Link 4 Text"
        }},
        {{
          "type": "url",
          "id": "manual{prefix}_link_4_url",
          "label": "Manual Link 4 URL"
        }},
        {{
          "type": "text",
          "id": "manual{prefix}_link_5_text",
          "label": "Manual Link 5 Text"
        }},
        {{
          "type": "url",
          "id": "manual{prefix}_link_5_url",
          "label": "Manual Link 5 URL"
        }},
"""

schema_cols = "".join([generate_schema(i) for i in range(3, 8)])

schema_2_end = r"""        {
          "type": "text",
          "id": "manual2_link_5_text",
          "label": "Manual Link 5 Text"
        },
        {
          "type": "url",
          "id": "manual2_link_5_url",
          "label": "Manual Link 5 URL"
        },"""

content = content.replace(schema_2_end, schema_2_end + "\n" + schema_cols)

with open('sections/header.liquid', 'w') as f:
    f.write(content)

print("Done updating header.liquid")
