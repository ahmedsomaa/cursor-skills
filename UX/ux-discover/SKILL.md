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

Read `<design>/docs.json`. If it is missing, ask using [docs-templates/index.json](../ux-new/docs-templates/index.json) the way [ux-new](../ux-new/SKILL.md) does, including custom, and write `docs.json` before the page. Build `brief.html` and the index with that layout, typography, fonts, and icons, using Tailwind classes, and link `docs.css`. Load the families from Google Fonts. Code uses the monospace named in `fonts`. Icons are Lucide, the way [ux-new](../ux-new/SKILL.md) loads them. Rebuild `docs.css` the way ux-new builds it. One theme control switches the docs chrome. Persist the choice in `localStorage` so later design pages open on the same theme.

## Read

Prefer the repo over assumptions. Read the requirements and the existing product:

- What the product does, and why
- Who uses it, and the role this work is for
- The task they must accomplish
- Features and screens this request covers
- Existing pages, navigation, and terminology
- Constraints the visual design has to respect

Leave unrelated parts of the repo alone. Use the product's words.

## Write

Write `<design>/brief.html` with:

- Who it is for
- What they must accomplish
- The features and the screens this work covers
- The constraints the visual design has to respect

Before the brief is finished, ask whether the designs are mobile first, website first, or both. Record that answer in the constraints. If they already named it, use that answer.

No product styling. No design system. No screens. This step writes `brief.html` and the index, in the docs chrome.

Add the brief to `<design>/index.html`. Create the index if it does not exist. Its navigation includes the design system and a link for each feature named in the brief.

This step is done when `brief.html` names the features and screens the later steps will design. Say "Brief finished. Next is the design system."
