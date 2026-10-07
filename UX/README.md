# 🎨 UX

Skills for product design in HTML when you do not design in Figma. Two pipelines, plus assist and create-only single commands.

## ✨ Create (new product UI)

`ux-new` → `ux-discover` → `ux-build-kit` → `ux-design-ui`

Artifacts under the project’s `design/` folder (brief, design system, storyboards, screens). Docs chrome from `ux-new/docs-templates/` (catalog + custom).

## 🔍 Audit (existing product)

`ux-audit` → `ux-understand` → `ux-walkthrough` → `ux-evaluate` → `ux-prioritize` → `ux-redesign`

All audit HTML under `design/audit/`, including its own `docs.json` / `docs.css` (same template options as create + custom). Inspiration stays inside redesign, not a separate skill.

## 🛟 Assist

| Skill | What it does |
| --- | --- |
| `ux-ask` | Which skill to run; catalog of both pipelines |
| `ux-show-status` | Progress report; no writes |
| `ux-resume` | Continue create or audit from the last unfinished state |
| `ux-critique` | Critique a create kit/ui substep (no edits) |
| `ux-handoff` | Engineering handoff page |

## ⚡ Single commands (create only)

| Skill | What it does |
| --- | --- |
| `ux-step` | Run one kit or ui substep (step → substep gate first) |
| `ux-repair` | Evaluate and auto-repair one substep |

Menus: `ux-new/menus.json`. Detail: [ROADMAP.md](ux-new/ROADMAP.md).

## 🗺️ Roadmap

Shipped: create + audit pipelines, assist skills, and create-only singles above.

### Planned (not built)

| Horizon | Skill (proposed) | Intent |
| --- | --- | --- |
| Next | `ux-marketing` | Astonishing marketing / landing sites — distinct from product `ux-design-ui` |
| Next | `ux-prototype` | Clickable HTML prototype from storyboards |
| Later | `ux-motion` | Motion language across kit + UI |
| Later | `ux-content` | UX writing pass across screens |
| Later | `ux-a11y` | Deep accessibility audit pass |
| Later | `ux-compare` | Side-by-side atmosphere or kit direction exploration |
| Later | `ux-migrate` | Restyle an existing app surface to match the kit |
| Later | `ux-email` | Email templates in the same visual language |
| Later | `ux-native` | Mobile-native frame conventions using the kit |
| Later | `ux-shop` | Store / catalog / checkout pattern pack |

Marketing sites stay out of the create and audit product pipelines. When built, they may reuse kit tokens if a product kit exists.

## 🏷️ Name clarity

- `ux-understand` (audit as-is) ≠ `ux-discover` (create brief)
- `ux-redesign` (audit improvements) ≠ `ux-design-ui` (create screens)
- `ux-evaluate` (product UX audit) ≠ `ux-critique` (create design-folder substep)
