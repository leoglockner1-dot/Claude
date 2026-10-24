---
title: "FC-GD-05- — Dig to 999M: a tutorial that asks for a purchase the player can't afford, and content that ends in an hour"
tags: [failure-case, documented, onboarding, progression, retention]
note_type: "failure-case"
evidence: "documented by the game's developer on the Roblox DevForum (2026-08-30); diagnosis by community replies; correction NOT tested by the academy"
source: "https://devforum.roblox.com/t/why-is-my-games-d1-retention-so-low-feedback-needed/4840487"
---

# Dig to 999M: a tutorial that asks for a purchase the player can't afford, and content that ends in an hour

| Field | Record |
|---|---|
| **Problem** | Dig to 999M: a tutorial that asks for a purchase the player can't afford, and content that ends in an hour |
| **Source** | [https://devforum.roblox.com/t/why-is-my-games-d1-retention-so-low-feedback-needed/4840487](https://devforum.roblox.com/t/why-is-my-games-d1-retention-so-low-feedback-needed/4840487) (2026-08-30) |
| **Context** | Re-released dig simulator (shovels with stats, pets, ores, secrets); advertised for a week. |
| **Observable symptoms (as reported)** | Low D1 retention. A tester found that the tutorial says to mine X blocks, sell, then buy a shovel, but after mining more than asked they still couldn't afford it. Mobile UI was cramped; a 'FREE' gift button showed even when nothing was claimable. Another tester beat World 2 in about an hour and saw "no real reason to come back tomorrow". |
| **Cause (reported / suggested)** | Tester diagnosis: a broken tutorial economy (the guided step is impossible without extra grinding) and a meta loop that runs out within the first session. |
| **Correction** | Suggested: grant enough starting money for the tutorial purchases, or redirect players to earn the exact amount; fix the gift button state; add content and longer-term systems (the developer planned World 3 and crafting). Not tested by us. |
| **How the correction was tested** | Not tested by the academy; outcome unknown unless stated in the thread. |
| **Reusable lesson** | Tutorial steps must be *guaranteed* to be completable, so test them with the actual economy numbers. A session-one ending needs a visible next goal for day two. |
| **Related** | [LU-12 Upgrade pricing](../../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md), [CL-06 First Session](../../23-Quality-Checklists/CL-06-First-Session-Onboarding.md) |
