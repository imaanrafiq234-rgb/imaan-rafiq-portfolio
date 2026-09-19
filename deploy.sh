#!/usr/bin/env bash
# One-shot publish for the portfolio site.
#
# Usage:
#   ./deploy.sh github.com/you/your-repo
#
# Requires a token with Contents:write on that repo. Set it as GH_TOKEN,
# or let git prompt / use your cached credentials.
set -euo pipefail

REMOTE="${1:?usage: deploy.sh <github.com/owner/repo>}"
SITE_URL="${2:-}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

# Rebuild so sitemap.xml / robots.txt carry real absolute URLs.
if [ -n "$SITE_URL" ]; then
  echo "==> Building with SITE_URL=$SITE_URL"
  (cd build && SITE_URL="$SITE_URL" python3 build.py >/dev/null)
fi

echo "==> Verifying assets"
python3 scripts/coverage.py

git add -A
git diff --cached --quiet || git commit -q -m "Rebuild for production deploy"

if [ -n "${GH_TOKEN:-}" ]; then
  URL="https://x-access-token:${GH_TOKEN}@${REMOTE}.git"
else
  URL="https://${REMOTE}.git"
fi

echo "==> Pushing to $REMOTE"
git push "$URL" master:main

cat <<'DONE'

Pushed. Enable hosting once, at:
  https://github.com/<owner>/<repo>/settings/pages
  Source = "Deploy from a branch", Branch = main, Folder = / (root)

The site then publishes to:
  https://<owner>.github.io/<repo>/
DONE