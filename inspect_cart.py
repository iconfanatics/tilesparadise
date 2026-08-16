import urllib.request
import urllib.parse
from http.cookiejar import CookieJar
import json
import re

# 1. Fetch a product to get a variant ID
url = "https://tilesparadiseuk.com/products.json?limit=1"
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = opener.open(req)
    products = json.loads(response.read().decode())
    variant_id = products['products'][0]['variants'][0]['id']
    print(f"Got variant ID: {variant_id}")

    # 2. Add to cart
    add_url = "https://tilesparadiseuk.com/cart/add.js"
    data = urllib.parse.urlencode({'id': variant_id, 'quantity': 1}).encode('utf-8')
    req = urllib.request.Request(add_url, data=data, headers={
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    })
    opener.open(req)
    print("Added to cart.")

    # 3. Fetch cart page
    cart_url = "https://tilesparadiseuk.com/cart"
    req = urllib.request.Request(cart_url, headers={'User-Agent': 'Mozilla/5.0'})
    cart_html = opener.open(req).read().decode('utf-8')

    # 4. Extract checkout button HTML
    # Looking for name="checkout" or id="checkout"
    checkout_btn = re.search(r'<button[^>]*name="checkout"[^>]*>.*?</button>', cart_html, re.IGNORECASE | re.DOTALL)
    if checkout_btn:
        print("\nCheckout Button HTML found:")
        print(checkout_btn.group(0))
    else:
        print("\nCheckout button not found with name='checkout'. Searching generic buttons...")
        generic_btns = re.findall(r'<button[^>]*>.*?</button>', cart_html, re.IGNORECASE | re.DOTALL)
        for b in generic_btns:
            if 'checkout' in b.lower():
                print(b)
                
    # 5. Extract form
    cart_form = re.search(r'<form[^>]*action="/cart"[^>]*>.*?</form>', cart_html, re.IGNORECASE | re.DOTALL)
    if cart_form:
        form_tag = re.search(r'<form[^>]*>', cart_form.group(0), re.IGNORECASE).group(0)
        print(f"\nCart Form Tag: {form_tag}")
        
    # 6. Look for app scripts intercepting checkout
    print("\nScripts containing 'checkout':")
    scripts = re.findall(r'<script[^>]*>.*?</script>', cart_html, re.IGNORECASE | re.DOTALL)
    for s in scripts:
        if 'checkout' in s.lower() and 'name="checkout"' not in s:
            # truncate for readability
            if len(s) < 500:
                print(s)
            else:
                print(s[:100] + " ... " + s[-100:])

except Exception as e:
    print(f"Error: {e}")
