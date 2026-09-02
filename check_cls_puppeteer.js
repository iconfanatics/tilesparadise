const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  // Set up performance observer for layout shifts BEFORE navigation
  await page.evaluateOnNewDocument(() => {
    window.layoutShifts = [];
    const observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          const shiftData = {
            value: entry.value,
            sources: entry.sources.map(source => ({
              nodeHTML: source.node ? source.node.outerHTML.slice(0, 150) : null,
              previousRect: source.previousRect,
              currentRect: source.currentRect
            }))
          };
          window.layoutShifts.push(shiftData);
        }
      }
    });
    observer.observe({ type: 'layout-shift', buffered: true });
  });

  // Emulate mobile
  await page.setViewport({ width: 375, height: 812, isMobile: true });

  console.log("Navigating to collection page on mobile...");
  await page.goto('https://tilesparadiseuk.com/collections/tile-sale', { waitUntil: 'networkidle0' });

  // Wait an extra few seconds to ensure all JS/fonts/images are loaded
  await new Promise(resolve => setTimeout(resolve, 5000));

  const shifts = await page.evaluate(() => window.layoutShifts);
  
  let totalCLS = 0;
  shifts.forEach(shift => {
    totalCLS += shift.value;
  });

  console.log(`\nTotal CLS: ${totalCLS.toFixed(4)}\n`);
  
  shifts.forEach((shift, index) => {
    if (shift.value > 0.01) {
      console.log(`Shift ${index + 1} (${shift.value.toFixed(4)}):`);
      shift.sources.forEach(source => {
         console.log(`  - Node: ${source.nodeHTML}`);
         console.log(`    Moved from y=${source.previousRect.y} to y=${source.currentRect.y}`);
      });
    }
  });

  await browser.close();
})();
