import re

def fix_css():
    filename = 'assets/custom.css'
    with open(filename, 'r') as f:
        content = f.read()

    # The mobile badge might be styled via another block in custom.css
    # Search for product-item__label-list span.product-label.product-label--on-sale and any mobile query overrides
    
    # Let's just append an override to the very bottom to ensure mobile badge is small
    
    css_append = """
/* Fix for mobile save badge */
@media screen and (max-width: 767px) {
  .product-item .product-item__label-list span.product-label.product-label--on-sale,
  .product-block-list__item--gallery .product-item__label-list span.product-label.product-label--on-sale,
  .product-block-list__item--gallery .product-item__label-list span {
    width: auto !important;
    height: auto !important;
    padding: 3px 8px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 11px !important;
    font-weight: 800 !important;
  }
  
  .product-item .product-item__label-list span.product-label.product-label--on-sale p,
  .product-block-list__item--gallery .product-item__label-list span.product-label.product-label--on-sale p,
  .product-block-list__item--gallery .product-item__label-list span p {
    font-size: 11px !important;
    line-height: normal !important;
    margin: 0 !important;
    display: inline !important;
  }
  
  .product-item .product-item__label-list span.product-label.product-label--on-sale:after,
  .product-block-list__item--gallery .product-item__label-list span.product-label.product-label--on-sale:after,
  .product-block-list__item--gallery .product-item__label-list span:after {
    display: none !important;
  }
  
  .product-item__label-list {
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 9;
  }
}
"""
    
    if "Fix for mobile save badge" not in content:
        with open(filename, 'a') as f:
            f.write(css_append)
        print("Fixed mobile save badge CSS in", filename)
    else:
        print("Mobile save badge CSS already fixed in", filename)

fix_css()
