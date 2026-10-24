---
title: "Detecting Generic, Template or 'AI-Looking' Design"
tags: [anti-pattern, ai-look, critique]
note_type: "critique"
---

# Detecting Generic, Template or "AI-Looking" Design

Players explicitly called a UI "AI generated" in a DevForum thread and the developer agreed ([UI-25](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md)). The comical thumbnail example ([TI-03](../02-Thumbnails-and-Icons/Analyses/TI-03-Comical-Theme-AI-Look.md)) shows the same issue in key art. "AI look" is a symptom of **unmade decisions**, not of a tool.

## Detection signals (observable)
| Signal | Check | Fix |
|---|---|---|
| Uniform heavy strokes on all text | Are strokes only where text sits over the world? | Stroke rule (UI-007) |
| Same glossy gradient on every button | Does the gradient encode anything? | Flat or one rule (AP-02) |
| Generic font everywhere, no pairing | Is there a display + reading face with roles? | ID-004 |
| Saturated colours at equal weight | Is there one accent? | UI-003 |
| Random scattered props (key art) | Does every prop support the idea? | Composition checklist |
| Symmetric, centred, posterlike compositions with no action | Is a verb shown? | THUMB-002 |
| Over-smooth painterly lighting, uncanny faces | Is it an in-engine capture? | THUMB-010 |
| Icons from different packs | One family? | UI-006 |
| Repeated identical cards with no reason | Does card shape vary by content type? | UI-06 grouping |
| Decorative effects with no meaning | Which player question does it answer? | AP-26 |
| Background unrelated to subject | Same world as the game? | ID-003 |

## Not to confuse with quality
- **Minimal ≠ good**; **chaotic ≠ bad**. Steal-a-Brainrot-style chaos can be intentional; template defaults cannot.
- Judge against: identity fit, clarity, composition, hierarchy, readability, responsiveness, emotional impact, distinctiveness, consistency, usefulness → [Design Critique Checklist](Design-Critique-Checklist.md)
