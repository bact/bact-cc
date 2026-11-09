#!/usr/bin/env python3
"""Convert the JSON in ./_export into Hugo content, preserving URLs.

Design choices
  * Post bodies are kept as the original rendered HTML (index.html page
    bundles). This is lossless: no HTML->Markdown conversion bugs across
    ~2,700 posts. New posts can be plain Markdown (see README).
  * Every page gets an explicit `url:` equal to its WordPress permalink.
  * Comments are archived as static JSON next to each post (emails masked).
  * Jetpack/Photon image URLs (i0.wp.com/bact.cc/f/...) are rewritten to
    local /f/... paths; the files are fetched by tools/fetch_media.py.

    python3 tools/wp_convert.py
"""
import html, json, os, re, shutil, sys, urllib.parse as U
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXP = os.path.join(ROOT, "_export")
CONTENT = os.path.join(ROOT, "content")
TZ = "+07:00"  # site timezone is Asia/Bangkok (no DST)
SITE_HOSTS = r"(?:www\.)?bact\.cc"

def load(n):
    with open(os.path.join(EXP, n + ".json"), encoding="utf-8") as f:
        return json.load(f)

def y(v):  # JSON is a valid YAML flow style: safe quoting for free
    return json.dumps(v, ensure_ascii=False)

def front_matter(d):
    return "---\n" + "".join(f"{k}: {y(v)}\n" for k, v in d.items() if v not in (None, "", [])) + "---\n"

def plain(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()

def thai_ratio(s):
    t = plain(s)
    return sum("฀" <= c <= "๿" for c in t) / max(1, len(t))

# ---------- HTML cleanup ----------
PHOTON = re.compile(r"https?://i[0-3]\.wp\.com/([^\"'\s<>?]+)(?:\?[^\"'\s<>]*)?")
def _unphoton(m):
    path = m.group(1)
    host, _, rest = path.partition("/")
    if re.fullmatch(SITE_HOSTS, host):
        return "/" + rest
    return "https://" + path

def clean_html(h):
    h = PHOTON.sub(_unphoton, h)                                   # Jetpack CDN -> origin/local
    h = re.sub(r"https?://" + SITE_HOSTS + r"/", "/", h)          # own absolute links -> root-relative
    h = re.sub(r"\s(?:srcset|sizes)=\"[^\"]*\"", "", h)           # photon-sized variants
    h = re.sub(r"<script[^>]+digg\.com[^>]*></script>", "", h)    # dead third-party script
    h = re.sub(r'(<iframe[^>]+src=")http://((?:www\.)?(?:youtube|youtube-nocookie|vimeo|player\.vimeo)\.com)', r"\1https://\2", h)
    h = re.sub(r'(<img[^>]+src=")http://(upload\.wikimedia\.org)', r"\1https://\2", h)
    h = re.sub(r"<img(?![^>]*\sloading=)", '<img loading="lazy"', h)
    h = h.replace("/wp-content/uploads/", "/f/")
    # categories deleted from WordPress long ago (already HTTP 500 on the live site): keep text, drop link
    h = re.sub(r'<a href="/on/(?:bangkokmetro|whatwewant)/">(.*?)</a>', r"\1", h)
    return h

EMAIL = re.compile(r"[\w.+-]+@([\w-]+(?:\.[\w-]+)+)")
def mask_email(h):  # comments are written by third parties: never republish their addresses
    return EMAIL.sub(lambda m: "[email hidden]@" + m.group(1), h)

LOCAL = re.compile(r"""(?:src|href)=["'](/f/[^"']+)["']""")

def slug_dir(slug, wpid):
    s = U.unquote(slug)
    return s if s.isascii() and re.fullmatch(r"[a-z0-9_-]+", s) else f"p{wpid}"

def link_slug(t):
    return U.unquote(U.urlparse(t["link"]).path.rstrip("/").rsplit("/", 1)[-1])

def main():
    posts, pages = load("posts"), load("pages")
    cats, tags = load("categories"), load("tags")
    media, comments = load("media"), load("comments")
    mid2url = {m["id"]: urlpath(m["source_url"]) for m in media}
    # NB: the slug that appears in the public URL is the source of truth. For some
    # categories the REST "slug" differs from the permalink (e.g. /on/coling/).
    catslug = {c["id"]: link_slug(c) for c in cats}
    tagslug = {t["id"]: link_slug(t) for t in tags}

    shutil.rmtree(CONTENT, ignore_errors=True)
    os.makedirs(CONTENT)
    refs, by_post_comments = set(), defaultdict(list)
    for c in comments:
        if c["status"] == "approved":
            by_post_comments[c["post"]].append(c)

    def write(path, text, mode="w"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, mode, encoding="utf-8") as f:
            f.write(text)

    # home + year archives
    write(f"{CONTENT}/_index.md", front_matter({"title": "Home", "type": "home"}))
    years = set()

    idmap, month_redirects = {}, set()
    for p in sorted(posts, key=lambda p: p["date"]):
        if p["status"] != "publish":
            continue
        path = U.unquote(U.urlparse(p["link"]).path)          # e.g. /2018/ทำเว็บ-.../
        year = path.split("/")[1]
        years.add(year)
        month_redirects.add(p["date"][:7])
        body = clean_html(p["content"]["rendered"])
        refs.update(LOCAL.findall(body))
        d = slug_dir(p["slug"], p["id"])
        base = f"{CONTENT}/{year}/{d}"
        feat = mid2url.get(p["featured_media"])
        if feat:
            refs.add(feat)
        fm = {
            "title": html.unescape(p["title"]["rendered"]),
            "date": p["date"] + TZ,
            "lastmod": p["modified"] + TZ,
            "type": "post",
            "url": path,
            "description": plain(p["excerpt"]["rendered"])[:300],
            "categories": [catslug[i] for i in p["categories"] if i in catslug],
            "tag": [tagslug[i] for i in p["tags"] if i in tagslug],
            "image": feat,
            "textlang": "th" if thai_ratio(body) > 0.25 else "en",
            "wpid": p["id"],
        }
        write(f"{base}/index.html", front_matter(fm) + body + "\n")
        idmap[str(p["id"])] = path
        cs = by_post_comments.get(p["id"])
        if cs:
            write(f"{base}/comments.json", json.dumps(thread(cs), ensure_ascii=False, indent=1))

    for y_ in sorted(years):
        write(f"{CONTENT}/{y_}/_index.md", front_matter({"title": y_, "type": "archive", "url": f"/{y_}/"}))

    for pg in pages:
        if pg["status"] != "publish":
            continue
        path = U.unquote(U.urlparse(pg["link"]).path)
        body = clean_html(pg["content"]["rendered"])
        refs.update(LOCAL.findall(body))
        d = slug_dir(pg["slug"], pg["id"])
        fm = {"title": html.unescape(pg["title"]["rendered"]), "date": pg["date"] + TZ,
              "lastmod": pg["modified"] + TZ, "type": "page", "url": path,
              "textlang": "th" if thai_ratio(body) > 0.25 else "en", "wpid": pg["id"],
              "weight": pg.get("menu_order") or None}
        write(f"{CONTENT}/pages/{d}/index.html", front_matter(fm) + body + "\n")
        idmap[str(pg["id"])] = path

    # taxonomy term pages (keep WP display names/descriptions); skip unused tags
    for c in cats:
        write(f"{CONTENT}/categories/{U.unquote(c['slug'])}/_index.md",
              front_matter({"title": html.unescape(c["name"]), "slug": link_slug(c),
                            "description": plain(c["description"])}))
    for t in tags:
        if t["count"] > 0:
            write(f"{CONTENT}/tag/{U.unquote(t['slug'])}/_index.md",
                  front_matter({"title": html.unescape(t["name"]), "description": plain(t["description"])}))

    # whole media library + site icon are carried over too
    for m in media:
        refs.add(urlpath(m["source_url"]))
        for s in (m["media_details"].get("sizes") or {}).values():
            pass  # resized variants are not needed: markup now references the original
    refs = {r for r in refs if r.startswith("/f/")}
    os.makedirs(os.path.join(ROOT, "_export"), exist_ok=True)
    write(os.path.join(EXP, "media-refs.txt"), "\n".join(sorted(refs)) + "\n")
    os.makedirs(os.path.join(ROOT, "functions"), exist_ok=True)
    write(os.path.join(ROOT, "functions", "_idmap.json"), json.dumps(idmap, ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(EXP, "months.txt"), "\n".join(sorted(month_redirects)) + "\n")
    print(f"posts={len(posts)} pages={len(pages)} cats={len(cats)} tags_used={sum(t['count']>0 for t in tags)} "
          f"comments={sum(len(v) for v in by_post_comments.values())} media_refs={len(refs)}")

def urlpath(u):
    return U.unquote(U.urlparse(u).path)

def thread(cs):
    nodes = {c["id"]: {"id": c["id"], "author": c["author_name"] or "Anonymous",
                       "url": c["author_url"] or "", "date": c["date"] + TZ,
                       "html": mask_email(clean_html(c["content"]["rendered"])), "replies": []} for c in cs}
    roots = []
    for c in sorted(cs, key=lambda c: c["date"]):
        (nodes[c["parent"]]["replies"] if c["parent"] in nodes else roots).append(nodes[c["id"]])
    return roots

if __name__ == "__main__":
    main()
