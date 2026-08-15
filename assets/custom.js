document.addEventListener('click', function(e) {
  const btn = e.target.closest('.custom-tab-btn');
  if (!btn) return;
  
  const section = btn.closest('.custom-tabs-section');
  if (!section) return;
  
  const index = btn.getAttribute('data-index');
  
  const btns = section.querySelectorAll('.custom-tab-btn');
  const contents = section.querySelectorAll('.custom-tab-content');
  
  btns.forEach(b => b.classList.remove('active'));
  contents.forEach(c => c.classList.remove('active'));
  
  btn.classList.add('active');
  const targetContent = section.querySelector(`.custom-tab-content[data-index="${index}"]`);
  if(targetContent) {
    targetContent.classList.add('active');
  }
});


/* Moved from theme.liquid */

document.addEventListener("DOMContentLoaded", function () {
  const addToCartBtns = document.querySelectorAll('.cst_add, .metafield_button');
  
  addToCartBtns.forEach(function(btn) {
    btn.addEventListener('click', function (event) {
      event.preventDefault(); // prevent default form submit

      const form = btn.closest('form');
      if (!form) return;
      
      const formData = new FormData(form);

      // Add to cart via AJAX
      fetch('/cart/add.js', {
        method: 'POST',
        body: formData,
      })
      .then(response => {
        if (response.ok) {
          // Dispatch event to update theme cart
          document.documentElement.dispatchEvent(new CustomEvent('cart:refresh', { bubbles: true }));
          
          if (window.theme.cartType === 'message') {
            var btnOriginalText = btn.innerHTML;
            btn.innerHTML = window.languages.productAddedShort || 'Added to cart';
            setTimeout(function() {
              btn.innerHTML = btnOriginalText;
            }, 2000);
          } else if (window.theme.cartType === 'page') {
            window.location.href = '/cart';
          } else {
            // Open the mini-cart drawer by clicking the cart icon
            var cartIcon = document.querySelector('.header__cart-toggle');
            if(cartIcon && cartIcon.hasAttribute('data-action')) {
              cartIcon.click();
            } else {
              // Fallback if the theme's drawer doesn't open via click
              var miniCart = document.getElementById('mini-cart');
              if(miniCart) miniCart.setAttribute('aria-hidden', 'false');
            }
          }
        } else {
          return response.json().then(err => {
            console.error("Add to cart failed:", err);
            alert(err.description || 'Could not add to cart');
          });
        }
      })
      .catch(err => {
        console.error("Add to cart error:", err);
        alert('Error adding to cart');
      });
    });
  });
});

window.addEventListener('scroll', function() {
  var navBar = document.querySelector('.nav-bar');
  if(navBar) {
    if(window.scrollY >= 200) navBar.classList.add('scroll_menu');
    else navBar.classList.remove('scroll_menu');
  }
});

document.addEventListener('DOMContentLoaded', function () {
    var content = document.querySelector('.article__content');
    var toc = document.getElementById('article-toc');
    var tocList = document.getElementById('article-toc-list');

    if (!content || !toc || !tocList) return;

    // Only include H2 headings in the TOC
    var headings = content.querySelectorAll('h2');

    if (!headings.length) {
      toc.style.display = 'none'; // Hide TOC if no headings found
      return;
    }

    headings.forEach(function (heading, index) {
      // Create a slug/id for the heading if it doesn't have one
      if (!heading.id) {
        var slug = heading.textContent
          .toLowerCase()
          .trim()
          .replace(/[^a-z0-9\s]/g, '')
          .replace(/\s+/g, '-');
        heading.id = slug || ('section-' + (index + 1));
      }

      var li = document.createElement('li');
      var a = document.createElement('a');

      a.href = '#' + heading.id;
      a.textContent = heading.textContent;

      li.appendChild(a);
      tocList.appendChild(li);
    });
  });

document.addEventListener('click', function(e) {

  if (e.target.classList.contains('tab-btn')) {
    const parent = e.target.closest('.product-specs-block');
    parent.querySelectorAll('.tab-btn, .tab-content').forEach(el => el.classList.remove('active'));
    e.target.classList.add('active');
    parent.querySelector('#' + e.target.dataset.tab).classList.add('active');
  }

  if (e.target.closest('.accordion-header')) {
    const accordion = e.target.closest('.accordion');
    accordion.classList.toggle('active');
  }

});
document.addEventListener("DOMContentLoaded", function () {

  const row = document.querySelector(".delivery-row");
  const estimator = document.querySelector(".estimator-message--manual");

  if (!row || !estimator) return;

  setTimeout(function(){
    if(estimator.innerText.trim() === ""){
      row.style.display = "none";
    }
  }, 1000);

});

document.addEventListener('DOMContentLoaded', function () {

  const filterToggle = document.querySelector('.mobile-filter-toggle');
  const filters = document.querySelector('.filters');

  if (filterToggle) {

    filterToggle.addEventListener('click', function (e) {

      // Prevent toggle when clicking clear all
      if (e.target.closest('.clear-filters-mobile')) {
        return;
      }

      filters.classList.toggle('active');

    });

  }

});

document.addEventListener("DOMContentLoaded", function () {

  document.addEventListener("click", async function (e) {

    const button = e.target.closest(
      '[data-action="increase-quantity"], [data-action="decrease-quantity"]'
    );

    if (!button) return;

    e.preventDefault();

    const line = button.dataset.line;

    let quantity = parseInt(button.dataset.quantity);

    if (!line || isNaN(quantity)) return;

    try {

      const response = await fetch('/cart/change.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          line: line,
          quantity: quantity
        })
      });

      if (!response.ok) {
        throw new Error('Cart update failed');
      }

      location.reload();

    } catch (error) {

      console.error('Cart quantity error:', error);

    }

  });

});


document.addEventListener('DOMContentLoaded', function() {

  function fixCheckoutButton() {

    const btn = document.querySelector('.custom-checkout-btn-selector');

    if (!btn) return;

    // remove disabled
    btn.removeAttribute('disabled');
    btn.disabled = false;

    // remove surrounding shipping-policy anchor
    const parentLink = btn.closest('a[href*="shipping-policy"]');

    if (parentLink) {
      parentLink.parentNode.insertBefore(btn, parentLink);
      parentLink.remove();
    }

    console.log('Checkout button fixed');
  }

  fixCheckoutButton();

  document.addEventListener('cart:refresh', fixCheckoutButton);
});
