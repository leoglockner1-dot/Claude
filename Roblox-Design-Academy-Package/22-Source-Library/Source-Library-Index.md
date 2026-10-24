---
title: "Source Library Index"
tags: [source-library, index]
note_type: "index"
---

# Source Library

| Note | Contents |
|---|---|
| [Roblox Documentation Sources](Roblox-Documentation-Sources.md) | Official Roblox docs used in v1, by topic |
| [DevForum Sources](DevForum-Sources.md) | DevForum threads used in v1 |
| [Game Data Sources](Game-Data-Sources.md) | Roblox APIs and the live chart snapshot |
| [External Design Sources](External-Design-Sources.md) | Non-Roblox design references |
| [All External Links (generated)](All-External-Links.md) | **Every** external URL cited anywhere in the package, grouped by host, with the notes that cite it |
| [Access Log](Access-Log.md) | What was reachable and what was blocked, in v1 and 2.0 |

## How sources are labelled in notes
- Frontmatter `evidence:` says what kind of evidence a note rests on.
- Tutorial notes mark **[SRC]** (the source says) vs **[ANALYSIS]** (ours) vs **[SIM-TESTED]**.
- Blender and Luau notes end with a **Sources** section listing the pages actually read.
- Case studies state the data date and "gameplay NOT observed".

## Counting rule
A source counts as *verified* only if it was opened in a session and its content was read; links found inside pages but not opened are not listed. Regenerate the full list with `python3 _tools/make_source_index.py`.
