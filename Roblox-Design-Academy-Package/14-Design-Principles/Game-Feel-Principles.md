---
title: "Game-Feel Principles (FEEL-001 – FEEL-010)"
tags: [principles, game-feel]
note_type: "principles"
---

# Game-Feel Principles (FEEL-001 – FEEL-010)

Animation, VFX and impact principles. Measured timings are from Roblox docs videos (see [Timing reference](../05-Animation-and-Game-Feel/Timing-Reference.md)); other values are starting hypotheses.

| ID | Principle | Confidence |
|---|---|---|
| FEEL-001 | Telegraph before payoff | High |
| FEEL-002 | Fast-in, soft-out for state changes | High |
| FEEL-003 | Ease organic motion; linear only for machines | High |
| FEEL-004 | Space repeated feedback | High |
| FEEL-005 | Effects carry meaning in shape and colour | High |
| FEEL-006 | Intensity proportional to importance | High |
| FEEL-007 | Every interactive element responds within 0.1 s | High |
| FEEL-008 | Wins deserve a short celebration and a next step | Medium |
| FEEL-009 | Ambient effects fade and stay low-contrast | High |
| FEEL-010 | Hide discontinuities with short fades | High |

## FEEL-001 — Telegraph before payoff
**Rule:** Every hazard or big effect gets an anticipation phase the player can read before it resolves.

- **Reasoning:** Anticipation (classic animation principle) makes outcomes feel fair and readable.
- **Evidence:** [V20 Burst Particle Trap](../16-Video-Analyses/V20-Burst-Particle-Trap.md), [GF 01 Winds of Fortune Combat Feedback](../05-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md)
- **Good application:** Trap tile emits idle sparks before the 0.4 s burst.
- **Failure mode:** Enemy attacks without wind-up.
- **Conditions & exceptions:** Player-triggered frequent actions need minimal anticipation to stay responsive.
- **Roblox implementation:** Idle `ParticleEmitter` + burst emitter `:Emit()`; enemy wind-up animation marker events.
- **Confidence:** High
- **Tags:** #game-feel

## FEEL-002 — Fast-in, soft-out for state changes
**Rule:** UI and meter changes should register within ~0.1–0.25 s and settle smoothly (Out easing).

- **Reasoning:** Front-loaded easing reads as immediate; NN/g 0.1 s instantaneous limit.
- **Evidence:** [V06 V07 HUD Meter Tween and Damage Flash](../16-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md)
- **Good application:** Health bar: TweenInfo(0.5, Exponential, Out) → visible change ≈0.25 s.
- **Failure mode:** Linear 1 s bar drains that lag behind events.
- **Conditions & exceptions:** Slow fills are fine for rewards that should be savoured (count-ups).
- **Roblox implementation:** `TweenInfo.new(0.25–0.5, Enum.EasingStyle.Quad/Exponential, Enum.EasingDirection.Out)`.
- **Confidence:** High
- **Tags:** #animation

## FEEL-003 — Ease organic motion; linear only for machines
**Rule:** Characters, UI panels and objects use eased curves; Linear only for constant mechanical motion (spinners, conveyors).

- **Reasoning:** Measured: linear = flat velocity plateau, cubic = bell curve.
- **Evidence:** [V28 Easing Linear vs Cubic](../16-Video-Analyses/V28-Easing-Linear-vs-Cubic.md), [V18 Loading Spinner](../16-Video-Analyses/V18-Loading-Spinner.md)
- **Good application:** Cubic door swing.
- **Failure mode:** Linear UI pop-ins look robotic.
- **Conditions & exceptions:** —
- **Roblox implementation:** Animation Editor easing per keyframe; `TweenInfo` EasingStyle.
- **Confidence:** High
- **Tags:** #animation

## FEEL-004 — Space repeated feedback
**Rule:** Repeated actions need cadence so each instance reads as one event; rate limits are part of feel.

- **Reasoning:** Spamming merges flashes into noise (measured).
- **Evidence:** [V10 V11 Blaster Cooldown vs Spam](../16-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md)
- **Good application:** Blaster ~0.6 s cadence via Ready/Blasting states.
- **Failure mode:** No cooldown → continuous glow.
- **Conditions & exceptions:** Rapid-fire weapons can use smaller per-shot effects instead of cooldowns.
- **Roblox implementation:** State enum per weapon; client gate + server check.
- **Confidence:** High
- **Tags:** #game-feel

## FEEL-005 — Effects carry meaning in shape and colour
**Rule:** Particles/VFX shapes and colours should encode what happened (health = green plus, damage = red, money = coins).

- **Reasoning:** Semantic shapes are read without text and match UI colour maps.
- **Evidence:** [V13 Health Pickup](../16-Video-Analyses/V13-Health-Pickup.md), [GF 01 Winds of Fortune Combat Feedback](../05-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md)
- **Good application:** Green "+" particles on heal; coins fly to the counter.
- **Failure mode:** Generic white sparkles for every event.
- **Conditions & exceptions:** Stylised games may abstract further but stay consistent.
- **Roblox implementation:** Custom particle textures per semantic event; colours from the palette module.
- **Confidence:** High
- **Tags:** #vfx

## FEEL-006 — Intensity proportional to importance
**Rule:** Tier effects (small/medium/large); full-screen effects only for rare, important events.

- **Reasoning:** If everything explodes, nothing feels special; full-screen effects obscure play.
- **Evidence:** [V20 Burst Particle Trap](../16-Video-Analyses/V20-Burst-Particle-Trap.md), [V06 V07 HUD Meter Tween and Damage Flash](../16-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md)
- **Good application:** Fail-state lightning covers the screen for 0.4 s, then clears.
- **Failure mode:** Screen shake and flashes on every click.
- **Conditions & exceptions:** Arcade/chaotic identities can raise the baseline — but keep tiers.
- **Roblox implementation:** Effect table: event → tier → particles count/duration/shake.
- **Confidence:** High
- **Tags:** #vfx

## FEEL-007 — Every interactive element responds within 0.1 s
**Rule:** Hover/press states change immediately on input (scale, colour, sound).

- **Reasoning:** Direct-manipulation feel (NN/g 0.1 s); community-described technique for "core-like" UI.
- **Evidence:** [UI 26 DevForum Pls Donate and Color Place Minimal UI](../01-UI-UX/Analyses/UI-26-DevForum-Pls-Donate-and-Color-Place-Minimal-UI.md), [V14 V17 Pickup and UI Sounds](../16-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md)
- **Good application:** Button toggles colour and plays a jingle on the same frame.
- **Failure mode:** Server round-trip before any visual response.
- **Conditions & exceptions:** —
- **Roblox implementation:** `MouseEnter/MouseLeave/MouseButton1Down` tweens 0.06–0.12 s; client-side sound.
- **Confidence:** High
- **Tags:** #ui #game-feel

## FEEL-008 — Wins deserve a short celebration and a next step
**Rule:** Victories, level-ups and milestones get a distinct, short celebration (≈1–2 s) and immediately show what comes next.

- **Reasoning:** Roblox onboarding guidance: end on "moments of joy"; a static victory screen undersells wins.
- **Evidence:** [V08 V09 Victory and Defeat Screens](../16-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md), [First Session Design](../09-Onboarding/First-Session-Design.md)
- **Good application:** —
- **Failure mode:** Same static layout for victory and defeat with no motion.
- **Conditions & exceptions:** Frequent micro-wins should stay subtle.
- **Roblox implementation:** Title scale pop (Back Out), particles, rising stinger, then "Next round in N".
- **Confidence:** Medium
- **Tags:** #game-feel #rewards

## FEEL-009 — Ambient effects fade and stay low-contrast
**Rule:** Ambient particles fade in/out over lifetime and stay below gameplay effects in contrast.

- **Reasoning:** Ambient noise should not compete with feedback.
- **Evidence:** [V27 Fading Particles Volcano](../16-Video-Analyses/V27-Fading-Particles-Volcano.md)
- **Good application:** Volcano smoke fades with transparency sequence.
- **Failure mode:** Bright ambient sparkles everywhere.
- **Conditions & exceptions:** —
- **Roblox implementation:** `Transparency` NumberSequence, low `Rate`, mobile particle cap 100/s per emitter.
- **Confidence:** High
- **Tags:** #vfx #environment

## FEEL-010 — Hide discontinuities with short fades
**Rule:** Teleports, respawns and scene changes are masked by brief fades (≈0.7–1.2 s observed) with a beat on arrival.

- **Reasoning:** Prevents disorientation; gives transitions intent.
- **Evidence:** [V21 V22 Duvall Cutscene and Respawn](../16-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md)
- **Good application:** Respawn: 0.7 s black, reappear near fall point.
- **Failure mode:** Instant teleport mid-frame.
- **Conditions & exceptions:** Competitive games keep respawn transitions minimal.
- **Roblox implementation:** Full-screen Frame tween + `PivotTo` while black.
- **Confidence:** High
- **Tags:** #transitions
