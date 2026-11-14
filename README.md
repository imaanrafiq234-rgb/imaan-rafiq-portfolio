# Imaan Rafiq — Portfolio

A static portfolio site for Imaan Rafiq (product & industrial designer). Built as a
small Python generator in `build/`, with all copy and project data in
`build/content.py`.

## Pages

| Path | Description |
| --- | --- |
| `/` | Home — hero, selected work, capabilities |
| `/work/` | Archive — all 21 projects with tag filters |
| `/work/<slug>/` | Project case study — overview, stats, sections, gallery, prev/next |
| `/about/` | Studio — capabilities and how I work |
| `/contact/` | Contact details (email + LinkedIn) |
| `/404.html` | Not-found page |

## Rebuild

The generated HTML is committed, so the site deploys as-is. To regenerate after
editing content or templates:

```bash
cd build
SITE_URL=https://<user>.github.io/<repo> python3 build.py
```

`SITE_URL` controls the absolute URLs in `sitemap.xml` and `robots.txt`.

## Deploy (GitHub Pages)

The included workflow (`.github/workflows/pages.yml`) publishes the repository root
to GitHub Pages on every push to `main`. In the repository settings, set
**Pages → Build and deployment → Source** to **GitHub Actions**.

## Notes

- No contact form. A static host cannot process one, so direct `mailto:` and
  LinkedIn links are used instead.
- The phone number is intentionally omitted from the site.
- Fonts (Inter, Instrument Serif) are self-hosted under `assets/fonts/`.
