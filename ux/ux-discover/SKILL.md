---
name: ux-discover
description: Discover project context and write design/brief.html.
disable-model-invocation: true
---

# UX — Discover

Read the app. Write the brief the design system and the screens will follow. Do not style the product. The page uses the docs chrome.

This is the Brief state. Say "Brief." before reading.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/docs.json`. If it is missing, ask using [layouts/](../ux-new/layouts/), [typography.html](../ux-new/typography.html), and [layouts/style.html](../ux-new/layouts/style.html) the way [ux-new](../ux-new/SKILL.md) does — layout, then font pairing, then Style — including custom, and write `docs.json` (with `fonts` and `style`) before the page. Build `brief.html` and the index with that layout, typography, fonts, icons, and style, using Tailwind classes, and link `docs.css`. Load the families from Google Fonts. Code uses the monospace named in `fonts`. Icons are Lucide, the way [ux-new](../ux-new/SKILL.md) loads them. Apply `style` radii to docs chrome. Rebuild `docs.css` the way ux-new builds it. One theme control switches the docs chrome. Persist the choice in `localStorage` so later design pages open on the same theme.

## Read

Prefer the repo over assumptions. Read the requirements and the existing product:

- What the product is, and the problem this work addresses
- Who uses it, and the role this work is for
- What they must accomplish, and what success looks like in plain language
- Features and screens in scope — and what is out of scope
- Existing pages, navigation, and terminology
- Constraints the visual design has to respect (brand, tech, a11y)

Leave unrelated parts of the repo alone. Use the product's words.

## Write

Write `<design>/brief.html` as one scrollable **spec sheet**. Match the Brief · Overview structure in [sidebar.html](../ux-new/layouts/sidebar.html#wf-brief) (wireframe is the layout source of truth). Fill these blocks in order:

1. **Meta** — product name, platform (mobile first / website first / both), one-line purpose
2. **Problem** — 2–3 sentences on what’s broken or missing; state the problem, not the UI solution
3. **Who** — primary role(s) and context of use
4. **Goals** — user goal, product goal, success in plain language
5. **Scope** — **In** and **Out** side by side (both required)
6. **Features → Screens** — table: each feature and the screens under it (source of truth for Screens nav)
7. **Constraints** — key/value rows (brand, tech, a11y, terms to keep, plus platform if not already clear in Meta)
8. **Open questions** — optional parking lot; omit the block when empty

Before the brief is finished, ask whether the designs are mobile first, website first, or both. Record that in Meta (and Constraints if useful). If they already named it, use that answer.

Keep the page short. No product mockups, cards-as-dashboard, tabs, or accordions on the brief. No product styling. No design system. No screen pages. This step writes `brief.html` and the index, in the docs chrome.

Add the brief to `<design>/index.html`. Create the index if it does not exist. Navigation: Brief → Overview; Design system; Screens → each feature from the table → Storyboard, Designs.

This step is done when `brief.html` has Meta (with platform), Problem, Who, Goals, Scope in and out, a Features → Screens table the later steps can follow, and Constraints. Say "Brief finished. Next is the design system."
