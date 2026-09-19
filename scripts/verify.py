import json, sys, os
from playwright.sync_api import sync_playwright

BASE = "http://localhost:12000"
pages = ["/", "/work/", "/about/", "/contact/"]
root = "/workspace/project/work"
for d in sorted(os.listdir(os.path.join(root))):
    if os.path.isdir(os.path.join(root, d)) and d not in ("__pycache__",):
        pages.append(f"/work/{d}/")

report = []
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width": 1440, "height": 900},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")
    pg = ctx.new_page()
    errors = []
    pg.on("console", lambda m: errors.append(f"{m.type}: {m.text}") if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    failed = []
    pg.on("requestfailed", lambda r: failed.append(r.url))
    pg.on("response", lambda r: failed.append(f"{r.status} {r.url}") if r.status >= 400 else None)

    for path in pages:
        errors.clear(); failed.clear()
        pg.goto(BASE + path, wait_until="load")
        pg.wait_for_timeout(400)
        # Force every lazy image to load, then wait until all settle.
        pg.evaluate("""() => {
            document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager');
        }""")
        pg.evaluate("""async () => {
            const h = document.body.scrollHeight;
            for (let y = 0; y < h; y += 700) { window.scrollTo(0, y); await new Promise(r=>setTimeout(r,60)); }
            window.scrollTo(0, 0);
        }""")
        # block until all images are complete (or 15s)
        try:
            pg.wait_for_function(
                "() => [...document.images].filter(i=>!i.closest('.lightbox')).every(i=>i.complete)",
                timeout=15000)
        except Exception:
            pass
        pg.wait_for_timeout(400)
        info = pg.evaluate("""() => {
            const imgs = [...document.images].filter(i => !i.closest('.lightbox'));
            const broken = imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src'));
            const noalt = imgs.filter(i => !i.hasAttribute('alt')).length;
            // horizontal overflow check
            const de = document.documentElement;
            const overflow = de.scrollWidth - de.clientWidth;
            // elements sticking out (ignore intentionally-wide marquee tracks)
            let widest = 0, culprit = '';
            document.querySelectorAll('body *').forEach(el => {
                if (el.closest('.marquee')) return;
                const r = el.getBoundingClientRect();
                if (r.right > de.clientWidth + 2) {
                    if (r.right > widest) { widest = r.right; culprit = el.tagName + '.' + (el.className||'').toString().slice(0,50); }
                }
            });
            return {
                title: document.title,
                nImages: imgs.length,
                broken,
                noalt,
                overflow,
                widest: Math.round(widest),
                culprit,
                h1: (document.querySelector('h1')||{}).textContent?.trim().slice(0,60) || '',
                reveals: document.querySelectorAll('[data-reveal]').length,
                revealsHidden: [...document.querySelectorAll('[data-reveal]')].filter(e=>!e.classList.contains('is-in')).length,
                imgsLoaded: imgs.filter(i=>i.naturalWidth>0).length,
            };
        }""")
        info["path"] = path
        info["consoleErrors"] = errors[:5]
        info["failedReqs"] = [f for f in failed if "favicon" not in f][:6]
        report.append(info)
        flag = "OK " if not (info["broken"] or info["overflow"] > 1 or info["consoleErrors"] or info["failedReqs"]) else "!! "
        print(f"{flag}{path:28s} imgs={info['imgsLoaded']}/{info['nImages']} broken={len(info['broken'])} overflow={info['overflow']} err={len(info['consoleErrors'])} failed={len(info['failedReqs'])}")
        for bx in info["broken"][:4]: print("      broken:", bx)
        for fx in info["failedReqs"][:4]: print("      failed:", fx)
        for ex in info["consoleErrors"][:3]: print("      console:", ex)
        if info["culprit"]: print("      culprit:", info["culprit"], info["widest"])
    b.close()
json.dump(report, open("/tmp/verify.json","w"), indent=1)