# Imaan Rafiq — Portfolio

The GitHub Pages site is a static copy of the portfolio at
[imaan-rafiq-portfolio-ki813a.freebuff.site](https://imaan-rafiq-portfolio-ki813a.freebuff.site/),
including its original layout, pages, styling, scripts, and portfolio imagery.
The deployable website lives in `site/`.

## Pages

| Path | Description |
| --- | --- |
| `/` | Home — selected work, process, studio, and contact |
| `/work.html` | Filterable project archive |
| `/smartwalker.html` | SmartWalker case study |
| `/caretekk.html` | Caretekk Health case study |
| `/khan.html` | Khan Terminal case study |

## Updating the site

Edit the corresponding HTML, CSS, JavaScript, or image files under `site/`.
The workflow publishes that folder as-is; it does not run the older generator
under `build/`.

## Deploy (GitHub Pages)

The workflow (`.github/workflows/pages.yml`) deploys `site/` to GitHub Pages on
every push to `main`. The site is available at
[https://imaanrafiq234-rgb.github.io/imaan-rafiq-portfolio/](https://imaanrafiq234-rgb.github.io/imaan-rafiq-portfolio/).
Pages is configured to publish using **GitHub Actions**. If that setting is changed,
restore it under **Settings → Pages → Build and deployment → Source**.

## Notes

- The original visual design loads Fraunces, Inter, and JetBrains Mono from Google
  Fonts; all page code and portfolio imagery are served from this repository.
- The site has no contact form; it uses direct email and LinkedIn links.
