#!/usr/bin/env python3
"""Auto-fix Markdown style with markdownlint-cli2, but only keep fixes that do not change the rendered page.

  1. Build the site (before).   2. markdownlint-cli2 --fix.   3. Build again (after).
  4. For every changed file compare the rendered article: text, links, images, embeds, emphasis, structure.
     If anything differs, the file is restored from git (it must be committed before running this).

    python3 tools/lint_markdown.py          # needs hugo + npm install done
"""
import importlib.util, os, shutil, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
spec = importlib.util.spec_from_file_location("w2m", os.path.join(ROOT, "tools", "wp_to_markdown.py"))
w2m = importlib.util.module_from_spec(spec); spec.loader.exec_module(w2m)

def run(*cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kw)

def build(dest):
    r = run("hugo", "--quiet", "--destination", dest)
    if r.returncode: sys.exit("hugo failed:\n" + r.stderr)

def page_for(dest, path):
    fm, _ = w2m.split_fm(open(os.path.join(ROOT, path), encoding="utf-8").read())
    return os.path.join(dest, w2m.fm_value(fm, "url").lstrip("/"), "index.html")

def main():
    if run("git", "status", "--porcelain", "content").stdout.strip():
        sys.exit("commit or stash changes under content/ first (rejected fixes are restored with git checkout)")
    before, after = tempfile.mkdtemp(prefix="lint-before-"), tempfile.mkdtemp(prefix="lint-after-")
    build(before)
    run("npx", "markdownlint-cli2", "--fix")
    changed = [l for l in run("git", "diff", "--name-only", "content").stdout.splitlines() if l.endswith(".md")]
    print(f"markdownlint changed {len(changed)} files; verifying rendered output...")
    build(after)
    reverted = {}
    for f in changed:
        a, b = page_for(before, f), page_for(after, f)
        if not (os.path.isfile(a) and os.path.isfile(b)):
            continue   # e.g. term pages / non-article files: not part of the comparison
        ra = w2m.rendered_body(open(a, encoding="utf-8").read())
        rb = w2m.rendered_body(open(b, encoding="utf-8").read())
        if ra is None or rb is None:
            continue
        why = w2m.compare(ra, rb)
        if why:
            reverted[f] = why
    for f in reverted:
        run("git", "checkout", "--", f)
    shutil.rmtree(before, ignore_errors=True); shutil.rmtree(after, ignore_errors=True)
    print(f"kept fixes in {len(changed) - len(reverted)} files; reverted {len(reverted)} that changed the rendering")
    for f, why in reverted.items():
        print("  reverted", f, "-", why[0][:100])
    rest = run("npx", "markdownlint-cli2")
    print("remaining findings after fix:\n" + (rest.stderr or rest.stdout).strip().splitlines()[-1] if (rest.stderr or rest.stdout).strip() else "none")

if __name__ == "__main__":
    main()
