# AGENTS.md — Imaan Rafiq Design Portfolio

## What this is

A fully static portfolio site with no framework, bundler, or npm dependency.
`site/` is the published copy of the portfolio design and is deployed verbatim
to GitHub Pages by `.github/workflows/pages.yml`.

## Build

```bash
cd build && python3 build.py    # regenerates all HTML from content.py
```

This older generator writes to the repository root and is not used for deployment.
Edit the corresponding files under `site/` to change the published website.

## Layout

- `site/` — published HTML pages, CSS, JavaScript, and the original portfolio images.
- `build/content.py` and `build/build.py` — legacy generator; not used by Pages.
- `assets/css/style.css`, `assets/js/main.js` — hand-written, not generated.

## Legacy generator path depth rule

The retired root generator creates pages at different nesting depths:

| Page | dir depth | asset prefix |
|---|---|---|
| `index.html`, `404.html` | 0 | `` |
| `work/`, `about/`, `contact/` | 1 | `../` |
| `work/<slug>/` | 2 | `../../` |

`nav()`, `head()`, `footer()` and `gallery_html()` take a `depth` matching the
*directory* depth — these are independent of the local `p` variable inside
`build_case()`. Changing one without the other silently breaks asset paths.

## Verification tooling

The scripts below validate the legacy generated site in the repository root,
not the published copy under `site/`.

```bash
python3 scripts/verify.py     # broken images, JS errors, 404s, overflow — all 22 pages
python3 scripts/audit.py      # typography, fonts, layout metrics
python3 scripts/interact.py   # filters, lightbox, mobile nav, reveals
python3 scripts/a11y.py       # no-JS fallback, 404, keyboard order
python3 scripts/coverage.py   # every image used; no dangling references
```

Requires `pip install playwright && playwright install chromium`. Run with
`env -u PLAYWRIGHT_BROWSERS_PATH` if the browser path env var is set.

To preview the published site, run `python3 -m http.server 12000 --directory site`.

## Deploying

- Target repo: `imaanrafiq234-rgb/imaan-rafiq-portfolio` (public, default
  branch `main`).
- `.github/workflows/pages.yml` publishes `site/` on pushes to `main`; Pages
  must use **GitHub Actions** as its source.
- Public URL: `https://imaanrafiq234-rgb.github.io/imaan-rafiq-portfolio/`.
- `.nojekyll` must stay in `site/` so Pages skips Jekyll for the deployed files.
- Do not use `deploy.sh`; it targets the retired root generator and branch-based
  publishing setup.

## Legacy generator gotchas

- `verify.py` must force `img.loading = 'eager'` and wait for `img.complete`
  before checking. Chromium lazy-loads images, so a naive check reports 0 broken
  images while the page is actually full of 404s.
- Exclude `.lightbox` images from audits — the lightbox `<img>` has no `src`
  until opened, which reads as "broken".
- Ignore `.marquee` children in overflow checks; the tracks are intentionally wider
  than the viewport.
- `[data-reveal]` is gated behind the `.js` class on `<html>` so content stays
  visible without JavaScript. Keep that behaviour if you touch the reveal code.
- Two source links are unreachable (see README): `ai.studio` needs Google auth, and
  Canva/Figma return 403. Don't chase them again.

## Content rules

- All imagery must be the designer's own work. **Never generate, substitute or
  invent images.** The portfolio images in `site/assets/img/` are designer-supplied.
- Technical figures in `content.py` are quoted from the client's own material.
  Do not embellish them.
- `assets/img/sketchbook/06.jpg` was removed — the source was a corrupt animated
  GIF that decoded to a blank white frame.

## Supplied workbook plates

- Eight workbook plates arrived as inline images in conversation history. If more
  attachments need decoding, events live in
  `/workspace/conversations/<id>/events/*.json`; the payload is at
  `llm_message.content[*].image_urls[]` as `data:image/png;base64,...`.
- Labeled plates carry a `// PROJECT NN` strapline; that numbering does **not**
  match `PROJECTS` order, so route each plate by subject, not number. Current
  mapping: SmartWalker 03, Professor Layton 07, Med-Diag 08, Aura 03, coffee
  machine, prosthetic hand, pump system, and one unlabeled structure/volumetrics
  study in `portfolio-deck`.
- Plates whose text is set in fine condensed caps may resist Tesseract entirely
  (the structure/volumetrics plate did, at every scale and threshold). Caption
  those from their visual content instead, and don't burn time re-OCRing.
- Several plates are variants of projects that already exist. Prefer appending them
  to the existing gallery over creating a near-duplicate case study.
- Project counts are derived from `PROJECTS` via `NUM_WORDS`; don't reintroduce
  hardcoded totals, and note `.capitalize()` (not `.title()`) so "twenty-one"
  doesn't render as "Twenty-One".