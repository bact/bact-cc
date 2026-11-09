#!/usr/bin/env python3
"""Download every /f/... file referenced by the converted content into static/f/.

Reads _export/media-refs.txt (written by wp_convert.py). Resumable: skips files
already present. Slow on purpose (the origin rate-limits with HTTP 429).
Failures are listed in _export/media-missing.txt.
"""
import os, sys, time, urllib.parse as U, urllib.request, urllib.error

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://bact.cc").rstrip("/")

def main():
    refs = [l.strip() for l in open(os.path.join(ROOT, "_export", "media-refs.txt"), encoding="utf-8") if l.strip()]
    missing, got, skipped = [], 0, 0
    for i, ref in enumerate(refs, 1):
        dest = os.path.join(ROOT, "static", ref.lstrip("/"))
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            skipped += 1
            continue
        url = SITE + U.quote(ref)
        for attempt in range(6):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "wp2hugo-migration/1.0"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = r.read()
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(data)
                got += 1
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(5 * (attempt + 1)); continue
                missing.append(f"{e.code} {ref}"); break
            except Exception as e:
                time.sleep(3 * (attempt + 1))
        else:
            missing.append(f"ERR {ref}")
        if i % 25 == 0:
            print(f"{i}/{len(refs)} downloaded={got} skipped={skipped} missing={len(missing)}", flush=True)
        time.sleep(0.4)
    with open(os.path.join(ROOT, "_export", "media-missing.txt"), "w") as f:
        f.write("\n".join(missing) + "\n")
    print(f"done: downloaded={got} skipped={skipped} missing={len(missing)}")

if __name__ == "__main__":
    main()
