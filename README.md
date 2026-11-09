# bact.cc — static site (Hugo + Cloudflare Pages)

Static version of <https://bact.cc>, migrated from WordPress.
2,731 posts · 4 pages · 3,530 archived comments · 14 categories · 1,414 tags · all original URLs preserved.

## Layout

| Path | What |
|---|---|
| `hugo.toml` | Site config (permalinks, taxonomies, menu) |
| `content/<year>/<slug>/index.html` | Posts. Body is the original WordPress HTML (lossless). `comments.json` beside it holds archived comments |
| `content/pages/*` | About, Courses, Media, Publications |
| `content/categories`, `content/tag` | Term titles/descriptions |
| `layouts/`, `assets/css/` | Own minimal theme (no third‑party theme/submodule) |
| `static/f/` | Uploaded files — same `/f/YYYY/MM/…` URLs as WordPress |
| `static/_redirects`, `static/_headers`, `static/robots.txt` | Cloudflare Pages config |
| `functions/index.js` | Optional: `/?p=123` old short‑link redirect |
| `tools/` | Migration + verification scripts |

## URL preservation

| Old WordPress URL | Now |
|---|---|
| `/2023/some-slug/` (and Thai slugs) | same (`url:` is set explicitly in each post) |
| `/about/`, `/courses/`, `/media/`, `/pub/` | same |
| `/on/<category>/`, `/tag/<tag>/`, `/page/N/` | same |
| `/2023/` yearly archive | same |
| `/2023/08/` monthly archive | 301 → `/2023/` |
| `/f/2022/10/file.pdf` uploads | same |
| `/feed/`, `/on/x/feed/`, `/tag/x/feed/`, `/comments/feed/` | 301 → Hugo RSS |
| `/sitemap.xml` / `/wp-sitemap.xml` | Hugo sitemap |
| `/?p=ID` short links (wp.me) | Pages Function (`functions/index.js`) |
| Jetpack image CDN (`i0.wp.com/bact.cc/f/…`) | rewritten to local `/f/…` |

Run `python3 tools/check_links.py` after `hugo` — it verifies every old URL exists and every internal link/image resolves.

## Local use

```sh
hugo server            # http://localhost:1313  (Hugo extended ≥ 0.152)
hugo --gc --minify     # build to ./public
python3 tools/check_links.py
```

Write a new post: create `content/2026/my-slug/index.md`:

```yaml
---
title: "My title"
date: 2026-01-31T10:00:00+07:00
type: post
url: /2026/my-slug/
categories: [misc]
tag: [hugo]
---
Markdown here.
```
(Use `hugo new` or copy an existing post. Note the tag key is `tag`, and `type: post` is required.)
If you start a year that has no `content/<year>/_index.md`, copy one from another year (it makes `/<year>/` exist).

## Deploying (Cloudflare Pages, free plan)

1. Push this repo to GitHub.
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick the repo.
3. Build settings: framework preset **Hugo**, build command `hugo --gc --minify`, output dir `public`,
   environment variable `HUGO_VERSION = 0.152.2` (plain text, not a secret).
4. Deploy, check the `*.pages.dev` preview, then **Custom domains → bact.cc** (see cutover below).

No API tokens, passwords or keys are needed in the repo or in GitHub. Cloudflare reads the repo via its GitHub App.

## Cutover checklist (do in this order)

1. **Before touching DNS**: take a full WordPress backup somewhere private (not GitHub) — the REST export here has only published content. Drafts, private posts, unpublished revisions, user accounts, plugin data are *not* included.
2. Test the `*.pages.dev` site: spot‑check posts, images, PDFs, `/feed/`, `/on/…`, Thai URLs.
3. Cloudflare apex domains need the zone on Cloudflare: add `bact.cc` as a site, and **copy every existing DNS record first — especially MX/SPF/DKIM/DMARC if you receive mail on this domain** (Cloudflare’s import usually catches them; verify).
4. Switch nameservers at the registrar; add the custom domain in Pages; wait for the certificate.
5. Re‑verify, submit `https://bact.cc/sitemap.xml` in Google/Bing Search Console (URLs are unchanged, so rankings should hold).
6. Keep WordPress hosting for a couple of weeks as fallback, then cancel it. Keep the domain registration!

## Not carried over (by design)

* **Commenting** — static sites can't accept comments. Existing 3,530 comments are archived read‑only; commenter emails were never exported and any email address typed into a comment body is masked. To re‑enable comments later, add e.g. Giscus (GitHub Discussions) in `layouts/post/single.html`.
* **Jetpack Stats** — replace with Cloudflare Web Analytics (free, cookie‑less; toggle in the Pages dashboard).
* **Site search** — not included; Pagefind is the usual free static option.
* **WordPress admin, plugins, xmlrpc, wp-json** — gone.
* Third‑party embeds (YouTube etc.) are untouched; some very old ones (Amazon widgets, Digg) were already dead upstream.

## Re‑running the migration

```sh
python3 tools/wp_export.py https://bact.cc   # public REST API only, no credentials → _export/
python3 tools/wp_convert.py                  # → content/ (overwrites it!)
python3 tools/fetch_media.py                 # → static/f/ (resumable)
```
`_export/` is git‑ignored. Do not re‑run `wp_convert.py` after hand‑editing content — it regenerates `content/`.

## Security notes

* Everything in this repo was already public on bact.cc. The exporter requests only public endpoints and a field allow‑list (no emails, no Jetpack/plugin metadata).
* `.gitignore` blocks `.env*`, `wp-config.php`, SQL dumps, WXR exports, `.wrangler/`, keys.
* If you ever need Cloudflare/GitHub tokens (e.g. wrangler CLI), keep them in your shell/CI secret store, never in files here.

## Files too big for Cloudflare Pages (25 MiB per-file limit)

These were NOT committed (a single oversized file makes the whole Pages deploy fail). Links to them
currently 404 until you host them elsewhere (e.g. a Cloudflare R2 bucket on a subdomain, free tier)
and add a 301 for each in `static/_redirects`:

- `/f/2020/04/20171215-good-man-concluding-present.pdf`
- `/f/2020/10/fcem-media-governance-report-bangkok-new-media-agenda.zip`
- `/f/2022/10/202012-ai-gov-framework-dga.pdf`

Alternatively compress the PDFs below 25 MiB and drop them back into `static/f/…`.
`tools/fetch_media.py` will re-download them (`.gitignore` entries below stop them being committed by accident).
