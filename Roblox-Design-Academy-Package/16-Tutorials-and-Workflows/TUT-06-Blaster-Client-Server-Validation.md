---
title: "TUT-06 — Implement blasters (client prediction, server validation)"
tags: [tutorial, luau, combat, validation, cooldown]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/implement-blasters"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-06 — Implement blasters (client prediction, server validation)

**Skill:** Make a responsive action on the client while the server stays the source of truth for timing and position.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/implement-blasters](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/implement-blasters)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Input fires on `UserInputState.Begin` (the tutorial invites testing `End` to feel the difference in responsiveness).
2. The client generates blast data (origin from the camera CFrame, directions, raycast results), plays effects immediately, and sends the data to the server with a RemoteEvent.
3. Both client and server enforce the cooldown (`secondsBetweenBlasts` attribute); the server is authoritative.
4. The server checks that the blast origin is near the player's character, using `DISTANCE_SANITY_CHECK_TOLERANCE_STUDS`.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Effects on the client first. | Waiting for the server round-trip would make the blaster feel laggy. |
| The same cooldown on both sides. | The client avoids sending requests the server will reject; the server prevents rapid-fire exploits. |
| A tolerance chosen from data. | The tutorial suggests printing the typical positional difference during play, then picking a threshold — and revisiting it if movement speed changes. |

## Our analysis
- **[ANALYSIS]** This is the most complete validation example in the official tutorials: calibrate thresholds from logs instead of guessing. Apply the same method to any rate or distance check ([LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)).
- **[ANALYSIS]** Tolerances are trade-offs: too tight rejects laggy honest players; too loose lets cheaters through. Log rejections in playtests to tune.

## Common mistakes
- Server trusting the client's timestamp for cooldowns.
- Playing effects only after the server answers.
- Hard-coding the tolerance and later doubling walk speed.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Honest players' shots rejected | Log the measured distance at rejection; raise the tolerance or account for ping. |
| Rapid fire still possible | Cooldown checked only on the client. |

## Reusable procedure (ours)
1. Client: act and show feedback immediately; send the minimum data needed.
2. Server: rate-limit (cooldown from server time), validate types, check positions against the character with a measured tolerance.
3. Apply effects server-side; replicate results.
4. Log rejected requests with the measured values.

## Exercise
Add a 'dash' ability with a 2 s cooldown: client moves immediately; server checks cooldown and dash distance.

### Acceptance criteria
- [ ] A test script firing the remote 10× per second gets at most one dash per 2 s.
- [ ] The distance tolerance is justified by a logged measurement written in the script comment.
- [ ] Dash feels instant at 200 ms emulated latency (Studio network simulation).

## Related
- [LU-06 Rate Limiting](../07-Roblox-Studio-and-Luau/LU-06-Rate-Limiting.md)
- [LU-15 Input Handling](../07-Roblox-Studio-and-Luau/LU-15-Input-Handling.md)
- [AV-08 Impact](../08-Animation-and-Game-Feel/Recipes/AV-08-Impact.md)
