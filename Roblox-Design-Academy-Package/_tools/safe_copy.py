#!/usr/bin/env python3
"""Copy the academy package into an Obsidian vault without overwriting anything.

Usage:
  python3 safe_copy.py --vault "<vault root>" [--dest "<folder inside vault>"] [--dry-run]

  --dest defaults to "Roblox Design Academy/Roblox-Design-Academy-Package" inside the vault.
  The package root is the parent of this _tools folder.

Behaviour:
  - Refuses to run if --vault has no .obsidian folder (pass --no-obsidian-check to override).
  - Never overwrites: a file that already exists at the destination path is skipped and reported.
  - Reports possible duplicates: Markdown files elsewhere in the vault (outside the destination) with the
    same file name or the same title as a package note. Nothing is merged, renamed or deleted.
  - Copies bytes unchanged (shutil.copy2), keeps the folder structure.
  - Writes a JSON report next to the destination folder: <dest>/../academy-copy-report.json
Exit code 0 if the copy finished (skips are not errors), 2 on usage errors.
"""
import os, sys, json, shutil, argparse, re, datetime

pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument('--vault', required=True)
ap.add_argument('--dest', default=os.path.join('Roblox Design Academy', 'Roblox-Design-Academy-Package'))
ap.add_argument('--dry-run', action='store_true')
ap.add_argument('--no-obsidian-check', action='store_true')
a = ap.parse_args()

vault = os.path.abspath(a.vault)
if not os.path.isdir(vault):
    sys.exit(f'vault not found: {vault}')
if not a.no_obsidian_check and not os.path.isdir(os.path.join(vault, '.obsidian')):
    print(f'{vault} has no .obsidian folder; is this the right vault? (use --no-obsidian-check to proceed)')
    sys.exit(2)
dest = os.path.abspath(os.path.join(vault, a.dest))
if os.path.commonpath([dest, vault]) != vault:
    sys.exit('--dest must be inside the vault')
if os.path.commonpath([dest, pkg]) == pkg or os.path.commonpath([dest, pkg]) == dest:
    sys.exit('destination overlaps the package source')

SKIP_DIRS = {'.git', '__pycache__', '.obsidian'}
def title_of(p):
    try:
        s = open(p, encoding='utf-8', errors='replace').read(4000)
    except OSError:
        return None
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', s, re.M) or re.search(r'^# (.+)$', s, re.M)
    return m.group(1).strip().lower() if m else None

# Index the vault outside the destination for duplicate detection.
vault_names, vault_titles = {}, {}
for d, dirs, files in os.walk(vault):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not os.path.abspath(os.path.join(d, x)).startswith(dest)]
    for f in files:
        if f.endswith('.md'):
            p = os.path.join(d, f)
            vault_names.setdefault(f.lower(), []).append(os.path.relpath(p, vault))
            t = title_of(p)
            if t:
                vault_titles.setdefault(t, []).append(os.path.relpath(p, vault))

copied, skipped, dup_name, dup_title = [], [], [], []
for d, dirs, files in os.walk(pkg):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for f in files:
        src = os.path.join(d, f)
        rel = os.path.relpath(src, pkg)
        dst = os.path.join(dest, rel)
        if f.endswith('.md'):
            if f.lower() in vault_names:
                dup_name.append({'package': rel, 'vault': vault_names[f.lower()]})
            t = title_of(src)
            if t and t in vault_titles:
                dup_title.append({'package': rel, 'title': t, 'vault': vault_titles[t]})
        if os.path.lexists(dst):
            skipped.append(rel)
            continue
        if not a.dry_run:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        copied.append(rel)

report = {'time': datetime.datetime.now().isoformat(timespec='seconds'), 'vault': vault, 'destination': dest,
          'dry_run': a.dry_run, 'copied': len(copied), 'skipped_existing': skipped,
          'possible_duplicates_by_filename': dup_name, 'possible_duplicates_by_title': dup_title}
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()}, indent=1))
for s in skipped[:30]:
    print('SKIPPED (exists)', s)
for x in dup_name[:30]:
    print('POSSIBLE DUPLICATE (filename)', x['package'], '<->', ', '.join(x['vault'][:3]))
for x in dup_title[:30]:
    print('POSSIBLE DUPLICATE (title)', x['package'], '<->', ', '.join(x['vault'][:3]))
if not a.dry_run:
    rp = os.path.join(os.path.dirname(dest), 'academy-copy-report.json')
    if os.path.exists(rp):
        rp = rp[:-5] + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.json'
    json.dump(report, open(rp, 'w', encoding='utf-8'), indent=1)
    print('report:', os.path.relpath(rp, vault))
