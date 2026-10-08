---
name: ux-repair
description: Get context from the user about what is wrong in the design folder, then auto-repair it against skill rules.
disable-model-invocation: true
---

# UX — Repair

Generic fix pass. No step/substep menus. Take what the user says is wrong (or what they want fixed), find the files, evaluate against the matching skill rules, and repair.

## Context (before writing)

Do not edit until you know enough to act. From the first message and follow-ups, gather:

1. **Where `design` lives** — ask if unknown. Do not assume the repo root.
2. **What to fix** — their description, paths, screenshots, or “the whole site feels like wireframes.” Use what they already gave; only ask when something required is missing (path, which feature/screen if the request is ambiguous).

Do not present docs / kit / ui option lists. Infer the surface from context.

## Repair

1. Map the request to the surfaces involved (docs site, design-system section, storyboard, Designs hub, screen, states, logo, chrome, etc.). A request may span more than one.
2. Load the matching rules:
   - Documentation site (index, brief, template, chrome): [docs-site.md](../ux-new/docs-site.md), [chrome.md](../ux-new/chrome.md), Docs template in [ux-new](../ux-new/SKILL.md); brief via [ux-discover](../ux-discover/SKILL.md).
   - Design system sections: [ux-build-kit](../ux-build-kit/SKILL.md) and that section’s GUIDE (paths in [menus.json](../ux-new/menus.json) if needed). Logo: [PROCESS.md](../ux-build-kit/sections/foundations/logo/PROCESS.md).
   - Screens (storyboard, Designs, screen, states): [ux-design-ui](../ux-design-ui/SKILL.md).
3. Compare existing files to those rules. List gaps briefly, then apply repairs.
4. Re-run any ask the original work would need only when a decision is missing (layout, fonts, style, Look, feature name, mobile vs web, etc.).
5. Rebuild `docs.css` the way [ux-new](../ux-new/SKILL.md) builds it when docs chrome classes change.
6. Keep scope to what they asked for, plus required shared fixes (broken index links, missing theme tokens used by that page).

Use `layouts/<id>.jobs.md` plus targeted `#wf-*` anchors for structure — **do not** load a full layout HTML dump. Wireframes are **structure guides only** (IA and element placement). Repaired output is always a finished polished site — not dashed wireframe clones. When the handbook looks like wireframes, generic scaffolding, or clashes with Look, restyle chrome to match `docs.json.look` / `look.json` (ensure `look` is present; custom needs `description`), keep docs fonts as handbook default (product type only in UI samples / typography specimens / storyboards / screens), and pull one round of Look-aligned docs-site inspiration if needed.

## Done

The described problems are fixed and the touched surfaces pass their rules. Say briefly what changed.
