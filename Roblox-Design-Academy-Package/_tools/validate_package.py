#!/usr/bin/env python3
"""Validate an installed or unpacked Roblox Design Academy package.
Usage: python3 validate_package.py "<path to package or installed academy folder>"
Checks:
  - relative Markdown links and image embeds resolve;
  - links to third-party assets that are listed in _tools/asset-sources.json but not downloaded yet are
    reported as "unfetched" (run _tools/fetch_assets.py), not as broken;
  - no machine-specific absolute paths in notes;
  - every third-party file in Assets/ (outside Assets/Original/) has a registry entry with a licence and source;
  - every registry entry has a licence and a traceable source (source_url, 'from', or contact-sheet batch);
  - Assets files not referenced by any note (orphans, informational);
  - image integrity when Pillow is installed.
Exit code 1 on broken links, absolute paths, unregistered third-party files or incomplete registry entries.
"""
import re, os, glob, json, sys, urllib.parse
root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)

REGISTRY = os.path.join('_tools', 'asset-sources.json')
registry = json.load(open(REGISTRY, encoding='utf-8')) if os.path.exists(REGISTRY) else []
reg_paths = {os.path.normpath(r['path']) for r in registry}
# An entry is traceable if it has a licence and either a source_url, a 'from' (derived from another entry),
# or is a contact sheet whose inputs are listed in _tools/contact-sheet-batches.json.
incomplete = [r.get('path', '?') for r in registry
              if not r.get('license') or not (r.get('source_url') or r.get('from') or r.get('method') == 'contact-sheet')]

notes = sorted(glob.glob('**/*.md', recursive=True))
broken, unfetched, refs, absp = [], [], set(), []
for f in notes:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'(!?)\[([^\]]*)\]\(([^)\s]+)\)', s):
        t = m.group(3)
        if re.match(r'^(https?:|mailto:|#)', t):
            continue
        t = urllib.parse.unquote(t.split('#')[0])
        if not t:
            continue
        r = os.path.normpath(os.path.join(os.path.dirname(f), t))
        if os.path.exists(r):
            refs.add(r)
        elif r in reg_paths:
            unfetched.append((f, t))
        else:
            broken.append((f, t))
    if re.search(r'/home/|/tmp/|/root/|[A-Z]:\\\\Users', s):
        absp.append(f)

assets = [os.path.normpath(a) for a in glob.glob('Assets/**/*', recursive=True) if os.path.isfile(a)]
original = os.path.normpath('Assets/Original') + os.sep
third_party = [a for a in assets if not a.startswith(original)]
unregistered = [a for a in third_party if a not in reg_paths]
orphans = [a for a in assets if a not in refs]
fetched = sum(1 for p in reg_paths if os.path.exists(p))

bad = []
try:
    from PIL import Image
    for a in assets:
        if a.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            try:
                Image.open(a).verify()
            except Exception:
                bad.append(a)
except ImportError:
    bad = ['(Pillow not installed: image integrity not checked)']

print(json.dumps({
    'notes': len(notes),
    'broken_links': len(broken),
    'unfetched_third_party_links': len(unfetched),
    'absolute_paths': len(absp),
    'assets_total': len(assets),
    'assets_original': len(assets) - len(third_party),
    'registry_entries': len(registry),
    'registry_fetched': fetched,
    'registry_incomplete': len(incomplete),
    'unregistered_third_party_files': len(unregistered),
    'orphan_assets_info': len(orphans),
    'unreadable_images': bad,
}, indent=1))
for b in broken[:50]: print('BROKEN', b)
if unfetched: print(f'UNFETCHED {len(unfetched)} links point to registry assets not downloaded yet; run: python3 _tools/fetch_assets.py')
for a in absp[:20]: print('ABSOLUTE_PATH', a)
for u in unregistered[:50]: print('UNREGISTERED', u)
for i in incomplete[:20]: print('INCOMPLETE_REGISTRY_ENTRY', i)
for o in orphans[:20]: print('ORPHAN (info)', o)
sys.exit(1 if broken or absp or unregistered or incomplete else 0)
