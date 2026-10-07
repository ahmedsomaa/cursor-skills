---
name: ux-system
description: List every catalog design system plus a custom option, then write design/design-system as HTML pages plus a filled system.json.
disable-model-invocation: true
---

# UX — System

Design a visual system that fits this app and would look wrong on a different product. Deliver it as HTML the screens will use, and as the JSON those pages are built from.

This is the Design system state. Say "Design system." before asking.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/brief.html` and `<design>/docs.json` first. If the brief is missing, follow [ux-understand](../ux-understand/SKILL.md) before designing. If `docs.json` is missing, ask using [docs-templates/index.json](../ux/docs-templates/index.json) the way [ux](../ux/SKILL.md) does, including custom, and write it before the pages. The HTML pages are the design-system pages. `system.json` lives in `design-system/`. `docs.json` lives next to the index. The catalog format stays in this skill. Do not copy it into the project.

## Ask first

Before writing the specimen, ask the user to choose. Read [design-systems/index.json](design-systems/index.json) and list every record, each with its name and fit. Mark one as the recommendation for this brief. Custom is always the last choice. The list is the whole catalog. The recommendation is a mark on that list, not a shorter list.

1. **A catalog system.** When they pick one, read that JSON file. The record shape is [design-systems/schema.json](design-systems/schema.json). Every field is a string. A field that says `Unconfirmed.` is not a value. Open `source` before using it. Adapt the record so the result belongs to this product.
2. **Cook a custom system.** Ask whether they will describe the settings or the agent should cook them.
   - They describe it. Give this format and wait for one reply. Color: the vibe, or background, text, and action. Typography: the families, or how the type should feel. Radius: sharp, slight, or round.
   - The agent cooks it. Decide the look from the brief first and write that decision in a few lines before any search. Then search once for references that match it, on Mobbin, Figma Community, Dribbble, Behance, Pinterest, or one other place. Use Mobbin MCP for Mobbin and the web for the others. Use what you find as a check, not as the design. The type, color, and shape belong to this product. A close copy of a found screen is unfinished.

A copied screen, and a system that could ship on any other app, are both unfinished.

Color, spacing, typography, and elevation are a small set of roles a page references.

## Direction

Take the final direction from the brief and from references that fit this product: who it is for, what they do, and any visual language already in the app. Someone who knows the product should recognize it from the type, color, and shape alone.

## Write

Create `<design>/design-system/`.

Write `system.json` first. It is one filled record in the same flat fields as a catalog record: this product's id, name, source, maker, fit, and every section string. The field list is [design-systems/schema.json](design-systems/schema.json). A catalog pick and a custom system both write this file. Later it can be copied into `design-systems/` and listed in `index.json`.

`system.json` is the source the HTML pages are built from. Its `color`, `spacing`, `typography`, and `elevation` strings name this product's roles.

One HTML file per section. `<design>/design-system/index.html` is the polished index: it links every section, marks where you are, and uses the layout and typography from `docs.json`.

| File | Section |
| --- | --- |
| `principles.html` | What this product looks like, and what it refuses to look like |
| `color.html` | Semantic background, text, border, and icon roles, each in light and dark |
| `typography.html` | Families, size scale, weights, line height, then title, heading, subheading, body, caption, and code, set in real product copy |
| `spacing.html` | One spacing scale, shown as gaps |
| `shape.html` | Radius steps and border widths |
| `elevation.html` | Resting, raised, and overlay shadows, in light and dark |
| `layout.html` | Page width, grid, and breakpoints. Follow the brief: mobile first, website first, or both |
| `icons.html` | Icon style, sizes, and the icons this app uses |
| `components.html` | Only components this app needs, with anatomy and real states |
| `themes.html` | The same screen fragment in light and in dark |

Put the product tokens and the theme switch in a `<style>` block. Declare one CSS custom property per role named in `system.json` for color, spacing, type, and elevation. Repeat that block on every design-system page. Both themes are this product, not a default inverted palette. The docs chrome is Tailwind classes from `docs.json`. Every page links `docs.css`. Rebuild `docs.css` the way [ux](../ux/SKILL.md) builds it.

Link `<design>/design-system/index.html` from `<design>/index.html`.

This step is done when `system.json` is a filled catalog record, the index links every section, both themes are recognizable as this product, and the system would look wrong on a different app. Say "Design system finished. Next is the screens."
