import json

with open('templates/product.tiles.json', 'r') as f:
    data = json.load(f)

# The proper liquid content
liquid_content = """{%- comment -%}
  Liquid block (no title needed; set Display mode "Show all").
  Banner linking to your standalone /pages/tile-calculator.
{%- endcomment -%}
<div class="tp-calcb">
  <div class="tp-calcb__txt">
    <h3>Doing a whole room?</h3>
    <p>Use our free Tile Calculator &mdash; enter your wall and floor measurements, deduct doors and windows, and we'll work out exactly how many boxes you need, plus 10% for wastage.</p>
  </div>
  <a class="tp-calcb__btn" href="/pages/tile-calculator">Open the Tile Calculator &rarr;</a>
</div>
<style>
  .tp-calcb{display:flex;align-items:center;justify-content:space-between;gap:22px;flex-wrap:wrap;
    background:linear-gradient(120deg,#1a1d24,#2a3340);color:#fff;border-radius:14px;padding:24px 26px;
    text-decoration:none;font-family:"Open Sans",sans-serif;}
  .tp-calcb__txt h3{font-size:18px;font-weight:800;margin:0;color:#fff;}
  .tp-calcb__txt p{font-size:13px;opacity:.85;margin:5px 0 0;max-width:560px;line-height:1.5;color:#fff;}
  a.tp-calcb__btn{background:#fff;color:#1a1d24;font-weight:800;font-size:14px;padding:13px 22px;border-radius:10px;white-space:nowrap;
    text-decoration:none !important; box-shadow:none !important; border:none !important; outline:none !important; background-image:none !important;}
  .tp-calcb:hover a.tp-calcb__btn{background:#c8102e;color:#fff;}
</style>"""

data['sections']['main']['blocks']['calculator_block']['settings']['liquid'] = liquid_content

with open('templates/product.tiles.json', 'w') as f:
    json.dump(data, f, indent=2)

