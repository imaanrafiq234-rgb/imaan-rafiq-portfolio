# -*- coding: utf-8 -*-
"""Static site generator for the Imaan Rafiq design portfolio."""
import os, re, shutil, html as H
from content import PROJECTS, TAGS, SITE, HERO_IMAGE

NUM_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one",
             "twenty-two", "twenty-three", "twenty-four"]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "assets/img"

def e(t):
    return H.escape(str(t), quote=True)

def depth_prefix(depth):
    return "../" * depth

# ---------------------------------------------------------------- components
def nav(depth=0, active=""):
    p = depth_prefix(depth)
    items = [("index.html", "Work"), ("work/index.html", "Archive"),
             ("about/index.html", "Studio"), ("contact/index.html", "Contact")]
    links = "".join(
        f'<a class="nav__link" href="{p}{href}"'
        + (' aria-current="page"' if active == href.split("/")[0] or active == href else "")
        + f'>{label}</a>' for href, label in items)
    return f'''<div class="progress" aria-hidden="true"></div>
<header class="nav">
  <a class="nav__logo" href="{p}index.html">Imaan Rafiq<span>&trade;</span></a>
  <nav class="nav__links" id="menu" data-open="false" aria-label="Primary">{links}</nav>
  <button class="nav__toggle" aria-expanded="false" aria-controls="menu" type="button">Menu</button>
</header>'''

def head(title, desc, depth=0, extra=""):
    p = depth_prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0c0c0d">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{p}{IMG}/smartwalker/00.jpg">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" as="font" type="font/woff2" href="{p}assets/fonts/Inter-normal-300_800-latin.woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/css/style.css">
<script>document.documentElement.classList.add('js');</script>
{extra}
</head>
<body>'''

FOOT = '''<footer class="footer">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Let&rsquo;s work together</p>
    <h2 class="display footer__cta mt-1" data-reveal>
      Designing things that <em>actually</em> work.<br>
      <a href="{p}contact/index.html" class="serif" style="font-size:0.62em">Start a conversation &rarr;</a>
    </h2>
    <div class="footer__cols">
      <div data-reveal>
        <p class="footer__h">Contact</p>
        <a class="footer__li" href="mailto:{email}">{email}</a>
        <a class="footer__li" href="tel:{phone_href}">{phone}</a>
        <span class="footer__li">{location}</span>
      </div>
      <div data-reveal>
        <p class="footer__h">Elsewhere</p>
        <a class="footer__li" href="{linkedin}" target="_blank" rel="noopener">LinkedIn &nearr;</a>
        <a class="footer__li" href="{p}work/index.html">Work archive</a>
        <a class="footer__li" href="{p}about/index.html">Studio</a>
      </div>
      <div data-reveal>
        <p class="footer__h">Focus</p>
        <span class="footer__li">Product &amp; industrial design</span>
        <span class="footer__li">Design engineering</span>
        <span class="footer__li">CAD &amp; prototyping</span>
      </div>
      <div data-reveal>
        <p class="footer__h">Availability</p>
        <span class="footer__li">Open to graduate roles</span>
        <span class="footer__li">Product design &middot; Medtech &middot; Manufacturing</span>
      </div>
    </div>
    <div class="footer__base">
      <span>&copy; <span data-year>2026</span> Imaan Rafiq. All work shown is the designer&rsquo;s own.</span>
      <span>BSc Product Design &amp; Technology &middot; Aston University</span>
    </div>
  </div>
</footer>
<script src="{p}assets/js/main.js" defer></script>
</body>
</html>'''

def footer(depth=0):
    return FOOT.format(p=depth_prefix(depth), email=e(SITE["email"]),
                       phone_href=e(SITE["phone"]), phone=e(SITE["phone"]),
                       location=e(SITE["location"]), linkedin=e(SITE["linkedin"]))

def card(pr, depth=0, size="", delay=0):
    p = depth_prefix(depth)
    cls = "card" + (f" card--{size}" if size else "")
    badge = (f'<span class="card__badge card__badge--award">{e(pr["award"])}</span>'
             if pr.get("award") else
             f'<span class="card__badge">{e(pr["category"])}</span>')
    first = pr["gallery"][0][0] if pr["gallery"] else pr["cover"]
    return f'''<a class="{cls}" href="{p}work/{pr['slug']}/index.html" data-tags="{e(pr['tags'])}" data-reveal style="--d:{delay}ms">
  <figure class="card__media">
    {badge}
    <img src="{p}{IMG}/{e(pr['cover'])}" alt="{e(pr['title'])} — {e(pr['subtitle'])}" loading="lazy" decoding="async">
  </figure>
  <div class="card__body">
    <h3 class="card__title">{e(pr['title'])}</h3>
    <span class="card__sub">{e(pr['year'])} &middot; {e(pr['subtitle'])}</span>
  </div>
  <p class="card__desc">{e(pr['summary'])}</p>
</a>'''

def gallery_html(pr, depth=0):
    p = depth_prefix(depth)
    blocks = []
    for i, (src, cap) in enumerate(pr["gallery"]):
        # wide plates for very wide images -> span 2 in 2-col gallery
        blocks.append(
            f'<figure data-reveal style="--d:{(i % 3) * 80}ms">'
            f'<button class="shot" data-lightbox type="button" aria-label="Enlarge: {e(cap)}">'
            f'<img src="{p}{IMG}/{e(src)}" alt="{e(cap)}" loading="lazy" decoding="async">'
            f'</button><figcaption>{e(cap)}</figcaption></figure>')
    return '<div class="gallery gallery--2">' + "".join(blocks) + "</div>"

# ---------------------------------------------------------------- pages
def build_index():
    feat = PROJECTS[0]
    cards = []
    sizes = ["wide", "", "", "", "", "wide", "", "", "", "", "", "", "", "", "", ""]
    for i, pr in enumerate(PROJECTS):
        sz = "wide" if i == 0 else ("" if i % 3 else "wide")
        cards.append(card(pr, 0, sz, (i % 2) * 100))
    marquee_items = ("Product design", "Industrial design", "Design engineering",
                     "CAD &amp; surfacing", "Prototyping", "UX / UI", "Electronics",
                     "Form analysis", "Sketching")
    mq = "".join(f'<span class="marquee__item">{m}</span>' for m in marquee_items)
    return (head(f"{SITE['name']} — {SITE['role']}",
                 SITE["intro"])
        + nav(0, "index.html") +
f'''
<main>
  <section class="hero">
    <div class="hero__bg" aria-hidden="true">
      <img src="{IMG}/{e(HERO_IMAGE)}" alt="" fetchpriority="high" decoding="async">
    </div>
    <div class="wrap hero__top">
      <p class="eyebrow" data-reveal style="--d:100ms">Product &amp; industrial designer &mdash; {e(SITE['location'])}</p>
    </div>
    <div class="wrap">
      <h1 class="display hero__title" data-reveal style="--d:200ms">
        Design that earns its <em>place</em> in the world.
      </h1>
      <div class="hero__meta" data-reveal style="--d:340ms">
        <p class="lede" style="max-width:46ch">
          {e(SITE['intro'])} From a smart mobility aid submitted to the James Dyson Award
          to a full e-commerce UX process in Figma &mdash; here is the work, process and
          reasoning behind it.
        </p>
        <div class="tag-row" style="align-self:center">
          <span class="tag">Product design</span>
          <span class="tag">Design engineering</span>
          <span class="tag">UX / UI</span>
          <span class="tag">CAD</span>
        </div>
      </div>
      <a class="hero__scroll" href="#work" aria-label="Scroll to selected work">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 4v15m0 0l-6-6m6 6l6-6"/></svg>
        Selected work
      </a>
    </div>
  </section>

  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">{mq}</div>
    <div class="marquee__track">{mq}</div>
  </div>

  <section class="section" id="work">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="eyebrow" data-reveal>01 / Selected work</p>
          <h2 class="display mt-1" data-reveal style="--d:80ms">{NUM_WORDS[len(PROJECTS)].capitalize()} projects,<br>one point of view.</h2>
        </div>
        <p class="lede" style="max-width:38ch" data-reveal style="--d:160ms">
          Engineering-led product design, digital product work, and the sketching practice
          that feeds both. Every image here is my own.
        </p>
      </div>
      <div class="work-grid">
        {''.join(cards)}
      </div>
      <div class="mt-4" data-reveal>
        <a class="btn" href="work/index.html">Browse the full archive
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14m0 0l-6-6m6 6l-6 6"/></svg>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow" data-reveal>02 / Approach</p>
          <h2 class="display mt-1" style="font-size:var(--step-3)" data-reveal style="--d:80ms">
            Form never merely follows function. <em>Form is function.</em>
          </h2>
        </div>
        <div class="timeline">
          <div class="tl" data-reveal><span class="tl__n">01</span><div><h3 class="tl__t">Understand the form before the software</h3><p class="tl__d">How often do we jump straight into CAD before truly understanding a form? The strongest designs start with a breakdown of shape, proportion and volume &mdash; on paper, quickly, without commitment.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">02</span><div><h3 class="tl__t">Make it physical early</h3><p class="tl__d">Clay, card and 3D-printed models fix ergonomics and apply the user journey in a way a screen cannot. Without that step there is no kaizen.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">03</span><div><h3 class="tl__t">Engineer it honestly</h3><p class="tl__d">Internal layout, tolerances, sensor packaging, BOM costing and FEA are the parts of design that deserve far more recognition than the exterior silhouette. Functionality should never compromise form &mdash; and form should never compromise the person using it.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">04</span><div><h3 class="tl__t">Design for everyone who needs it</h3><p class="tl__d">Mobility issues do not discriminate by income. Assistive technology split into affordable and premium tiers is a design decision as much as an ethical one.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="stats">
        <div class="stat" data-reveal><span class="stat__k">{len(PROJECTS)}</span><span class="stat__v">Projects documented end to end</span></div>
        <div class="stat" data-reveal><span class="stat__k">130 kg</span><span class="stat__v">Supported user weight, SmartWalker</span></div>
        <div class="stat" data-reveal><span class="stat__k">6.5 kg</span><span class="stat__v">Total SmartWalker system weight</span></div>
        <div class="stat" data-reveal><span class="stat__k">8 hrs</span><span class="stat__v">Continuous operation per battery cycle</span></div>
        <div class="stat" data-reveal><span class="stat__k">&pound;252.99</span><span class="stat__v">Target bill-of-materials cost</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap center">
      <p class="eyebrow" data-reveal>03 / The practice</p>
      <blockquote class="statement__q mt-2" data-reveal style="--d:80ms">
        &ldquo;Professional UX isn&rsquo;t about perfect starting points, it&rsquo;s about
        <em>intentional user flows</em>.&rdquo;
      </blockquote>
      <p class="lede mt-2" style="margin-inline:auto" data-reveal style="--d:160ms">
        I sketch two to three times a week and post the results, because sketching still gets
        undervalued in design conversations that jump straight to renders. It is where the
        early thinking happens &mdash; fast, rough, low commitment.
      </p>
      <div class="mt-3" data-reveal style="--d:240ms">
        <a class="btn" href="work/sketchbook/index.html">See the sketchbook</a>
      </div>
    </div>
  </section>
</main>''' + footer(0))

def build_work():
    cards = "".join(card(pr, 1, "" if i % 3 else "wide", (i % 3) * 70)
                    for i, pr in enumerate(PROJECTS))
    chips = "".join(
        f'<button class="chip" type="button" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>'
        for k, v in TAGS)
    return (head(f"Work archive — {SITE['name']}",
                 "The complete archive of product design, design engineering, digital and sketching projects.",
                 1) + nav(1, "work/index.html") +
f'''
<main>
  <section class="case-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Archive</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">Everything,<br>in one place.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        {NUM_WORDS[len(PROJECTS)].capitalize()} projects spanning product design, design engineering, digital
        product work and a continuous sketching practice. Filter by discipline.
      </p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="filters" data-filters role="group" aria-label="Filter projects by discipline">
        {chips}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:clamp(1.5rem,3vw,3rem)">
    <div class="wrap">
      <div class="work-grid">{cards}</div>
      <p class="faint mt-3" style="font-size:var(--step--1)">
        <span data-count>{len(PROJECTS)}</span> projects &middot; all imagery is the designer&rsquo;s own work.
      </p>
    </div>
  </section>
</main>''' + footer(1))

def build_about():
    return (head(f"Studio — {SITE['name']}",
                 "Imaan Rafiq is a product and industrial designer and BSc Product Design & Technology graduate from Aston University.",
                 1) + nav(1, "about/index.html") +
f'''
<main>
  <section class="case-hero">
    <div class="wrap split">
      <div>
        <p class="eyebrow" data-reveal>Studio</p>
        <h1 class="display mt-1" data-reveal style="--d:80ms">Oh, hello<br>there.</h1>
        <figure style="margin-top:2.5rem;width:min(260px,60vw)" data-reveal>
          <img src="../{IMG}/avatar.jpg" alt="Portrait of Imaan Rafiq" width="400" height="400"
               style="width:100%;height:auto;border:1px solid var(--line);border-radius:3px;filter:grayscale(0.15)" loading="lazy">
          <figcaption class="faint" style="font-size:var(--step--2);padding-top:0.6rem">
            Imaan Rafiq &middot; Product &amp; industrial designer
          </figcaption>
        </figure>
      </div>
      <div data-reveal style="--d:160ms">
        <p class="lede">
          I&rsquo;m a product design graduate with a keen interest in user-centred design and
          problem solving. I&rsquo;m skilled in CAD, prototyping and visual communication, and
          I&rsquo;m passionate about creating functional and aesthetically refined solutions.
        </p>
        <p class="lede mt-2">
          I&rsquo;m seeking a graduate role in product or industrial design. My background is a
          bit of a mix, which I think is genuinely useful: I can design complex parts in
          Dassault SOLIDWORKS and CATIA, write the embedded C++ that makes those parts actually
          do something, understand lean manufacturing and supply chains from time spent on the
          Toyota production floor, and cost a full BOM with a commercial pricing strategy
          around it.
        </p>
      </div>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <figure class="card__media" style="aspect-ratio:21/9;border:1px solid var(--line);border-radius:3px;overflow:hidden" data-reveal>
        <img src="../{IMG}/smartwalker/00.jpg" alt="SmartWalker — the final year project prototype" loading="lazy">
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="eyebrow" data-reveal>01 / Capabilities</p>
          <h2 class="display mt-1" data-reveal style="--d:80ms">What I actually do.</h2>
        </div>
      </div>
      <div class="caps">
        <div class="cap" data-reveal>
          <span class="cap__n">01</span>
          <h3 class="cap__t">Design skills</h3>
          <p class="cap__d">Research-led concept development from first question to manufacturable answer.</p>
          <ul><li>User research</li><li>Concept development</li><li>Sketching &amp; ideation</li><li>Prototyping</li></ul>
        </div>
        <div class="cap" data-reveal style="--d:80ms">
          <span class="cap__n">02</span>
          <h3 class="cap__t">Technical</h3>
          <p class="cap__d">Parametric modelling, surfacing, rendering and production drawings.</p>
          <ul><li>SOLIDWORKS</li><li>Fusion 360</li><li>CATIA</li><li>KeyShot</li><li>Illustrator / Photoshop</li></ul>
        </div>
        <div class="cap" data-reveal style="--d:160ms">
          <span class="cap__n">03</span>
          <h3 class="cap__t">Electronics</h3>
          <p class="cap__d">Firmware and sensor integration &mdash; the code that makes physical products behave.</p>
          <ul><li>ESP32-S3</li><li>Arduino / C++</li><li>Sensor fusion</li><li>Circuit design</li></ul>
        </div>
        <div class="cap" data-reveal style="--d:240ms">
          <span class="cap__n">04</span>
          <h3 class="cap__t">Commercial</h3>
          <p class="cap__d">Understanding what a design costs to make, and what that means for who can afford it.</p>
          <ul><li>BOM costing</li><li>Pricing strategy</li><li>Lean manufacturing</li><li>Supply chains</li></ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow" data-reveal>02 / How I work</p>
          <h2 class="display mt-1" style="font-size:var(--step-3)" data-reveal style="--d:80ms">
            Sketch first. <em>Sometimes.</em>
          </h2>
          <p class="lede mt-2" data-reveal style="--d:160ms">
            Sketch first, or straight to CAD? I don&rsquo;t think there&rsquo;s a single right
            answer. For me sketching is usually where the early thinking happens &mdash; fast,
            rough, low commitment. That said, I go straight into 3D sometimes too, when I
            already know the form and just want to get it out before the idea moves.
          </p>
        </div>
        <div class="timeline">
          <div class="tl" data-reveal><span class="tl__n">Foundation</span><div><h3 class="tl__t">Sketch plane, centreline, construction line</h3><p class="tl__d">A robust sketch is built, not drawn. It follows a strict hierarchy of operations &mdash; and this is where every model begins.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">Generation</span><div><h3 class="tl__t">Line, arc, circle, ellipse, spline, polygon</h3><p class="tl__d">Getting the volume and proportion out of the head and onto the screen without over-committing.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">Modification</span><div><h3 class="tl__t">Offset, trim, extend, mirror, pattern</h3><p class="tl__d">Refining the form against real constraints &mdash; manufacturing, packaging, assembly.</p></div></div>
          <div class="tl" data-reveal><span class="tl__n">Control</span><div><h3 class="tl__t">Constraint and dimension</h3><p class="tl__d">Locking the design down so it can be manufactured, costed and produced reliably at scale.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="stats">
        <div class="stat" data-reveal><span class="stat__k">BSc</span><span class="stat__v">Product Design &amp; Technology, Aston University</span></div>
        <div class="stat" data-reveal><span class="stat__k">James Dyson Award</span><span class="stat__v">2026 entry &mdash; SmartWalker</span></div>
        <div class="stat" data-reveal><span class="stat__k">2&ndash;3&times;</span><span class="stat__v">Design and form analysis posts per week</span></div>
        <div class="stat" data-reveal><span class="stat__k">Open to work</span><span class="stat__v">Product design, medtech, manufacturing</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="eyebrow" data-reveal>03 / Archive plate</p>
          <h2 class="display mt-1" data-reveal style="--d:80ms">Selected pages from the book.</h2>
        </div>
        <a class="arrow-link" href="../work/portfolio-deck/index.html" data-reveal style="--d:160ms">
          Open the portfolio deck
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14m0 0l-6-6m6 6l-6 6"/></svg>
        </a>
      </div>
      <div class="archive">
        {''.join(f'<button class="shot" data-lightbox type="button" aria-label="Enlarge portfolio page {i+1:02d}"><img src="../{IMG}/portfolio-deck/{i:02d}.jpg" alt="Portfolio page {i+1}" loading="lazy"></button>' for i in range(20))}
      </div>
    </div>
  </section>
</main>''' + footer(1))

def build_contact():
    return (head(f"Contact — {SITE['name']}",
                 "Get in touch with Imaan Rafiq about graduate roles in product design, design engineering, medtech or manufacturing.",
                 1) + nav(1, "contact/index.html") +
f'''
<main>
  <section class="case-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Contact</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">
        Let&rsquo;s build<br>something <em>useful</em>.
      </h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        I&rsquo;m open to graduate roles in product design, design engineering, embedded
        systems, medtech and manufacturing &mdash; or a conversation about a project.
      </p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="stats">
        <div class="stat" data-reveal>
          <span class="stat__v" style="text-transform:none;letter-spacing:0.02em;text-align:left">Email</span>
          <a class="stat__k" href="mailto:{e(SITE['email'])}" style="font-size:var(--step-2)">{e(SITE['email'])}</a>
        </div>
        <div class="stat" data-reveal>
          <span class="stat__v" style="text-transform:none;letter-spacing:0.02em;text-align:left">Phone</span>
          <a class="stat__k" href="tel:{e(SITE['phone'])}" style="font-size:var(--step-2)">{e(SITE['phone'])}</a>
        </div>
        <div class="stat" data-reveal>
          <span class="stat__v" style="text-transform:none;letter-spacing:0.02em;text-align:left">LinkedIn</span>
          <a class="stat__k" href="{e(SITE['linkedin'])}" target="_blank" rel="noopener" style="font-size:var(--step-2)">/in/imaanrafiq &nearr;</a>
        </div>
        <div class="stat" data-reveal>
          <span class="stat__v" style="text-transform:none;letter-spacing:0.02em;text-align:left">Based in</span>
          <span class="stat__k" style="font-size:var(--step-2)">{e(SITE['location'])}</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow" data-reveal>What I&rsquo;m looking for</p>
        <h2 class="display mt-1" style="font-size:var(--step-3)" data-reveal style="--d:80ms">
          A team where I can keep building things that <em>matter</em>.
        </h2>
      </div>
      <div data-reveal style="--d:160ms">
        <p class="lede">
          I graduated with a BSc in Product Design &amp; Technology from Aston University and
          I&rsquo;m ready for my first full-time engineering role. My final year project brought
          the whole skill set together: I built a SmartWalker mobility aid from scratch &mdash;
          user research, CAD, electronics, sensor fusion, FEA, BOM costing and a 12-section
          technical report.
        </p>
        <p class="lede mt-2">
          If you&rsquo;re hiring graduates in product design, embedded systems, medtech or
          manufacturing &mdash; or you just want to have a chat &mdash; feel free to connect or
          drop me a message.
        </p>
        <div class="tag-row mt-3">
          <span class="tag">Product design</span>
          <span class="tag">Industrial design</span>
          <span class="tag">Embedded systems</span>
          <span class="tag">Medtech</span>
          <span class="tag">Manufacturing</span>
          <span class="tag">Design engineering</span>
        </div>
        <div class="mt-3">
          <a class="btn btn--solid" href="mailto:{e(SITE['email'])}">Email me directly</a>
        </div>
      </div>
    </div>
  </section>
</main>''' + footer(1))

def build_case(pr, prev, nxt):
    p = "../../"
    meta = f'''<dl class="case-hero__meta">
      <div><dt>Discipline</dt><dd>{e(pr['category'])}</dd></div>
      <div><dt>Year</dt><dd>{e(pr['year'])}</dd></div>
      <div><dt>Role</dt><dd>{e(pr['roles'])}</dd></div>
      <div><dt>Tools</dt><dd>{e(pr['tools'])}</dd></div>
      {'<div><dt>Recognition</dt><dd>' + e(pr['award']) + '</dd></div>' if pr.get('award') else ''}
    </dl>'''

    sections = []
    for i, s in enumerate(pr["sections"]):
        bullets = ""
        if s.get("bullets"):
            bullets = '<ul class="stack" style="--s:0.6rem">' + "".join(
                f'<li style="display:flex;gap:0.75rem;color:var(--bone-dim)">'
                f'<span style="color:var(--accent);flex:none">&mdash;</span><span>{e(b)}</span></li>'
                for b in s["bullets"]) + "</ul>"
        paras = "".join(f"<p>{e(b)}</p>" for b in s.get("body", []))
        sections.append(
            f'<div data-reveal>'
            f'<h2 class="display mb-2" style="font-size:var(--step-2)">{e(s["title"])}</h2>'
            f'<div class="prose">{paras}{bullets}</div>'
            f'</div>')

    stats = ""
    if pr.get("stats"):
        stats = '<div class="stats mt-4">' + "".join(
            f'<div class="stat" data-reveal><span class="stat__k">{e(k)}</span>'
            f'<span class="stat__v">{e(v)}</span></div>' for k, v in pr["stats"]) + "</div>"

    aside_tags = "".join(f'<li>{e(t)}</li>' for t in pr["tags"].split())

    return (head(f"{pr['title']} — {SITE['name']}", pr["summary"], 2) + nav(2, "work") +
f'''
<main>
  <article>
    <header class="case-hero">
      <div class="wrap">
        <a class="eyebrow" href="../index.html" style="display:inline-block">&larr; Work archive</a>
        <h1 class="display mt-2" data-reveal style="--d:60ms">{e(pr['title'])}</h1>
        <p class="lede mt-2" data-reveal style="--d:140ms">{e(pr['subtitle'])}</p>
        {meta}
        <figure class="case-cover" data-reveal style="--d:220ms">
          <img src="{p}{IMG}/{e(pr['cover'])}" alt="{e(pr['title'])} — cover" fetchpriority="high" decoding="async">
        </figure>
      </div>
    </header>

    <section class="section">
      <div class="wrap case-body">
        <aside class="case-aside">
          <p class="case-aside__h">At a glance</p>
          <ul>
            <li>{e(pr['category'])}</li>
            <li>{e(pr['year'])}</li>
            <li>{e(pr['roles'])}</li>
          </ul>
          <div class="mt-3">
            <p class="case-aside__h">Disciplines</p>
            <div class="tag-row">{aside_tags}</div>
          </div>
        </aside>
        <div class="stack" style="--s:clamp(2.5rem,5vw,4.5rem)">
          <div class="prose stack" style="--s:1.15rem">
            {''.join(f'<p>{e(x)}</p>' for x in pr['intro'])}
          </div>
          {''.join(sections)}
          {stats}
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap">
        <div class="sec-head">
          <div>
            <p class="eyebrow" data-reveal>Image plate</p>
            <h2 class="display mt-1" style="font-size:var(--step-2)" data-reveal style="--d:80ms">
              {len(pr['gallery'])} images from the project
            </h2>
          </div>
          <p class="faint" style="font-size:var(--step--1)" data-reveal>Click any image to enlarge</p>
        </div>
        {gallery_html(pr, 2)}
      </div>
    </section>
  </article>

  <nav class="case-nav" aria-label="Project navigation">
    <a href="../{e(prev['slug'])}/index.html">
      <span class="case-nav__l">&larr; Previous</span>
      <span class="case-nav__t">{e(prev['title'])}</span>
    </a>
    <a href="../{e(nxt['slug'])}/index.html">
      <span class="case-nav__l">Next &rarr;</span>
      <span class="case-nav__t">{e(nxt['title'])}</span>
    </a>
  </nav>
</main>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer" data-open="false" aria-hidden="true">
  <button class="lightbox__close" type="button">Close</button>
  <img alt="">
  <div class="lightbox__nav">
    <button class="lightbox__prev" type="button">&larr; Prev</button>
    <span class="lightbox__count"></span>
    <button class="lightbox__next" type="button">Next &rarr;</button>
  </div>
</div>
''' + footer(2))

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" fill="#0c0c0d"/>
<text x="32" y="44" font-family="Georgia,serif" font-size="34" fill="#c8f24e" text-anchor="middle">IR</text>
</svg>'''

def build_404():
    return (head(f"Page not found — {SITE['name']}",
                 "That page doesn't exist. Head back to the work archive.", 0) + nav(0, "") +
f'''
<main>
  <section class="case-hero" style="min-height:70svh;display:flex;align-items:center">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Error 404</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">This one never<br>made the cut.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        The page you were looking for isn&rsquo;t here. It may have been renamed, moved,
        or it was an early concept that didn&rsquo;t survive the review.
      </p>
      <div class="mt-3" data-reveal style="--d:240ms">
        <a class="btn btn--solid" href="index.html">Back to the work</a>
      </div>
    </div>
  </section>
</main>''' + footer(0))

def main():
    os.makedirs(ROOT, exist_ok=True)
    open(os.path.join(ROOT, "index.html"), "w").write(build_index())
    open(os.path.join(ROOT, "404.html"), "w").write(build_404())
    open(os.path.join(ROOT, "assets", "favicon.svg"), "w").write(FAVICON)

    for sub, fn in (("work", build_work), ("about", build_about), ("contact", build_contact)):
        d = os.path.join(ROOT, sub)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(fn())

    n = len(PROJECTS)
    for i, pr in enumerate(PROJECTS):
        d = os.path.join(ROOT, "work", pr["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(
            build_case(pr, PROJECTS[(i - 1) % n], PROJECTS[(i + 1) % n]))
        print("  case:", pr["slug"])

    # sitemap + robots
    base = os.environ.get("SITE_URL", SITE.get("url", "")).rstrip("/")
    urls = ["", "work/", "about/", "contact/"] + [f"work/{p['slug']}/" for p in PROJECTS]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{base}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n"
        + (f"Sitemap: {base}/sitemap.xml\n" if base else "# Set SITE_URL to emit an absolute sitemap URL\n"))
    print("built", n + 4, "pages")

if __name__ == "__main__":
    main()