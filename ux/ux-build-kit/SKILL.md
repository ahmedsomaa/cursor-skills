---
name: ux-build-kit
description: Write design/design-system HTML plus system.json from look.json (Tone, Design system, or Custom).
disable-model-invocation: true
---

# UX — Build kit

Design a visual system that fits this app and would look wrong on a different product. Deliver it as HTML the screens will use, and as the JSON those pages are built from. Make system-level decisions — do not only document tokens.

This is the Design system state. Say "Design system." before writing (or before Look if `look.json` is missing).

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/look.json`, `<design>/brief.html`, and `<design>/docs.json` first.

- If `look.json` is missing, run **Look** in [ux-new](../ux-new/SKILL.md) and write it before continuing.
- If the brief is missing, follow [ux-discover](../ux-discover/SKILL.md) before designing.
- If `docs.json` is missing, follow Docs template in [ux-new](../ux-new/SKILL.md) (after Look if needed), including custom, and write it before the pages.

The HTML pages are the design-system pages. `system.json` lives in `design-system/`. `docs.json` and `look.json` live next to the index. The catalog format stays in this skill. Do not copy it into the project.

## Look

If `look.json` is valid (`source` is `tone`, `design-system`, or `custom`), **skip asking** — open the chosen guide (or custom notes) and go to Write.

If `look.json` is missing or they chose Remake, run the Look ask from [ux-new](../ux-new/SKILL.md) (Tone | Design system | Custom — one path only), rewrite `look.json`, then Write.

Look pick lists live in [tones/catalog.md](tones/catalog.md) and [design-systems/catalog.md](design-systems/catalog.md) — use those for listing; open only the chosen `{id}.html` after pick (never dump `index.html` for the pick).

| `source` | How to write the kit |
| --- | --- |
| `tone` | Open [tones/](tones/) `{id}.html`. Carry philosophy → layout → type → components → color into Foundations. Invent roles and structure from the tone — **no** second catalog design-system pick. Put id + name into `system.json` `tone`. |
| `design-system` | Open [design-systems/](design-systems/) `{id}.html`. Carry Suggested fonts, icon libraries, primary, and 6+1 fields into `system.json`. That system *is* the look; set `tone` from philosophy / closest-tone pills. Adapt so tokens belong to this product. |
| `custom` | Invent both climate and machinery from `look.json` `description` (and brief). They describe or agent cooked — same outcome: a filled `system.json` unique to this app. |

Tone guides and design-system guides use the **6+1 framework**. Specimen galleries are structure references — execute them as **finished UI specimens** with real type, color, shape, and density, not dashed wireframe clones.

A copied screen, and a system that could ship on any other app, are both unfinished.

## Hierarchy

```text
Foundations → Components → Patterns → Content → Accessibility
```

Never document something at a lower level when it belongs higher (spacing → Foundations; button → Components; destructive confirm → Patterns; preferred wording → Content; focus visible → Accessibility).

Every design-system page answers **What / Why / When / How / When not**, then shows the representation its guide names. Before writing each HTML page, read that section’s `GUIDE.md` under `sections/` (Produce / Represent / Do / Don't).

## Direction

Take the final direction from `look.json`, the brief, and references that fit this product: who it is for, what they do, and any visual language already in the app. Someone who knows the product should recognize it from the type, color, and shape alone.

## Write

Create `<design>/design-system/`.

Write `system.json` first. It is one filled record for this product (including `tone`, `motion`, `patterns`, `content`, `accessibility`, fonts, color roles, shape, elevation). Use the chosen tone or design-system HTML guide as the field source when `source` is catalog; fill Unconfirmed or missing values for this product. Open any `source` URL before relying on it. Custom Look fills every field from the decision notes.

`system.json` is the source the HTML pages are built from.

Follow [sections/foundations/logo/PROCESS.md](sections/foundations/logo/PROCESS.md) for the mark (read [sections/foundations/logo/GUIDE.md](sections/foundations/logo/GUIDE.md) for display). Then write the other section pages as a **polished design-system site** — real UI, chosen Look applied. Docs chrome structure follows `docs.json` and `layouts/<id>.jobs.md` (layout id from `docs.json`) — read that jobs file once for chrome + page inventory; for each section use its GUIDE plus the matching jobs row. Open only that section’s `#wf-*` in the layout HTML if needed. **Never** load the full layout HTML at kit start. Visual finish is a unique finished Tailwind handbook + product tokens inside samples — not agent-guide wireframes.

Docs fonts (`docs.json`) are the **handbook default** for chrome and section prose — including `principles.html`, `patterns.html`, `icons.html`, `themes.html`, and any other mostly-written page. Design-system typography from `system.json` is used **only inside** UI samples / component and pattern examples / product frames, on `typography.html` specimens (the scale itself), and later on storyboards and screens. Do not wrap whole principles / patterns / icons / themes bodies in product type. Index and category hubs use docs fonts throughout. Group navigation by layer: Foundations, Components, Patterns, Content, Accessibility. Mark the current page.

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
2. **Remake.** Re-run Look (rewrite `look.json`), then Write again, then ask again.
3. **Change parts.** Ask which parts (layer or section). For logo alone, follow [sections/foundations/logo/PROCESS.md](sections/foundations/logo/PROCESS.md). For other sections, update `system.json` and those HTML pages; re-read the section guide. Ask again after the change until they confirm.

Do not start [ux-design-ui](../ux-design-ui/SKILL.md) until they confirm.

This step is done when they confirm, `system.json` is filled for this product, `logo.html` and the logo assets exist, the index links every section grouped by layer, both themes are recognizable as this product, specimens are finished UI (not wireframe clones), and the system would look wrong on a different app.
