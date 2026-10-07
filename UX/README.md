# UX

Skills for product design in HTML when you do not design in Figma. Two pipelines, plus assist and create-only single commands.

## Create (new product UI)

`ux-new` → `ux-discover` → `ux-build-kit` → `ux-design-ui`

Artifacts under the project’s `design/` folder (brief, design system, storyboards, screens). Docs chrome from `ux-new/docs-templates/` (catalog + custom).

## Audit (existing product)

`ux-audit` → `ux-understand` → `ux-walkthrough` → `ux-evaluate` → `ux-prioritize` → `ux-redesign`

All audit HTML under `design/audit/`, including its own `docs.json` / `docs.css` (same template options as create + custom). Inspiration stays inside redesign, not a separate skill.

## Assist

| Skill | What it does |
| --- | --- |
| `ux-ask` | Which skill to run; catalog of both pipelines |
| `ux-show-status` | Progress report; no writes |
| `ux-resume` | Continue create or audit from the last unfinished state |
| `ux-critique` | Critique a create kit/ui substep (no edits) |
| `ux-handoff` | Engineering handoff page |

## Single commands (create only)

| Skill | What it does |
| --- | --- |
| `ux-step` | Run one kit or ui substep (step → substep gate first) |
| `ux-repair` | Evaluate and auto-repair one substep |

Menus: `ux-new/menus.json`. Roadmap: `ux-new/ROADMAP.md`.

## Name clarity

- `ux-understand` (audit as-is) ≠ `ux-discover` (create brief)
- `ux-redesign` (audit improvements) ≠ `ux-design-ui` (create screens)
- `ux-evaluate` (product UX audit) ≠ `ux-critique` (create design-folder substep)
