# Project Work Log

This file tracks all the major tasks and changes made to the theme, along with their corresponding Git commit IDs.

## Recent Tasks (Today)

### 1. Conditional Metafield Accordions & Jump Links
- **Description:** Updated the product accordions (`sections/product-accordions.liquid`) and gallery jump links (`snippets/product-gallery.liquid`). The `custom.dimensions` and `custom.instructions_pdf` accordions will now only render if they actually contain data. If the metafields are empty, the accordions and their jump links automatically hide.
- **Commit ID:** `95ae83f`

### 2. Popup CSS Overlap Fixes
- **Description:** Fixed an issue where the sticky header was overlapping third-party popups (like Klaviyo/Omnisend). Lowered the header's `z-index` to 99 and forced generic popup containers to maximum `z-index`. (Note: Attempted to add a cross button and resize the popup via CSS, but reverted it as it broke the third-party app's internal layout).
- **Commit IDs:** `8ec4858`, `1f64254`, `55e778d` (Reverted experimental CSS)

## Previous Metafield & Template Tasks

### 3. Shower and Toilets Templates
- **Description:** Duplicated the `radiator-v3` template to create new custom templates for `product.shower.json` and `product.toilets.json`. Hid the "FREE STANDARD DELIVERY" text specifically on these templates.
- **Commit IDs:** `4eebb23`, `bb2010e`

### 4. Radiator V3 Swatch Redesign & Metafields
- **Description:** Heavily modified the radiator swatches to perfectly match the `mirrors-v2` design. Fixed liquid syntax errors and resolved a bug where the size swatches weren't properly fetching the `custom.size_name` metafield fallback. 
- **Commit IDs:** `8fc57b4`, `0485175`, `483fc07`, `2af4acc`, `cf6a4e8`

### 5. Metafield Implementations (General)
- **Description:** Integrated `custom.brand_logo` for brand imagery, and built the foundation for `custom.dimensions` (List of Images) and `custom.instructions_pdf` (List of Files) to properly render in loops within the custom product accordions.
