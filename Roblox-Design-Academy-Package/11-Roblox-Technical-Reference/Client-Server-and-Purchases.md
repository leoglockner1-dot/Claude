---
title: "Client/Server Responsibilities and Purchases"
tags: [technical, networking, economy]
note_type: "technical-reference"
---

# Client/Server Responsibilities and Purchases

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- Validate every client-sent value on the server (type, range, rate, context) — e.g., check fire rate, positions, ownership. [security tactics](https://create.roblox.com/docs/scripting/security/security-tactics)
- Developer products: process in `MarketplaceService.ProcessReceipt`; return `PurchaseGranted` only after granting/saving; return `NotProcessedYet` to retry on next join; don't use `PromptProductPurchaseFinished` for granting. [developer products](https://create.roblox.com/docs/production/monetization/developer-products)
- *(recommendation)* Pattern: **client** = immediate feedback (press anim, sound, pending state); **server** = authority (currency, inventory, odds rolls); **client** = confirmation feedback on server reply.
- Paid random items: odds disclosure rules → [Random Rewards and Fairness](../04-Progression-and-Economy/Random-Rewards-and-Fairness.md)
