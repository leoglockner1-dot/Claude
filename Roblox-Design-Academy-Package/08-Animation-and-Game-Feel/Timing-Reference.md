---
title: "Timing Reference (measured vs recommended)"
tags: [game-feel, animation, data]
note_type: "topic"
---

# Timing Reference (measured vs recommended)

## Measured from official Roblox videos (High confidence)
| Event | Duration / interval | Source |
|---|---|---|
| Health bar change (Exponential Out, 0.5 s tween) | ≈0.25 s visible change | [V06/V07](../21-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md) |
| Damage tick on hazard | ≈1.03 s interval | V06 |
| Red damage flash | peak in 1 frame; ≈50 % by ~50 ms; ≈15 % by ~200 ms; ~0.3 s total | V06 |
| Blaster cadence with state machine | ≈0.6 s between shots | [V10](../21-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md) |
| Burst trap peak | ≈0.4 s | [V20](../21-Video-Analyses/V20-Burst-Particle-Trap.md) |
| Hold-to-interact (lock pick) | ≈3.3 s | [V19](../21-Video-Analyses/V19-Proximity-Hold-Duration.md) |
| Respawn fade (black) | ≈0.7 s | [V22](../21-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md) |
| Scene transport black hold | ≈1.2 s, then blur→focus ≈1.3 s | V21 |
| Avatar grid load | ≈0.6 s | [V01](../21-Video-Analyses/V01-Berry-Avenue-Avatar-Flow.md) |
| Loading ring revolution | ≈4 s | [V18](../21-Video-Analyses/V18-Loading-Spinner.md) |
| Typewriter reveal | ≈10–15 chars/s (approx.) | [V26](../21-Video-Analyses/V26-Typewriter-Text.md) |
| Pickup sound vs visual | +120 / +50 / −20 ms offsets | [V14](../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md) |
| UI button sound vs visual | same frame | V16 |
| Roblox docs sample tween | 0.75 s Cubic Out for a settings menu (accessibility doc code) | [docs](https://create.roblox.com/docs/production/publishing/accessibility) |

## Perception anchors (external, labelled)
NN/g response-time limits: **0.1 s** feels instantaneous; **1 s** keeps flow; **10 s** keeps attention (percent-done beyond).

## Recommended starting values (Hypotheses — tune by playtest)
| Interaction | Start with |
|---|---|
| Button press/release | 0.06 s down / 0.10–0.15 s up (Quad Out / Back Out) |
| Panel open / close | 0.18–0.25 s / 0.12–0.18 s |
| Frequent action total feedback | ≤ 0.3 s |
| Common reward | 0.3–0.6 s |
| Rare reward reveal | 1.5–3 s, skippable after first |
| Level-up / milestone | 1–2 s, input unblocked quickly |
| Screen shake | 0.1–0.3 s, decaying; heavy events only |
| Hit-stop | 0.03–0.08 s local only |

Do not treat the hypothesis table as rules; record what playtests show in `08 Lessons` of your vault.
