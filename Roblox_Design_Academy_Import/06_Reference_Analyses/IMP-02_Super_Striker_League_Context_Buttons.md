# Reference IMP-02 — Super Striker League: Context-Swapping Action Buttons

## Metadata
- Category: UI / HUD / Mobile
- Source: Roblox Creator Docs, "UI and UX design" > Prioritization. Game: https://www.roblox.com/games/3360853050/
- Asset: `../Assets/UI/IMP-02_super-striker-league-no-ball.png`, `../Assets/UI/IMP-02_super-striker-league-with-ball.png`
- Date added: 2026-10-24
- Rating: 4/5 for the context-swap idea, 2.5/5 for the visual polish
- Confidence: High for the swap behaviour (Roblox describes it), Medium for the visual observations
- Reference type: Mixed

## Context
A mobile soccer game. **Without the ball** the buttons are Tackle, Shoot and Sprint. **With the ball** they become Deke, Pass and Shoot. The layout stays the same and only the meaning changes.

## What Works
- **Context-sensitive buttons.** Only actions that are possible right now are on screen, so the player never sees a dead button.
- **Thumb-zone placement.** Three large circles sit bottom-right in a triangle, which is easy to reach on a phone.
- **Team colour carries meaning.** The score reads red 0 | black timer | blue 0, so team colours double as the score key.
- **In-world guidance.** Blue chevrons on the grass and a yellow arrow over the player show where to run or pass, which teaches by pointing rather than by text.
- A segmented stamina bar with a lightning icon sits bottom-left, away from the action buttons.

## What Does Not Work
- **Two unrelated button languages.** The action buttons are round translucent "glass", while Scoreboard and Callouts are rectangular solid-blue tabs. The HUD feels assembled rather than designed.
- **Translucent buttons over bright grass** lose contrast, and the label alone carries legibility.
- The stamina bar's brown wood texture matches nothing else on screen.

## Visual Analysis
- Composition: the centre and upper-middle are kept clear for play. UI hugs the corners, which is good.
- Contrast: white text with a dark outline survives the background, but the button bodies barely do.
- Consistency: low, since there are three styles (glass, flat-blue, wood).

## Reusable Design Rules
1. **Swap button meanings by context** instead of showing every action at once. Keep positions fixed so muscle memory holds.
2. When the context changes, make the change noticeable (brief scale pulse or icon swap) so the player sees that the button now does something else.
3. One HUD = one button family. Shape, fill and stroke rules apply to every button.

## Anti-Patterns
- Context swaps that **move** buttons break muscle memory.
- Glass or translucent buttons over a variable 3D background need a solid fallback or a darker plate.

## Application to Roblox Development
Use the Input Action System: bind actions per context, use `InputActionLabel` for glyphs, and toggle action sets when possession changes. Use `GuiService.PreferredTransparency` to make translucent buttons opaque for players who ask for it.

## Limitations
Swap timing, animation and sound were not observable. Only the doc's two screenshots were seen.

## Related Notes
[HUD Design](../02_UI_UX/HUD_Design.md) · [Mobile UI](../02_UI_UX/Mobile_UI.md) · [UI Anti Patterns](../02_UI_UX/UI_Anti_Patterns.md) · [Core Loops](../05_Game_Design/Core_Loops.md)
