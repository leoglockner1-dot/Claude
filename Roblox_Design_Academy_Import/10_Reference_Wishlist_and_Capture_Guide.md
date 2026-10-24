# Reference Wishlist and Capture Guide

The research environment could **not** open roblox.com, so no live game pages, current thumbnails, gameplay or audio were inspected. This page lists what to capture next and how. The user (or the vault Claude, if it can browse) fills these gaps.

## A. How the user supplies references

1. **Screenshots** (Windows: `Win+Shift+S`; macOS: `Cmd+Shift+4`; Roblox: the in-game screenshot button) as PNG. Capture at least one at phone size.
2. **Clips:** a 5–20 s screen recording of the moment (with sound if audio matters). For thumbnails or icons, screenshot the game's Roblox page **and** the home-page grid where it appears.
3. **Drop the files into** `Roblox Design Academy/Assets/<Category>/_inbox/` and tell Claude: *"New references in the inbox: [what each one is, what you like or dislike]."*
4. Claude then names the files `REF-###_<game>_<what>.png`, moves them to the right Assets folder, writes the analysis from the template, and links it to the principles.
5. For videos Claude can't watch directly, extract frames (if ffmpeg is installed):
   ```bash
   ffmpeg -i clip.mp4 -vf "fps=4" "Assets/Video_Frames/REF-###/frame_%03d.png"   # 4 frames per second
   ffmpeg -ss 00:00:03.5 -i clip.mp4 -frames:v 1 "Assets/Video_Frames/REF-###/t03.5.png"  # one exact moment
   ```
   Record the timestamps in the analysis. Without sound, write "audio not analyzed".
6. **Your feedback is the most valuable input.** One sentence like "this looks cheap because ___" becomes a lesson in `08_Lessons_Learned/`.

## B. Priority capture list (games are verified as cited by Roblox's docs; IDs from those docs)

| Priority | Game (URL) | Capture | Why |
|---|---|---|---|
| 1 | DOORS — https://www.roblox.com/games/6516141723/ | Pre-run elevator shop; item pickup; entity-encounter clip **with audio**; thumbnail and icon | Pre-play purchases; horror audio feedback; Roblox cites it for older audiences |
| 1 | Jailbreak — https://www.roblox.com/games/606849621/ | First 3 minutes as a new player (clip); robbery-complete reward; current season pass | Onboarding by implication (IMP-18); reward sequence |
| 1 | Brookhaven — https://www.roblox.com/games/4924922222/ | HUD on phone; Creator Cam; house menu | Roleplay social tools; streamer features |
| 1 | Bee Swarm Simulator — https://www.roblox.com/games/1537690962/ | Collect → convert loop clip; egg hatch; pass shop | Simulator loop; complementary passes |
| 1 | Dress to Impress — https://www.roblox.com/games/15101393044/ | Intermission offer; runway reveal and voting clip | In-play contextual purchase; social reveal |
| 2 | Tower Defense Simulator — https://www.roblox.com/games/3260590327/ | Crate opening clip; wave-start UI | Reward reveal; HUD under pressure |
| 2 | Arsenal — https://www.roblox.com/games/286090429/ | Hit/kill feedback clip **with audio**; kill-feed | Combat game feel |
| 2 | Tower of Hell — https://www.roblox.com/games/1962086868/ | Fail and respawn loop; timer UI | Fast retry; minimal UI |
| 2 | Adopt Me! — https://www.roblox.com/games/920587237/ | First-session mansion offer modal; egg hatch | Modal offer timing; pet reveal |
| 2 | Dragon Adventures — https://www.roblox.com/games/3475397644/ | Current shop vs IMP-05; egg hatch | Track UI evolution |
| 3 | Super Striker League — https://www.roblox.com/games/3360853050/ | Lobby 3D shop | Lobby contextual purchases |
| 3 | Winds of Fortune — https://www.roblox.com/games/7714627632/ | Combat clip with audio | Verify IMP-19 sequence and timing |
| 3 | Interactivity Showcase (Roblox) — https://www.roblox.com/games/132115384567250/ | Same screen on phone, PC and gamepad | Roblox's own adaptive-design demo |

**Negative examples needed** (see the end of the [Anti-Pattern Catalog](07_Bad_Examples/Anti_Pattern_Catalog.md)): look for low-player-count games in popular genres. These are usually easy to find, and the useful ones are cluttered shop UIs, glow-heavy buttons, thumbnails crowded with text and several characters, and long reveals for common items. Capture them in the same way and label them Negative.

## C. If the vault Claude can browse
- Search the Roblox DevForum "Community Resources / Art Design Support" for UI critiques with before/after images (record URL and date).
- Check whether create.roblox.com has newer versions of the pages in [Sources.md](Sources.md) and update [Roblox_Platform_Facts.md](Roblox_Platform_Facts.md).
- Never store copyrighted images from game pages in a public place. The private vault is fine for study.
