const fs = require('fs');
const file = 'assets/custom.css';
let lines = fs.readFileSync(file, 'utf8').split('\n');

// Add mobile override
const insertIdx = lines.findIndex((l, i) => i > 4060 && l.trim() === '}' && lines[i-1].includes('z-index: 99 !important;'));

if (insertIdx !== -1) {
  lines.splice(insertIdx, 0, `
  /* Prevent the search bar from becoming a full-screen fixed sidebar on focus */
  .header__search-bar-wrapper.is-fixed {
    position: absolute !important;
    height: auto !important;
    max-width: 100% !important;
    margin-left: 0 !important;
  }
  
  .header__search-bar-wrapper.is-fixed .search-bar__inner {
    max-height: 60vh !important;
    overflow-y: auto !important;
    background: #fff !important;
    border: 1px solid #eee;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }`);
} else {
    console.log("Could not find insert index!");
}

// Remove lines 444-446 (0-indexed 443-445)
lines.splice(443, 3);

// Remove lines 392-395 (0-indexed 391-394)
lines.splice(391, 4);

fs.writeFileSync(file, lines.join('\n'));
console.log('Fixed custom.css');
