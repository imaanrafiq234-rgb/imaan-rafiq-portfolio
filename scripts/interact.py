from playwright.sync_api import sync_playwright

BASE = "http://localhost:12000"
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_context(viewport={"width": 1440, "height": 900}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:" + m.text) if m.type == "error" else None)

    # ---- Filters ----
    pg.goto(BASE + "/work/", wait_until="load")
    pg.wait_for_timeout(600)
    def visible_cards():
        return pg.evaluate("()=>[...document.querySelectorAll('[data-tags]')].filter(c=>!c.hidden).map(c=>c.dataset.tags.split(' ')[0])")
    total = pg.evaluate("()=>document.querySelectorAll('[data-tags]').length")
    print("total cards:", total, "initially visible:", len(visible_cards()))
    for key in ["ux", "sketch", "hardware", "product", "engineering", "all"]:
        pg.click(f'.chip[data-filter="{key}"]')
        pg.wait_for_timeout(350)
        vis = visible_cards()
        pressed = pg.evaluate("()=>document.querySelector('.chip[aria-pressed=\"true\"]').dataset.filter")
        print(f"  filter={key:12s} visible={len(vis):2d} pressed={pressed} hash={pg.evaluate('()=>location.hash')}")

    # ---- Lightbox ----
    pg.goto(BASE + "/work/smartwalker/", wait_until="load")
    pg.wait_for_timeout(800)
    shots = pg.evaluate("()=>document.querySelectorAll('[data-lightbox]').length")
    print("lightbox shots:", shots)
    pg.evaluate("()=>document.querySelectorAll('[data-lightbox]')[2].scrollIntoView({block:'center'})")
    pg.wait_for_timeout(400)
    pg.click("[data-lightbox] >> nth=2")
    pg.wait_for_timeout(500)
    st = pg.evaluate("()=>({open:document.querySelector('.lightbox').dataset.open, src:document.querySelector('.lightbox img').getAttribute('src'), count:document.querySelector('.lightbox__count').textContent, hidden:document.querySelector('.lightbox').getAttribute('aria-hidden')})")
    print("after open:", st)
    pg.click(".lightbox__next"); pg.wait_for_timeout(300)
    print("after next:", pg.evaluate("()=>document.querySelector('.lightbox__count').textContent"))
    pg.keyboard.press("ArrowLeft"); pg.wait_for_timeout(300)
    print("after left:", pg.evaluate("()=>document.querySelector('.lightbox__count').textContent"))
    pg.keyboard.press("Escape"); pg.wait_for_timeout(400)
    print("after esc:", pg.evaluate("()=>({open:document.querySelector('.lightbox').dataset.open, bodyOverflow:document.body.style.overflow})"))
    # click backdrop
    pg.click("[data-lightbox] >> nth=0"); pg.wait_for_timeout(400)
    pg.mouse.click(20, 450); pg.wait_for_timeout(400)
    print("backdrop close:", pg.evaluate("()=>document.querySelector('.lightbox').dataset.open"))

    # ---- Mobile nav ----
    m = b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True).new_page()
    m.goto(BASE + "/", wait_until="load")
    m.wait_for_timeout(600)
    print("menu before:", m.evaluate("()=>getComputedStyle(document.querySelector('.nav__links')).transform"))
    m.click(".nav__toggle"); m.wait_for_timeout(800)
    print("menu after :", m.evaluate("()=>getComputedStyle(document.querySelector('.nav__links')).transform"))
    m.click(".nav__link >> nth=1"); m.wait_for_timeout(600)
    print("after nav click url:", m.url, "toggle:", m.inner_text(".nav__toggle"))

    # ---- reveal animation actually fired ----
    m.goto(BASE + "/work/smartwalker/", wait_until="load")
    m.evaluate("async()=>{const h=document.body.scrollHeight;for(let i=0;i<h;i+=400){window.scrollTo(0,i);await new Promise(r=>setTimeout(r,40));}}")
    m.wait_for_timeout(700)
    print("reveals hidden after scroll:", m.evaluate("()=>[...document.querySelectorAll('[data-reveal]')].filter(e=>!e.classList.contains('is-in')).length"), "of", m.evaluate("()=>document.querySelectorAll('[data-reveal]').length"))

    print("JS errors:", errs[:8] if errs else "none")
    b.close()