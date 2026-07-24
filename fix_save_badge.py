import re

def fix_css():
    filename = 'assets/custom.css'
    with open(filename, 'r') as f:
        content = f.read()

    # Find the CSS rule and comment it out or remove the giant dimensions
    # Specifically looking for .product-item .product-item__label-list span.product-label.product-label--on-sale
    
    # Let's replace the width:70px;height:70px with auto
    content = re.sub(r'width:70px;height:70px;', 'width:auto;height:auto;padding:3px 8px;', content)
    
    # Let's hide the paragraph tag inside it if it exists
    content = re.sub(r'\.product-item \.product-item__label-list span\.product-label\.product-label--on-sale p\{font-size:20px;line-height:24px\}', '.product-item .product-item__label-list span.product-label.product-label--on-sale p{font-size:14px;line-height:18px}', content)
    
    # Remove the after pseudo element that creates the border
    content = re.sub(r'\.product-item \.product-item__label-list span\.product-label\.product-label--on-sale:after\{[^\}]+\}', '.product-item .product-item__label-list span.product-label.product-label--on-sale:after{display:none;}', content)
    
    with open(filename, 'w') as f:
        f.write(content)
        
    print("Fixed save badge CSS in", filename)

fix_css()
