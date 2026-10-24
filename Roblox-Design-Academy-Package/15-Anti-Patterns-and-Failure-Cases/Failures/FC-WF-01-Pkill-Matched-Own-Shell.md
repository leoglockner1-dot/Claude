---
title: "FC-WF-01 — Workflow: `pkill -f script.py` killed the shell that was relaunching the script"
tags: [failure-case, workflow, tooling]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Workflow: `pkill -f script.py` killed the shell that was relaunching the script

| Field | Record |
|---|---|
| **Problem** | Workflow: `pkill -f script.py` killed the shell that was relaunching the script |
| **Context** | Restarting a long background Blender render: `pkill -f "ex_props.py"; python ex_props.py …` in one command. |
| **Observable symptoms** | Both the old and the new run exited with code 144; no output. |
| **Cause (established)** | `pkill -f` matches full command lines. The launching shell's own command line contained `ex_props.py`, so pkill killed it along with the old process. |
| **Correction** | Run the kill and the relaunch as separate commands, or kill by PID. |
| **How the correction was tested** | The relaunch completed. |
| **Final result** | Fixed (cost ~12 minutes of render time). |
| **Reusable lesson** | Never pattern-kill with a pattern that appears in your own command line. |
| **Related** | [BL-19](../../06-Blender-and-3D-Assets/BL-19-Blender-Python-Automation.md) |
