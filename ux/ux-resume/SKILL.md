---
name: ux-resume
description: Continue the UX create or audit pipeline from the last unfinished state.
disable-model-invocation: true
---

# UX — Resume

Continue from the last unfinished pipeline state. Do not restart finished work unless the user asks.

## Designs directory

The folder is always named `design`. If the path is unknown, ask where it lives. Do not assume the repo root.

## Detect

Same markers as [ux-show-status](../ux-show-status/SKILL.md). Prefer `look.json` `status` and `pilotFeature` when present. If both create and audit are unfinished, ask which to resume.

### Create

Map `status` → skill:

| `status` | Resume at |
| --- | --- |
| missing / before `look` | Round 1 → [ux-new](../ux-new/SKILL.md) |
| `look` | Parallel inventory if needed, then Round 2 → [ux-discover](../ux-discover/SKILL.md) |
| `scope` | Kit → [ux-build-kit](../ux-build-kit/SKILL.md) |
| `kit` | Confirm if needed, else Screens → [ux-design-ui](../ux-design-ui/SKILL.md) |
| `screens` | Finish remaining features in [ux-design-ui](../ux-design-ui/SKILL.md) |
| `done` | Nothing to resume unless they ask to remake |

Fallback when `status` is absent: Folder / Round 1 → Scope → Kit → Screens (file markers).

### Audit

1. Folder / docs → [ux-audit](../ux-audit/SKILL.md)  
2. Understand → [ux-understand](../ux-understand/SKILL.md)  
3. Walkthrough → [ux-walkthrough](../ux-walkthrough/SKILL.md)  
4. Evaluate → [ux-evaluate](../ux-evaluate/SKILL.md)  
5. Prioritize → [ux-prioritize](../ux-prioritize/SKILL.md)  
6. Redesign → [ux-redesign](../ux-redesign/SKILL.md)  

If nothing exists yet, ask create (`ux-new`) vs audit (`ux-audit`).

## Run

Say the current state (`status` + markers), then the next state. Read that step’s skill and continue (including wait-on-user asks). Announce progress the way the orchestrator does. Keep `status` updated as you advance.
