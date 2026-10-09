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
2. **What to fix** — their description, paths, screenshots, or “the handbook doesn’t feel premium.” Use what they already gave; only ask when something required is missing (path, which feature if the request is ambiguous).

Do not present system / screens option lists. Infer the surface from context.

## Repair

1. Map the request to the surfaces involved (`look.json`, handbook shell, `brief.html`, `system.html`, `screens.html`, `logo/`). A request may span more than one.
2. Load the matching rules:
   - Handbook chrome / shell: [handbook.md](../ux-new/handbook.md) and [ux-new](../ux-new/SKILL.md)
   - Scope / brief: [ux-discover](../ux-discover/SKILL.md)
   - Design system sections: [ux-build-kit](../ux-build-kit/SKILL.md)
   - Screens artboard: [ux-design-ui](../ux-design-ui/SKILL.md)
3. Compare existing files to those rules. List gaps briefly, then apply repairs.
4. Re-run any ask the original work would need only when a decision is missing (Look description, platform, feature name, etc.).
5. Keep scope to what they asked for, plus required shared fixes (missing ON THIS PAGE (uppercase) on any page, home missing Overview/Start here/How to use/Status, missing favicon or document meta, site name not linking home, TOC rail flush to top, ⌘K command palette / separator, Lucide nav icons, fonts not General Sans / Geist Mono, handbook tinted from product or given an accent hue instead of zinc-only, product fonts applied to whole system page instead of specimens only, missing dashed category separators on system/screens, unminified or Tailwind handbook assets, Preview/Code not CSS-radio driven, Design system sidebar subnav added, logo downloads missing for a custom mark, library link missing for a library mark, variables in `screens.html` out of sync with `system.html`, weak hierarchy/contrast/states/targets on frames).

Repaired output keeps the Design Handbook shell and Brand / Foundations / Components / Tokens on one system page — not a multi-page foundations site and not dashed wireframes.

## Done

The described problems are fixed and the touched surfaces pass their rules. Say briefly what changed.
