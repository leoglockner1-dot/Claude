# Checklist Additions (Import)

**Merge into:** the matching files in `09_Quality_Checklists/`. Add only the items that aren't already there. Every item is **observable**. Mark each one as ✅ verified (how) / ❌ failed / ⬜ not checked. **Never tick an item that wasn't checked.**

## → UI_Review.md
- [ ] Screenshot taken **on a phone or the phone emulator** at the smallest supported size; all text readable without zooming
- [ ] Squint/blur test: the brightest, most saturated element is the screen's primary action
- [ ] Exactly **one** accent-coloured primary action per screen
- [ ] At most two font families; no sentence set in all caps
- [ ] Padding and gaps use only the spacing scale (check 3 random gaps)
- [ ] All button states exist: normal, hover, pressed, selected, disabled, pending
- [ ] The selected tab is **more** prominent than unselected ones
- [ ] No UI overlaps the Roblox top bar, chat or player list (`ScreenInsets` checked)
- [ ] No information relies on colour alone (greyscale screenshot check)
- [ ] Works with `PreferredTextSize = Largest` (no clipping; not relying on `TextScaled`)
- [ ] Works with `PreferredTransparency = 0` and with `ReducedMotionEnabled = true`
- [ ] Gamepad: every control is reachable with D-pad and select/back; key actions take ≤ 3 moves
- [ ] Input hints match the active device (no keyboard letters on touch)
- [ ] Longest expected string (and one localized string) fits
- [ ] Modals never stack (open two triggers at once and observe)
- [ ] Robux buttons are visually distinct from soft-currency buttons
- [ ] Paid random items show all outcomes and % odds (sum 100%) before purchase, behind a labelled button if needed
- [ ] Flow chart drawn; the tap count to the main goal is recorded and accepted

## → Thumbnail_Review.md
- [ ] 1920×1080, 16:9, no visible compression artefacts
- [ ] Viewed at actual grid size next to 10 competitor thumbnails: the subject is recognisable
- [ ] A viewer can complete "a game where you ___" in one second (ask someone who hasn't seen it)
- [ ] Exactly one focal point (blur test); silhouette readable
- [ ] Nothing essential in the bottom strip
- [ ] In-engine render that represents real gameplay and visuals
- [ ] At most 3 words of text, or none; no ads or claims
- [ ] 2–5 variants uploaded for personalization
- [ ] No duplicate thumbnails; no out-of-season art still active
- [ ] Live detail page checked logged-out: every thumbnail rendered (no grey placeholder)
- [ ] Any number or odds claim is identical across name, icon and thumbnails, and matches in-game odds
- [ ] Next to the genre leader at 320×180, a stranger can tell the two games apart
- [ ] Icon and all thumbnails follow one written visual rule
- Icon:
  - [ ] 512×512 square
  - [ ] Checked at 150 px **and** about 64 px
  - [ ] One subject
  - [ ] No stickers
  - [ ] Not the default icon
  - [ ] Still recognisable if darkened with a countdown overlay (if you plan to use one)

## → Animation_and_VFX_Review.md
- [ ] Each effect has a stated trigger and the player question it answers
- [ ] Frequent-action feedback ≤ about 0.3 s (measured from a screen recording)
- [ ] Rare sequences skippable after the first view
- [ ] Intensity tier matches event importance (list the events → tier)
- [ ] The play area stays readable during the largest effect (screenshot at peak)
- [ ] Particle rates respect mobile (≤ 100/s per emitter); tested on the baseline phone
- [ ] `ReducedMotionEnabled` reduces shake, zoom and tween motion
- [ ] Every important sound has a visual counterpart
- [ ] Audio checked **with sound on** (do not mark as passed from silent video)

## → Core_Loop_Review.md
- [ ] The three layers are written down: minute-to-minute → most repeated action → progression engine
- [ ] A new tester performs the core action within about 60 s without help (timed)
- [ ] The tester can say what to do *and why* after the first loop
- [ ] First level-up or reward within the first session's first minutes (timed)
- [ ] Short, mid and long goals visible in the UI or world
- [ ] Every system in the game maps to a loop step (table exists; orphans removed or justified)
- [ ] Solo player in an empty server can complete the full loop
- [ ] Friends can join and play together without paywalls
- [ ] Tutorials are triggered by relevance; timed hints only for stuck players
- [ ] Onboarding ends on a deliberate moment of joy

## → Final_Game_Quality_Gate.md
- [ ] Baseline low-end device chosen; FPS and memory recorded on it (not the Studio emulator)
- [ ] All four checklists above completed, with unverified items listed explicitly
- [ ] UI identity statement written (motif, palette, type pairing) and visible across all screens
- [ ] Comparison against two academy references per area; differences noted
- [ ] Lessons recorded in `08_Lessons_Learned/`
