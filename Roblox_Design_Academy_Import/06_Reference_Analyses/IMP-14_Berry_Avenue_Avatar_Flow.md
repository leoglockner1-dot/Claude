# Reference IMP-14 — Berry Avenue: Low-Friction Avatar Flow (Process Reference)

## Metadata
- Category: UX / Flows
- Source: Roblox Creator Docs, "UI and UX design" > Design flows. Game: https://www.roblox.com/games/8481844229/
- Asset: `../Assets/UI/IMP-14_berry-avenue-avatar-flow.png` (Roblox's flow chart), `../Assets/Animations/IMP-14_berry-avenue-avatar-flow.mp4` (**downloaded, not analyzed**)
- Date added: 2026-10-24
- Rating: 4/5 as a method
- Confidence: High for the method, none for the visuals (video not watched)
- Reference type: Positive (process)

## Context
The flow is: Tap Avatar → (Body-part tab **or** Search) → Select item ⇄ Remove item → Done. Roblox presents it as a low-friction flow, derived from player goals: modify quickly, find items easily, preview instantly, remove easily.

## Reusable Design Rules
1. Write the **player goals** for a feature first, then design the flow, then the screens.
2. **Draw the flow chart and count the taps** to the core goal. Every extra step is friction.
3. Give two ways in (browse by category **and** search) for any collection over about 30 items.
4. **Preview instantly on the avatar or object**, without a confirm step.
5. Make "undo" equal to "tap again".

## Application to Roblox Development
Before building any menu in Studio, add a Mermaid flow chart to the project note in Obsidian. Use it as an acceptance criterion: "equip in ≤ 4 taps".

## Limitations
The video still needs to be watched to judge animation and feedback. Add a sequence analysis later.

## Related Notes
[Menus and Navigation](../02_UI_UX/Menus_and_Navigation.md) · [Shops and Inventory](../02_UI_UX/Shops_and_Inventory.md) · [UI Review](../09_Quality_Checklists/UI_Review.md)
