const fs = require('fs');
const file = 'assets/custom.css';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  'button.search-bar__submit {\n    background: #000 !important;\n    border-radius: 0px 10px 10px 0px;\n}',
  `button.search-bar__submit {
    background: #000 !important;
    border-radius: 0px 10px 10px 0px;
    flex-shrink: 0 !important;
    min-width: 45px !important;
}`
);

fs.writeFileSync(file, content);
console.log('Fixed button CSS');
