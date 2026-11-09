#!/usr/bin/env python3
"""Verify the built site in ./public.

 1. URL parity: every URL of the old WordPress site (from _export/, if present)
    must exist in public/ (or be covered by an explicit _redirects rule).
 2. Internal links: every root-relative href/src in the built HTML must resolve
    to a file, a directory index, or a _redirects rule.
Exit code 1 if anything is dead.   Usage: python3 tools/check_links.py
"""
import json, os, re, sys, urllib.parse as U
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUB = os.path.join(ROOT, "public")

def redirect_rules():
    rules = []
    p = os.path.join(ROOT, "static", "_redirects")
    for l in open(p, encoding="utf-8"):
        l = l.split("#")[0].strip()
        if l:
            src = l.split()[0]
            rules.append(re.compile("^" + re.sub(r":\w+", "[^/]+", re.escape(src).replace(r"\*", ".*").replace(r"\:", ":")) + "$"))
    return rules
RULES = redirect_rules()

def exists(path):
    path = U.unquote(path.split("#")[0].split("?")[0])
    if not path.startswith("/"):
        return True
    f = os.path.join(PUB, path.lstrip("/"))
    if os.path.isfile(f) or os.path.isfile(os.path.join(f, "index.html")):
        return True
    return any(r.match(path) for r in RULES)

def main():
    if not os.path.isdir(PUB):
        sys.exit("run `hugo` first")
    bad = 0
    exp = os.path.join(ROOT, "_export")
    if os.path.isdir(exp):
        old = []
        for kind, pre in (("posts", ""), ("pages", ""), ("categories", ""), ("tags", "")):
            for it in json.load(open(os.path.join(exp, kind + ".json"), encoding="utf-8")):
                if kind == "tags" and it["count"] == 0:
                    continue
                old.append(U.urlparse(it["link"]).path)
        missing = [u for u in old if not exists(u)]
        print(f"[parity] old URLs checked: {len(old)}, missing: {len(missing)}")
        for u in missing[:30]: print("   MISSING", u)
        bad += len(missing)
    pat = re.compile(r"""(?:href|src)=["']?(/[^"'\s>#]*)""")
    seen, dead = set(), {}
    pages = 0
    for d, _, fs in os.walk(PUB):
        for fn in fs:
            if not fn.endswith(".html"): continue
            pages += 1
            page = os.path.join(d, fn)
            for ln in pat.findall(open(page, encoding="utf-8", errors="replace").read()):
                if ln.startswith("//") or ln in seen: continue
                seen.add(ln)
                if not exists(ln):
                    dead.setdefault(ln, os.path.relpath(page, PUB))
    print(f"[links] html pages: {pages}, unique internal links: {len(seen)}, dead: {len(dead)}")
    for l, p in list(dead.items())[:60]: print("   DEAD", l, " <-", p)
    bad += len(dead)
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
