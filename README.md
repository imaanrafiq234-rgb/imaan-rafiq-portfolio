# Imaan Rafiq — Design Portfolio

A fully static, production-ready portfolio site for **Imaan Rafiq**, product and
industrial designer (BSc Product Design & Technology, Aston University).

No build step or server runtime is required to *view* the site — open
`index.html`, or serve the folder with any static host.

---

## Running it

```bash
# any static server works
python3 -m http.server 12000
# then open http://localhost:12000
```

Deploy by uploading the project root to Netlify, Vercel, GitHub Pages, Cloudflare
Pages, S3 — anything that serves files. There is no backend.

Set `SITE_URL` when building so the sitemap and robots file carry absolute URLs:

```bash
cd build && SITE_URL=https://imaanrafiq.design python3 build.py
```

---

## What's in it

| Page | Purpose |
|---|---|
| `/` | Hero, marquee, all 18 projects, approach, headline stats, practice statement |
| `/work/` | Full archive with discipline filters |
| `/work/<slug>/` | 18 individual case studies |
| `/about/` | Studio, capabilities, working method, portfolio plates |
| `/contact/` | Contact details and what the designer is looking for |
| `/404.html` | Not-found page |

> Note: `/contact/` intentionally has **no form**. A static host cannot process
> one, and shipping a form that silently drops messages is worse than no form.
> Direct `mailto:` / `tel:` links are used instead. To add a form, point it at a
> service such as Formspree or Netlify Forms.

---

## The 18 projects

**Flagship**
1. **SmartWalker** — intelligent rollator, final year project, James Dyson Award 2026 entry
2. **LOOM** — end-to-end e-commerce UX/UI
3. **Nova Ledger** — dark-mode fintech concept carousel

**Product design**
4. **Cobra Coffee Machine** — form, flow and internal architecture
5. **Cocomelon Pacifier** — child safety, materials and circular economy
6. **Rugged Speaker** — first university project

**Design engineering**
7. **Prosthetic Hand** — designed around how a chef actually works
8. **Pump System** — the engineering paper trail
9. **Breathalyser** — sketch, CAD, render

**Concept & form**
10. **Professor Layton Device** — world-building through form
11. **Audi R8 Form Analysis** — form is function
12. **Underwater Drone** — Golden Snitch inspired
13. **Pizza Oven** — sketch, mockup, render
14. **Embedded Systems Series** — technical communication
15. **Sketchbook** — why I still can't give it up
16. **Form Analysis & CAD** — toaster breakdown and CAD workflow
17. **Portfolio Deck** — the printed book
18. **Design Engineering Graduand** — background

---

## Imagery

Every photograph, render, sketch and CAD plate in `assets/img/` is **Imaan Rafiq's
own work**, taken from the supplied LinkedIn project write-ups, the printed
portfolio deck, and the Figma/Canva references.

**No images were generated, substituted or invented.** The single exception is
`assets/img/avatar.jpg`, which is the designer's own LinkedIn profile photo.

Two supplied links could not be harvested:

- `ai.studio/apps/...` — requires an authenticated Google account
- `canva.link/...` and the Figma design files — returned HTTP 403 to server-side fetches

`scripts/coverage.py` asserts that **every** file in `assets/img/` is referenced
by a built page, and that no page references a file that does not exist.

---

## Design system

- **Type** — `Instrument Serif` for display, `Inter` for everything else.
  Both self-hosted as `woff2` in `assets/fonts/` (no third-party font CDN).
- **Palette** — near-black `#0c0c0d`, bone `#f2efe9`, lime accent `#c8f24e`.
- **Motion** — IntersectionObserver reveals, a drifting hero plate, a paused-on-hover
  marquee, and a film-grain overlay. All respect `prefers-reduced-motion`.
- **Reveal safety** — `[data-reveal]` elements are only hidden when `<html>` has the
  `.js` class, so the site is fully readable with JavaScript disabled.

---

## Project structure

```
.
├── index.html                 # generated
├── 404.html                   # generated
├── work/
│   ├── index.html             # generated archive
│   └── <18 slugs>/index.html  # generated case studies
├── about/index.html           # generated
├── contact/index.html         # generated
├── assets/
│   ├── css/style.css          # design system + layout (hand-written)
│   ├── js/main.js             # nav, reveals, filters, lightbox (hand-written)
│   ├── fonts/                 # self-hosted Inter + Instrument Serif
│   └── img/<project>/         # the designer's own work
├── build/
│   ├── content.py             # all copy and project data
│   └── build.py               # static site generator
└── scripts/                   # verification tooling
```

The generated HTML is committed so the site can be deployed as-is. If you edit
`content.py` or `build.py`, regenerate:

```bash
cd build && python3 build.py
```

---

## Verification

```bash
# requires: pip install playwright && playwright install chromium
python3 scripts/verify.py      # every page: broken images, JS errors, failed requests, overflow
python3 scripts/audit.py       # typography, fonts, layout metrics
python3 scripts/interact.py    # filters, lightbox, mobile nav, reveal behaviour
python3 scripts/a11y.py        # no-JS fallback, 404, keyboard tab order
python3 scripts/coverage.py    # every image used, no dangling references
```

Last full run: **22/22 pages clean** — zero broken images, zero console errors,
zero failed requests, zero horizontal overflow. Image coverage 117/117.

---

## Accessibility & robustness

- Semantic landmarks, a single `<h1>` per page, descriptive `alt` text on every image
- Visible focus rings; filters and lightbox are fully keyboard operable
- Lightbox supports `Esc`, `←`/`→`, backdrop click and touch swipe
- Works without JavaScript (content is never hidden behind JS-only reveals)
- Print stylesheet strips the nav, grain and lightbox

---

## Content source

All copy was written from the client's own supplied material — the LinkedIn
project write-ups and the printed portfolio deck. Technical figures (weights,
power draws, tolerances, amplifier gains) are quoted directly from that material.