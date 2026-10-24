---
title: "Core Loop Library — concepts evaluated with the framework"
tags: [core-loop, concepts, game-design, benchmark]
note_type: "library"
evidence: "concept work by the academy ([HYP] throughout); patterns cited from case studies"
---

# Core Loop Library

Concept sheets written with the [Core Loop Evaluation Framework](Core-Loop-Evaluation-Framework.md). **Every claim here is a hypothesis [HYP]** until playtested. The value is in the reasoning, the explicit boredom points and the failure criteria. Also serves as the worked answer to benchmark [BM-01](../19-Benchmarks-and-Practical-Exams/BM-01-Three-Core-Loops-One-Theme.md).

## Theme: "A volcano island"
Three deliberately different loops for one theme, to show that a theme does not decide the game.

### Concept A — "Ember Keepers" (cozy collection incremental)
| # | Field | Answer |
|---|---|---|
| 1 | Premise | You tend lava pools that grow **ember creatures**; each species changes how your pools behave, but the volcano's mood shifts daily. |
| 2 | Main action | Scoop glowing embers from your pools and feed them to creatures (click/tap a pool, drag to a creature). |
| 3 | Feedback | Ember arcs to the creature, creature grows a size step with a "pop" ([R03](../18-Skill-Training/Design-Recipes/R03-Currency-Collection-Interaction.md)), a sound pitch rising with combo. |
| 4 | Reward | Grown creatures produce **heat** (currency) and sometimes hatch a new species. |
| 5 | New possibility | New species have a **pool rule** (Frost Salamander cools a pool to make obsidian; Ash Moth spreads embers to neighbours) → new layouts and combinations, not only rates. |
| 6 | Micro loop | Scoop → feed → grow (5–10 s). Decision: which creature to feed first (combo bonus for the same species). |
| 7 | Core loop | Feed → produce heat → buy pool expansions/species eggs → rearrange pools for synergies (5–10 min). |
| 8 | Meta loop | Species index (collection), daily "volcano mood" modifier, offline growth (server timestamp), visiting friends' calderas. |
| 9 | First session | 0–10 s: you stand by one glowing pool with one sleepy creature (a world point, no text). 10–30 s: tap pool → feed → creature wakes. 60–90 s: first heat reward flies to the counter. 3–5 min: first new species hatches **and changes a pool**. End: the index shows silhouettes of 3 undiscovered species. |
| 10 | Progression | Species count and synergies; pacing target: next purchase ≤ 45 s in the first 10 min ([LU-12](../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md)). |
| 11 | Boredom points | Once synergies are solved; feeding becomes routine → daily moods must alter the best layout. |
| 12 | Minimal prototype | 3 pools, 3 species (one with a rule), heat counter, one expansion; no shop UI beyond 3 buttons. |
| 13 | Playtest | 6 testers, 15 min each; watch time to first feed, whether they rearrange pools unprompted, reactions to the first rule-changing species. |
| 14 | Success | ≥ 4/6 rearrange pools without being told; ≥ 4/6 can name what the second species does; median session ≥ 10 min. |
| 15 | Failure | Players ignore species rules (treat them as stat boosts) → rules too subtle; or session < 5 min → micro loop not satisfying. |

### Concept B — "Last Boat Out" (co-op escape, 4 players)
| # | Field | Answer |
|---|---|---|
| 1 | Premise | The volcano erupts in **8 minutes**; your crew must repair a boat with parts scattered across the island while lava flows reshape the paths. |
| 2 | Main action | Carry parts (one per player, two for heavy parts) to the boat; choose routes around lava. |
| 3 | Feedback | Lava creep shown on a diegetic map at the dock; part snaps onto the boat with a hammer sound; eruption rumble escalates. |
| 4 | Reward | Escape (with a score by speed and parts saved); cosmetic crew boat decorations. |
| 5 | New possibility | Each run's lava pattern differs (randomized vents); unlocked tools (grapple, cooling bucket) open shortcuts. |
| 6 | Micro loop | Route choice + timing under rising threat; carrying heavy parts **together** (physical cooperation like [Webbed!](../20-Game-Case-Studies/CS-33-Webbed.md), not role dependency). |
| 7 | Core loop | Spawn → split up → fetch → regroup for heavy parts → launch before eruption (8 min). |
| 8 | Meta loop | Crew level, tool unlocks, island variants, weekly "volcano type" event. |
| 9 | First session | 0–10 s: the dock, the broken boat and a huge countdown on the volcano. 10–30 s: highlighted nearest part. First run likely fails; failure shows "3 parts missing" on the boat (failure as information, [CS-07 DOORS](../20-Game-Case-Studies/CS-07-DOORS.md)). |
| 10 | Progression | Tools (new routes), harder islands; mastery of routes. |
| 11 | Boredom points | Memorized layouts → vent randomization; solo players → bots carry heavy parts slowly (solo fallback). |
| 12 | Minimal prototype | One island graybox, 4 parts (1 heavy), lava that blocks 2 paths at fixed times, a countdown. |
| 13 | Playtest | 3 groups of friends + 2 groups of strangers; record communication, failure reasons, rematch choice. |
| 14 | Success | ≥ 4/5 groups choose "play again"; strangers complete at ≥ 50% of the friends' rate. |
| 15 | Failure | Strangers rarely finish (dependency too hard) → loosen heavy-part rule; groups never split up (map too small to need planning). |

### Concept C — "Obsidian Rush" (competitive risk/reward, rounds)
| # | Field | Answer |
|---|---|---|
| 1 | Premise | Players mine obsidian from cooling lava fields; **the longer you stay on hot ground, the more you mine, and the more you risk melting**; bank before the field re-erupts. |
| 2 | Main action | Hold to mine on a lava crust that heats under you; step to safe rock to bank. |
| 3 | Feedback | Ground colour shifts from black → red → white under your feet; sizzling audio rising; banked obsidian stacks behind you visibly. |
| 4 | Reward | Banked obsidian = round score; round win → season points; cosmetics for pickaxes. |
| 5 | New possibility | Each round's field shape changes; players can **steal** unbanked obsidian by bumping (risk for both). |
| 6 | Micro loop | Push-your-luck: mine one more second or retreat ([GM-11](../04-Game-Mechanics/GM-11-Risk-and-Reward.md)). |
| 7 | Core loop | Round (90 s): mine → bank → re-erupt → results. |
| 8 | Meta loop | Season ranks, pickaxe cosmetics (no stat advantages: [P6](../20-Game-Case-Studies/Case-Study-Index.md)). |
| 9 | First session | 0–10 s: arena of glowing crust; the first ground "heats" under the player with a big warning ring. First round teaches greed by failure. |
| 10 | Progression | Skill (reading the heat), cosmetics, rank. |
| 11 | Boredom points | One dominant strategy (always bank at 50% heat) → random "cool spots" and bump-steals keep decisions live. |
| 12 | Minimal prototype | One flat arena, heating tiles, a bank zone, 4 players, 90-second rounds. |
| 13 | Playtest | 8 testers in 2 servers × 5 rounds; track the heat level at banking per round (do strategies vary?). |
| 14 | Success | Banking heat levels vary across players and rounds; ≥ 6/8 want another round. |
| 15 | Failure | Everyone converges on one banking point by round 3 (solved); eliminations feel random (heat unreadable). |

### Comparison (why three loops for one theme matters)
| | A Ember Keepers | B Last Boat Out | C Obsidian Rush |
|---|---|---|---|
| Core feeling | Calm cultivation | Shared panic | Greed vs fear |
| Skill / decision | Layout synergy (decision) | Routing + cooperation | Push-your-luck timing |
| Session shape | Long, returning daily | 8-minute runs | 90-second rounds |
| Social | Visits | Cooperation | Competition |
| Biggest risk | Number-only feel if rules are subtle | Stranger dependency | Solved strategy |
| Cheapest to prototype | ✅ (single player) | ✗ (needs 4 testers) | ✓ |
**Recommendation if only one can be built:** C first (cheapest and fastest to falsify; the failure criteria show up within 5 rounds). Then A if the team wants long-term live ops.

## More concept sheets
Add new sheets below in the same 15-field format. Keep the [HYP] label until a playtest result is attached.
