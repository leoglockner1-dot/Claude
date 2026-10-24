---
title: "UI-24 — Racing HUD and a rainbow lobby menu (TURBOSTORM, DevForum)"
tags: [reference, ui, hud, menus]
reference_type: "DevForum in-game screenshots (Mixed)"
date_accessed: "2026-10-24"
---

# UI-24 — Racing HUD and a rainbow lobby menu (TURBOSTORM, DevForum)

## Identity
- **Name:** UI-24 — Racing HUD and a rainbow lobby menu (TURBOSTORM, DevForum)
- **Reference type:** DevForum in-game screenshots (Mixed)
- **Source URL:** <https://devforum.roblox.com/t/looking-for-onboarding-feedback-turbostorm-car-racing-10-min-avg-session-0-organic-traffic/4951901>
- **Creator/publisher:** Developer Tyyjz_91; screenshots by TheFaeTwins and the developer
- **Date posted / accessed:** 2026-10-23 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4951901-r1-90adb84afca9c455-2-69.jpg](../../Assets/UI/devforum/df-4951901-r1-90adb84afca9c455-2-69.jpg)
![df-4951901-r5-38cc8c73009b4da016ffa.jpg](../../Assets/UI/devforum/df-4951901-r5-38cc8c73009b4da016ffa.jpg)
![df-4951901-r7-477576920b12ba09b1434.jpg](../../Assets/UI/devforum/df-4951901-r7-477576920b12ba09b1434.jpg)
![df-4951901-r7-ac77b2651d407aeb8f5d4.jpg](../../Assets/UI/devforum/df-4951901-r7-ac77b2651d407aeb8f5d4.jpg)

## What is observable
**Race HUD:** top-left position card "15/15" + standings list with coloured name chips; top-centre "DRAFTING +14" chip and a big yellow lap gain "+51.095"; top-right lap timer card, mini-map and a red EXIT; bottom-right analogue speedometer (173–284 MPH, gear); bottom-left health bar. Overlays mid-screen: "LEVEL 6 REACHED", "TURRET ONLINE – 10 SECONDS – HOLD CLICK TO FIRE", "SHIELD ONLINE".
**Lobby:** voting panel ("Getting the race ready… you're in") and a right column of **nine stacked buttons in six colours** (CANCEL, GARAGE, SHOP, GAMEPASSES, WEEKLY, FREE CARS, WHEEL SPIN, EVENT CARS, SETTINGS).

## Community critique (quoted/paraphrased from the thread)
- "I recorded a playthrough on my default settings … minimal to mimic the 'mobile' players … your current world construction does not like that." (TheFaeTwins)
- "The first 5 seconds of your video ground a player what they're looking at, the next 5 give them an idea of what's about…" (TheFaeTwins)

## What works
- Race HUD follows racing conventions; information lives in corners; centre stays on the road.
- Contextual ability prompts state **name + duration + input** ("HOLD CLICK TO FIRE").

## Why it might work
Genre conventions transfer from other racing games; contextual instructions appear exactly when relevant.

## What does not work
- Lobby menu = rainbow list with no hierarchy; monetization entries (GAMEPASSES, WHEEL SPIN, FREE CARS) compete with core actions.
- Centre overlays during racing can obscure the track.
- Thread context: 10-minute sessions from ads but **zero organic traffic** — replies point to name discoverability, video's first 5 s, low-graphics world appearance; UI is not the only lever.

## Reusable principles
- **UI-001** Primary action dominance in lobbies; **UI-016** contextual instructions = verb + input + duration, placed away from the action focus.

## Roblox implementation
Lobby: one large "Race" button, secondary grid of icon buttons; monetization grouped under one "Store" entry. Ability prompts as top-centre banners with `InputActionLabel` for the right glyph.

## Original application
A kart lobby where the only big button is "Join Race"; garage/shop/events are four equal icon tiles below.

## Confidence
High for observations; Medium on causes of traffic (community opinions).

## Related
[HUD Layouts](../HUD-Layouts.md) · [CS 15 TURBOSTORM Racing](../../15-Game-Case-Studies/CS-15-TURBOSTORM-Racing.md)
