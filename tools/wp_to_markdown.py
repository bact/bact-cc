#!/usr/bin/env python3
"""Convert content/**/index.html (WordPress HTML bodies) to Markdown, safely.

Steps
  1. Back up every original file to _export/html-originals/.
  2. pandoc: HTML -> GitHub-flavoured Markdown. Anything Markdown cannot express
     (iframes, tables with attributes, scripts, ...) stays as raw HTML.
  3. Build the site with Hugo and compare each rendered page with the original:
     text, link targets, images, embeds and block structure must all match.
  4. Pages that do not match are restored to their original HTML.
  5. Write MARKDOWN_CONVERSION_REPORT.txt:  full / partial (Markdown + raw HTML) / not converted.

Needs: pandoc, hugo on PATH.   Run after tools/wp_convert.py:
    python3 tools/wp_to_markdown.py
"""
import collections, html, os, re, shutil, subprocess, sys, tempfile, unicodedata
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT = os.path.join(ROOT, "content")
BACKUP = os.path.join(ROOT, "_export", "html-originals")
REPORT = os.path.join(ROOT, "MARKDOWN_CONVERSION_REPORT.txt")
SKIP = {os.path.join("pages", "search")}

# ---------- helpers ----------
def split_fm(text):
    m = re.match(r"---\n(.*?\n)---\n", text, re.S)
    return (text[:m.end()], text[m.end():]) if m else ("", text)

def fm_value(fm, key):
    m = re.search(rf'^{key}: "?(.*?)"?$', fm, re.M)
    return m.group(1) if m else ""

IMG = re.compile(r"<img\b[^>]*>", re.I)
def simplify_img(m):
    tag = m.group(0)
    keep = []
    for attr in ("src", "alt", "title"):
        a = re.search(rf'\s{attr}="([^"]*)"', tag)
        if a: keep.append((attr, a.group(1)))
    if not any(k == "alt" for k, _ in keep):
        keep.append(("alt", ""))
    return "<img " + " ".join(f'{k}="{v}"' for k, v in keep) + ">"

def prep(body):
    body = re.sub(r'(\shref=")([^"]*)(")', lambda m: m.group(1) + m.group(2).strip() + m.group(3), body)   # browsers ignore stray whitespace
    body = IMG.sub(simplify_img, body)                      # drop WP-only presentational attrs (class, data-*, width, srcset...)
    body = re.sub(r'(<a\b[^>]*?)\s(?:class|rel|target|data-[\w-]+)="[^"]*"', r"\1", body)
    body = re.sub(r'(<a\b[^>]*?)\s(?:class|rel|target|data-[\w-]+)="[^"]*"', r"\1", body)
    return body

PROTECT = re.compile(r"<(object|iframe|embed|script|video|audio|form|style)\b.*?</\1\s*>|<embed\b[^>]*/?>"
                     r"|<pre\b[^>]*>(?:(?!</pre>).)*?<(?:strong|em|b|i|a|span|font|u|img)\b.*?</pre\s*>",   # code blocks with inline markup
                     re.S | re.I)

def protect(body):
    """Pandoc drops embeds it cannot represent. Swap them for placeholders and put them back verbatim."""
    blocks = []
    def sub(m):
        blocks.append(re.sub(r"\n\s*\n", "\n", m.group(0)))
        return f"RAWBLOCKQQ{len(blocks)-1}QQ"
    return PROTECT.sub(sub, body), blocks

def restore(md, blocks):
    for i, b in enumerate(blocks):
        ph = f"RAWBLOCKQQ{i}QQ"
        md = re.sub(rf"^{ph}$", lambda _: "\n" + b + "\n", md, flags=re.M)   # alone on a line -> own HTML block
        md = md.replace(ph, b)                                                  # inline use
    return md

LINE_START = [(re.compile(r"^([+*-])(\s)"), r"\\\1\2"), (re.compile(r"^(\d+)([.)])(\s)"), r"\1\\\2\3"),
              (re.compile(r"^(#)"), r"\\\1"), (re.compile(r"^([-=_])(\1{2,}\s*$)"), r"\\\1\2")]

def escape_after_breaks(md):
    """A line after a hard line break that begins like '1) ', '+ ', '* ' would become a list. Escape it."""
    out, prev, fence = [], "", False
    for line in md.split("\n"):
        if line.startswith(("```", "~~~")): fence = not fence
        if not fence and (prev.endswith("  ") or prev.endswith("\\")):
            for rx, rep in LINE_START:
                if rx.match(line):
                    line = rx.sub(rep, line, count=1); break
        out.append(line); prev = line
    return "\n".join(out)

_TILDE_SKIP = re.compile(r"(`[^`\n]*`|<[^>\n]*>|\]\([^)\n]*\))")
def escape_tildes(md):
    """GFM treats ~x~ as strikethrough; WordPress text uses ~ literally (e.g. '~5 km')."""
    out, fence = [], False
    for line in md.split("\n"):
        if line.startswith(("```", "~~~")): fence = not fence
        if not fence and "~" in line:
            parts = _TILDE_SKIP.split(line)
            line = "".join(x if i % 2 else re.sub(r"(?<!~)~(?!~)", r"\\~", x) for i, x in enumerate(parts))
        out.append(line)
    return "\n".join(out)

EMPH_TAG = re.compile(r"<(/?)(strong|b|em|i)\b[^>]*>", re.I)

def pandoc(body, raw_emphasis=False):
    """raw_emphasis: keep <strong>/<em> as inline HTML. Markdown's **bold** cannot be parsed when it touches
    Thai letters or punctuation without a space (CommonMark flanking rules), so this is the fallback."""
    body, blocks = protect(body)
    if raw_emphasis:
        body = EMPH_TAG.sub(lambda m: f"ZZ{'C' if m.group(1) else 'O'}{ {'b':'strong','i':'em'}.get(m.group(2).lower(), m.group(2).lower()) }ZZ", body)
    r = subprocess.run(["pandoc", "-f", "html-native_divs-native_spans", "-t", "gfm", "--wrap=none"],
                       input=body, capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        raise RuntimeError(r.stderr)
    md = restore(escape_tildes(escape_after_breaks(r.stdout.strip())), blocks)
    if raw_emphasis:
        md = re.sub(r"ZZ([OC])(strong|em)ZZ", lambda m: f"<{'/' if m.group(1) == 'C' else ''}{m.group(2)}>", md)
    return md.strip() + "\n"

def raw_html_tags(md):
    md = re.sub(r"^(```|~~~).*?^\1", "", md, flags=re.S | re.M)   # fenced code
    md = re.sub(r"`[^`\n]*`", "", md)                               # inline code
    return collections.Counter(t.lower() for t in re.findall(r"(?<!\\)<([a-zA-Z][\w-]*)(?=[\s>/])[^>]*>", md))

# ---------- comparison ----------
STRUCT = {"img", "iframe", "script", "table", "tr", "blockquote", "ul", "ol", "li", "pre",
          "h1", "h2", "h3", "h4", "h5", "h6", "hr", "sup", "sub", "object", "embed", "video", "audio"}
ALIAS = {"b": "strong", "i": "em", "strike": "del", "s": "del"}
EMPH = ("strong", "em", "del")

class Sig(HTMLParser):
    """Collects what a reader would see: text, link targets (of links that have visible content),
    images, embeds, emphasised text and block structure counts."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text, self.tags, self.links, self.imgs, self.frames = [], collections.Counter(), [], [], []
        self.emph = {k: [] for k in EMPH}
        self._depth = collections.Counter()
        self._skip = 0
        self._a = []            # stack of (href, text_len_at_start, img_count_at_start)
    def handle_starttag(self, tag, attrs):
        tag = ALIAS.get(tag, tag); a = dict(attrs)
        if tag in STRUCT: self.tags[tag] += 1
        if tag in EMPH: self._depth[tag] += 1
        if tag == "a": self._a.append((a.get("href"), sum(map(len, self.text)), len(self.imgs)))
        if tag == "img": self.imgs.append((a.get("src", ""), (a.get("alt") or "").strip()))
        if tag == "iframe": self.frames.append(a.get("src", ""))
        if tag == "script": self._skip += 1
        if tag == "q": self.handle_data("\u201c")          # browsers draw quotes around <q>; pandoc writes them out
    def handle_endtag(self, tag):
        tag = ALIAS.get(tag, tag)
        if tag == "script" and self._skip: self._skip -= 1
        if tag == "q": self.handle_data("\u201d")
        if tag in EMPH and self._depth[tag]: self._depth[tag] -= 1
        if tag == "a" and self._a:
            href, tl, ic = self._a.pop()
            visible = sum(map(len, self.text)) > tl and "".join(self.text)[tl:].strip() or len(self.imgs) > ic
            if href and visible: self.links.append(href)
    def handle_data(self, d):
        if self._skip: return
        self.text.append(d)
        for k in EMPH:
            if self._depth[k]: self.emph[k].append(d)
    @property
    def norm_text(self):
        return re.sub(r"\s+", "", unicodedata.normalize("NFC", "".join(self.text)))
    def emph_text(self, k):
        return re.sub(r"\s+", "", "".join(self.emph[k]))

def sig(h):
    p = Sig(); p.feed(h); p.close(); return p

def rendered_body(page_html):
    m = re.search(r'<div class="content">(.*?)</div>\s*(?:<p class="tags">|</article>)', page_html, re.S)
    return m.group(1) if m else None

def norm_href(h):
    import urllib.parse as U
    return U.unquote(html.unescape(h)).strip()      # %20 / %E0.. vs literal characters are the same link

def compare(orig_body, new_body):
    a, b = sig(orig_body), sig(new_body)
    why = []
    if a.norm_text != b.norm_text:
        import difflib
        ops = [o for o in difflib.SequenceMatcher(None, a.norm_text, b.norm_text, autojunk=False).get_opcodes() if o[0] != "equal"]
        shown = "; ".join(f"{o[0]} «{a.norm_text[o[1]:o[2]][:25]}»->«{b.norm_text[o[3]:o[4]][:25]}»" for o in ops[:3])
        why.append(f"text differs ({len(ops)} spots): {shown}")
    la, lb = [norm_href(x) for x in a.links], [norm_href(x) for x in b.links]
    if la != lb:
        i = next((k for k, (x, y) in enumerate(zip(la, lb)) if x != y), min(len(la), len(lb)))
        why.append(f"link targets differ ({len(la)} -> {len(lb)}): «{(la[i] if i < len(la) else '-')[:60]}» vs «{(lb[i] if i < len(lb) else '-')[:60]}»")
    if [(norm_href(s), t) for s, t in a.imgs] != [(norm_href(s), t) for s, t in b.imgs]: why.append("images differ")
    if a.frames != b.frames: why.append("embeds (iframe) differ")
    for k in EMPH:
        if a.emph_text(k) != b.emph_text(k):
            x, y = a.emph_text(k), b.emph_text(k)
            i = next((j for j, (c, d) in enumerate(zip(x, y)) if c != d), min(len(x), len(y)))
            why.append(f"<{k}> text differs: «{x[max(0,i-10):i+20]}» vs «{y[max(0,i-10):i+20]}»")
    for t in sorted(set(a.tags) | set(b.tags)):
        if a.tags[t] != b.tags[t]: why.append(f"<{t}> count {a.tags[t]} -> {b.tags[t]}")
    return why

def verify(items):
    """Render with Hugo and compare to the original HTML body. Returns {rel: [reasons]} for mismatches."""
    out = tempfile.mkdtemp(prefix="verify-")
    r = subprocess.run(["hugo", "--quiet", "--destination", out], cwd=ROOT, capture_output=True, text=True)
    if r.returncode: sys.exit("hugo failed:\n" + r.stderr)
    failed = {}
    for rel, p, fm, body in items:
        page = os.path.join(out, fm_value(fm, "url").lstrip("/"), "index.html")
        if not os.path.isfile(page):
            failed[rel] = ["rendered page not found"]; continue
        rb = rendered_body(open(page, encoding="utf-8").read())
        why = ["could not locate content in rendered page"] if rb is None else compare(body, rb)
        if why: failed[rel] = why
    shutil.rmtree(out, ignore_errors=True)
    return failed

# ---------- main ----------
def main():
    if os.path.isdir(BACKUP):          # re-run: put the original HTML back first
        for d, _, fs in os.walk(BACKUP):
            for f in fs:
                rel = os.path.relpath(os.path.join(d, f), BACKUP)
                md = os.path.join(CONTENT, os.path.dirname(rel), "index.md")
                if os.path.exists(md): os.remove(md)
                shutil.copy2(os.path.join(d, f), os.path.join(CONTENT, rel))
    items = []   # (relpath, path, fm, body)
    for d, _, fs in os.walk(CONTENT):
        if "index.html" in fs and os.path.relpath(d, CONTENT) not in SKIP:
            p = os.path.join(d, "index.html")
            fm, body = split_fm(open(p, encoding="utf-8").read())
            items.append((os.path.relpath(p, CONTENT), p, fm, body))
    items.sort()
    shutil.rmtree(BACKUP, ignore_errors=True)
    for rel, p, fm, body in items:
        os.makedirs(os.path.dirname(os.path.join(BACKUP, rel)), exist_ok=True)
        shutil.copy2(p, os.path.join(BACKUP, rel))
    kind, info, failed, how = {}, {}, {}, {}
    pending = items
    for mode in ("strict", "raw_emphasis"):
        for rel, p, fm, body in pending:
            md = pandoc(prep(body), raw_emphasis=(mode == "raw_emphasis"))
            open(os.path.join(os.path.dirname(p), "index.md"), "w", encoding="utf-8").write(fm + md)
            if os.path.exists(p): os.remove(p)
            raw = raw_html_tags(md)
            kind[rel] = "partial" if raw else "full"
            info[rel] = raw
            how[rel] = mode
        failed = verify(pending)
        for rel, why in failed.items():          # revert to the original HTML
            d = os.path.dirname(os.path.join(CONTENT, rel))
            os.remove(os.path.join(d, "index.md"))
            shutil.copy2(os.path.join(BACKUP, rel), os.path.join(d, "index.html"))
            kind[rel] = "failed"
        pending = [it for it in pending if it[0] in failed]
        print(mode, "->", collections.Counter(kind.values()), flush=True)
    write_report(items, kind, info, failed, how)

def write_report(items, kind, info, failed, how):
    n = collections.Counter(kind.values())
    meta = {rel: (fm_value(fm, "title"), fm_value(fm, "url")) for rel, _, fm, _ in items}
    L = ["MARKDOWN CONVERSION REPORT", "=" * 72, "",
         f"Total pages checked : {len(items)}",
         f"Fully Markdown      : {n['full']}   (pure Markdown, rendered output verified equal to the original)",
         f"Markdown + raw HTML : {n['partial']}   (converted, but some parts stay as inline HTML - listed in section B)",
         f"NOT converted       : {n['failed']}   (kept as HTML because the Markdown version did not match - section A)", "",
         "Verification = each page is rendered by Hugo and compared with the original: all text, every link",
         "target, every image (src+alt), embeds (iframe), and structure counts (lists, tables, headings, quotes...).",
         "Deliberate normalisation (not counted as loss): WordPress-only image attributes (class, data-*, width, height,",
         "srcset), link classes/rel/target, and whitespace.", ""]
    L += ["", "A. NOT CONVERTED - still HTML (edit as HTML)", "-" * 72]
    for rel in sorted(failed):
        t, u = meta[rel]
        L += [f"* {t}", f"    URL : {u}", f"    File: content/{rel}"] + [f"    Why : {w}" for w in failed[rel][:4]]
    if not failed: L.append("(none)")
    L += ["", "B. CONVERTED BUT CONTAINS RAW HTML (valid Markdown files; listed tags stay as inline HTML)", "-" * 72,
          "   Grouped by the HTML tag that could not be expressed in Markdown. A page appears under each tag it uses.", ""]
    part = [r for r in sorted(kind) if kind[r] == "partial"]
    bytag = collections.defaultdict(list)
    for rel in part:
        for k, v in info[rel].items(): bytag[k].append((rel, v))
    HINT = {"span": "styled text, e.g. <span class=\"small\"> (no Markdown equivalent)", "u": "underline", "sup": "superscript",
            "sub": "subscript", "iframe": "embedded video/map/widget", "object": "legacy Flash/object embed", "embed": "legacy embed",
            "script": "script tag (e.g. Twitter widget)", "figure": "image with caption", "figcaption": "image caption",
            "img": "image with extra attributes", "table": "complex table", "font": "legacy <font> styling", "center": "centered block"}
    for k, rows in sorted(bytag.items(), key=lambda kv: -len(kv[1])):
        L += ["", f"B-{k}: <{k}> in {len(rows)} pages" + (f"  - {HINT[k]}" if k in HINT else "")]
        for rel, v in rows:
            t, u = meta[rel]
            L.append(f"    {u}   [x{v}]  content/{rel[:-5]}.md   ({t[:60]})")
    if not part: L.append("(none)")
    open(REPORT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(dict(n))

if __name__ == "__main__":
    main()
