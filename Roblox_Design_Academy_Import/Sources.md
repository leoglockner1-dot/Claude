# Sources — Import Package (2026-10-24)

All sources were accessed on **2026-10-24**. Everything here was actually read or viewed. Nothing is cited from memory as if it had been read.

## Primary source: Official Roblox Creator Documentation

- Live site: `https://create.roblox.com/docs/...`. It was **blocked** from the research environment, so it was not opened directly.
- Read instead through its official open-source mirror: <https://github.com/Roblox/creator-docs>, commit `4e795e65a41fd48624fd85442292a81baa6bb3f5` (2026-10-24).
- License: documentation text and media are **CC BY 4.0** (repo `LICENSE`), and code samples are MIT (`LICENSE-CODE`). Attribution: "Roblox Corporation, Roblox Creator Documentation".
- Screenshots of third-party games inside those docs (Jailbreak, Dragon Adventures, etc.) are copyrighted by their developers. Keep them in the private vault for study only and don't republish them.

Each page is listed below with its live URL. The GitHub source path is `content/en-us/<path>.md`.

| Topic | Live URL | Used for |
|---|---|---|
| UI and UX design | https://create.roblox.com/docs/production/game-design/ui-ux-design | Prioritization, attention, visual language, conventions, consistency, feedback, flows, plus 14 annotated game screenshots |
| Core loops | https://create.roblox.com/docs/production/game-design/core-loops | Three-layer core loop model |
| Design for Roblox | https://create.roblox.com/docs/production/game-design/design-for-roblox | Platform behaviour, tourists and locals, audience, mobile-first, genre table |
| Onboarding | https://create.roblox.com/docs/production/game-design/onboarding | FTUE goals, D1 retention, moments of joy |
| Onboarding techniques | https://create.roblox.com/docs/production/game-design/onboarding-techniques | Visual elements, contextual tutorials, timed hints, plus 15 screenshots |
| Contextual purchases | https://create.roblox.com/docs/production/game-design/contextual-purchases | In-play, pre-play, lobby, complementary and UI offers; the modal-stacking warning |
| Thumbnails | https://create.roblox.com/docs/production/publishing/thumbnails | Specs, video rules, personalization, best practices, plus example images |
| Icons | https://create.roblox.com/docs/production/publishing/experience-icons | Specs, small-size preview, best practices, plus example images |
| Adaptive design | https://create.roblox.com/docs/production/publishing/adaptive-design | Input fluidity, responsive layout, dynamic sizing, legibility |
| Accessibility | https://create.roblox.com/docs/production/publishing/accessibility | Text size, contrast, colour and sound non-reliance, PreferredTransparency, PreferredTextSize, ReducedMotion |
| Console guidelines | https://create.roblox.com/docs/production/publishing/console-guidelines | 10-ft UI, TV-safe area, controller navigation, haptics, UI audio |
| Cross-platform development | https://create.roblox.com/docs/projects/cross-platform | Scale vs offset, ViewportDisplaySize, layouts, input hints |
| Screen insets (include) | https://create.roblox.com/docs/ui/on-screen-containers | ScreenInsets modes |
| Size modifiers | https://create.roblox.com/docs/ui/size-modifiers | UISizeConstraint, UITextSizeConstraint, AutomaticSize |
| UI animation | https://create.roblox.com/docs/ui/animation | Tween easing styles and directions, style transitions |
| Design for performance | https://create.roblox.com/docs/performance-optimization/design | Low-end devices, transparency, 16.67 ms frame budget, streaming |
| Particle emitters | https://create.roblox.com/docs/effects/particle-emitters | Rate limits, fill-rate, overdraw, lifetime cap |
| Highlighting | https://create.roblox.com/docs/effects/highlighting | 255 Highlight limit |
| Sound groups / audio objects | https://create.roblox.com/docs/sound/groups | SoundGroup now discouraged in favour of audio objects |
| Paid random items | https://create.roblox.com/docs/production/monetization/paid-random-items | Odds disclosure rules |
| The Roblox user base | https://create.roblox.com/docs/production/roblox-user-base | Session behaviour, social factors, conventions |

## Secondary: general game-design literature (from training knowledge, not re-read)

These are well-known works. The principles attributed to them are standard summaries. **They were not re-read during this research.** Treat them as background, not as quoted evidence.

- Frank Thomas & Ollie Johnston, *The Illusion of Life: Disney Animation* (1981): the 12 principles of animation (anticipation, follow-through, slow in/slow out, exaggeration…).
- Steve Swink, *Game Feel* (2008): real-time control, response, polish.
- Martin Jonasson & Petri Purho, "Juice it or lose it" (GDC Europe 2012 talk): layering feedback onto simple actions.
- Jan Willem Nijman (Vlambeer), "The Art of Screenshake" (2013 talk): impact feedback techniques.
- WCAG 2.x contrast guidance (4.5:1 body text, 3:1 large text or UI components). This is a web standard, applied here as a heuristic for game UI.

## Live Roblox data (accessed 2026-10-24, after the network policy was widened)
- `https://apis.roblox.com/explore-api/v1/get-sorts` (charts: Top Trending, Up-and-Coming, Top Playing Now, Top Revisited; device = all, country = all)
- `https://games.roblox.com/v1/games?universeIds=…` (names, genres, visits, players, created/updated dates)
- `https://thumbnails.roblox.com/v1/games/icons` and `/v1/games/multiget/thumbnails` (current icons 512×512 and detail-page thumbnails 768×432), images from `tr.rbxcdn.com`
- Images are copyrighted by their game developers. They're stored only in the private assets zip for study.

## Not accessed (blocked or not attempted)

- During the first research pass, create.roblox.com, roblox.com and devforum.roblox.com were blocked. They were later opened for the live snapshot. The docs content was **not** re-checked against the live site.
- Personalized home-page thumbnails (each viewer may get a different one) and video thumbnails were not inspected.
- No gameplay videos were watched. The two videos in the docs were downloaded to the manifest only (IMP-14) and **not analyzed**.
- No audio was heard. No claim in this package is based on listening to anything.
