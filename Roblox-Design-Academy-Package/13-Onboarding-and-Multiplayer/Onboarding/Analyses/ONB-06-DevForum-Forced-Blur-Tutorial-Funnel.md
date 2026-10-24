---
title: "ONB-06 — Forced blurred tutorial and its funnel (troll tower obby, DevForum)"
tags: [reference, onboarding, analytics, anti-pattern]
reference_type: "DevForum screenshots incl. Creator Analytics funnel (Negative, with data)"
date_accessed: "2026-10-24"
---

# ONB-06 — Forced blurred tutorial and its funnel (troll tower obby, DevForum)

## Identity
- **Name:** ONB-06 — Forced blurred tutorial and its funnel (troll tower obby, DevForum)
- **Reference type:** DevForum screenshots incl. Creator Analytics funnel (Negative, with data)
- **Source URL:** <https://devforum.roblox.com/t/is-it-normal-to-have-a-30-onboarding-rate/4810040>
- **Creator/publisher:** Developer MashySob
- **Date posted / accessed:** 2026-08-14 / 2026-10-24
- **Access limitations:** Analytics screenshots posted by the developer; numbers not independently verifiable; the game was not played.

![df-4810040-00.jpg](../../../Assets/UI/devforum/df-4810040-00.jpg)
![df-4810040-03.jpg](../../../Assets/Other/devforum/df-4810040-03.jpg)
![df-4810040-06.jpg](../../../Assets/Other/devforum/df-4810040-06.jpg)

## What is observable
**Tutorial:** on join, the whole screen is blurred; a yellow arrow points at a "SHOP" coin button on the right. No text explains why.
**Funnel (Creator Analytics, 6,327 users):** 1 Onboarding Required 100 % → **2 Shop Opened 51.89 % (48.11 % churn — biggest drop)** → 3 Welcome Gift Secured 93.73 % → 4 Belly Buy Attempted 92.43 % → 5 Belly Purchased 99.96 % → 6 Target Hit / Onboarding Completed 66.85 % → **total 30.03 %**.
**Progress funnel (1,716 users):** Floor 1 100 % → **Floor 2 3.13 % (96.87 % churn)** → Floor 3 11.86 % of those → **0.06 %** reach floor 3.
Developer's reason for the tutorial: before it, only **4 %** of players claimed free rewards and few used troll tools.

## Community critique (quoted/paraphrased from the thread)
- "I thought the game was broken with everything being blurred but it turns out that I am forced to go through a tutorial without any explanations on what the arrows do or why they are there." (cegberry)
- "why does a tower obby game force you to claim coins … there's really no reason to force a tutorial unless it's about a vital feature" (PANDASonNOOB)

## What works
Funnel instrumentation per step made the leak visible — the right tool (Roblox recommends funnels/Experiments).

## Why it might work
—

## What does not work
- The forced step teaches a **secondary** feature (shop) instead of the core verb (climbing); half of players leave at that step.
- Full-screen blur reads as "broken" (reply). Arrow without reason.
- Almost nobody reaches floor 2 → the core loop itself was not engaging/clear for new players.

## Reusable principles
- **ONB-001** Teach the core verb first, through play; **ONB-004** never block the screen without explaining why; **ONB-007** measure every onboarding step as a funnel.

## Roblox implementation
Use `AnalyticsService:LogOnboardingFunnelStepEvent` per step and `AnalyticsService:LogFunnelStepEvent` for the per-floor funnel (both names verified in the analytics docs, 2026-10-24); move shop teaching to a contextual moment (first time coins ≥ cheapest item).

## Original application
A tower obby whose first 20 seconds are a short, fun climb ending at a chest that pays the first coins — the shop is introduced only when those coins can buy something.

## Confidence
High (author-posted analytics).

## Related
[Onboarding Evidence From Developers](../Onboarding-Evidence-From-Developers.md) · [CS 16 Troll Tower Obby Funnel](../../../20-Game-Case-Studies/CS-16-Troll-Tower-Obby-Funnel.md)
