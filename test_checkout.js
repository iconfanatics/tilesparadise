const puppeteer = require('puppeteer');

(async () => {
    try {
        const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
        const page = await browser.newPage();
        
        page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
        page.on('pageerror', err => console.log('BROWSER ERROR:', err.toString()));

        // Add item to cart
        await page.goto('https://tilesparadiseuk.com/products/hexo-matt-green-hexagon-tiles?variant=46497162690850', { waitUntil: 'networkidle2' });
        
        await page.evaluate(() => {
            document.querySelector('form[action="/cart/add"] button[type="submit"]').click();
        });
        
        await page.waitForTimeout(3000); // wait for ajax cart
        
        // Go to cart
        await page.goto('https://tilesparadiseuk.com/cart', { waitUntil: 'networkidle2' });
        
        // Take screenshot
        await page.screenshot({path: 'cart_screenshot.png', fullPage: true});
        
        // Click checkout button
        await page.evaluate(() => {
            const btn = document.querySelector('button[name="checkout"]');
            if (btn) {
                console.log("Found checkout button. Disabled: " + btn.disabled);
                btn.click();
            } else {
                console.log("Checkout button not found");
            }
        });
        
        await page.waitForTimeout(3000);
        console.log("Final URL after click:", page.url());
        
        await browser.close();
    } catch (e) {
        console.error(e);
        process.exit(1);
    }
})();
