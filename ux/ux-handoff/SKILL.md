---
name: ux-handoff
description: Write an engineering-ready handoff page from the design folder.
disable-model-invocation: true
---

# UX — Handoff

Turn the `design` folder into a concise engineering handoff.

## Designs directory

The folder is always named `design`. If the path is unknown, ask where it lives. Do not assume the repo root. If a `design` directory already exists, use that one.

Read create artifacts when present: `brief.html`, `design-system/system.json`, feature screens.  
Read audit artifacts when present under `design/audit/`: `docs.json`, `understand.html`, walkthrough, `evaluate.html`, `prioritize.html`, `redesign/`.

If neither create brief nor audit understand exists, say so and stop — or follow the matching pipeline skill only if the user asks to create it first.

## Write

Create `<design>/handoff.html` using the docs chrome from `docs.json` (ask for a docs template via [ux-new](../ux-new/SKILL.md) if `docs.json` is missing). Rebuild `docs.css` the way ux-new builds it.

Include as applicable:

**Create**

- Product summary from the brief  
- Features and screen inventory with links  
- Design-system pointer and key tokens  
- Implementation notes (HTML reference, CSS variables)

**Audit**

- Product context summary from understand  
- Links to walkthrough, evaluate, prioritize  
- Approved improvements and links to `redesign/<id>/`  
- What not to change (out of scope from prioritize)

- Open questions / unfinished pipeline states  

Link `handoff.html` from `<design>/index.html`.

## Done

Engineers can open `handoff.html` and reach every relevant design artifact without hunting the folder.
