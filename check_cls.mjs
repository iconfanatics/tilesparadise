import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  await page.evaluateOnNewDocument(() => {
    window.layoutShifts = [];
    const observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          const shiftData = {
            value: entry.value,
            sources: entry.sources.map(source => ({
              nodeHTML: source.node ? (source.node.outerHTML ? source.node.outerHTML.slice(0, 150) : 'TextNode') : null,
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

  await page.setViewport({ width: 375, height: 812, isMobile: true });

  const urls = [
      'https://tilesparadiseuk.com/collections/bathroom-brown-tiles',
      'https://tilesparadiseuk.com/products/aquari-brushed-gold-thermostatic-concealed-shower-mixer-set-3-way-wall-mounted-valve-with-square-heads'
  ];

  for (const url of urls) {
      console.log(`\nNavigating to ${url}...`);
      await page.goto(url, { waitUntil: 'networkidle2' });
      await new Promise(resolve => setTimeout(resolve, 3000));
      const shifts = await page.evaluate(() => window.layoutShifts);
      
      let totalCLS = 0;
      shifts.forEach(shift => totalCLS += shift.value);

      console.log(`Total CLS for ${url}: ${totalCLS.toFixed(4)}`);
      
      shifts.forEach((shift, index) => {
        if (shift.value > 0.01) {
          console.log(`Shift ${index + 1} (${shift.value.toFixed(4)}):`);
          shift.sources.forEach(source => {
             console.log(`  - Node: ${source.nodeHTML}`);
             if(source.previousRect) console.log(`    Moved from y=${source.previousRect.y} to y=${source.currentRect.y}`);
          });
        }
      });
      // reset for next page
      await page.evaluate(() => { window.layoutShifts = []; });
  }

  await browser.close();
})();
