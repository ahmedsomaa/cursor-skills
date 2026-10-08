---
name: ux-understand
description: Understand an existing product — users, goals, flows, terminology — without evaluating or redesigning.
disable-model-invocation: true
---

# UX — Understand

Explore the **existing** application from a product-design perspective. Document what the product is and how people use it. **Do not evaluate or redesign.**

This is the Understand state in [ux-audit](../ux-audit/SKILL.md). Say "Understand." before reading.

Not [ux-discover](../ux-discover/SKILL.md) (that writes a forward create brief).

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one. All outputs go under `<design>/audit/`.

If `audit/docs.json` is missing, follow the Docs template step in [ux-audit](../ux-audit/SKILL.md) (layout from [layouts/*.jobs.md](../ux-audit/layouts/), then fonts + style in one turn from [typography.html](../ux-audit/typography.html) and [layouts/style.html](../ux-audit/layouts/style.html) — plus custom). Write `audit/docs.json` and `audit/docs.css`.

## Explore

Prefer the running product and codebase over documentation alone:

- What the product does
- Who uses it and primary roles
- Problems it solves
- Important user goals
- Main business/product objectives
- Major areas and features
- Key user flows and workflows
- Lightweight vocabulary / wording dictionary (product terms used consistently)

Leave unrelated repo areas alone. Use the product’s words.

## Write

Write `<design>/audit/understand.html` using audit docs chrome (`audit/docs.json`, link `docs.css`) with the findings above and a clear list of key flows for the walkthrough. Use the Understand row in `layouts/<id>.jobs.md` (layout id from `audit/docs.json`); open `#wf-understand` only if that line is ambiguous — **do not** read the full layout HTML. Link it from `<design>/audit/index.html` and `<design>/index.html`.

No usability judgments. No redesign proposals. No design-system invention.

This step is done when someone can read `understand.html` and know what the product is, who it serves, and which flows matter. Say "Understand finished. Next is walkthrough."
