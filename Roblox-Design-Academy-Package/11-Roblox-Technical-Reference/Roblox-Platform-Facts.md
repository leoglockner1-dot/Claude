---
title: "Roblox Platform Facts (summary)"
tags: [technical, facts]
note_type: "technical-reference"
---

# Roblox Platform Facts (summary)

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.



## Thumbnails

| Fact | Value | Source |
|---|---|---|
| Aspect ratio | **16:9**. Other ratios are **stretched** to 16:9 on display | thumbnails |
| Ideal resolution | **1920×1080** | thumbnails |
| Max per game detail page | **10** images or videos | thumbnails |
| Image formats | .jpg .gif .png .tga .bmp | thumbnails |
| Upload size for personalization | under **3 MB** and 1920×1080 | thumbnails |
| Video uploads | free, quota of **3 per month**. Rejected videos still count | thumbnails |
| Video support | **not** on Xbox, PlayStation or VR | thumbnails |
| Bottom edge | avoid essential text or elements at the **bottom**, because player count and other metadata may cover it | thumbnails |
| Personalization | starts with **≥2 active** thumbnails (UI lets you activate 2–5). Roblox reports **+8.5% average** qualified play-through rate in testing, some games +50% | thumbnails |
| Personalization advice | keep several active, test new ones with each major update, then leave them alone until the next update | thumbnails |
| Qualified play-through rate | qualified plays ÷ home-page impressions | thumbnails |
| Video rules (rejected if broken) | no misrepresented gameplay or theme, no artificially enhanced graphics, no real-life footage, **no voice-over, narration, voice chat or music with lyrics**, overlay text only to describe gameplay ("Collect coins to boost jumps"). No ads or claims ("50% off", "Free UGC!") | thumbnails |
| Video: allowed | cinematic camera angles of real gameplay, minor brightness and contrast changes, logo overlay, curated highlight sequences, in-game UI text, catalog music | thumbnails |
| Capture tool | Freecam: **Left Shift + P** during a solo playtest | thumbnails |

## Icons

| Fact | Value |
|---|---|
| Size | square, at least **512×512** |
| Displayed small | scales down to sizes like **150×150**, so preview it small |
| Count | **one icon per locale** |
| Moderation | every icon must pass asset moderation |
| Default | a generic default icon is auto-generated at first publish. Roblox's own docs show it as a *bad* example |

## Screen, layout and safe areas

- `ScreenGui.ScreenInsets` options:
  - `CoreUISafeInsets` (default) keeps UI clear of top-bar buttons and cutouts. **Recommended for interactive UI.**
  - `DeviceSafeInsets` avoids notches only, not the Roblox top bar.
  - `TopbarSafeInsets` fits UI between the top-bar controls and the right edge.
  - `None` is for non-interactive backgrounds only.
- Core UI (top bar, chat, player list) is in every game. Test that your UI doesn't collide with it.
- Prefer `Scale` for position and size. Pixel counts and density vary per device. A pure-scale size, though, becomes huge on a 4K TV, so combine it with constraints or screen-size adaptation.
- `GuiService.ViewportDisplaySize` is `Small` (most phones and tablets), `Medium` (laptops and monitors) or `Large` (TVs). The Style Editor supports queries such as `@ViewportDisplaySizeSmall` and `@PreferredInputTouch`.
- `UserInputService.PreferredInput` reports the current primary input and updates live when the player switches devices.
- `InputActionLabel` shows the right key or button glyph per device with no code. `UserInputService:GetImageForKeyCode()` and `GetStringForKeyCode()` are the manual alternative.
- `UISizeConstraint` sets min and max pixel size. `UITextSizeConstraint` sets min and max font size. With `AutomaticSize` on, the `Size` property acts as the minimum.
- Console: players sit about **8–10 ft** from the screen. Some TVs crop the edges, so keep important UI inside the TV-safe area. **Disable the chat window on console.**

## Accessibility settings the game must respect

- `GuiService.PreferredTransparency`: 1 = default, 0 = wants opaque backgrounds. Multiply `BackgroundTransparency` by it.
- `GuiService.PreferredTextSize`: Medium (default), Large, Larger or Largest.
  - **`TextScaled = true` ignores this setting.**
  - A `UITextSizeConstraint` caps the setting.
  - `AutomaticSize` grows the element to fit.
  - `TextWrapped` wraps within its bounds.
  - Consequence: heavy use of `TextScaled` silently breaks the accessibility text-size setting.
- `GuiService.ReducedMotionEnabled`: when true, snap tweens (time 0) or swap movement for a fade (CanvasGroup `GroupTransparency`).
- Never rely on colour alone (over 5% of people have some colour blindness) or on sound alone. Offer separate volume groups for music, SFX and speech.

## Animation and tweening

- `TweenInfo` defaults are EasingStyle **Quad** and EasingDirection **Out**. Linear ignores direction.
- Available styles include Sine, Quad, Cubic, Quart, Quint, Exponential, Circular, Back (overshoot), Bounce and Elastic.
- UI style transitions can tween properties via `StyleRule` definitions, which work like CSS transitions.
- `CanvasGroup` tweens a whole group's transparency uniformly.

## VFX limits

- `ParticleEmitter.Rate`: max **400 particles/s per emitter on desktop, 100/s on mobile**.
- Particle lifetime is capped at **20 s**. Flipbook framerate max is 30 fps.
- Cost drivers: **fill-rate** (screen pixels covered) and **overdraw** (overlapping transparent layers). Big, overlapping, semi-transparent particles are the expensive case.
- `Highlight`: only **255** render at once on the client. Extras are silently ignored.
- General: avoid partial transparency (anything other than 0 or 1) where you can, because of overdraw.

## Audio

- `SoundGroup` is now **discouraged**. Roblox recommends the newer **audio objects** API for mixing and effects.
- Docs recommend at least separate SFX and Music groups so each can be balanced and adjusted by the player.
- Console guidance: add UI sounds to confirm selection and menu movement.

## Performance

- At 60 FPS the frame budget is **16.67 ms**. Prefer event-driven code over per-frame work, and split long tasks across frames.
- Pick a **baseline low-end device** and test on it throughout. The Studio emulator is fine for aspect ratio and controls but **not accurate for memory**.
- Example budget from the docs (illustrative, device-specific): stay under about 1,000 draw calls and 1,000,000 triangles on the baseline device.
- Built-in materials use far less memory than custom textures. Reuse meshes and textures, and use packages to avoid duplicate asset IDs.
- Use instance streaming for most places. Don't put server-only assets in ReplicatedStorage.
- Most Roblox users play on **mobile**, and the audience is sensitive to load times (design-for-roblox).

## Monetization rules that affect UI

- **Paid random items** include eggs, spins, chests, luck boosts, pity systems and rate-up items, whether paid directly or through currency bought with Robux.
  - Before purchase, the game must show **all outcomes and their numerical odds as percentages summing to 100%**.
  - Many outcomes may go behind a labelled "Info" or "Details" button. **A bare (i) symbol without a label is not enough.**
  - Odds must update if an outcome can only be obtained once.
- Contextual purchase modals: add logic so offers **never stack** on top of each other. Leave time for the Robux purchase flow (it can take several seconds) before gameplay resumes.


## Added in this package
- Audio objects: `AudioPlayer`, `AudioEmitter`, `AudioListener`, `AudioDeviceOutput`, `AudioFader`, effects such as `AudioReverb`, `AudioEqualizer`, `AudioCompressor` ([audio objects](https://create.roblox.com/docs/audio/objects)).
- Developer products: grant via `MarketplaceService.ProcessReceipt` returning `Enum.ProductPurchaseDecision.PurchaseGranted` / `NotProcessedYet`; do **not** use `PromptProductPurchaseFinished` to process purchases ([developer products](https://create.roblox.com/docs/production/monetization/developer-products)).
- Analytics: `AnalyticsService:LogOnboardingFunnelStepEvent`, `LogFunnelStepEvent`, `LogEconomyEvent`, `LogCustomEvent` ([analytics](https://create.roblox.com/docs/production/analytics)).
- `Workspace.StreamingEnabled` is on by default for new places and cannot be set from a script.
- Every client-sent value must be validated by the server ([security](https://create.roblox.com/docs/scripting/security/security-tactics)).
