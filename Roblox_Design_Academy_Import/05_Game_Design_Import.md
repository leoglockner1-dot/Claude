# Game Design (Core Loop, Progression, Retention, Social) — Import Content

**Merge into:** the `05_Game_Design/` notes. Labels are as in [02_UI_UX_Import.md](02_UI_UX_Import.md).

---

## → Core_Loops.md

### Roblox's three-layer model [RBX]
1. **Minute-to-minute interaction**: the constant baseline activity (exploring, running, clicking).
2. **Most repeated set of actions**: the defining mechanic that the baseline feeds (fighting, collecting, building).
3. **Progression engine**: what turns repetition into growth (levels, upgrades, unlocks). Without it, Roblox says, a game "becomes repetitive, boring, and shallow".

Example (action RPG): explore → fight → upgrade tree, which makes exploring and fighting stronger.

### The player's first loop (academy model, aligned with Roblox onboarding guidance)
**Join → Understand → Act → Feedback → Reward → Progress → Repeat**
- **Understand**: what and *why* within seconds. Roblox: players must grasp "both *what* they are expected to do and *why*" [RBX].
- **Act**: the first meaningful action within roughly the first minute [HYP; Roblox says players "decide their interest within minutes"].
- **Feedback**: immediate, layered (see [04_Game_Feel_Import.md](04_Game_Feel_Import.md)).
- **Reward → Progress**: an early level-up should come fast. Roblox: "keeping thresholds low for a player's early levels" [RBX].

### Genre loops on Roblox [RBX genre table]
| Genre | Loop in one line | Example |
|---|---|---|
| Simulator | Click or act → item maxes out → trade up → higher ceiling | Bee Swarm Simulator |
| Tycoon | Collect from droppers → buy parts → unlock more droppers → … until complete | Lumber Tycoon 2 |
| Obby | Navigate obstacles → checkpoint → harder stage | Tower of Hell |
| Roleplay | Tools for social play; players generate the content | Brookhaven |
| Survival | Survive or escape hazards per round | Natural Disaster Survival |
| Hide-and-seek | Hide or escape a hunter (player or NPC), often with puzzles | Piggy |
| Customization | Collect and show off looks | Fashion Famous |
| Action | PvP combat; single-player action is rare on Roblox | Arsenal |

### Simple mechanics, meaningful depth [GEN]
- One verb, many contexts: the same action gains depth from new targets, combos, environments and risk.
- Depth checklist: does mastery change *how* you do the verb, not just *how much*? Is there a decision in each repetition (timing, positioning, which target, which upgrade)?

---

## → Progression_and_Rewards.md

- **Short, mid and long goals visible** in the world or UI: skill trees, season passes, quests, collections [RBX onboarding].
- **Early levels fast**; make thresholds tunable live (Configs) [RBX].
- **Meaningful upgrades** change behaviour or open options (new area, new ability, new interaction), not only +5% [GEN]. Pure-number upgrades work best when the player *sees* the number change something (faster kill, bigger yield).
- **Make the next reward legible**: progress bar plus a concrete preview of what unlocks [OBS IMP-04, IMP-11].
- **Starter items and currency**: give enough to use the systems early; test amounts with Experiments [RBX].
- **Free vs premium tracks** separated spatially and by colour [OBS IMP-04].
- **Economy:** see the Roblox docs "Balance virtual economies" (not summarized in this import). Track sources and sinks per currency [GEN].
- **Paid random items:** odds disclosure is mandatory [FACT].

---

## → Retention_and_Replayability.md

### Onboarding (FTUE) [RBX]
- The goals are **teach the essentials, get to the fun quickly, leave players wanting more**.
- Success is measured by **Day-1 retention** and by funnel completion per step. Find the steps where players leave and fix them with A/B tests (Experiments).
- **Visual over text.** Players skip text ([IMP-16](06_Reference_Analyses/IMP-16_Color_or_Die_Rules_Sign.md)).
- **Highlight, don't describe** ([IMP-17](06_Reference_Analyses/IMP-17_Hello_Kitty_Cafe_Spotlight_and_Trail.md)).
- **Hints imply, players feel clever** ([IMP-18](06_Reference_Analyses/IMP-18_Jailbreak_Footprint_Hint.md)).
- **Contextual (just-in-time) tutorials** teach features when they first become relevant ([IMP-20](06_Reference_Analyses/IMP-20_Squishmallows_Contextual_Tutorial.md)).
- **Timed hints** appear only for players who are stuck, once, just after the typical completion time ([IMP-21](06_Reference_Analyses/IMP-21_Plant_Timed_Hints.md)).
- **End onboarding on a moment of joy**, with the full range of future content visible.
- **Genre conventions reduce teaching.** The closer your patterns are to the genre's top games, the less you explain [RBX].

### Platform behaviour [RBX]
- Sessions hop between several games, and Roblox is "closer to YouTube than the App Store". Your game must hook fast and be easy to return to.
- **Tourists** (variety seekers) vs **locals** (deeply engaged; almost the whole engaged base). Locals start as tourists, so design for both.
- **Younger players:** exploration, experimentation and socializing over competition; less sensitive to visual fidelity; reading-averse. Fun beats fidelity.
- **Older players** (13+ is now the majority): more investment, more overlap with other platforms' genres.
- **Influencers:** could a YouTuber make fun content with it? Can friends join easily? Is there a hide-UI camera?
- Updates: test new thumbnails with each major update [FACT thumbnails]. Live-ops content cadence is in Roblox's "Content updates" and "LiveOps" docs (not summarized here).

---

## → Multiplayer_and_Solo_Experience.md

- **Social is a core Roblox strength.** Players treat Roblox as a hangout, and invites drive growth. "Single-player games often find it harder to build and retain an audience" [RBX].
- **Players are content for each other.** Roleplay games give tools and let interactions create the content [RBX].
- **Avatars matter.** Players invest in avatars and want them seen. Replace them only with a good reason [RBX].
- **Don't block friends from playing together.** E.g., don't price private servers prohibitively [RBX].
- Social onboarding: collaboration and competition early for social players; test matchmaking in the FTUE [RBX].
- **Solo players still need a full loop.** Every multiplayer mechanic should have a solo fallback (NPCs, bots, scaled difficulty) so an empty server isn't a dead game [GEN/HYP]. This is directly relevant to an AI-bot system.
- Trading and parties turn invitations into gameplay [RBX].

---

## → Game_Design_Anti_Patterns.md

| Anti-pattern | Why it fails | When it's acceptable | Fix |
|---|---|---|---|
| Long upfront text tutorial | Players skip it, and Roblox's join and leave is near-instant | Never as a gate; optional "how to play" board is fine | Visual, in-world, contextual teaching |
| Teaching every system in session 1 | Cognitive overload | — | Trigger table: teach on first relevance |
| Feature bloat (systems that don't feed the core loop) | Dilutes the loop and UI clutter grows | When the system clearly feeds the loop (e.g., trading for a collection loop) | Each system must answer: which loop step does it strengthen? |
| Number-only upgrades | Progress feels invisible | Idle or simulator genres where numbers *are* the fantasy | Visible effect for each upgrade |
| Purchase popups during play | Breaks the session | Intermissions, pre-run, lobby | Contextual purchases at natural pauses |
| Solo-hostile design | Empty servers kill retention | Pure social hangouts | Bots or NPCs, solo-scaled content |
| Port from another platform unchanged | Ignores Roblox norms (short FTUE, social) | — | Slim tutorials, add social features |
