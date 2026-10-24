---
title: "Progression & Economy Principles (PROG-001 – PROG-008)"
tags: [principles, progression, economy]
note_type: "principles"
---

# Progression & Economy Principles (PROG-001 – PROG-008)

Progression, reward and monetization principles. Market data: 1,041 passes from 85 games ([study](../04-Progression-and-Economy/Game-Pass-Economy-Study.md)).

| ID | Principle | Confidence |
|---|---|---|
| PROG-001 | Early levels fast, goals visible | High |
| PROG-002 | Upgrades change something you can see | Medium |
| PROG-003 | Purchases confirm locally and preview effects | High |
| PROG-004 | Value ladder in shops | High |
| PROG-005 | Disclose odds and stay fair | High |
| PROG-006 | Price where the market lives | Medium |
| PROG-007 | Monetize convenience and expression, not access to fun | Medium |
| PROG-008 | Offers at natural pauses, one at a time | High |

## PROG-001 — Early levels fast, goals visible
**Rule:** Keep early thresholds low and show short/mid/long goals in the UI or world.

- **Reasoning:** Roblox onboarding guidance.
- **Evidence:** [First Session Design](../09-Onboarding/First-Session-Design.md), [UI 04 Jailbreak Season Pass](../01-UI-UX/Analyses/UI-04-Jailbreak-Season-Pass.md)
- **Good application:** Season track as a visible line with next reward preview.
- **Failure mode:** First level after 20 minutes.
- **Conditions & exceptions:** —
- **Roblox implementation:** XP thresholds in a Config; progress bar with next-reward icon.
- **Confidence:** High
- **Tags:** #progression

## PROG-002 — Upgrades change something you can see
**Rule:** Prefer upgrades that change behaviour or visuals; pure numbers need a visible consequence.

- **Reasoning:** Invisible progress feels arbitrary.
- **Evidence:** [V12 Upgrade Button Baseline](../16-Video-Analyses/V12-Upgrade-Button-Baseline.md), [TI 30 Incremental Genre Grammar](../02-Thumbnails-and-Icons/Analyses/TI-30-Incremental-Genre-Grammar.md)
- **Good application:** Bigger stone throws farther, more skips.
- **Failure mode:** Leaderboard number changes, nothing else.
- **Conditions & exceptions:** Incremental genres celebrate numbers — still show them growing in the world.
- **Roblox implementation:** Upgrade definition includes a visual hook (size, colour, VFX tier).
- **Confidence:** Medium
- **Tags:** #progression

## PROG-003 — Purchases confirm locally and preview effects
**Rule:** Every purchase gives immediate local feedback (cost leaves, stat pops, sound) and shows "current → next".

- **Reasoning:** Feedback principle + decision support.
- **Evidence:** [V12 Upgrade Button Baseline](../16-Video-Analyses/V12-Upgrade-Button-Baseline.md), [R04 Upgrade Purchase Interaction](../13-Reusable-Design-Recipes/R04-Upgrade-Purchase-Interaction.md)
- **Good application:** —
- **Failure mode:** Silent number change far from the button.
- **Conditions & exceptions:** —
- **Roblox implementation:** Client-side feedback, server-authoritative transaction.
- **Confidence:** High
- **Tags:** #progression #ui

## PROG-004 — Value ladder in shops
**Rule:** Order offers by value; one hero offer gets space and size; quantities shown by art scale.

- **Reasoning:** Roblox UI doc example (Dragon Adventures).
- **Evidence:** [UI 05 Dragon Adventures Premium Shop](../01-UI-UX/Analyses/UI-05-Dragon-Adventures-Premium-Shop.md), [Shops and Monetization UI](../01-UI-UX/Shops-and-Monetization-UI.md)
- **Good application:** Coin art grows from stack to vault; best value isolated.
- **Failure mode:** Five "BEST!" badges.
- **Conditions & exceptions:** —
- **Roblox implementation:** Grid + hero card; one badge type.
- **Confidence:** High
- **Tags:** #economy #ui

## PROG-005 — Disclose odds and stay fair
**Rule:** Paid random items show all outcomes with % odds before purchase; marketing claims match in-game odds.

- **Reasoning:** Roblox policy; trust.
- **Evidence:** [Random Rewards and Fairness](../04-Progression-and-Economy/Random-Rewards-and-Fairness.md), [TI 15 Number and Odds Bait](../02-Thumbnails-and-Icons/Analyses/TI-15-Number-and-Odds-Bait.md)
- **Good application:** Labelled "Odds" button before buying.
- **Failure mode:** Icon says 0.0001 %, thumbnail 0.00001 %.
- **Conditions & exceptions:** —
- **Roblox implementation:** Odds table UI; one source of truth module for odds.
- **Confidence:** High
- **Tags:** #economy #policy

## PROG-006 — Price where the market lives
**Rule:** Most passes sit between 99 and 499 Robux (observed median 249); outliers need clear value.

- **Reasoning:** Market data from 695 for-sale passes.
- **Evidence:** [Game Pass Economy Study](../04-Progression-and-Economy/Game-Pass-Economy-Study.md)
- **Good application:** —
- **Failure mode:** A 7,999 R$ admin pass as a main offer.
- **Conditions & exceptions:** Data is descriptive, not evidence of optimal pricing.
- **Roblox implementation:** Roblox price optimization / regional pricing tools (see docs).
- **Confidence:** Medium
- **Tags:** #economy

## PROG-007 — Monetize convenience and expression, not access to fun
**Rule:** Sell cosmetics, convenience and boosts; keep the core loop fully playable and fair without paying.

- **Reasoning:** Ethics + Roblox design-for-roblox note against blocking social play; cosmetic and multiplier passes dominate the sample.
- **Evidence:** [Game Pass Economy Study](../04-Progression-and-Economy/Game-Pass-Economy-Study.md), [CS 01 99 Nights in the Forest](../15-Game-Case-Studies/CS-01-99-Nights-in-the-Forest.md)
- **Good application:** 99 Nights: one 199 R$ decorator pass at 457k concurrent players.
- **Failure mode:** Paywalled core mode or private servers priced to block friends.
- **Conditions & exceptions:** Competitive games must avoid pay-to-win.
- **Roblox implementation:** Pass catalogue review against CL-08 ethics checklist.
- **Confidence:** Medium
- **Tags:** #economy #ethics

## PROG-008 — Offers at natural pauses, one at a time
**Rule:** Purchase prompts appear in lobbies, intermissions and pre-run moments, never stacked.

- **Reasoning:** Roblox contextual purchases doc.
- **Evidence:** [Shops and Monetization UI](../01-UI-UX/Shops-and-Monetization-UI.md)
- **Good application:** Doors pre-run shop; Dress to Impress intermission theme props.
- **Failure mode:** Popup during combat; three modals on join.
- **Conditions & exceptions:** —
- **Roblox implementation:** Modal queue manager; allow time for the Robux flow.
- **Confidence:** High
- **Tags:** #economy #ux
