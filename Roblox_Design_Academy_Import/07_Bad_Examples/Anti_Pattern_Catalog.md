# Anti-Pattern Catalog (Import)

**Merge into:** `07_Bad_Examples/`. Keep this as a catalog file and link it from `UI_Anti_Patterns.md`, `Thumbnail_Anti_Patterns.md` and `Game_Design_Anti_Patterns.md`.

These are **hypotheses to evaluate, not universal bans**. Each entry answers the academy's six questions: what it looks like, why it fails, when it's harmful, when it works, how to fix it, and a better reference. Evidence: **[OBS]** = seen in a reference, **[RBX]** = Roblox docs, **[GEN]** = general practice, **[HYP]** = untested.

---

### AP-01 Gradient, glow, outline and shadow stacking
- **Looks like:** every element has a gradient fill, an outer glow, a thick outline and a drop shadow, all at once.
- **Fails because:** when everything carries the same ornament, the ornament stops signalling anything. Visual noise rises and hierarchy disappears. [GEN]
- **Harmful when:** applied to body text, small icons, or dense panels on a phone.
- **Works when:** used on **one** hero element (the main CTA or a legendary reward) in an otherwise flat UI.
- **Fix:** pick one depth cue per element type (e.g., a 2 px `UIStroke` *or* a shadow, not both). Reserve glow for rarity or attention.
- **Better:** [IMP-08](../06_Reference_Analyses/IMP-08_BotClash_Inventory_Master_Detail.md) (flat fills; one accent) · [IMP-07](../06_Reference_Analyses/IMP-07_Winds_of_Fortune_Stat_Icon_System.md)

### AP-02 Generic "template" UI identical across unrelated games
- **Looks like:** the same cartoon bevelled buttons, the same red-ribbon headers and the same rainbow tabs as dozens of other games, whatever the theme.
- **Fails because:** there's no identity, so players can't tell your game from its screenshots. [GEN/HYP]
- **Harmful when:** the theme is distinctive (horror, sci-fi, cozy) but the UI is stock cartoon.
- **Works when:** the game deliberately sits in a genre where that look *is* the convention and the identity is carried elsewhere.
- **Fix:** keep conventional **placement and meaning**, then create one geometric motif, one palette and one type pairing that come from your theme.
- **Better:** [IMP-10](../06_Reference_Analyses/IMP-10_Close_Button_Convention.md) · [IMP-08](../06_Reference_Analyses/IMP-08_BotClash_Inventory_Master_Detail.md) · [IMP-12](../06_Reference_Analyses/IMP-12_Mermaid_Life_Themed_Proximity_Prompt.md)

### AP-03 Too many competing focal points
- **Looks like:** several badges, timers, glowing buttons and animated arrows on one screen.
- **Fails because:** attention tools cancel each other out. Roblox: "Excessive use of bright, moving elements might overwhelm and confuse." [RBX]
- **Harmful when:** a first-time player needs to find one action.
- **Works when:** never for a primary screen. A celebratory screen may briefly be busy.
- **Fix:** per screen, have one primary (accent), at most two secondary, and keep the rest neutral. Run a blur/squint test.
- **Better:** [IMP-05](../06_Reference_Analyses/IMP-05_Dragon_Adventures_Premium_Shop.md) value ladder · [IMP-25](../06_Reference_Analyses/IMP-25_Duvall_Drive_Horror_Thumbnail.md)

### AP-04 Poor typography and inconsistent spacing
- **Looks like:** four or more fonts, all-caps sentences, italic grey body text, random padding.
- **Fails because:** reading slows, hierarchy flattens and the UI looks unplanned. [OBS IMP-04, IMP-11]
- **Harmful when:** text carries decisions (stats, prices, odds).
- **Works when:** a display font is used for 1–3 word titles and numbers.
- **Fix:** two families at most, one spacing scale (4 or 8 px), and a type scale with 4–5 sizes.
- **Better:** [IMP-09](../06_Reference_Analyses/IMP-09_Winds_of_Fortune_Shop_List.md)

### AP-05 Tiny text and unreadable mobile UI
- **Looks like:** desktop-sized labels on a phone, `TextScaled` shrinking text to fit, 10 px badges.
- **Fails because:** most players are on mobile [FACT]. `TextScaled` also ignores the player's PreferredTextSize setting [FACT].
- **Harmful when:** the information is needed mid-action.
- **Fix:** design at phone size first, use `UITextSizeConstraint` minimums, `AutomaticSize` containers, and test on a real phone.
- **Better:** [IMP-03](../06_Reference_Analyses/IMP-03_The_Survival_Game_Minimal_HUD.md) · [IMP-01](../06_Reference_Analyses/IMP-01_Spellbound_RPG_Contextual_Radial_Menu.md)

### AP-06 Unclear purchase buttons / confusing upgrade information
- **Looks like:** Robux and coin buttons identical; upgrade shows "Lv 4" without what changes; unaffordable items look buyable.
- **Fails because:** accidental spending, mistrust, or no purchase at all. [OBS IMP-06; GEN]
- **Fix:** distinct real-money treatment, "current → next" values with a delta, red price when unaffordable, a pending state during the prompt.
- **Better:** [IMP-05](../06_Reference_Analyses/IMP-05_Dragon_Adventures_Premium_Shop.md) (consistent price buttons) · [IMP-07](../06_Reference_Analyses/IMP-07_Winds_of_Fortune_Stat_Icon_System.md) (what an attribute increases)

### AP-07 Excessive particles and camera shake
- **Looks like:** every click explodes, the camera shakes on every hit, and particles cover enemies.
- **Fails because:** gameplay becomes unreadable, causes motion sickness, and costs performance through fill-rate and overdraw (**mobile is limited to 100 particles/s per emitter**) [FACT + GEN].
- **Works when:** rare, high-value moments (boss kill, legendary drop).
- **Fix:** scale intensity to importance, use `Emit()` bursts, honour `ReducedMotionEnabled`.
- **Better:** [IMP-19](../06_Reference_Analyses/IMP-19_Winds_of_Fortune_Combat_Feedback.md)

### AP-08 Long animations for frequent actions
- **Looks like:** a 2-second reveal every time a common coin or item is collected.
- **Fails because:** it blocks input and turns delight into waiting. [GEN]
- **Works when:** rare rewards, the first-time reveal of a feature.
- **Fix:** keep frequent feedback under about 0.3 s; make long sequences skippable and batched. [HYP values]

### AP-09 Sound effects too loud or repetitive
- **Looks like:** the same full-volume sample on every click.
- **Fails because:** fatigue leads players to mute the game, which loses all the audio feedback. [GEN]
- **Fix:** pitch and sample variation, a loudness hierarchy, separate volume sliders [FACT accessibility]. *(No audio was evaluated in this research.)*

### AP-10 Overcomplicated progression
- **Looks like:** five currencies, three upgrade trees, rebirths, a pass and crafting, all in the first hour.
- **Fails because:** cognitive overload and an unclear next goal. Roblox recommends teaching the essentials and delaying non-essential systems. [RBX]
- **Works when:** introduced gradually through contextual tutorials to players who have already been retained.
- **Fix:** one currency and one upgrade path in session 1, with each new system unlocked on first relevance.
- **Better:** [IMP-20](../06_Reference_Analyses/IMP-20_Squishmallows_Contextual_Tutorial.md)

### AP-11 Attractive visuals that obscure gameplay
- **Looks like:** bloom, fog, dense foliage or particles hiding hazards; decorative UI over the play area.
- **Fails because:** players fail without understanding why. [GEN]
- **Fix:** keep the centre clear, give gameplay-relevant objects the highest contrast and readable silhouettes, keep decoration low-contrast.
- **Better:** [IMP-03](../06_Reference_Analyses/IMP-03_The_Survival_Game_Minimal_HUD.md)

### AP-12 Thumbnails with too many subjects or too much text
- **Looks like:** several characters, logos, badges and slogans in one frame.
- **Fails because:** nothing reads at grid size, and the bottom gets covered by metadata [FACT].
- **Fix:** one idea, one focal point, 0–3 words.
- **Evidence:** [IMP-24](../06_Reference_Analyses/IMP-24_Comical_Theme_Thumbnail.md) (prop clutter) · [IMP-23](IMP-23_Unclear_Thumbnail.md) (no subject)

### AP-13 Copying a popular game without its own identity
- **Looks like:** the same loop, UI, thumbnail composition and name pattern as a trending game.
- **Fails because:** the copy can't win on the original's terms, and players already have the original. [GEN/HYP]
- **Works when:** iterating on a proven *loop* with a genuinely new twist, theme or social hook. Roblox notes iteration on proven designs is valid and that "strange and innovative games can find more success on Roblox than they would elsewhere" [RBX].
- **Fix:** copy the **principle** ("value shown by illustration scale"), never the **expression** (their art, layout or colours).

### AP-14 Default or unrelated icon, stickers on key art
- **Evidence:** [IMP-27](IMP-27_Icon_Failures.md) [RBX ❌ examples]
- **Fix:** a custom 512×512 icon with one subject and no stickers.

### AP-15 Stacked modals and interrupting purchase prompts
- **Looks like:** a daily reward, an offer and an update popup stacked on join; a buy prompt mid-combat.
- **Fails because:** the first minutes decide retention, and Roblox explicitly warns against layered modals [RBX].
- **Fix:** a modal queue (one at a time), with offers only at natural pauses (lobby, intermission, pre-run).

---

## Still needed (not found in accessible material)
Real-world negative examples from actual Roblox games for AP-01, AP-02, AP-07, AP-08, AP-09 and AP-12. The user should supply screenshots or clips (see [10_Reference_Wishlist_and_Capture_Guide.md](../10_Reference_Wishlist_and_Capture_Guide.md)).
