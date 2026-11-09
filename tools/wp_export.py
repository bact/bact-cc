#!/usr/bin/env python3
"""Export PUBLIC content of a WordPress site through its REST API.

No credentials are used or accepted: only what any visitor can already read
(published posts/pages, public terms, approved comments, media library).
Output goes to ./_export (git-ignored) as raw JSON.

    python3 tools/wp_export.py https://bact.cc
"""
import json, os, sys, time, urllib.request

KINDS = ["posts", "pages", "categories", "tags", "media", "comments", "users"]
# Only the fields we need. Keeps private-ish plugin metadata (Jetpack etc.) out.
FIELDS = {
    "posts": "id,date,modified,slug,status,link,title,content,excerpt,categories,tags,featured_media,sticky,format",
    "pages": "id,date,modified,slug,status,link,title,content,excerpt,parent,featured_media,menu_order",
    "categories": "id,slug,name,description,count,parent,link",
    "tags": "id,slug,name,description,count,link",
    "media": "id,date,slug,source_url,mime_type,post,title,media_details",
    "comments": "id,post,parent,author_name,author_url,date,content,status,type",
    "users": "id,slug,name,link",   # no email: not exposed publicly, and never requested
}

def get(url, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "wp2hugo-migration/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r), r.headers
        except Exception as e:
            print(f"  retry {i+1}: {e}", file=sys.stderr)
            time.sleep(3 * (i + 1))
    sys.exit(f"giving up on {url}")

def main():
    site = (sys.argv[1] if len(sys.argv) > 1 else "https://bact.cc").rstrip("/")
    out = os.path.join(os.path.dirname(__file__), "..", "_export")
    os.makedirs(out, exist_ok=True)
    for kind in KINDS:
        items, page = [], 1
        while True:
            url = f"{site}/wp-json/wp/v2/{kind}?per_page=100&page={page}&context=view&_fields={FIELDS[kind]}"
            data, hdr = get(url)
            items += data
            pages = int(hdr.get("X-WP-TotalPages", 1))
            print(f"{kind}: page {page}/{pages} ({len(items)})", flush=True)
            if page >= pages:
                break
            page += 1
            time.sleep(0.3)
        with open(os.path.join(out, f"{kind}.json"), "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
