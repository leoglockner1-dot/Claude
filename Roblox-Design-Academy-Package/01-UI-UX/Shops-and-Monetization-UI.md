---
title: "Shops and Monetization UI"
tags: [ui, shop, economy]
note_type: "topic"
---

# Shops and Monetization UI

## Evidence
| Pattern | Evidence |
|---|---|
| Value ladder; quantity shown by art scale; hero offer isolated | [UI-05](Analyses/UI-05-Dragon-Adventures-Premium-Shop.md) |
| Group product types by container; rarity tag + colour; restock timer in header | [UI-06](Analyses/UI-06-Tower-Defense-Simulator-Daily-Shop.md) |
| Free vs premium separated by position + colour | [UI-04](Analyses/UI-04-Jailbreak-Season-Pass.md) |
| Soft vs premium currency buttons in different colours | [UI-16](Analyses/UI-16-DevForum-Inconsistent-Quest-and-Shop.md) |
| Harsh palette, unreadable contents, mixed fidelity | [UI-15](Analyses/UI-15-DevForum-Harsh-Pack-Shop.md) |
| Currency icons that look alike | [UI-17](Analyses/UI-17-DevForum-Cream-Category-Shop.md) |
| Row hierarchy: name → coloured price → muted meta | [UI-09](Analyses/UI-09-Winds-of-Fortune-Shop-List.md) |

## Contextual purchases (Roblox docs)
In-play (Dress to Impress intermission theme props), **pre-play** (Doors elevator pre-run shop), lobby 3D objects (Super Striker League), complementary passes (Bee Swarm), UI offers (loading screens, modal — Adopt Me mansion). Rules: never interrupt active play; allow time for the Robux flow; prevent modal stacking.

## Market context
Median pass price **249 R$** (695 for-sale passes, 85 games); most common prices 99/199/299/399/499 → [Game Pass Economy Study](../05-Progression-and-Economy/Game-Pass-Economy-Study.md).

## Policy (must)
Paid random items: show all outcomes with % odds summing to 100 % before purchase; labelled "Odds/Details" button, not a bare (i) → [Random Rewards and Fairness](../05-Progression-and-Economy/Random-Rewards-and-Fairness.md).

## Recipe & checklist
[R07 Responsive Shop](../18-Skill-Training/Design-Recipes/R07-Responsive-Shop.md) · [CL 08 Shop and Monetization Ethics](../23-Quality-Checklists/CL-08-Shop-and-Monetization-Ethics.md)
