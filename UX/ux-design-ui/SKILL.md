---
name: ux-design-ui
description: Create high-fidelity HTML screens and a storyboard, grouped by feature, showing the critical states for each screen.
disable-model-invocation: true
---

# UX — Design UI

These are the Figma files, in HTML. One page per screen, grouped by feature, using the design system. The page shows that screen and its details.

This is the Screens state. Say "Screens." before writing.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/brief.html`, `<design>/docs.json`, `<design>/design-system/system.json`, and `<design>/design-system/index.html` first. If the brief is missing, follow [ux-discover](../ux-discover/SKILL.md). If the design system index or `system.json` is missing, follow [ux-build-kit](../ux-build-kit/SKILL.md). If `docs.json` is missing, ask using [docs-templates/index.json](../ux-new/docs-templates/index.json) the way [ux-new](../ux-new/SKILL.md) does, including custom, and write it before the pages.

Every screen is HTML and repeats the `<style>` block from the design-system pages, including light and dark. That block declares one CSS custom property per role in `system.json` for color, spacing, type, elevation, and motion. Every color, space, type, and shadow on a screen is one of those custom properties. Product text uses semantic type roles (`heading-1`, `body`, `caption`, `code`). Screens reuse Foundations roles, Components, Patterns, Content vocabulary, and Accessibility rules from the design system — they do not invent new tokens, patterns, or terms. The set stays small so coverage stays at 90% or better. Carry the same type, color, shape, and density into every feature. A generic admin layout is not a finished screen. The page chrome follows `docs.json`, uses Tailwind classes, and links `docs.css`. One theme control switches the docs chrome and the product frames together. Persist the choice in `localStorage` so every design page opens on the same theme. Rebuild `docs.css` the way [ux-new](../ux-new/SKILL.md) builds it.

Foundation specs, component anatomy, patterns, content rules, and accessibility stay on the design-system pages. A note on a screen appears only when the behavior cannot be seen in the frame.

## Per feature

For each feature named in the brief, create `<design>/<feature>/`.

**Storyboard.** `<feature>/storyboard.html` is a film strip of the experience. It is not a flowchart of boxes, and it is not a technical sequence.

The header names the feature, who it is for, and the goal. Each step has a number, a **16:9 panel**, the screen name, the user action, and the outcome. Every panel in the strip uses the same fixed width and height. The panel is the film frame, not a tall phone card. Even when the product is mobile-first, the screen sits inside that 16:9 panel with breathing room around it. The miniature is recognizable, uses the same design system, and stays fully visible: scale it to fit the panel so nothing clips at the bottom or sides. The panel links to that screen's HTML page. Action and outcome sit under the panel as the caption. A Lucide `arrow-right` connects one step to the next. A branch appears only when this flow actually splits. A row holds at most 3 panels. The next step starts a new row, joined by a Lucide `arrow-down` from the end of the row above. Notes at the bottom cover decisions and edge cases. An annotation says why something happens, and only when the frames do not already show it.

**High fidelity.** One HTML page per screen. Show only what this screen actually has:

- Purpose: what the user accomplishes here
- Layout: navigation, header, content structure, primary and secondary sections
- Production-like labels, data, names, dates, and statuses
- The main action, secondary actions, and a destructive action when this screen has one
- The interactions this screen uses: forms, tabs, filters, sort, modal, drawer, menu
- The critical states this screen can reach: default, and loading, empty, error, success, or disabled only when that state is real here
- The edge cases that change this screen: long content, a large set, a failed action, a permission block
- How the layout adapts. Mobile first leads with the phone and shows how it grows. Website first leads with the desktop and shows how it shrinks. Both treats phone and desktop as primary. The brief names which one.
- Focus, labels, error identification, and target size, shown in the frame

The default is shown in light and dark through the page theme switch, which also switches the docs chrome. Other states are extra frames only when they differ.

## Index

Update `<design>/index.html`. The navigation always includes each feature, with its storyboard and its high-fidelity screens under that feature.

This step is done when every feature in the brief has a storyboard and a page for each of its screens, each page shows that screen and the details above, and the index links all of them. Say "Screens finished."
