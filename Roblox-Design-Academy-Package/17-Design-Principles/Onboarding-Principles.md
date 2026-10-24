---
title: "Onboarding Principles (ONB-001 – ONB-008)"
tags: [principles, onboarding]
note_type: "principles"
---

# Onboarding Principles (ONB-001 – ONB-008)

First-time user experience principles, grounded in Roblox onboarding docs and developer-posted funnel data.

| ID | Principle | Confidence |
|---|---|---|
| ONB-001 | Teach the core verb first, through play | High |
| ONB-002 | Rules as pictures | High |
| ONB-003 | Point, don't describe | High |
| ONB-004 | Never block the screen without a reason shown | High |
| ONB-005 | Contextual tutorials at first relevance | High |
| ONB-006 | Hints only for the stuck | High |
| ONB-007 | Measure every step | High |
| ONB-008 | End on a moment of joy with visible next goals | Medium |

## ONB-001 — Teach the core verb first, through play
**Rule:** The first guided step is the core action, performed by the player, not a menu.

- **Reasoning:** Funnel: 48 % churn at a forced shop step; Roblox: get to the fun quickly.
- **Evidence:** [ONB 06 DevForum Forced Blur Tutorial Funnel](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md), [Onboarding Evidence From Developers](../13-Onboarding-and-Multiplayer/Onboarding/Onboarding-Evidence-From-Developers.md)
- **Good application:** Tutorial starts with selling (the satisfying step) after reviewer feedback (DevForum ASMR-style case).
- **Failure mode:** Forced shop tutorial in an obby.
- **Conditions & exceptions:** —
- **Roblox implementation:** Spawn at the first interactable; first funnel step = first core action.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-002 — Rules as pictures
**Rule:** Explain core rules with 2–3 picture panels and 1–3 word captions, placed where players look.

- **Reasoning:** Players skip text; visuals localise and suit young readers.
- **Evidence:** [ONB 02 Color or Die Rules Sign](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-02-Color-or-Die-Rules-Sign.md), [UI 22 DevForum Smash Style Buttons and Pictogram Guide](../01-UI-UX/Analyses/UI-22-DevForum-Smash-Style-Buttons-and-Pictogram-Guide.md)
- **Good application:** Color Or Die "Hidden!/Dead!" sign.
- **Failure mode:** Paragraph popups at spawn.
- **Conditions & exceptions:** Complex systems need contextual follow-ups.
- **Roblox implementation:** `SurfaceGui` signs or modal with 3 `ImageLabel` cards.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-003 — Point, don't describe
**Rule:** Use arrows, outlines, trails and world markers on the target.

- **Reasoning:** Roblox onboarding techniques.
- **Evidence:** [ONB 03 Hello Kitty Cafe Spotlight and Trail](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-03-Hello-Kitty-Cafe-Spotlight-and-Trail.md), [ONB 01 Creatures of Sonaria Guided Trail](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-01-Creatures-of-Sonaria-Guided-Trail.md)
- **Good application:** Arrow + outline + floor trail.
- **Failure mode:** "Click the backpack button" text.
- **Conditions & exceptions:** —
- **Roblox implementation:** `Beam` trails, `Highlight`, spotlight overlay.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-004 — Never block the screen without a reason shown
**Rule:** If you must pause or blur the game, state why in one line and keep the target obvious.

- **Reasoning:** Blur without explanation reads as "broken" (player report).
- **Evidence:** [ONB 06 DevForum Forced Blur Tutorial Funnel](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md)
- **Good application:** —
- **Failure mode:** Full-screen blur + lone arrow.
- **Conditions & exceptions:** —
- **Roblox implementation:** Dim (not blur) with spotlight hole + one-line reason.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-005 — Contextual tutorials at first relevance
**Rule:** Teach secondary systems when they become useful, not upfront.

- **Reasoning:** Roblox: contextual tutorials improve retention and reduce load.
- **Evidence:** [ONB 04 Squishmallows Contextual Tutorials](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-04-Squishmallows-Contextual-Tutorials.md)
- **Good application:** Fusion tutorial when owning duplicates.
- **Failure mode:** Teaching the market in minute one.
- **Conditions & exceptions:** —
- **Roblox implementation:** Trigger table: condition → tutorial.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-006 — Hints only for the stuck
**Rule:** Show timed hints after the typical completion time, once.

- **Reasoning:** Roblox Plant example.
- **Evidence:** [ONB 05 Plant Timed Hints](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-05-Plant-Timed-Hints.md)
- **Good application:** Glow at 11 s if not pressed.
- **Failure mode:** Hints for everyone immediately.
- **Conditions & exceptions:** —
- **Roblox implementation:** `task.delay` per step; delay in Config/Experiments.
- **Confidence:** High
- **Tags:** #onboarding

## ONB-007 — Measure every step
**Rule:** Instrument onboarding as a funnel and compare variants with Experiments.

- **Reasoning:** Roblox analytics; developer funnels found exact leak points.
- **Evidence:** [Onboarding Evidence From Developers](../13-Onboarding-and-Multiplayer/Onboarding/Onboarding-Evidence-From-Developers.md), [Analytics and Experiments](../14-Technical-Reference/Analytics-and-Experiments.md)
- **Good application:** Shop-opened step revealed 48 % churn.
- **Failure mode:** Guessing from total playtime.
- **Conditions & exceptions:** Paid-ad traffic lowers ratings and may distort metrics (developer reports).
- **Roblox implementation:** `AnalyticsService:LogOnboardingFunnelStepEvent(player, step, name)`.
- **Confidence:** High
- **Tags:** #onboarding #analytics

## ONB-008 — End on a moment of joy with visible next goals
**Rule:** Finish onboarding with a celebration and show what to work toward next.

- **Reasoning:** Roblox onboarding guidance.
- **Evidence:** [First Session Design](../13-Onboarding-and-Multiplayer/Onboarding/First-Session-Design.md)
- **Good application:** First rare pet hatch + quest board reveal.
- **Failure mode:** Tutorial ends silently in an empty map.
- **Conditions & exceptions:** —
- **Roblox implementation:** Celebration recipe R06 + goal panel.
- **Confidence:** Medium
- **Tags:** #onboarding
