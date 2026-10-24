---
title: "Audio and Sound APIs"
tags: [technical, audio]
note_type: "technical-reference"
---

# Audio and Sound APIs

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- `SoundGroup` is now **discouraged** in favour of **audio objects** (`AudioPlayer`, `AudioEmitter`, `AudioListener`, `AudioDeviceOutput`, `AudioFader`, `AudioEqualizer`, `AudioCompressor`, `AudioReverb`, voice: `AudioDeviceInput`, `AudioTextToSpeech`, `AudioSpeechToText`). [audio objects](https://create.roblox.com/docs/audio/objects) · [sound groups](https://create.roblox.com/docs/sound/groups)
- 2D one-shot audio for UI/gameplay feedback; 3D emitters for world events (add-2D-audio / add-3D-audio tutorials).
- Accessibility: provide separate volume groups (SFX, music, speech) and never rely on sound alone. [accessibility](https://create.roblox.com/docs/production/publishing/accessibility)
- Thumbnail videos may use catalog music; **no voice-over, narration or lyrics**.
