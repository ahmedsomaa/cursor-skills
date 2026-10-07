---
name: ux-build-kit
description: Ask catalog vs custom for overall tone, then catalog vs custom for design system; write design/design-system HTML plus a filled system.json.
disable-model-invocation: true
---

# UX — Build kit

Design a visual system that fits this app and would look wrong on a different product. Deliver it as HTML the screens will use, and as the JSON those pages are built from. Make system-level decisions — do not only document tokens.

This is the Design system state. Say "Design system." before asking.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/brief.html` and `<design>/docs.json` first. If the brief is missing, follow [ux-discover](../ux-discover/SKILL.md) before designing. If `docs.json` is missing, ask using [layouts/](../ux-new/layouts/) the way [ux-new](../ux-new/SKILL.md) does, including custom, and write it before the pages. The HTML pages are the design-system pages. `system.json` lives in `design-system/`. `docs.json` lives next to the index. The catalog format stays in this skill. Do not copy it into the project.

## Ask first

Before writing the specimen, ask in this order. Feeling first, then machinery. At each step, **wait for their answer** before continuing. Do not assume catalog or custom.

### 1. Overall tone

The visual flavor of the whole app — SaaS-fit only.

**Ask first (two options only):** Catalog tone, or Custom tone? Mark which you recommend for this brief and why (one line). Wait.

#### If they choose Catalog tone

1. Read [tones/index.html](tones/index.html) and list **every** tone (name + fit).
2. Mark one recommendation again.
3. Wait until they pick a tone id.
4. Open that tone’s HTML. Each guide uses the **6+1 framework**: (1) Core Philosophy, (2) Layout & Spatial Architecture, (3) Typography Rules, (4) Component Anatomy (incl. border-radius pick `square`|`squircle`|`pill` + icons), (5) Intentional Color Systems, (6) Do vs Don’t matrix, (7) Specimen gallery — **four best-fit SaaS wireframes**: App shell · Data view · Form/settings · Focal moment.
5. Put id + name into `system.json` `tone`. Carry philosophy → layout → type → components → color into Foundations. Match the specimens.

#### If they choose Custom tone

Ask whether **they will describe** the vibe or **the agent should cook** it. Wait.

- **They describe it.** Wait for one reply: overall feel, surfaces, density, ornament. Write id + name into `system.json` `tone`.
- **The agent cooks it.** Decide from the brief in a few lines, then optionally search once for references. Write the decision into `system.json` `tone`.

### 2. Design system

Machinery that executes the chosen tone.

**Ask first (two options only):** Catalog design system, or Custom design system? Mark which you recommend for this brief given the chosen tone (one line). Use that tone’s “From our catalog” / closest-tone pills as the hint when recommending a catalog system. Wait.

#### If they choose Catalog design system

1. Read [design-systems/index.html](design-systems/index.html) and list **every** system (name + fit + primary).
2. Mark one recommendation (closest to the chosen tone that still fits the brief).
3. Wait until they pick a system id.
4. Open that system’s HTML guide (same **6+1** shape: Philosophy → Layout → Type → Anatomy → Color → Do/Don’t → four shared Harbor specimens).
5. Carry fields from the guide into `system.json` (field list: [design-systems/schema.json](design-systems/schema.json)). Use **Suggested fonts**, **Icon libraries**, and the system **primary** for action color. A field marked Unconfirmed is not a value — fill it for this product. Open `source` before using it. Adapt so tokens and specimens **execute the chosen tone** and belong to this product.

#### If they choose Custom design system

Ask whether **they will describe** the settings or **the agent should cook** them. Wait.

- **They describe it.** Give this format and wait for one reply. Color: the vibe, or background, text, and action. Typography: the families, or how the type should feel. Radius: sharp, slight, or round.
- **The agent cooks it.** Decide the look from the brief and tone first and write that decision in a few lines before any search. Then search once for references that match it, on Mobbin, Figma Community, Dribbble, Behance, Pinterest, or one other place. Use Mobbin MCP for Mobbin and the web for the others. Use what you find as a check, not as the design. The type, color, and shape belong to this product and serve the tone. A close copy of a found screen is unfinished.

A copied screen, and a system that could ship on any other app, are both unfinished. When writing Foundations, tone drives climate; the design system supplies roles and structure.

## Hierarchy

```text
Foundations → Components → Patterns → Content → Accessibility
```

Never document something at a lower level when it belongs higher (spacing → Foundations; button → Components; destructive confirm → Patterns; preferred wording → Content; focus visible → Accessibility).

Every design-system page answers **What / Why / When / How / When not**, then shows the representation its guide names. Before writing each HTML page, read that section’s `GUIDE.md` under `sections/` (Produce / Represent / Do / Don't).

## Direction

Take the final direction from the brief and from references that fit this product: who it is for, what they do, and any visual language already in the app. Someone who knows the product should recognize it from the type, color, and shape alone.

## Write

Create `<design>/design-system/`.

Write `system.json` first. It is one filled record in the same flat fields as a catalog record. The field list is [design-systems/schema.json](design-systems/schema.json). Fill every required string for this product (including `tone`, `motion`, `patterns`, `content`, `accessibility`). A catalog pick and a custom system both write this file.

`system.json` is the source the HTML pages are built from.

Follow [sections/foundations/logo/PROCESS.md](sections/foundations/logo/PROCESS.md) for the mark (read [sections/foundations/logo/GUIDE.md](sections/foundations/logo/GUIDE.md) for display). Then write the other section pages.

`<design>/design-system/index.html` is the polished index. Group navigation by layer: Foundations, Components, Patterns, Content, Accessibility. Mark the current page. Use layout and typography from `docs.json`.

| Layer         | File                 | Guide                                                                                  |
| ------------- | -------------------- | -------------------------------------------------------------------------------------- |
| Foundations   | `principles.html`    | [sections/foundations/principles/GUIDE.md](sections/foundations/principles/GUIDE.md)   |
| Foundations   | `color.html`         | [sections/foundations/color/GUIDE.md](sections/foundations/color/GUIDE.md)             |
| Foundations   | `typography.html`    | [sections/foundations/typography/GUIDE.md](sections/foundations/typography/GUIDE.md)   |
| Foundations   | `spacing.html`       | [sections/foundations/spacing/GUIDE.md](sections/foundations/spacing/GUIDE.md)         |
| Foundations   | `layout.html`        | [sections/foundations/layout/GUIDE.md](sections/foundations/layout/GUIDE.md)           |
| Foundations   | `shape.html`         | [sections/foundations/shape/GUIDE.md](sections/foundations/shape/GUIDE.md)             |
| Foundations   | `elevation.html`     | [sections/foundations/elevation/GUIDE.md](sections/foundations/elevation/GUIDE.md)     |
| Foundations   | `icons.html`         | [sections/foundations/iconography/GUIDE.md](sections/foundations/iconography/GUIDE.md) |
| Foundations   | `motion.html`        | [sections/foundations/motion/GUIDE.md](sections/foundations/motion/GUIDE.md)           |
| Foundations   | `logo.html`          | [sections/foundations/logo/GUIDE.md](sections/foundations/logo/GUIDE.md)               |
| Foundations   | `themes.html`        | [sections/foundations/themes/GUIDE.md](sections/foundations/themes/GUIDE.md)           |
| Components    | `components.html`    | [sections/components/GUIDE.md](sections/components/GUIDE.md)                           |
| Patterns      | `patterns.html`      | [sections/patterns/GUIDE.md](sections/patterns/GUIDE.md)                               |
| Content       | `content.html`       | [sections/content/GUIDE.md](sections/content/GUIDE.md)                                 |
| Accessibility | `accessibility.html` | [sections/accessibility/GUIDE.md](sections/accessibility/GUIDE.md)                     |

Put the product tokens and the theme switch in a `<style>` block. Declare one CSS custom property per role named in `system.json` for color, spacing, type, elevation, and motion. Repeat that block on every design-system page. Both themes are this product, not a default inverted palette. The docs chrome is Tailwind classes from `docs.json`. Every page links `docs.css`. Rebuild `docs.css` the way [ux-new](../ux-new/SKILL.md) builds it. One theme control switches the docs chrome and the product frames together. Persist the choice in `localStorage` so every design page opens on the same theme.

Link `<design>/design-system/index.html` from `<design>/index.html`.

## Confirm

When the pages and logo exist, say "Design system ready." Point them at `<design>/design-system/index.html`. Ask one of:

1. **Confirm.** Keep this system. Say "Design system finished. Next is the screens."
2. **Remake.** Follow Ask first and Write again for a new system, then ask again.
3. **Change parts.** Ask which parts (layer or section). For logo alone, follow [sections/foundations/logo/PROCESS.md](sections/foundations/logo/PROCESS.md). For other sections, update `system.json` and those HTML pages; re-read the section guide. Ask again after the change until they confirm.

Do not start [ux-design-ui](../ux-design-ui/SKILL.md) until they confirm.

This step is done when they confirm, `system.json` is a filled catalog record, `logo.html` and the logo assets exist, the index links every section grouped by layer, both themes are recognizable as this product, and the system would look wrong on a different app.
