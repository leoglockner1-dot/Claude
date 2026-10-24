---
title: "Audio Principles (AUDIO-001 – AUDIO-008)"
tags: [principles, audio]
note_type: "principles"
---

# Audio Principles (AUDIO-001 – AUDIO-008)

Sound principles. Audio evidence in this academy is **measured waveform data**, not listening; perceptual statements are labelled.

| ID | Principle | Confidence |
|---|---|---|
| AUDIO-001 | Sound on the same frame as the visual | Medium |
| AUDIO-002 | Encode valence in timbre and pitch | Medium |
| AUDIO-003 | Vary frequent sounds | Medium |
| AUDIO-004 | Every sound event has a visual counterpart | High |
| AUDIO-005 | Separate volume groups | High |
| AUDIO-006 | Beds for mood, one-shots for events | Medium |
| AUDIO-007 | Give players control over music | High |
| AUDIO-008 | Not every action needs a sound | Medium |

## AUDIO-001 — Sound on the same frame as the visual
**Rule:** Feedback sounds start client-side on the frame of the visual event.

- **Reasoning:** Measured desync of 50–120 ms in a docs example; >0.1 s risks reading as separate events (heuristic from NN/g limits).
- **Evidence:** [V14 V17 Pickup and UI Sounds](../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md)
- **Good application:** UI button: jingle onset on the same frame as the toggle.
- **Failure mode:** Pickup sound 120 ms after the gem disappears.
- **Conditions & exceptions:** —
- **Roblox implementation:** Play from LocalScript on local detection; server confirms silently.
- **Confidence:** Medium
- **Tags:** #audio

## AUDIO-002 — Encode valence in timbre and pitch
**Rule:** Positive outcomes use brighter/higher sounds; negative outcomes darker/lower ones.

- **Reasoning:** Measured: victory centroid 1,655 Hz vs defeat 1,150 Hz with 170–180 Hz energy.
- **Evidence:** [V08 V09 Victory and Defeat Screens](../21-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md), [V14 V17 Pickup and UI Sounds](../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md)
- **Good application:** Bright coin "ding"; low defeat stinger.
- **Failure mode:** Same sound for reward and failure.
- **Conditions & exceptions:** Horror may invert expectations deliberately.
- **Roblox implementation:** Pick/EQ sounds by brightness; `PlaybackSpeed` for pitch.
- **Confidence:** Medium
- **Tags:** #audio

## AUDIO-003 — Vary frequent sounds
**Rule:** High-frequency sounds use pitch/sample variation or musical progression.

- **Reasoning:** Identical repeats cause fatigue (general practice); docs example repeats 466 Hz twice then changes.
- **Evidence:** [V14 V17 Pickup and UI Sounds](../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md)
- **Good application:** Pickup notes climb a scale during a streak.
- **Failure mode:** One identical sample for every coin.
- **Conditions & exceptions:** Critical alerts may stay identical for recognisability.
- **Roblox implementation:** Randomise `PlaybackSpeed` 0.95–1.08 or step per combo.
- **Confidence:** Medium
- **Tags:** #audio

## AUDIO-004 — Every sound event has a visual counterpart
**Rule:** Important events are never sound-only; the visual cue sits on the source.

- **Reasoning:** Roblox accessibility docs; measured A/B shows no reaction without visual cue.
- **Evidence:** [V04 Sound Reliance Phone](../21-Video-Analyses/V04-Sound-Reliance-Phone.md)
- **Good application:** Ringing phone light pulses.
- **Failure mode:** Alarm audible only.
- **Conditions & exceptions:** —
- **Roblox implementation:** Drive sound + light from one function.
- **Confidence:** High
- **Tags:** #audio #accessibility

## AUDIO-005 — Separate volume groups
**Rule:** Expose at least Music and SFX volumes in settings.

- **Reasoning:** Roblox accessibility docs; players balance noisy games.
- **Evidence:** [V05 Audio Volume Mixer](../21-Video-Analyses/V05-Audio-Volume-Mixer.md), [Audio and Sound APIs](../14-Technical-Reference/Audio-and-Sound-APIs.md)
- **Good application:** Icon-coded SFX/music sliders.
- **Failure mode:** "Players can mute their device" (DevForum anti-example).
- **Conditions & exceptions:** —
- **Roblox implementation:** Audio-objects mixing (`AudioFader` etc.) per Roblox recommendation; persist settings.
- **Confidence:** High
- **Tags:** #audio #settings

## AUDIO-006 — Beds for mood, one-shots for events
**Rule:** Sustained beds start with the first visual change and carry mood; one-shots mark discrete events.

- **Reasoning:** Measured pantry A/B: bed starts with motion and persists (−19.8 dBFS median).
- **Evidence:** [V23 V24 Duvall Pantry With and Without Sound](../21-Video-Analyses/V23-V24-Duvall-Pantry-With-and-Without-Sound.md)
- **Good application:** Horror stretch room with rising bed.
- **Failure mode:** Silence during slow scary visuals.
- **Conditions & exceptions:** Silence can itself be a tool (before a scare) — make it intentional.
- **Roblox implementation:** Looped `Sound` with volume tween in/out.
- **Confidence:** Medium
- **Tags:** #audio #mood

## AUDIO-007 — Give players control over music
**Rule:** Music must be adjustable/mutable in-game; never rely on device mute.

- **Reasoning:** DevForum critique: "if too loud players can mute" called bad UX.
- **Evidence:** [DevForum Sources](../22-Source-Library/DevForum-Sources.md)
- **Good application:** Settings toggle + slider.
- **Failure mode:** Loud unskippable music.
- **Conditions & exceptions:** —
- **Roblox implementation:** Settings UI bound to music group volume.
- **Confidence:** High
- **Tags:** #audio #ux

## AUDIO-008 — Not every action needs a sound
**Rule:** Reserve audio for actions with meaning; restraint keeps important sounds legible.

- **Reasoning:** Too many concurrent sounds mask each other (general practice; Roblox notes overlapping sounds can overwhelm).
- **Evidence:** [V05 Audio Volume Mixer](../21-Video-Analyses/V05-Audio-Volume-Mixer.md)
- **Good application:** Footsteps quiet, rewards prominent.
- **Failure mode:** Every UI hover beeps loudly.
- **Conditions & exceptions:** Console UI benefits from navigation sounds (Roblox console guidelines).
- **Roblox implementation:** Audio priority list per project.
- **Confidence:** Medium
- **Tags:** #audio
