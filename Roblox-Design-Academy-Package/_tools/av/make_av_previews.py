#!/usr/bin/env python3
"""Generate the academy's animation/VFX/sound recipe previews: synthesized UI/game sound placeholders
(WAV + waveform/spectrogram + measurements), easing/timing diagrams, and frame-rendered motion previews.

Everything is ORIGINAL, synthesized from code (no samples) -> free to use as placeholders.
The sounds were measured, not listened to (the generating agent cannot hear); treat them as timing and
spectral references, not finished audio.

Usage: python3 make_av_previews.py <out_dir>
Needs: numpy, scipy, matplotlib, Pillow.
"""
import json
import math
import os
import sys
import wave

import numpy as np

SR = 44100
OUT = sys.argv[1] if len(sys.argv) > 1 else 'av_out'
os.makedirs(OUT, exist_ok=True)


# ---------- synthesis helpers ----------
def env(n, a=0.002, d=0.08, s=0.0, r=0.0, total=None):
    """Attack-decay envelope (seconds) -> array of length n."""
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-6), np.exp(-(t - a) / max(d, 1e-6)))
    return e


def tone(freq, dur, shape='sine', a=0.002, d=0.08, gain=1.0, pitch_end=None):
    n = int(SR * dur)
    t = np.arange(n) / SR
    f = np.full(n, float(freq)) if pitch_end is None else np.linspace(freq, pitch_end, n)
    phase = 2 * np.pi * np.cumsum(f) / SR
    if shape == 'sine':
        w = np.sin(phase)
    elif shape == 'tri':
        w = 2 / np.pi * np.arcsin(np.sin(phase))
    elif shape == 'square':
        w = np.sign(np.sin(phase)) * 0.6
    return w * env(n, a, d) * gain


def noise(dur, a=0.001, d=0.03, gain=1.0, lowpass=None, seed=1):
    n = int(SR * dur)
    w = np.random.default_rng(seed).standard_normal(n)
    if lowpass:
        from scipy.signal import butter, lfilter
        b, aa = butter(2, lowpass / (SR / 2))
        w = lfilter(b, aa, w)
        w /= np.max(np.abs(w)) + 1e-9
    return w * env(n, a, d) * gain


def mix(*parts, offsets=None, length=None):
    offsets = offsets or [0] * len(parts)
    end = max(int(o * SR) + len(p) for p, o in zip(parts, offsets))
    n = length and int(length * SR) or end
    out = np.zeros(max(n, end))
    for p, o in zip(parts, offsets):
        i = int(o * SR)
        out[i:i + len(p)] += p
    return out


def normalize(x, peak_db=-3.0):
    peak = np.max(np.abs(x)) + 1e-12
    return x / peak * (10 ** (peak_db / 20))


def write_wav(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


def measure(x):
    a = np.abs(x)
    peak_db = 20 * np.log10(a.max() + 1e-12)
    # duration until the signal stays below -60 dBFS
    thr = 10 ** (-60 / 20)
    idx = np.where(a > thr)[0]
    dur = (idx[-1] + 1) / SR if len(idx) else 0
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x))))
    freqs = np.fft.rfftfreq(len(x), 1 / SR)
    centroid = float((spec * freqs).sum() / (spec.sum() + 1e-12))
    hop = 441
    rms = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)])
    db = 20 * np.log10(rms + 1e-9)
    onsets = [round(i * hop / SR, 3) for i in range(2, len(db)) if db[i] - db[max(0, i - 3):i].min() > 9 and db[i] > -40]
    pruned = []
    for o in onsets:
        if not pruned or o - pruned[-1] > 0.04:
            pruned.append(o)
    return {'duration_s': round(dur, 3), 'peak_dbfs': round(float(peak_db), 1), 'spectral_centroid_hz': round(centroid), 'onsets_s': pruned}


# ---------- the sound recipes (AV-xx refers to the recipe book) ----------
def snd_button():          # AV-01: soft pop, mid-high, < 120 ms
    return mix(tone(1400, 0.07, 'sine', 0.001, 0.018, 0.8, pitch_end=900), noise(0.02, 0.0005, 0.006, 0.25, lowpass=6000))


def snd_coin_streak():     # AV-03: bright ding; pitch steps up a semitone per pickup in a streak (5 pickups 110 ms apart)
    parts, offs = [], []
    for k in range(5):
        f = 1568 * 2 ** (k / 12)                       # G6 upwards in semitones
        parts.append(mix(tone(f, 0.18, 'sine', 0.001, 0.06, 0.7), tone(f * 2.01, 0.12, 'sine', 0.001, 0.03, 0.25)))
        offs.append(k * 0.11)
    return mix(*parts, offsets=offs)


def snd_purchase():        # AV-04: two-note rise + shimmer, played on SERVER CONFIRM
    a = tone(784, 0.16, 'tri', 0.002, 0.08, 0.7)
    b = tone(1175, 0.30, 'tri', 0.002, 0.14, 0.7)
    shimmer = sum(tone(f, 0.35, 'sine', 0.01, 0.12, 0.12) for f in (2349, 2794, 3136))
    return mix(a, b, shimmer, offsets=[0, 0.09, 0.12])


def snd_error():           # AV-05: short, low, muted thud - never harsh
    return mix(tone(180, 0.16, 'sine', 0.002, 0.05, 0.9, pitch_end=120), noise(0.05, 0.001, 0.02, 0.2, lowpass=800))


def snd_levelup():         # AV-06: ascending arpeggio + soft whoosh
    notes = [523, 659, 784, 1047]
    arp = [tone(f, 0.35, 'tri', 0.003, 0.18, 0.6) for f in notes]
    whoosh = noise(0.9, 0.25, 0.3, 0.15, lowpass=2500, seed=4)
    return mix(*arp, whoosh, offsets=[0, 0.09, 0.18, 0.27, 0.0])


def snd_rare_reveal():     # AV-07: 1.2 s rising riser (anticipation) -> impact + sparkle at the reveal frame (t=1.2 s)
    riser = tone(220, 1.2, 'square', 0.9, 2.0, 0.18, pitch_end=880) * np.linspace(0.2, 1, int(SR * 1.2))
    riser += noise(1.2, 1.0, 2.0, 0.08, lowpass=4000, seed=7) * np.linspace(0, 1, int(SR * 1.2))
    impact = mix(tone(110, 0.5, 'sine', 0.001, 0.2, 0.9), noise(0.15, 0.0005, 0.05, 0.5, lowpass=5000, seed=9))
    sparkle = sum(tone(f, 0.6, 'sine', 0.001, 0.25, 0.15) for f in (2093, 2637, 3136, 4186))
    return mix(riser, impact, sparkle, offsets=[0, 1.2, 1.21])


def snd_impact_light():    # AV-08
    return mix(noise(0.09, 0.0005, 0.025, 0.7, lowpass=3500, seed=11), tone(300, 0.08, 'sine', 0.001, 0.03, 0.5, pitch_end=180))


def snd_impact_heavy():    # AV-08 heavy variant: low thump + crack + tail
    thump = tone(70, 0.35, 'sine', 0.002, 0.12, 1.0, pitch_end=45)
    crack = noise(0.06, 0.0003, 0.015, 0.7, lowpass=7000, seed=12)
    # v1 measured 0.43 s (recipe target 0.2-0.4 s): tail shortened from 0.4 s to 0.3 s
    tail = noise(0.3, 0.01, 0.09, 0.2, lowpass=900, seed=13)
    return mix(thump, crack, tail, offsets=[0, 0, 0.03])


def snd_victory():         # AV-13: bright major rise
    # v1 measured 0.9 s (recipe target 1-2 s): the last note now rings 1.1 s with a slower decay
    seq = [(523, 0), (659, 0.12), (784, 0.24), (1047, 0.36)]
    parts = [tone(f, 0.9 - o, 'tri', 0.004, 0.35, 0.6) for f, o in seq[:-1]] + [tone(1047, 1.1, 'tri', 0.004, 0.5, 0.7)]
    return mix(*parts, offsets=[o for _, o in seq])


def snd_defeat():          # AV-14: low, falling, darker
    seq = [(392, 0), (349, 0.25), (294, 0.5), (233, 0.75)]
    parts = [tone(f, 1.2, 'sine', 0.01, 0.45, 0.6) for f, _ in seq]
    return mix(*parts, offsets=[o for _, o in seq])


SOUNDS = {'AV-01_button_press': snd_button, 'AV-03_coin_pickup_streak': snd_coin_streak, 'AV-04_purchase_confirm': snd_purchase,
          'AV-05_error_denied': snd_error, 'AV-06_level_up': snd_levelup, 'AV-07_rare_reveal': snd_rare_reveal,
          'AV-08_impact_light': snd_impact_light, 'AV-08_impact_heavy': snd_impact_heavy, 'AV-13_victory': snd_victory,
          'AV-14_defeat': snd_defeat}


def plot_sound(name, x, path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 3.6), dpi=110, sharex=True)
    t = np.arange(len(x)) / SR
    ax1.plot(t, x, lw=0.5, color='#2a6fdb')
    ax1.set_ylabel('amp')
    ax1.set_title(name, fontsize=9)
    ax2.specgram(x, NFFT=1024, Fs=SR, noverlap=768, cmap='magma')
    ax2.set_ylim(0, 8000)
    ax2.set_ylabel('Hz')
    ax2.set_xlabel('seconds')
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


# ---------- easing / timing diagrams (same formulas as _tools/luau/src/Feel.luau) ----------
EASE = {
    'linear': lambda t: t,
    'quadOut': lambda t: 1 - (1 - t) ** 2,
    'cubicOut': lambda t: 1 - (1 - t) ** 3,
    'backOut': lambda t: 1 + 2.70158 * (t - 1) ** 3 + 1.70158 * (t - 1) ** 2,
    'elasticOut': lambda t: t if t in (0, 1) else 2 ** (-10 * t) * math.sin((t * 10 - 0.75) * (2 * math.pi) / 3) + 1,
}


def plot_easings(path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ts = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(figsize=(6, 4), dpi=110)
    for name, f in EASE.items():
        ax.plot(ts, [f(t) for t in ts], label=name)
    ax.axhline(1, color='#888', lw=0.6, ls='--')
    ax.set_xlabel('normalized time')
    ax.set_ylabel('progress')
    ax.set_title('Easing curves (Feel.luau formulas). backOut overshoots ~10%, elasticOut oscillates')
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def plot_reveal_timeline(path):
    """AV-07 timeline: anticipation -> impact -> follow-through with the synthesized audio envelope overlaid."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    x = normalize(snd_rare_reveal())
    hop = 441
    rms = [np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)]
    t = np.arange(len(rms)) * hop / SR
    fig, ax = plt.subplots(figsize=(8, 3), dpi=110)
    phases = [(0, 1.2, '#f2c14e', 'Anticipation: crate shakes, glow builds,\nriser pitch climbs'), (1.2, 1.35, '#e4572e', 'Impact'),
              (1.35, 2.4, '#76b041', 'Follow-through: item settles,\nname + rarity label, input unblocked at ~1.6 s')]
    for a, b, c, label in phases:
        ax.axvspan(a, b, color=c, alpha=0.25)
        ax.text((a + b) / 2, 0.95, label, ha='center', va='top', fontsize=7, transform=ax.get_xaxis_transform())
    ax.plot(t, rms / np.max(rms), color='#222', lw=1, label='audio RMS (synthesized preview)')
    ax.set_xlim(0, 2.4)
    ax.set_xlabel('seconds')
    ax.set_yticks([])
    ax.set_title('AV-07 Rare reward reveal: timing plan (skippable after the first time)')
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


# ---------- frame-rendered motion previews ----------
def gif_button_press(path, fps=60):
    """AV-01: press 0.07 s down to 0.94 scale (quadOut), release 0.14 s with backOut. Rendered at 60 fps."""
    from PIL import Image, ImageDraw
    frames, scales = [], []
    down, up, hold = 0.07, 0.14, 0.25
    total = 0.1 + down + up + hold
    for i in range(int(total * fps)):
        t = i / fps - 0.1
        if t < 0:
            s = 1.0
        elif t < down:
            s = 1 - 0.06 * EASE['quadOut'](t / down)
        elif t < down + up:
            s = 0.94 + 0.06 * EASE['backOut']((t - down) / up)
        else:
            s = 1.0
        scales.append(round(s, 4))
        im = Image.new('RGB', (240, 140), (30, 32, 38))
        d = ImageDraw.Draw(im)
        w, h = 150 * s, 56 * s
        d.rounded_rectangle([120 - w / 2, 70 - h / 2, 120 + w / 2, 70 + h / 2], radius=int(14 * s), fill=(76, 175, 80) if t < down + up and t >= 0 else (90, 190, 95))
        d.text((120 - 14, 64), 'BUY', fill=(255, 255, 255))
        d.text((6, 124), f't={max(t, 0):.2f}s  scale={s:.3f}', fill=(170, 170, 170))
        frames.append(im)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=int(1000 / fps), loop=0)
    return {'frames': len(frames), 'fps': fps, 'min_scale': min(scales), 'max_scale': max(scales)}


def gif_reward_pop(path, fps=30):
    """AV-02/AV-06: reward card pops in with backOut over 0.25 s, glow pulses, text fades."""
    from PIL import Image, ImageDraw, ImageFilter
    frames = []
    for i in range(int(0.9 * fps)):
        t = i / fps
        p = min(1, t / 0.25)
        s = EASE['backOut'](p) if p < 1 else 1.0
        im = Image.new('RGB', (260, 200), (20, 22, 28))
        glow = Image.new('RGB', (260, 200), (0, 0, 0))
        gd = ImageDraw.Draw(glow)
        r = 70 * s * (1 + 0.08 * math.sin(t * 12))
        gd.ellipse([130 - r, 95 - r, 130 + r, 95 + r], fill=(255, 196, 64))
        glow = glow.filter(ImageFilter.GaussianBlur(18))
        im = Image.blend(im, glow, 0.55)
        d = ImageDraw.Draw(im)
        w, h = 90 * s, 110 * s
        d.rounded_rectangle([130 - w / 2, 95 - h / 2, 130 + w / 2, 95 + h / 2], radius=10, fill=(255, 220, 120), outline=(255, 255, 255), width=3)
        alpha = int(255 * min(1, max(0, (t - 0.2) / 0.2)))
        d.text((96, 170), 'LEGENDARY!', fill=(alpha, alpha, int(alpha * 0.6)))
        frames.append(im)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=int(1000 / fps), loop=0)
    return {'frames': len(frames), 'fps': fps, 'pop_duration_s': 0.25}


def gif_coin_burst(path, fps=30, count=14, seed=3, version='v2'):
    """AV-03 VFX: a burst of coins with spread angle, gravity and fade; then coins home to a counter.
    v1 (speed 140-220, 60 deg spread, g=600) rose only ~20-40 px and clumped into one blob - it did not read
    as a burst. v2: faster launch, wider 100 deg spread, slightly longer burst phase, size varies per coin."""
    from PIL import Image, ImageDraw
    rng = np.random.default_rng(seed)
    if version == 'v1':
        ang = rng.uniform(math.radians(60), math.radians(120), count)       # 60 deg spread around up
        spd = rng.uniform(140, 220, count)
        g, burst = 600, 0.45
    else:
        ang = rng.uniform(math.radians(40), math.radians(140), count)       # 100 deg spread
        spd = rng.uniform(280, 380, count)
        g, burst = 900, 0.5
    size = rng.uniform(5, 8, count)
    frames = []
    counter = (220, 20)
    for i in range(int(1.1 * fps)):
        t = i / fps
        im = Image.new('RGB', (260, 200), (24, 26, 32))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([190, 8, 252, 32], 6, fill=(50, 54, 64))
        collected = 0
        for k in range(count):
            if t < burst:         # burst phase
                x = 130 + math.cos(ang[k]) * spd[k] * t
                y = 160 - math.sin(ang[k]) * spd[k] * t + 0.5 * g * t * t
            else:                 # home to the counter, staggered, cubicOut
                sx = 130 + math.cos(ang[k]) * spd[k] * burst
                sy = 160 - math.sin(ang[k]) * spd[k] * burst + 0.5 * g * burst ** 2
                p = min(1, max(0, (t - burst - k * 0.02) / 0.3))
                e = EASE['cubicOut'](p)
                x, y = sx + (counter[0] - sx) * e, sy + (counter[1] - sy) * e
                if p >= 1:
                    collected += 1
                    continue
            r = size[k]
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 205, 60), outline=(255, 245, 180))
        d.text((198, 14), f'x {collected}', fill=(255, 230, 120))
        frames.append(im)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=int(1000 / fps), loop=0)
    return {'frames': len(frames), 'fps': fps, 'coins': count, 'version': version, 'spread_deg': 60 if version == 'v1' else 100}


if __name__ == '__main__':
    report = {'sounds': {}, 'previews': {}}
    for name, fn in SOUNDS.items():
        x = normalize(fn())
        write_wav(os.path.join(OUT, name + '.wav'), x)
        plot_sound(name, x, os.path.join(OUT, name + '.png'))
        report['sounds'][name] = measure(x)
    plot_easings(os.path.join(OUT, 'easing-curves.png'))
    plot_reveal_timeline(os.path.join(OUT, 'AV-07_rare_reveal_timeline.png'))
    report['previews']['AV-01_button_press.gif'] = gif_button_press(os.path.join(OUT, 'AV-01_button_press.gif'))
    report['previews']['AV-02_reward_pop.gif'] = gif_reward_pop(os.path.join(OUT, 'AV-02_reward_pop.gif'))
    report['previews']['AV-03_coin_burst_v1.gif'] = gif_coin_burst(os.path.join(OUT, 'AV-03_coin_burst_v1.gif'), version='v1')
    report['previews']['AV-03_coin_burst.gif'] = gif_coin_burst(os.path.join(OUT, 'AV-03_coin_burst.gif'))
    with open(os.path.join(OUT, 'av_measurements.json'), 'w') as f:
        json.dump(report, f, indent=1)
    print(json.dumps(report, indent=1))
