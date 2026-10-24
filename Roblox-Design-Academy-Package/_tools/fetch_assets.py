#!/usr/bin/env python3
"""Rebuild the third-party reference assets of the Roblox Development Academy from their sources.

Why this exists: game icons, thumbnails, DevForum screenshots and Roblox docs media belong to
their creators, so the public repository does not contain them. This script downloads them
again into Assets/ for private study, and rebuilds the derived sheets (video analysis sheets,
health-bar strips, contact sheets) from the downloaded files.

Usage:   python3 _tools/fetch_assets.py [package_root] [--only PREFIX] [--dry-run]
Needs:   Python 3.9+, Pillow, numpy; ffmpeg on PATH for videos and video sheets.
Safety:  never overwrites an existing file; prints a summary and exits 1 if anything failed.
Caveat:  live icons/thumbnails are served from Roblox's CDN and can expire or change. A file that
         no longer downloads is reported as FAILED; the notes still describe what it showed.
"""
import io, json, os, subprocess, sys, time, urllib.request

ROOT = next((a for a in sys.argv[1:] if not a.startswith('--')), os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ONLY = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else ''
DRY = '--dry-run' in sys.argv
os.chdir(ROOT)
REG = json.load(open('_tools/asset-sources.json', encoding='utf-8'))
UA = {'User-Agent': 'Mozilla/5.0 (Roblox Development Academy asset fetcher)'}


def get(url):
    for attempt in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def save_jpg(data, path):
    from PIL import Image
    im = Image.open(io.BytesIO(data))
    im = im.convert('RGBA').convert('RGB') if im.mode in ('P', 'LA', 'RGBA') else im.convert('RGB')
    im.save(path, 'JPEG', quality=88)


def ffmpeg(*args):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *args], check=True)


def video_360p(data, path):
    tmp = path + '.src'
    open(tmp, 'wb').write(data)
    try:
        ffmpeg('-i', tmp, '-vf', 'scale=-2:360', '-c:v', 'libx264', '-crf', '26', '-preset', 'veryfast', '-c:a', 'aac', '-b:a', '96k', path)
    finally:
        os.remove(tmp)


def frame(src, at, path):
    ffmpeg('-ss', str(at), '-i', src, '-frames:v', '1', '-q:v', '3', path)


def midframe(data, path):
    tmp = path + '.src.mp4'
    open(tmp, 'wb').write(data)
    try:
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', tmp], capture_output=True, text=True).stdout)
        frame(tmp, dur / 2, path)
    finally:
        os.remove(tmp)


def strip(src, path, step_ms):
    """Health-bar crop every step_ms around the largest bar change (crop tuned for the 640x360 clips)."""
    import numpy as np
    from PIL import Image, ImageDraw
    fps = int(1000 / step_ms)
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', src, '-vf', f'fps={fps},crop=260:22:376:2', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(-1, 22, 260, 3).astype(int)
    sat = (f.max(3) - f.min(3) > 60).sum((1, 2))
    c = int(np.argmax(np.convolve(np.abs(np.diff(sat)), np.ones(5), 'same')))
    s = max(0, c - 8); e = min(len(f), s + 20)
    im = Image.new('RGB', (590, (e - s) * 46), (20, 20, 20)); d = ImageDraw.Draw(im)
    for k, i in enumerate(range(s, e)):
        im.paste(Image.fromarray(f[i].astype(np.uint8)).resize((520, 44)), (70, k * 46))
        d.text((4, k * 46 + 15), f'{i * step_ms / 1000:.2f}s', fill=(255, 255, 0))
    im.save(path, quality=88)


def contact_sheets():
    import glob, re
    from PIL import Image
    batches = json.load(open('_tools/contact-sheet-batches.json'))
    icons = {re.search(r'__u(\d+)', p).group(1): p for p in glob.glob('Assets/Icons/live-2026-10-24/*.jpg')}

    def grid(files, size, cols, out):
        if os.path.exists(out) or not files:
            return
        w, h = size; pad = 10; rows = (len(files) + cols - 1) // cols
        im = Image.new('RGB', (cols * (w + pad) + pad, rows * (h + pad) + pad), (25, 27, 31))
        for k, p in enumerate(files):
            im.paste(Image.open(p).convert('RGB').resize((w, h), Image.LANCZOS), (pad + (k % cols) * (w + pad), pad + (k // cols) * (h + pad)))
        im.save(out, quality=88)

    os.makedirs('Assets/Thumbnails/sheets', exist_ok=True)
    for b, ids in batches.items():
        lst = [icons[u] for u in ids if u in icons]; half = (len(lst) + 1) // 2
        grid(lst[:half], (150, 150), 6, f'Assets/Thumbnails/sheets/grid-icons-150px-{b}-a.jpg')
        grid(lst[half:], (150, 150), 6, f'Assets/Thumbnails/sheets/grid-icons-150px-{b}-b.jpg')
        grid(lst, (64, 64), 12, f'Assets/Thumbnails/sheets/grid-icons-64px-{b}.jpg')
        th = [p.replace('/Icons/', '/Thumbnails/')[:-4] + '__00.jpg' for p in lst]
        th = [p for p in th if os.path.exists(p)]; q = (len(th) + 3) // 4
        for i in range(4):
            grid(th[i * q:(i + 1) * q], (320, 180), 3, f'Assets/Thumbnails/sheets/grid-lead-thumbnails-{b}-{i}.jpg')
    for slug, out in (('rivals__u6035872082__', 'set-rivals-10-thumbnails'), ('dress-to-impress__u5203828273__', 'set-dress-to-impress-10-thumbnails')):
        grid(sorted(glob.glob(f'Assets/Thumbnails/live-2026-10-24/{slug}*.jpg')), (320, 180), 5, f'Assets/Thumbnails/sheets/{out}.jpg')


def main():
    order = {'download-jpg': 0, 'download-video-360p': 0, 'video-midframe': 0, 'frame-from': 1, 'video-sheet': 2, 'generated': 2, 'contact-sheet': 3}
    todo = sorted((e for e in REG if e['path'].startswith('Assets/' + ONLY) or e['path'].startswith(ONLY)), key=lambda e: order[e['method']])
    ok = skip = 0; failed = []
    for e in todo:
        p, m = e['path'], e['method']
        if os.path.exists(p):
            skip += 1; continue
        if DRY:
            print('WOULD', m, p); continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        try:
            if m == 'download-jpg': save_jpg(get(e['source_url']), p)
            elif m == 'download-video-360p': video_360p(get(e['source_url']), p)
            elif m == 'video-midframe': midframe(get(e['source_url']), p)
            elif m == 'frame-from': frame(e['from'], e['at_s'], p)
            elif m == 'video-sheet':
                sys.path.insert(0, '_tools'); import make_video_sheet; make_video_sheet.main(e['from'], p)
            elif m == 'generated': strip(e['from'], p, 50 if 'V06' in p else 100)
            elif m == 'contact-sheet': contact_sheets()
            if not os.path.exists(p):
                raise RuntimeError('not produced')
            ok += 1; print('OK', p)
        except Exception as ex:
            failed.append((p, str(ex)[:120])); print('FAILED', p, ex)
    print(json.dumps({'created': ok, 'already_present': skip, 'failed': len(failed)}, indent=1))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
