# -*- coding: utf-8 -*-
"""Static site generator for Imaan Rafiq's design portfolio."""
import os
import html as H
from content import PROJECTS, TAGS, SITE, HERO_IMAGE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "assets/img"
YEAR = "2026"


def e(t):
    return H.escape(str(t), quote=True)


def pfx(depth):
    return "../" * depth


# ---------------------------------------------------------------- components
def head(title, desc, depth=0):
    p = pfx(depth)
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
<meta property="og:image" content="{p}{IMG}/{e(PROJECTS[0]['cover'])}">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" as="font" type="font/woff2" href="{p}assets/fonts/Inter-normal-300_800-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="{p}assets/fonts/InstrumentSerif-normal-400-latin.woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/css/style.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>'''


def nav(depth=0, active=""):
    p = pfx(depth)
    items = [("index.html", "Work"), ("work/index.html", "Archive"),
             ("about/index.html", "Studio"), ("contact/index.html", "Contact")]
    links = "".join(
        f'<a class="nav__link" href="{p}{href}"'
        + (' aria-current="page"' if active == href else "")
        + f'>{label}</a>' for href, label in items)
    return f'''<div class="progress" aria-hidden="true"></div>
<header class="nav">
  <a class="nav__logo" href="{p}index.html">Imaan Rafiq<span>&trade;</span></a>
  <nav class="nav__links" id="menu" data-open="false" aria-label="Primary">{links}</nav>
  <button class="nav__toggle" aria-expanded="false" aria-controls="menu" type="button"><i></i>Menu</button>
</header>'''


def footer(depth=0):
    p = pfx(depth)
    return f'''<footer class="footer">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Let&rsquo;s work together</p>
    <h2 class="footer__cta mt-1" data-reveal>
      Designing things that <em>actually</em> work.<br>
      <a href="{p}contact/index.html" class="serif">Start a conversation &rarr;</a>
    </h2>
    <div class="footer__cols">
      <div data-reveal>
        <p class="footer__h">Contact</p>
        <a class="footer__li" href="mailto:{e(SITE['email'])}">{e(SITE['email'])}</a>
        <span class="footer__li">{e(SITE['location'])}</span>
      </div>
      <div data-reveal>
        <p class="footer__h">Elsewhere</p>
        <a class="footer__li" href="{e(SITE['linkedin'])}" target="_blank" rel="noopener">LinkedIn &nearr;</a>
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
      <span>&copy; <span data-year>{YEAR}</span> Imaan Rafiq. All work shown is the designer&rsquo;s own.</span>
      <span>BSc Product Design &amp; Technology &middot; Aston University</span>
    </div>
  </div>
</footer>
<script src="{p}assets/js/main.js" defer></script>
</body>
</html>'''


def card(pr, depth=0, size="", delay=0):
    p = pfx(depth)
    cls = "card" + (f" card--{size}" if size else "")
    badge = (f'<span class="card__badge card__badge--award">{e(pr["award"])}</span>'
             if pr.get("award") else
             f'<span class="card__badge">{e(pr["category"])}</span>')
    return f'''<a class="{cls}" href="{p}work/{pr['slug']}/index.html" data-tags="{e(pr['tags'])}" data-reveal style="--d:{delay}ms">
  <figure class="card__media">
    {badge}
    <img src="{p}{IMG}/{e(pr['cover'])}" alt="{e(pr['title'])} &mdash; {e(pr['subtitle'])}" loading="lazy" decoding="async">
  </figure>
  <div class="card__body">
    <h3 class="card__title">{e(pr['title'])}</h3>
    <span class="card__sub">{e(pr['year'])} &middot; {e(pr['subtitle'])}</span>
  </div>
</a>'''


def lightbox():
    return '''<div class="lightbox" data-lightbox hidden>
  <button class="lightbox__close" type="button" aria-label="Close">&times;</button>
  <button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Previous image">&larr;</button>
  <figure class="lightbox__stage">
    <img alt="" data-lightbox-img>
    <figcaption data-lightbox-cap></figcaption>
  </figure>
  <button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Next image">&rarr;</button>
</div>'''


# ---------------------------------------------------------------- pages
def build_index():
    featured = PROJECTS[:6]
    cards = "".join(
        card(pr, 0, size=("wide" if i == 0 else ""), delay=i * 60)
        for i, pr in enumerate(featured))
    return (head(f"{SITE['name']} — {SITE['role']}",
                 "Portfolio of Imaan Rafiq, a product design and technology graduate working across "
                 "industrial design, design engineering, CAD and prototyping.")
            + nav(0, "index.html") +
            f'''<main id="main">
  <section class="hero">
    <div class="hero__bg" aria-hidden="true">
      <img src="{IMG}/{e(HERO_IMAGE)}" alt="" fetchpriority="high" decoding="async">
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow" data-reveal>{e(SITE['role'])} &middot; {e(SITE['location'])}</p>
      <h1 class="hero__title" data-reveal style="--d:80ms">
        I design considered products that <em>work</em> for the people who use them.
      </h1>
      <p class="lede hero__lede" data-reveal style="--d:160ms">{e(SITE['intro'])}</p>
      <div class="hero__actions" data-reveal style="--d:240ms">
        <a class="btn btn--solid" href="work/index.html">View the work</a>
        <a class="btn" href="contact/index.html">Get in touch</a>
      </div>
    </div>
  </section>

  <section class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span>{e(SITE['discipline'])}</span><span>&bull;</span>
      <span>{e(SITE['discipline'])}</span><span>&bull;</span>
      <span>{e(SITE['discipline'])}</span><span>&bull;</span>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow" data-reveal>Selected work</p>
          <h2 class="display" data-reveal style="--d:60ms">Flagship projects.</h2>
        </div>
        <a class="text-link" href="work/index.html" data-reveal style="--d:120ms">All {len(PROJECTS)} projects &rarr;</a>
      </div>
      <div class="grid">{cards}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <p class="eyebrow" data-reveal>By the numbers</p>
      <div class="stats stats--wide">
        <div class="stat" data-reveal><span class="stat__k">{len(PROJECTS)}</span><span class="stat__v">Projects documented end to end</span></div>
        <div class="stat" data-reveal><span class="stat__k">BSc</span><span class="stat__v">Product Design &amp; Technology, Aston University</span></div>
        <div class="stat" data-reveal><span class="stat__k">Dyson</span><span class="stat__v">2026 award entry &mdash; SmartWalker</span></div>
        <div class="stat" data-reveal><span class="stat__k">Open</span><span class="stat__v">To graduate roles in product, medtech &amp; manufacturing</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="split__aside">
        <p class="eyebrow" data-reveal>What I do</p>
        <h2 class="display" data-reveal style="--d:60ms">Design and engineering,<br>end to end.</h2>
        <a class="btn" href="about/index.html" data-reveal style="--d:120ms">More about the studio</a>
      </div>
      <div class="split__body">
        <ul class="caps">
          <li data-reveal><h3>Design</h3><p>Research-led concept development, from first question to a manufacturable answer.</p></li>
          <li data-reveal><h3>Engineering</h3><p>Parametric modelling, surfacing, rendering and production drawings.</p></li>
          <li data-reveal><h3>Electronics</h3><p>Firmware and sensor integration &mdash; the code that makes products behave.</p></li>
          <li data-reveal><h3>Commercial</h3><p>BOM costing and pricing strategy, so a design can reach the people who need it.</p></li>
        </ul>
      </div>
    </div>
  </section>
</main>''' + lightbox() + footer(0))


def build_work():
    chips = "".join(
        f'<button class="chip{" is-active" if key == "all" else ""}" type="button" data-filter="{e(key)}">{e(label)}</button>'
        for key, label in TAGS)
    cards = "".join(card(pr, 1, delay=(i % 3) * 70) for i, pr in enumerate(PROJECTS))
    return (head(f"Archive — {SITE['name']}",
                 "The full archive of Imaan Rafiq's product design, engineering and concept work.",
                 1)
            + nav(1, "work/index.html") +
            f'''<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Archive</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">Every project,<br>in one place.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        {len(PROJECTS)} projects spanning product design, design engineering, electronics and
        form study &mdash; each one documented from brief to outcome.
      </p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="filters" data-reveal>{chips}</div>
      <div class="grid" data-grid>{cards}</div>
      <p class="grid__empty" data-empty hidden>Nothing matches that filter yet.</p>
    </div>
  </section>
</main>''' + lightbox() + footer(1))


def build_case(pr, prev_pr, next_pr):
    p = pfx(2)
    meta = [("Year", pr["year"]), ("Discipline", pr["category"])]
    if pr.get("roles"):
        meta.append(("Role", pr["roles"]))
    if pr.get("tools"):
        meta.append(("Tools", pr["tools"]))
    meta_html = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in meta)

    stats = pr.get("stats", [])
    stats_html = ""
    if stats:
        stats_html = '<div class="stats">' + "".join(
            f'<div class="stat" data-reveal><span class="stat__k">{e(k)}</span>'
            f'<span class="stat__v">{e(v)}</span></div>' for k, v in stats) + "</div>"

    intro_html = "".join(f'<p class="lede">{e(t)}</p>' for t in pr.get("intro", []))

    sections_html = ""
    for s in pr.get("sections", []):
        body = "".join(f"<p>{e(t)}</p>" for t in s.get("body", []))
        bullets = ""
        if s.get("bullets"):
            bullets = ('<ul class="bullets">'
                       + "".join(f"<li>{e(b)}</li>" for b in s["bullets"]) + "</ul>")
        sections_html += f'''<section class="prose-block" data-reveal>
        <h2>{e(s["title"])}</h2>
        <div class="prose">{body}{bullets}</div>
      </section>'''

    gallery_html = "".join(
        f'''<figure class="shot" data-reveal>
          <button class="shot__btn" type="button" data-full="{p}{IMG}/{e(src)}" data-cap="{e(cap)}">
            <img src="{p}{IMG}/{e(src)}" alt="{e(cap)}" loading="lazy" decoding="async">
          </button>
          <figcaption>{e(cap)}</figcaption>
        </figure>''' for src, cap in pr.get("gallery", []))

    gallery = ""
    if gallery_html:
        gallery = f'''<section class="section">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Gallery</p>
      <div class="shots">{gallery_html}</div>
    </div>
  </section>'''

    award = (f'<span class="tag tag--award">{e(pr["award"])}</span>'
             if pr.get("award") else "")

    return (head(f"{pr['title']} — {SITE['name']}", pr["summary"], 2)
            + nav(2, "work/index.html") +
            f'''<main id="main">
  <section class="case-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal><a href="{p}work/index.html">Archive</a> &rsaquo; {e(pr['category'])}</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">{e(pr['title'])}</h1>
      <p class="lede mt-2" data-reveal style="--d:140ms">{e(pr['subtitle'])}</p>
      {award}
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <dl class="meta" data-reveal>{meta_html}</dl>
      <figure class="case-cover" data-reveal style="--d:160ms">
        <img src="{p}{IMG}/{e(pr['cover'])}" alt="{e(pr['title'])} &mdash; cover" fetchpriority="high" decoding="async">
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="case-intro">
        <p class="eyebrow" data-reveal>Overview</p>
        <div class="case-intro__body" data-reveal style="--d:60ms">
          <p class="lede">{e(pr['summary'])}</p>
          {intro_html}
        </div>
      </div>
      {stats_html}
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap case-body">{sections_html}</div>
  </section>

  {gallery}

  <section class="section--tight">
    <div class="wrap pager">
      <a class="pager__link" href="{p}work/{prev_pr['slug']}/index.html">
        <span class="pager__dir">&larr; Previous</span>
        <span class="pager__title">{e(prev_pr['title'])}</span>
      </a>
      <a class="pager__link pager__link--next" href="{p}work/{next_pr['slug']}/index.html">
        <span class="pager__dir">Next &rarr;</span>
        <span class="pager__title">{e(next_pr['title'])}</span>
      </a>
    </div>
  </section>
</main>''' + lightbox() + footer(2))


def build_about():
    return (head(f"Studio — {SITE['name']}",
                 "About Imaan Rafiq: a product design and technology graduate working across "
                 "industrial design, CAD, prototyping and electronics.", 1)
            + nav(1, "about/index.html") +
            f'''<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Studio</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">Oh, hello there.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        I&rsquo;m Imaan Rafiq, a product design graduate with a keen interest in user-centred
        design and problem solving. I&rsquo;m skilled in CAD, prototyping and visual
        communication, and I&rsquo;m passionate about creating functional and aesthetically
        refined solutions &mdash; and I&rsquo;m seeking a graduate role in product or
        industrial design.
      </p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap split">
      <div class="split__aside">
        <p class="eyebrow" data-reveal>01 / Capabilities</p>
        <h2 class="display" data-reveal style="--d:60ms">What I actually do.</h2>
      </div>
      <div class="split__body">
        <ul class="caps caps--about">
          <li data-reveal><span class="caps__no">01</span><h3>Design skills</h3>
            <p>Research-led concept development from first question to manufacturable answer.</p>
            <span class="caps__tags">User research &middot; Concept development &middot; Sketching &amp; ideation &middot; Prototyping</span></li>
          <li data-reveal><span class="caps__no">02</span><h3>Technical</h3>
            <p>Parametric modelling, surfacing, rendering and production drawings.</p>
            <span class="caps__tags">SOLIDWORKS &middot; Fusion 360 &middot; CATIA &middot; KeyShot &middot; Illustrator / Photoshop</span></li>
          <li data-reveal><span class="caps__no">03</span><h3>Electronics</h3>
            <p>Firmware and sensor integration &mdash; the code that makes physical products behave.</p>
            <span class="caps__tags">ESP32-S3 &middot; Arduino / C++ &middot; Sensor fusion &middot; Circuit design</span></li>
          <li data-reveal><span class="caps__no">04</span><h3>Commercial</h3>
            <p>Understanding what a design costs to make, and what that means for who can afford it.</p>
            <span class="caps__tags">BOM costing &middot; Pricing strategy &middot; Lean manufacturing &middot; Supply chains</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap split">
      <div class="split__aside">
        <p class="eyebrow" data-reveal>02 / How I work</p>
        <h2 class="display" data-reveal style="--d:60ms">Sketch first.<br><em>Sometimes.</em></h2>
        <p class="lede" data-reveal style="--d:120ms">
          Sketch first, or straight to CAD? There isn&rsquo;t a single right answer. For me
          sketching is usually where the early thinking happens &mdash; fast, rough, low
          commitment. That said, I go straight into 3D sometimes too, when I already know the
          form and just want to get it out before the idea moves.
        </p>
      </div>
      <div class="split__body">
        <ol class="steps">
          <li data-reveal><span class="steps__k">Foundation</span><p>Sketch plane, centreline, construction line. A robust sketch is built, not drawn &mdash; and this is where every model begins.</p></li>
          <li data-reveal><span class="steps__k">Generation</span><p>Line, arc, circle, ellipse, spline, polygon. Getting the volume and proportion out of the head and onto the screen without over-committing.</p></li>
          <li data-reveal><span class="steps__k">Modification</span><p>Offset, trim, extend, mirror, pattern. Refining the form against real constraints &mdash; manufacturing, packaging, assembly.</p></li>
          <li data-reveal><span class="steps__k">Control</span><p>Constraint and dimension. Locking the design down so it can be manufactured, costed and produced reliably at scale.</p></li>
        </ol>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats stats--wide">
        <div class="stat" data-reveal><span class="stat__k">BSc</span><span class="stat__v">Product Design &amp; Technology, Aston University</span></div>
        <div class="stat" data-reveal><span class="stat__k">Dyson</span><span class="stat__v">James Dyson Award 2026 entry &mdash; SmartWalker</span></div>
        <div class="stat" data-reveal><span class="stat__k">2&ndash;3&times;</span><span class="stat__v">Design and form analysis posts per week</span></div>
        <div class="stat" data-reveal><span class="stat__k">Open to work</span><span class="stat__v">Product design, medtech, manufacturing</span></div>
      </div>
      <div class="mt-3" data-reveal>
        <a class="btn btn--solid" href="{pfx(1)}work/portfolio-deck/index.html">Open the portfolio deck</a>
      </div>
    </div>
  </section>
</main>''' + footer(1))


def build_contact():
    return (head(f"Contact — {SITE['name']}",
                 "Get in touch with Imaan Rafiq about graduate roles in product design, design "
                 "engineering, medtech or manufacturing.", 1)
            + nav(1, "contact/index.html") +
            f'''<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Contact</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">Let&rsquo;s build<br>something <em>useful</em>.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        I&rsquo;m open to graduate roles in product design, design engineering, embedded
        systems, medtech and manufacturing &mdash; or a conversation about a project.
      </p>
    </div>
  </section>

  <section class="section--tight">
    <div class="wrap">
      <div class="contact">
        <a class="contact__card" href="mailto:{e(SITE['email'])}" data-reveal>
          <span class="contact__label">Email</span>
          <span class="contact__value">{e(SITE['email'])}</span>
        </a>
        <a class="contact__card" href="{e(SITE['linkedin'])}" target="_blank" rel="noopener" data-reveal style="--d:80ms">
          <span class="contact__label">LinkedIn</span>
          <span class="contact__value">/in/imaanrafiq &nearr;</span>
        </a>
        <div class="contact__card contact__card--static" data-reveal style="--d:160ms">
          <span class="contact__label">Based in</span>
          <span class="contact__value">{e(SITE['location'])}</span>
        </div>
      </div>
      <p class="contact__note" data-reveal style="--d:220ms">
        The quickest way to reach me is email. I usually reply within a day or two.
      </p>
    </div>
  </section>
</main>''' + footer(1))


def build_404():
    return (head(f"Not found — {SITE['name']}", "That page isn't here.")
            + nav(0, "") +
            f'''<main id="main">
  <section class="page-hero page-hero--tall">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Error 404</p>
      <h1 class="display mt-1" data-reveal style="--d:80ms">This one never<br>made the cut.</h1>
      <p class="lede mt-2" data-reveal style="--d:160ms">
        The page you were looking for isn&rsquo;t here. It may have been renamed, moved, or
        it was an early concept that didn&rsquo;t survive the review.
      </p>
      <div class="mt-3" data-reveal style="--d:240ms">
        <a class="btn btn--solid" href="index.html">Back to the work</a>
      </div>
    </div>
  </section>
</main>''' + footer(0))


# ---------------------------------------------------------------- build
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    write(os.path.join(ROOT, "index.html"), build_index())
    write(os.path.join(ROOT, "404.html"), build_404())

    for sub, fn in (("work", build_work), ("about", build_about), ("contact", build_contact)):
        write(os.path.join(ROOT, sub, "index.html"), fn())

    n = len(PROJECTS)
    for i, pr in enumerate(PROJECTS):
        write(os.path.join(ROOT, "work", pr["slug"], "index.html"),
              build_case(pr, PROJECTS[(i - 1) % n], PROJECTS[(i + 1) % n]))
        print("  case:", pr["slug"])

    base = os.environ.get("SITE_URL", SITE.get("url", "")).rstrip("/")
    urls = ["", "work/", "about/", "contact/"] + [f"work/{p['slug']}/" for p in PROJECTS]
    write(os.path.join(ROOT, "sitemap.xml"),
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{base}/{u}</loc></url>\n" for u in urls)
          + "</urlset>\n")
    write(os.path.join(ROOT, "robots.txt"),
          "User-agent: *\nAllow: /\n"
          + (f"Sitemap: {base}/sitemap.xml\n" if base else
             "# Set SITE_URL to emit an absolute sitemap URL\n"))
    write(os.path.join(ROOT, ".nojekyll"), "")
    print("built", n + 4, "pages")


if __name__ == "__main__":
    main()
