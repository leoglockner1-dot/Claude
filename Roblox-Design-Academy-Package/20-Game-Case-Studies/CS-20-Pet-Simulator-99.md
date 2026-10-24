---
title: "CS-20 — Pet Simulator 99 (pet collection incremental with heavy monetization surface)"
tags: [case-study, simulator, incremental, collection, pets, monetization]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-20 — Pet Simulator 99 (pet collection incremental with heavy monetization surface)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [🎉 [PSX] Pet Simulator 99! 🐾](https://www.roblox.com/games/8737899170/) · universe 3317771874 · by BIG Games Pets |
| Genre (Roblox) | Simulation / Incremental Simulator · max 10 players per server |
| Concurrent players at capture | 64,652 |
| Visits · favourites | 2,680,132,839 · 2,215,399 (0.83 per 1k visits) |
| Like ratio | 95% (3,074,384 up / 170,726 down) |
| Created / updated | 2022-02-05 / 2026-10-24 |
| Game passes for sale | 13 · 175–3250 R$ (median 625) · e.g. Huge Hunter! 🔥 (3250), Auto Farm! ♻️ (175), Ultra Lucky! 🍀✨ (800), VIP! ⭐ (400), +15 Eggs! 🥚 (625), Magic Eggs! ✨ (1200), Auto Tap! ☝️ (350), +15 Pets! 🐾 (375) |

**Developer description (excerpt):** "Create an army of the coolest pets! They will help you get RICH! ✨ Currently 3,000+ pets to collect! 🐾 🧡 Thanks for playing!"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Create an army of pets that help you get rich; "3,000+ pets to collect". |
| Main action | [INF] Break breakables/collect coins with pets; hatch eggs. |
| Immediate feedback | [INF] Coin popups, egg hatch reveals (rarity presentation). |
| Reward → new possibility | [INF] Currency → eggs → stronger pets → new areas/zones; rarity tiers. |
| Micro loop (seconds) | [INF] Target selection, mostly automatic once pets are assigned. |
| Core loop (minutes) | [INF] collect currency → hatch → equip best pets → unlock next zone. |
| Meta loop (days) | [DEV] 3,000+ collectibles; [DATA] 13 passes for sale incl. "Auto Farm" (175 R$), "Ultra Lucky" (800), "VIP" (400) and a "Huge Hunter" (3,250). |

## First-time experience
[INF] The description is two lines and states only the fantasy (army of pets, get rich). A new player's first actions are not described. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A collection target that is effectively unbounded (3,000+) and rarity tiers make every hatch a lottery moment. |
| Weakest part / quit risks | [INF] Many monetization options around luck and automation; the "Auto Farm" pass means the core action itself can be skipped, so the game may be valued for collecting rather than playing. **Paid luck boosts are probability modifiers under Roblox's paid random items policy** and need numerical disclosure ([LU-13](../07-Roblox-Studio-and-Luau/LU-13-Random-Rewards.md)). |
| Essential features | Hatch reveal, rarity ladder, zone gates, pet equip/strength. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 3 eggs × 5 pets with rarities, a coin field, one zone gate; test whether hatching alone motivates 10+ minutes. |

## Reusable lessons
- When automation is sold, the *purpose* of play shifts to collection/status; design the collection to carry the game.
- Rarity reveal presentation is the payoff; budget animation and sound for it ([R05](../18-Skill-Training/Design-Recipes/R05-Rare-Reward-Reveal.md)).

## Original application (do not copy the game)
A fossil museum: excavate dig sites with assistant dinosaurs; rare fossils complete exhibits that visitors pay to see.

## Confidence
Low–medium: the description is minimal; structure inferred from genre and passes.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
