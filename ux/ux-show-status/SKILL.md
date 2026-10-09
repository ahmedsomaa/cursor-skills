---
name: ux-show-status
description: Report UX create or audit pipeline progress and missing files without writing.
disable-model-invocation: true
---

# UX — Show status

Report where the design work stands. Do not write or edit files.

## Designs directory

The folder is always named `design`. If the path is unknown, ask where it lives. Do not assume the repo root. If a `design` directory already exists, use that one.

## Which pipeline

Inspect markers for **Create** and **Audit**. If both are in progress, say so and report each. If unclear which the user cares about, ask.

### Create markers

Prefer `look.json` `status` when present (`look` | `scope` | `kit` | `screens` | `done`). Also report `pilotFeature` when set. Cross-check file markers:

| Marker | State |
| --- | --- |
| Path / `design/` exists | Folder |
| `look.json` with `description` + `logo` (`status` ≥ `look`) | Round 1 / Look |
| `look.json` with `name` + `platform` + `features` + `pilotFeature`, plus `brief.html` + `handbook.css` (`status` ≥ `scope`) | Round 2 / Scope (`ux-discover`) |
| `system.html` (user confirmed in session, or file complete; `status` ≥ `kit`) | Design system (`ux-build-kit`) |
| `screens.html` covering features from `look.json` (`status` `screens` or `done`) | Screens (`ux-design-ui`) |

### Audit markers

| Marker | State |
| --- | --- |
| Path / `design/` exists | Folder |
| `audit/docs.json` + `audit/docs.css` | Docs template (audit style) |
| `audit/understand.html` | Understand (`ux-understand`) |
| `audit/walkthrough/` with flow pages | Walkthrough (`ux-walkthrough`) |
| `audit/evaluate.html` | Evaluate (`ux-evaluate`) |
| `audit/prioritize.html` | Prioritize (`ux-prioritize`) |
| `audit/redesign/<id>/` for approved items | Redesign (`ux-redesign`) |

## Report

1. Pipeline(s) detected  
2. Furthest completed state per pipeline (`status` + markers)  
3. `pilotFeature` when present  
4. Next unfinished state  
5. Missing files (paths)  
6. Which skill to run next (`ux-resume`, `ux-new`, `ux-audit`, or a step skill)

No writes. For create system/screens critique use [ux-critique](../ux-critique/SKILL.md). To continue, name [ux-resume](../ux-resume/SKILL.md).
