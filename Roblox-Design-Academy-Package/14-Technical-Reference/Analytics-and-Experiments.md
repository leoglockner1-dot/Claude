---
title: "Analytics, Funnels and Experiments"
tags: [technical, analytics]
note_type: "technical-reference"
---

# Analytics, Funnels and Experiments

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- `AnalyticsService:LogOnboardingFunnelStepEvent(player, step, stepName)`, `:LogFunnelStepEvent(...)`, `:LogEconomyEvent(...)`, `:LogCustomEvent(...)` (names verified in analytics docs). [analytics](https://create.roblox.com/docs/production/analytics)
- **Experiments** for A/B tests and **Configs** for live tuning (Roblox game-design docs reference both for onboarding, hints, starter currency).
- Thumbnail personalization statistics: impressions, qualified plays, average playtime, qualified play-through rate.
- *(recommendation)* Define funnel steps before launch; change one variable per experiment; beware ad-traffic bias (DevForum reports).
