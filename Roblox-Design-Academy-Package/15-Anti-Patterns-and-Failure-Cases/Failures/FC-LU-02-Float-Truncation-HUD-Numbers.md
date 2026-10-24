---
title: "FC-LU-02 — HUD showed 9.86M for 9,870,000 (floating-point truncation)"
tags: [failure-case, luau, ui, hud]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# HUD showed 9.86M for 9,870,000 (floating-point truncation)

| Field | Record |
|---|---|
| **Problem** | HUD showed 9.86M for 9,870,000 (floating-point truncation) |
| **Context** | `Feel.abbreviate()` HUD formatter, truncating to 3 significant digits so values never round up. |
| **Observable symptoms** | Test `T.eq(Feel.abbreviate(9870000), "9.87M")` failed: got `9.86M`. |
| **Cause (established)** | 9,870,000 / 1,000,000 = 9.869999… in binary floating point; `math.floor(n*100)/100` truncated it to 9.86. |
| **Correction** | Add a tiny epsilon (1e-9) before `floor`, keeping truncation (no round-up). Added a regression test that 999,999 stays `999K` and never becomes `1.00M`. |
| **How the correction was tested** | Test re-run. |
| **Final result** | All formatting tests pass. |
| **Reusable lesson** | Any display math with floor/truncation needs boundary tests at values that are not exactly representable. Never round currency up for display. |
| **Related** | [LU-27](../../07-Roblox-Studio-and-Luau/LU-27-HUD-Number-Formatting.md) |
