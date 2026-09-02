const https = require('https');

https.get('https://tilesparadiseuk.com/cart', (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    // Grep for pickeasy
    const pickeasy = data.match(/pickeasy/ig);
    console.log("PickEasy mentions in HTML:", pickeasy ? pickeasy.length : 0);
    // Print out script tags
    const scripts = data.match(/<script.*?<\/script>/ig) || [];
    console.log("Total scripts:", scripts.length);
  });
}).on('error', (err) => {
  console.log("Error: " + err.message);
});
