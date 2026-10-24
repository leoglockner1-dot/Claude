---
title: "LU-13 — Random rewards, odds disclosure and pity"
tags: [luau, rewards, random, monetization, ethics]
note_type: "procedure"
evidence: "tested (CLI); policy pointer must be re-checked"
code: "_tools/luau/src/WeightedLoot.luau"
---

# LU-13 — Random rewards, odds disclosure and pity

## Purpose
Weighted random rewards where the shown odds are the real odds, rolls happen on the server, and bad-luck streaks are bounded.

## Approach
- `WeightedLoot.new(entries, rng, pity?)`. Pass a server RNG, e.g. `local r = Random.new(); function() return r:NextNumber() end`.
- `odds(t)` returns the exact probabilities to display before a roll.
- Pity: after `after − 1` misses below `rarity`, the next roll is forced to that tier and the counter resets. Pity changes the effective odds; say so in the UI.

## Policy: paid random items (Roblox docs, `production/monetization/paid-random-items`, read 2026-10-24)
These rules apply when a random outcome is bought with Robux **or with in-game currency that can be bought with Robux**. That covers indirect cases such as keys, spin tickets and re-roll tokens. Covered item types: capsules (eggs, chests, wheels), enhancement items, combination items, and **probability modifiers, explicitly including luck boosts and pity systems**.
- Show **all possible outcomes and their actual numerical odds** before purchase.
- Show odds as **percentages that sum to exactly 100%**. Long decimals may be rounded (the docs specify how) with a disclaimer.
- If outcomes do not fit on screen, use a pop-up behind a button with a **descriptive word** ("Info", "Details"). A bare (i) icon is not sufficient.
- If an outcome can be obtained only once, **update the remaining odds** for that player.
- Paid odds-modifiers (lucky potions and similar) must be **numerically explained** before purchase, and the displayed odds must update while they are active.
- Game passes **cannot** grant paid random items (`passes.md`).
Implications for this module: `odds()` provides the base percentages. If pity or luck boosts apply to a *paid* roll, show the **effective** odds instead (below). Policies change, so re-read the page before shipping.

`WeightedLoot.effectiveOdds(t, userId)` (added and tested) returns the true next-roll odds including a forced pity roll: after 9 misses with `after = 10`, legendary shows 100%. Show these to players when pity applies to a paid roll. **Exercise:** extend it for a paid luck boost that multiplies rare weights by 2, and test that the percentages still sum to 100%.

## Verified behaviour (tests passing)
- Odds sum to 1 and match the weights.
- Over **100,000 seeded rolls**, legendary frequency is within ±0.5 percentage points of 5%, and common within ±1 point of 70%.
- Pity forces legendary on roll 10 after 9 commons and resets the counter.
- NaN weights are rejected at construction.

## Design guidance (interpretation)
- Make the roll *readable*: rarity colour, a short anticipation beat, a stronger reveal for rarer tiers ([R05 Rare Reward Reveal](../18-Skill-Training/Design-Recipes/R05-Rare-Reward-Reveal.md)).
- Do not fake near-misses that misrepresent odds.
- See [CL-08 Shop and Monetization Ethics](../23-Quality-Checklists/CL-08-Shop-and-Monetization-Ethics.md).

## Common mistakes
- Rolling on the client.
- `math.random(1,100) <= 5` scattered through code instead of one table that drives both odds and display.
- Reusing the same `Random` seed across servers.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Paid random items policy](https://create.roblox.com/docs/production/monetization/paid-random-items)
