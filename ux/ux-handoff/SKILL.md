---
name: ux-handoff
description: Write an engineering-ready handoff page from the design folder.
disable-model-invocation: true
---

# UX — Handoff

Turn the `design` folder into a concise engineering handoff.

## Designs directory

The folder is always named `design`. If the path is unknown, ask where it lives. Do not assume the repo root. If a `design` directory already exists, use that one.

Read create artifacts when present: `look.json`, `index.html`, `brief.html`, `system.html`, `screens.html`, and `logo/` when present.  
Read audit artifacts when present under `design/audit/`: `docs.json`, `understand.html`, walkthrough, `evaluate.html`, `prioritize.html`, `redesign/`.

If neither create `brief.html` / `system.html` nor audit `understand.html` exists, say so and stop — or follow the matching pipeline skill only if the user asks to create it first.

## Write

Create `<design>/handoff.html` as a handbook page using [handbook.md](../ux-new/handbook.md) when create chrome exists; otherwise a short self-contained page. Link it from the sidebar or `index.html` if the create handbook is present.

Include as applicable:

**Create**

- Product summary from `look.json` / `brief.html`
- Features and screen inventory
- Links to `system.html` (Brand / Foundations / Components / Tokens) and `screens.html`
- Logo: point at Brand downloads under `logo/` when custom, or the library URL when from an icon set
- Implementation notes: reuse CSS variables; match elevation per theme; open the handbook from `index.html`

**Audit**

- Product context summary from understand  
- Links to walkthrough, evaluate, prioritize  
- Approved improvements and links to `redesign/<id>/`  
- What not to change (out of scope from prioritize)

- Open questions / unfinished pipeline states  

## Done

Engineers can open `handoff.html` and reach every relevant design artifact without hunting the folder.
