#!/usr/bin/env python3
"""Validate an installed or unpacked Roblox Design Academy package.
Usage: python3 validate_package.py "<path to package or installed academy folder>"
Checks: relative Markdown links and image embeds resolve; no machine-specific absolute paths;
every file in Assets/ is referenced by a note; registry entries exist. Pillow is optional (image integrity).
"""
import re, os, glob, json, sys, urllib.parse
root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
notes = sorted(glob.glob('**/*.md', recursive=True))
broken, refs, absp = [], set(), []
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
        (refs.add(r) if os.path.exists(r) else broken.append((f, t)))
    if re.search(r'/home/|/tmp/|[A-Z]:\\\\Users', s):
        absp.append(f)
assets = [a for a in glob.glob('Assets/**/*', recursive=True) if os.path.isfile(a) and not a.endswith('asset-registry.json')]
orphans = [a for a in assets if os.path.normpath(a) not in refs]
missing = []
if os.path.exists('Assets/asset-registry.json'):
    missing = [r['path'] for r in json.load(open('Assets/asset-registry.json', encoding='utf-8')) if not os.path.exists(r['path'])]
bad = []
try:
    from PIL import Image
    for a in assets:
        if a.lower().endswith(('.jpg', '.png')):
            try: Image.open(a).verify()
            except Exception: bad.append(a)
except ImportError:
    bad = ['(Pillow not installed: image integrity not checked)']
print(json.dumps({'notes': len(notes), 'broken_links': len(broken), 'absolute_paths': len(absp),
                  'assets': len(assets), 'orphan_assets': len(orphans), 'registry_missing': len(missing),
                  'unreadable_images': bad}, indent=1))
for b in broken[:50]: print('BROKEN', b)
for o in orphans[:50]: print('ORPHAN', o)
for m in missing[:50]: print('MISSING', m)
sys.exit(1 if broken or absp or missing else 0)
