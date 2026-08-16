import urllib.request
import json

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://tilesparadiseuk.com&strategy=mobile"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=30)
    d = json.loads(response.read().decode())
    
    cats = d.get('lighthouseResult', {}).get('categories', {})
    audits = d.get('lighthouseResult', {}).get('audits', {})
    
    score = int(cats.get('performance', {}).get('score', 0) * 100)
    lcp = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
    tbt = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
    cls = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')
    fcp = audits.get('first-contentful-paint', {}).get('displayValue', 'N/A')
    speed_index = audits.get('speed-index', {}).get('displayValue', 'N/A')
    
    print(f"Mobile Score: {score}")
    print(f"FCP: {fcp}")
    print(f"LCP: {lcp}")
    print(f"TBT: {tbt}")
    print(f"CLS: {cls}")
    print(f"Speed Index: {speed_index}")
    
    # Top opportunities
    print("\nTop Opportunities:")
    opportunities = d.get('lighthouseResult', {}).get('categories', {}).get('performance', {}).get('auditRefs', [])
    for ref in opportunities:
        if ref.get('weight', 0) > 0:
            audit = audits.get(ref['id'], {})
            if audit.get('score') is not None and audit.get('score') < 0.9:
                title = audit.get('title', '')
                display = audit.get('displayValue', '')
                print(f"  - {title}: {display}")

except Exception as e:
    print(f"Error: {e}")
