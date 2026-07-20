const fs = require('fs');
const file = 'assets/custom.css';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  /\.header__search-bar-wrapper\.is-visible \{\s*margin-bottom: -75px !important;\s*z-index: 99 !important;\s*\/\* Prevent the search bar/s,
  `.header__search-bar-wrapper.is-visible {
    margin-bottom: -75px !important;
    z-index: 99 !important;
  }
  
  /* Prevent the search bar`
);

fs.writeFileSync(file, content);
console.log('Fixed nesting');
