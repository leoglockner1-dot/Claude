---
title: "Measured Audio Observations (Roblox docs videos)"
tags: [audio, data]
note_type: "topic"
---

# Measured Audio Observations (Roblox docs videos)

| Video | Measurement | Interpretation |
|---|---|---|
| [V04](../21-Video-Analyses/V04-Sound-Reliance-Phone.md) | Rings at 12.4/15.2/18.0 s and 31.0/33.8/36.55 s; centroid ≈1.06 kHz; peak −20.7 dBFS; no bed between rings | Same audio both halves; only visual cue changes behaviour |
| [V05](../21-Video-Analyses/V05-Audio-Volume-Mixer.md) | Impact onsets 8–21 s; level drops after sliders at ≈25/29 s | Channels controllable separately |
| [V08/V09](../21-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md) | Victory centroid 1,655 Hz (peak energy ≈1.7 kHz); Defeat 1,150 Hz with 170–180 Hz energy, ~2.3 s tail | Valence via brightness |
| [V14](../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md) | Visual→audio offsets +120/+50/−20 ms; pitches 466/466/623 Hz | Sync and variation issues |
| V15 | Chomp centroid ≈3.4 kHz, ~0.2–0.3 s after pickup | Bright positive, slight lag |
| V16 | Button jingle on the same frame as visual toggle | Ideal sync |
| V17 | Jump whoosh/coin ding onsets at 0.25/0.60/2.05/2.35 s (centroids 1.3–2.8 kHz) | Docs: "as soon as" the action |
| [V19](../21-Video-Analyses/V19-Proximity-Hold-Duration.md) | Click onsets during hold at 2.65/4.1 s; door at 5.4 s | Active waiting |
| [V23](../21-Video-Analyses/V23-V24-Duvall-Pantry-With-and-Without-Sound.md) | Bed from ≈2.9 s, median −19.8 dBFS | Bed starts with motion |

Method: ffmpeg → 16 kHz mono → 50 ms RMS windows, onset = jump >1.8× previous and >25 % of max; spectral centroid on 250 ms after onset. **Limitations:** no listening, compressed web audio, small sample.
