import json
from playwright.sync_api import sync_playwright

BASE = "http://localhost:12000"
CHECK = ["/", "/work/", "/about/", "/contact/", "/work/smartwalker/", "/work/loom/",
         "/work/portfolio-deck/", "/work/sketchbook/"]

AUDIT = """() => {
  const out = {issues: []};
  const de = document.documentElement;

  // 1. fonts actually applied
  const h1 = document.querySelector('h1.display');
  if (h1) {
    const cs = getComputedStyle(h1);
    out.h1font = cs.fontFamily;
    out.h1size = cs.fontSize;
    out.h1weight = cs.fontWeight;
  }
  const body = getComputedStyle(document.body);
  out.bodyfont = body.fontFamily;

  // 2. font files loaded?
  out.fonts = [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+':'+f.weight).slice(0,8);

  // 3. nav overlap with content
  const nav = document.querySelector('.nav');
  if (nav) {
    const r = nav.getBoundingClientRect();
    out.navH = Math.round(r.height);
    out.navPos = getComputedStyle(nav).position;
  }

  // 4. any element whose text overflows its own box horizontally
  let clipped = 0;
  document.querySelectorAll('h1,h2,h3,p,li,span,a,dt,dd').forEach(el=>{
    if (el.scrollWidth > el.clientWidth + 3 && el.clientWidth > 0) {
      const cs = getComputedStyle(el);
      if (cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis') {
        clipped++; out.issues.push('clipped text: ' + el.tagName + ' "' + el.textContent.trim().slice(0,40) + '"');
      }
    }
  });

  // 5. images with object-fit cover should fill container
  const cardImgs = [...document.querySelectorAll('.card__media img')];
  out.cardImgs = cardImgs.length;
  out.badCards = cardImgs.filter(i=>{
    const r = i.getBoundingClientRect();
    return r.height < 40 || r.width < 40;
  }).length;

  // 6. gallery images with zero displayed size (lazy not triggered)
  const gal = [...document.querySelectorAll('.gallery img, .archive img, .case-cover img')];
  out.galImgs = gal.length;
  out.galZero = gal.filter(i=>{const r=i.getBoundingClientRect(); return r.width<10;}).length;

  // 7. contrast sample: bone on ink
  out.bg = body.backgroundColor;
  out.fg = body.color;

  // 8. tap target sizes (mobile-ish)
  const small = [];
  document.querySelectorAll('a,button').forEach(el=>{
    const r = el.getBoundingClientRect();
    if (r.width>0 && r.height>0 && (r.height<32) && el.closest('.footer__li, .nav__link, .chip')) {
      small.push(el.textContent.trim().slice(0,24));
    }
  });
  out.smallTargets = [...new Set(small)].slice(0,8);

  // 9. section count / page height
  out.height = document.body.scrollHeight;

  // 10. images w/ alt text missing
  out.noalt = [...document.images].filter(i=>!i.closest('.lightbox')).filter(i=>!i.alt).length;

  return out;
}"""

with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_context(viewport={"width": 1440, "height": 900}).new_page()
    for path in CHECK:
        pg.goto(BASE + path, wait_until="load")
        pg.evaluate("async ()=>{const h=document.body.scrollHeight;for(let i=0;i<h;i+=600){window.scrollTo(0,i);await new Promise(r=>setTimeout(r,50));}window.scrollTo(0,0);}")
        pg.wait_for_timeout(900)
        r = pg.evaluate(AUDIT)
        print("=" * 70)
        print(path)
        print("  h1:", r.get("h1font"), r.get("h1size"), "w" + str(r.get("h1weight")))
        print("  body font:", r.get("bodyfont"))
        print("  fonts loaded:", r.get("fonts"))
        print("  nav:", r.get("navPos"), r.get("navH"), "px")
        print("  cards:", r.get("cardImgs"), "bad:", r.get("badCards"),
              "| gallery:", r.get("galImgs"), "zero:", r.get("galZero"))
        print("  height:", r.get("height"), "| noalt:", r.get("noalt"))
        print("  issues:", r["issues"][:4])
        print("  small targets:", r.get("smallTargets"))
    b.close()