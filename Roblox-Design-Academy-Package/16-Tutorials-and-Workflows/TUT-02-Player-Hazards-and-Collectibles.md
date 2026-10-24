---
title: "TUT-02 — Create player hazards and touch collectibles"
tags: [tutorial, luau, touched, hazards, collectibles]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-02 — Create player hazards and touch collectibles

**Skill:** Detect a character touching a part and react on the server (kill volume, collectible coin with cooldown).

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/create-player-hazards) · [https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Hazard: an invisible, non-colliding part over the water; a server Script gets every part in a `Hazards` folder with `GetChildren()`, connects `Touched`, finds a `Humanoid` in the toucher's parent and sets `Health = 0`.
2. Coins (script-game-behavior page): same pattern; on touch the coin becomes transparent, the player is credited, and after a cooldown the coin reappears.
3. The hazard part is set `Transparency = 1` and `CanCollide = false` so players see the real water and fall into it.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Invisible trigger volume rather than scripting the water itself. | Decouples the visual (water/terrain) from the rule (the trigger part), so either can change. |
| Server Script, not LocalScript. | Health and currency changes must be authoritative. |
| Folder + loop instead of one script per part. | One place to change behaviour; adding a hazard is just adding a part. |

## Our analysis
- **[ANALYSIS] `GetChildren()` runs once at start.** Hazards or coins added later (streamed in, spawned by a round system) are never connected. Use `CollectionService` tags with `GetInstanceAddedSignal`, or connect `ChildAdded` on the folder.
- **[ANALYSIS, source-supported] Touched is client-influenced.** Roblox's security-tactics page lists triggering Touched events "at any range or frequency" as an exploiter capability, and the network-ownership page notes clients can manipulate Touched firing. For a kill brick that is harmless (they hurt themselves); for coins it means collecting from anywhere. Add a server distance check between the character's root and the coin before crediting.
- **[ANALYSIS]** `Touched` fires many times per contact (each limb). The coin's cooldown flag acts as a debounce; a hazard does not need one because setting health to 0 twice is idempotent.
- **[ANALYSIS] Feel.** An instant, silent kill reads as unfair. Telegraph the hazard ([AV-22 Hazard Telegraph](../08-Animation-and-Game-Feel/Recipes/AV-22-Hazard-Telegraph.md)).

## Common mistakes
- No debounce on coins → one touch credits 5–10 times.
- Checking `otherPart.Parent:FindFirstChild("Humanoid")` on accessories, whose parent is the accessory, not the character (use `FindFirstAncestorOfClass("Model")` or `Players:GetPlayerFromCharacter`).
- Trigger part left `CanCollide = true`, so players stand on the 'water'.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Some coins don't work | They were added after the loop ran; switch to tags or `ChildAdded`. |
| Coins credited multiple times | Missing or late debounce; set the flag before any yield. |
| Hazard fires on unanchored debris | Filter for a character with a Humanoid and a Player. |

## Reusable procedure (ours)
1. Tag every interactive part (`Hazard`, `Coin`) with CollectionService.
2. Server: handle existing tagged parts and `GetInstanceAddedSignal` for new ones.
3. On `Touched`: resolve the player with `Players:GetPlayerFromCharacter(model)`; ignore non-players.
4. Debounce per part (coin) or per player-part pair; check distance on the server for rewards.
5. Apply the effect, then play feedback (sound/particles) — feedback can be client-side.

## Exercise
Make a lava floor (kill) and 10 respawning coins using tags; spawn 5 more coins 10 s after start.

### Acceptance criteria
- [ ] The 5 late coins work without restarting.
- [ ] One coin pickup credits exactly 1 coin (verify with a print counter while walking through it repeatedly).
- [ ] A coin cannot be collected from more than ~10 studs away (test by firing the touch from a remote position in a test script).
- [ ] The lava shows a warning cue before contact.

## Related
- [LU-03 Client–Server Responsibilities](../07-Roblox-Studio-and-Luau/LU-03-Client-Server-Responsibilities.md)
- [LU-05 Server Validation](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)
- [R03 Currency Collection](../18-Skill-Training/Design-Recipes/R03-Currency-Collection-Interaction.md)
- [AV-03 Collecting](../08-Animation-and-Game-Feel/Recipes/AV-03-Collecting.md)
