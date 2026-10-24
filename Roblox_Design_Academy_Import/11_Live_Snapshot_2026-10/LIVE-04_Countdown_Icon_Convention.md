# Reference LIVE-04 — The Countdown Icon Convention (12 of 46 icons)

## Metadata
- Category: Icons / Live-ops
- Source: 12 games in the 2026-10-24 sample:
  - Cat Battles (10769543567)
  - +1 Venom Evolution (10769464063) — "24 HOUR"
  - Steel Fighters (10765618402) — "NOW!"
  - Bike For Egg! (10766620257) — "NOW!"
  - Something Is Wrong With My Dog (10762148295) — "NOW"
  - +1 Slinky Escape (10769903740) — "3 HOURS"
  - Steal a Brainrot (7709344486) — "30 MINS"
  - Murderers VS Sheriffs (7219654364) — "2 HOURS"
  - Fish It! (6701277882) — "6 HOURS"
  - Huss Valley (10764627709) — "NOW!"
  - Ragdoll Reality (10770605947) and Speed Keyboard Escape (9584852943), which use a big "NOW" without the hourglass
- Asset: `../Assets/Icons/LIVE/<universeId>.jpg` for each; grids `../Assets/Thumbnails/LIVE/_sheets/icons150_a.jpg`, `icons150_b.jpg`, `icons64.jpg`
- Date added: 2026-10-24 (snapshot: Halloween week)
- Rating: 3/5 (useful convention, costly to identity)
- Confidence: High for the observation. The *effect* on clicks is unknown.
- Reference type: Mixed

## Context
Before an update, many games temporarily replace their icon with the original art darkened, a large white hourglass, and a countdown word ("24 HOUR", "6 HOURS", "30 MINS", "NOW!"). The name often carries a matching tag ([6 HRS], [NOW]).

## What Works
- **It signals that something is happening.** It gives returning players a reason to join at a specific time, and Roblox's home grid gives the icon real estate for free.
- It's a **shared platform convention**: players clearly understand it, since even top-10 games use it.

## What Does Not Work
- **It erases identity.** At 64 px the 12 icons are nearly interchangeable (white hourglass, dark background). New players can't tell what the games are.
- It serves **locals** (people who already know the game) at the expense of **tourists** (discovery). See the tourists-and-locals idea in [Retention](../05_Game_Design/Retention_and_Replayability.md).
- It becomes noise when a quarter of the grid does the same thing.

## Reusable Design Rules
1. If you use a countdown icon, **keep the game's key subject recognisable**. Put the timer in a corner band, not a full-frame overlay. *(Hypothesis: test it with thumbnail personalization and Experiments.)*
2. Use it **only briefly** (hours), then restore or upgrade the icon.
3. Design the base icon so its silhouette survives darkening (strong shape, not texture).

## Limitations
No data on click-through. Icons change daily, so this is one snapshot.

## Related Notes
[Game Icon Principles](../03_Thumbnails_And_Icons/Game_Icon_Principles.md) · [Retention and Replayability](../05_Game_Design/Retention_and_Replayability.md)
