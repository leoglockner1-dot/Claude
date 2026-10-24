# Animation, VFX, SFX and Game Feel — Import Content

**Merge into:** the `04_Animation_And_Game_Feel/` notes.

**Honesty note:** there were **no observable animation sequences or audio** in this research; the only video was downloaded, not watched. Everything here is [GEN] (established practice from animation and game-feel literature, see [Sources](Sources.md)), [FACT] (Roblox engine limits) or [HYP] (starting values to tune by playtest). **All durations are starting points, not rules.**

---

## → Animation_Principles.md

### The action-feedback arc [GEN]
**Anticipation → Action → Impact → Follow-through/Recovery → Reward/Settle**

- **Anticipation** tells the player something is about to happen (wind-up, squash, button press-down). Keep it short for frequent player-triggered actions, because long wind-ups feel laggy, and longer for enemy attacks, because that gives the player time to react.
- **Action** is the fast part, usually the shortest phase.
- **Impact** is the peak moment. Stack feedback here: flash, hit-stop, shake, sound, particles.
- **Follow-through** means overshoot and settle (Back/Elastic easing), with debris and particles finishing.
- **Recovery** returns to neutral and re-enables input.

### Timing starting points [HYP]
| Interaction | Total duration | Notes |
|---|---|---|
| Button press feedback | about 0.05–0.1 s down, 0.1–0.15 s up | Instant on press, never wait for the server |
| Panel open | about 0.15–0.25 s | Out easing (fast start, soft end) |
| Panel close | about 0.1–0.2 s | Faster than open |
| Frequent action (click, collect, hit) | under about 0.3 s total | Players do this hundreds of times |
| Rare reward reveal | about 1.5–4 s | Must be **skippable** after the first time |
| Level-up or milestone | about 1–2 s | Don't block input longer than needed |

Roblox's own docs sample uses 0.75 s Cubic Out for a settings menu [FACT example]. That's slower than the range above, so treat it as an example, not a standard.

### Easing [FACT + GEN]
- Default `TweenInfo` easing is Quad / Out [FACT].
- **Out** (fast start, slow end) for things appearing or responding: feels responsive.
- **In** for things leaving: feels like acceleration away.
- **Back Out** for playful overshoot on pop-ins (cartoon tone).
- **Elastic and Bounce**: rarely, only for celebratory moments, never for frequent UI.
- **Linear**: only for continuous motion (spinners, scrolling backgrounds).

### Reduced motion [FACT]
If `GuiService.ReducedMotionEnabled`, snap (time 0) or swap motion for a fade (CanvasGroup). Shake, zoom and flashes should also scale down.

---

## → VFX_Principles.md

### Hierarchy [GEN]
- **VFX intensity ∝ event importance.** If every action explodes, nothing feels special.
- Tier the effects: small (collect, hit) → medium (kill, combo, upgrade) → large (boss kill, legendary drop, level-up).
- **Gameplay readability beats spectacle.** Effects must never hide enemies, hazards, the player's character or the decision UI.
- Use **colour semantics** consistent with the UI map (health green, damage red, rare gold…).
- **One feedback channel per question** the player has after an action: did I hit? how much? am I in danger? what did I gain? [OBS IMP-19].
- **Rewards travel to their counter.** Coins or XP fly from the source to the HUD balance, which shows where the value went [OBS IMP-19 via Roblox's description].

### Roblox limits [FACT]
- ParticleEmitter: **≤ 400 particles/s per emitter (100/s on mobile)**. Lifetime is capped at 20 s.
- Cost comes from **fill-rate and overdraw**. Large, overlapping, semi-transparent particles near the camera are the most expensive kind. Prefer fewer, smaller, more opaque particles, plus short lifetimes.
- `Highlight`: max **255** visible at once.
- Avoid partial transparency where possible (overdraw).
- Use `ParticleEmitter:Emit(n)` bursts for impacts instead of a continuous `Rate`.

### Implementation patterns
- Hit flash: a short `Highlight` fill tween, or a brief colour swap.
- Damage numbers: pooled `BillboardGui`s.
- Trails: `Trail` or `Beam` for weapons, dashes and guidance paths.
- Screen effects: a full-screen `ImageLabel` vignette tied to a state; `ColorCorrectionEffect` and `BlurEffect` for brief impact or menu focus.

---

## → SFX_and_Audio_Feedback.md

- **Every player action gets a sound**; UI too. Console guidance explicitly recommends sounds for selection and menu traversal [FACT console + GEN].
- **Sound must start on the input frame, client-side.** Waiting for the server makes it feel laggy [GEN].
- **Variation for frequent sounds:** randomize pitch by about ±5–10% or rotate 3–4 samples so repetition doesn't grate [GEN/HYP].
- **Loudness hierarchy:** rare and important sounds above frequent ones. Frequent sounds should be short and soft [GEN].
- **Separate volume groups** (Music, SFX, UI, ambient, voice) and give players sliders [FACT accessibility].
- **Never sound-only information.** Pair every audio cue with a visual one [FACT accessibility].
- **API note:** `SoundGroup` is now discouraged in favour of the newer audio objects API [FACT]. Check the current docs before building a mixer.
- Rewards: rising pitch for combos or streaks, and a distinct "cha-ching" for purchases (Roblox's own example of feedback) [RBX].
- Thumbnail videos can't contain voice-over or music with lyrics [FACT].

---

## → Camera_and_Impact.md

- **Screen shake:** short (about 0.1–0.3 s), decaying, scaled by event importance and by distance from the camera. Use translation or rotation noise, not random teleports [GEN/HYP].
- **Never shake for frequent actions** (each click or footstep). Save it for impacts that matter.
- **Hit-stop (freeze-frame):** pause the attacker and target animations for about 0.03–0.1 s on a heavy hit. It sells weight [GEN/HYP]. On Roblox, freeze locally only (pause the `AnimationTrack` speed); never stall the server.
- **FOV kick:** a brief +3–8° FOV on dash or boost, easing back [HYP].
- **Respect reduced motion:** scale shake, zoom and FOV kicks down or to zero when `ReducedMotionEnabled` [FACT setting + GEN].
- Shake and flash also add up as **accessibility risks**: avoid rapid full-screen flashing [GEN].

---

## → Reward_Reveal_Sequences.md

### Common vs rare [GEN]
| Tier | Sequence | Duration [HYP] |
|---|---|---|
| Common | Pop-in plus small sound, auto-collect | about 0.3–0.6 s |
| Uncommon | Pop-in plus rarity-colour flash | about 0.6–1 s |
| Rare | Anticipation (shake or glow building) → burst → item reveal with rarity colour | about 1.5–2.5 s |
| Legendary | Longer anticipation, screen dim, unique sound, camera move, then a celebration | about 2.5–4 s, skippable |

### Rules
1. **Anticipation is the pleasure**: a short build-up before the reveal (an egg wobbling, a chest glowing). The reveal itself should be fast.
2. **Rarity is signalled early**, through colour and sound during anticipation, so rare pulls feel different from the first frame.
3. **Skippable after first view**, and **batch** multi-opens ("open 10" shows a summary grid).
4. Name and rarity text appear **after** the visual reveal, large and readable.
5. Joy at milestones: end onboarding on an intentional "moment of joy" (rewards, delightful animations, celebratory VFX) [RBX onboarding].
6. **Policy:** if the reveal comes from a paid random item, the odds must be shown before purchase [FACT].

### Implementation sketch (Roblox)
Use `ViewportFrame` for the 3D item, tween `CanvasGroup` for fades, `ParticleEmitter:Emit()` for the burst, `Lighting.ColorCorrection` tint for the rarity mood, and a client-side `Sound` triggered on the reveal frame.
