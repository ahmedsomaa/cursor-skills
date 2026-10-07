---
name: ux-ask
description: Ask anything about the ux skills, such as how to start or which step to run.
disable-model-invocation: true
---

# UX — Ask

Answer the question. Do not start a design unless the user asks you to start one.

Read a step skill only when the answer depends on its rules. [ux](../ux/SKILL.md) is how a full run proceeds.

## Get started

Name `ux` and say what to design. It asks where in the current project to put the `design` directory, which docs template to use, and whether the designs are mobile first, website first, or both. Then it writes the brief, the design system, and the high-fidelity screens. The index navigation always includes each feature. A full run says which state is current, and says that state is finished before the next one: Folder, Docs template, Brief, Design system, Screens.

```text
/ux Design the assignment flow from this app's requirements.
```

## Which step to run

`ux` runs all three. Name one step when only that part is needed.

| Need | Skill |
| --- | --- |
| What the app requires, before any visuals | `ux-understand` |
| A design system that belongs to this app. The ask lists every catalog system, then custom | `ux-system` |
| High-fidelity screens, storyboard, and the critical states for each screen | `ux-screens` |
| A change to the design system or to screens that already exist | `ux-edit` |
| The design folder looks unstyled or is missing light and dark | `ux-polish` |

`ux-system` and `ux-screens` expect the earlier files to exist.

## Where the files go

The folder is always named `design`. The skill asks where in the current project it should live, and does not assume the repo root. If a `design` directory is already there, it confirms that one.

`design/index.html` is the navigation. It links the brief, the design system, and each feature. The docs chrome is `design/docs.json`, chosen from sidebar, cards, grid, or top bar, or cooked custom. Each option names its layout, its typography, and its fonts, including a monospace for code. Fonts load from Google Fonts. Icons are Lucide. The minified Tailwind build is `design/docs.css`. The design system lives in `design/design-system/`: `system.json` is this product's filled record, in the same flat fields as a catalog record, and the index links principles, color, typography, spacing, shape, elevation, layout, icons, components, and themes. Catalog systems the skill can start from are JSON records in the ux-system skill, listed in `design-systems/index.json`. The catalog format stays in that skill. Docs templates are listed in `ux/docs-templates/index.json`. Under a feature, the main index links that feature's storyboard and its high-fidelity screens. Screen pages show the critical states for that screen. The brief is `design/brief.html`. The folder is HTML, plus `docs.json`, `docs.css`, and `system.json`. Storybook is a later version of this skill. This version is the static HTML site.

## Answer

1. Answer in a few sentences.
2. Name the one skill to run, when a skill is the next move.
3. Give one prompt they can paste.

```text
/ux-system Create the design system from design/brief.html.
```
