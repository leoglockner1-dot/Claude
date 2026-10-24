# Roblox Development Academy 2.0 — Portable Obsidian Package

An evidence-linked training system for agents and people building Roblox games. It covers game design and core loops, mechanics, progression, Blender assets for Roblox, Roblox Studio and Luau, UI/UX, thumbnails and icons, animation, VFX and sound, level design, onboarding, multiplayer, testing and debugging.

It is built for **doing**, not only reading. Each area pairs principles with procedures, executed exercises, benchmarks with pass/fail criteria, a self-critique loop, and a library of real failures and their fixes.

**Built:** 2026-10-24 by a Claude Code session. **Portable:** relative links only, and no plugins needed.

## Start here
1. [Academy Overview](00-Start-Here/Academy-Overview.md): how to use it for a real task
2. [Research Limitations](00-Start-Here/Research-Limitations.md): what this academy could and could not see or test
3. [Master Index](00-Start-Here/Master-Index.md): every area, plus "find by question"
4. [Self-Critique Loop](18-Skill-Training/Self-Critique-Loop.md): the mandatory working method

## What's inside (actual counts; full inventory in [MANIFEST](MANIFEST.md))
| Area | Count | Evidence level |
|---|---|---|
| Game case studies | 54 (18 v1 + 36 new) | Public data; **gameplay not observed** |
| Mechanics analyses | 19, plus a 15-field core-loop framework, a loop library and 6 documented loop failures | Synthesis + developer post-mortems |
| Blender/3D procedures | 22 (BL-00…BL-21) + 10 executed exercises | Exercises **executed** with bpy 5.2.3: renders, QC JSON, exports |
| Luau/Studio procedures | 28 (LU-00…LU-27) + 13 tested modules | **54 specs pass** + 6 tutorial-defect reproductions; Studio **not** used |
| Animation/VFX/sound recipes | 23 (AV-01…AV-23) + 15 design recipes | Previews and audio synthesized and measured; not in-engine |
| Tutorials turned into procedures | 16 official Roblox tutorials | Text read; 2 defects reproduced in simulation |
| Benchmarks | 18 (15 executed, 1 partly, 2 specification only) | Evidence linked per benchmark |
| Design principles | 128 | Each links its evidence |
| Quality checklists | 14 | — |
| Failures | 13 real (this academy's own) + 6 developer post-mortems + 28 anti-patterns | Labelled real vs documented vs generalized |
| Video analyses | 19 notes covering 29 official Roblox videos | Measured timing/audio; **no YouTube** (blocked) |
| UI / thumbnail-icon analyses | 26 / 30 | v1 research |
| Assets | 123 original (committed) + 367 third-party (fetched by script) | Licence and source per file |

## Install
Follow [IMPORT_INSTRUCTIONS.md](IMPORT_INSTRUCTIONS.md); report with [IMPORT_REPORT_TEMPLATE.md](IMPORT_REPORT_TEMPLATE.md).
- From the **ZIP**: everything is included.
- From a **git clone**: run `python3 _tools/fetch_assets.py` once to download the third-party reference media, which is not committed for licensing reasons.

## Tools (`_tools/`)
- `validate_package.py`: links, assets, licences, absolute paths
- `fetch_assets.py`: rebuilds third-party media from `asset-sources.json` without overwriting
- `blender/`: headless Blender toolkit (scene, QC, export, shapes) and the exercise scripts
- `luau/`: tested Luau modules, mocks, specs, benchmark BM-02 (`bash run_tests.sh <luau-bin-dir>`)
- `ui/`: BM-03 HUD mock-ups and the Playwright checker
- `av/`: audio and motion preview generator
- `make_manifest.py`, `make_source_index.py`: regenerate the manifest and the link index

## Rights
- Roblox Creator Docs prose and media: CC BY 4.0; code samples: MIT (Roblox Corporation).
- Game icons, thumbnails and DevForum screenshots belong to their creators. They are fetched only for **private study** inside your vault. Do not republish them.
- Original assets (`Assets/Original/`) and tools were made by this academy.
