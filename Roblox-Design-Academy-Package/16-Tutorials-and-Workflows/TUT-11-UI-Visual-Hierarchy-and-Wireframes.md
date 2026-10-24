---
title: "TUT-11 — UI design curriculum: art style, visual hierarchy, wireframes, implementation"
tags: [tutorial, ui, wireframe, hierarchy, mobile]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-11 — UI design curriculum: art style, visual hierarchy, wireframes, implementation

**Skill:** Plan UI by importance and screen position, block it in, then implement and test on emulated devices.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts) · [https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/implement-designs-in-studio](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/implement-designs-in-studio)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Choose an art style for UI consistent with the world.
2. Plan a **visual hierarchy**: order elements by importance and decide where on screen each lives (the laser tag table: objective at top centre, crosshair and hit marker centre, blaster info over the blaster, blast button near the right thumb).
3. Block in elements with basic shapes; reserve space for Roblox core UI and default touch controls.
4. Place interactive elements within thumb reach on mobile.
5. Develop user flows, then implement in Studio with multiple `ScreenGui`s grouped by context, testing with the Device Emulator.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Hierarchy before visuals. | Importance decides size, position and contrast; styling comes after. |
| Reserve touch zones. | Default controls overlap custom UI on phones. |

## Our analysis
- **[ANALYSIS]** Matches our [R02 Clean Readable HUD](../18-Skill-Training/Design-Recipes/R02-Clean-Readable-Gameplay-HUD.md) and the [UI review checklist](../23-Quality-Checklists/CL-01-UI-Review.md); the tutorial adds the explicit reserved-zones step.
- **[ANALYSIS]** Separate ScreenGuis per context make it cheap to hide whole groups (e.g. during results screens).

## Common mistakes
- Designing on a desktop canvas only.
- Buttons at the top corners on mobile.
- Everything the same size → no hierarchy.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| UI hidden behind thumbsticks | Check the reserved touch zones image in the docs; move elements. |
| UI overlaps the notch | See TUT-12 safe areas. |

## Reusable procedure (ours)
1. List information and actions; rank by importance and frequency.
2. Assign screen zones; reserve core/touch areas.
3. Wireframe with grey boxes at phone size first.
4. Implement, grouped by context ScreenGuis.
5. Test on 3+ emulated devices; fix overlaps.

## Exercise
Wireframe the HUD for 'Ember Keepers' at phone size: heat counter, species index button, pool action.

### Acceptance criteria
- [ ] A ranked list of HUD elements exists with reasons.
- [ ] On the smallest emulated phone, no element overlaps touch controls or core UI.
- [ ] The primary action sits in thumb reach.

## Related
- [HUD Layouts](../01-UI-UX/HUD-Layouts.md)
- [Mobile, Controller and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md)
- [LU-14 UI Implementation](../07-Roblox-Studio-and-Luau/LU-14-UI-Implementation.md)
- [R13 Readable Mobile Interface](../18-Skill-Training/Design-Recipes/R13-Readable-Mobile-Interface.md)
