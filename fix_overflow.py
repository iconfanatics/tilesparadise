def fix_css():
    filename = 'assets/custom.css'
    with open(filename, 'r') as f:
        content = f.read()

    css_append = """
/* Fix mobile layout overflow for product form buttons and samples */
@media screen and (max-width: 991px) {
  .product-form__payment-container,
  .tp-samples,
  .tp-sample-btn,
  .finance-delivery-card,
  .card__section .btn_conts {
    box-sizing: border-box !important;
    max-width: 100% !important;
  }
  
  /* Ensure padding doesn't cause overflow on width 100% */
  .tp-sample-btn {
    width: 100% !important;
  }
}
"""
    
    if "Fix mobile layout overflow for product form buttons and samples" not in content:
        with open(filename, 'a') as f:
            f.write(css_append)
        print("Fixed mobile layout overflow CSS in", filename)
    else:
        print("Mobile layout overflow CSS already fixed in", filename)

fix_css()
