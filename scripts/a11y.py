from playwright.sync_api import sync_playwright

BASE = "http://localhost:12000"
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])

    # ---- no-JS fallback: content must be visible ----
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
    pg = ctx.new_page()
    pg.goto(BASE + "/work/smartwalker/", wait_until="load")
    pg.wait_for_timeout(500)
    r = pg.evaluate("""()=>{
      const els=[...document.querySelectorAll('[data-reveal]')];
      const hidden=els.filter(e=>getComputedStyle(e).opacity==='0').length;
      return {total:els.length, hidden,
              h1op:getComputedStyle(document.querySelector('h1')).opacity,
              visibleText:document.body.innerText.length};
    }""")
    print("NO-JS:", r)
    ctx.close()

    # ---- 404 ----
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    pg = ctx.new_page()
    pg.goto(BASE + "/404.html", wait_until="load")
    pg.wait_for_timeout(500)
    print("404 title:", pg.title(), "| h1:", pg.inner_text("h1").replace("\n", " "))
    print("404 header status:", pg.evaluate("()=>document.querySelector('h1')? 'rendered':'missing'"))
    ctx.close()

    # ---- keyboard accessibility on filters ----
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    pg = ctx.new_page()
    pg.goto(BASE + "/work/", wait_until="load")
    pg.wait_for_timeout(400)
    pg.keyboard.press("Tab")
    seq = []
    for _ in range(6):
        el = pg.evaluate("()=>{const a=document.activeElement;return a.tagName+':'+(a.textContent||'').trim().slice(0,20)}")
        seq.append(el)
        pg.keyboard.press("Tab")
    print("tab order:", seq)
    # activate a chip via keyboard
    pg.focus('.chip[data-filter="ux"]')
    pg.keyboard.press("Enter")
    pg.wait_for_timeout(400)
    print("kb filter ux visible:", pg.evaluate("()=>[...document.querySelectorAll('[data-tags]')].filter(c=>!c.hidden).length"))
    ctx.close()
    b.close()