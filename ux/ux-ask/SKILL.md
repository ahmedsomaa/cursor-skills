---
name: ux-ask
description: Ask anything about the ux skills, such as how to start or which skill to run.
disable-model-invocation: true
---

# UX — Ask

Answer the question. Do not start a design unless the user asks you to start one.

Read a step skill only when the answer depends on its rules. Two pipelines:

- **Create** (new product UI): [ux-new](../ux-new/SKILL.md)
- **Audit** (existing product): [ux-audit](../ux-audit/SKILL.md)

Planned skills: [ROADMAP.md](../ux-new/ROADMAP.md).

## Get started

**Create** — three user waits: Round 1 (folder + visual + logo) → Round 2 (scope) → Kit Confirm; then pilot screens. Ship: Mintlify / Fumadocs-style Design Handbook. Chrome: [handbook.md](../ux-new/handbook.md).

**When to grill first vs ux-new alone**

- **Fuzzy product language** (terms unsettled, domain unclear) → run `/grill-with-docs` (or your main-flow grilling) first so `GLOSSARY.md` / ADRs exist, then `/ux-new`. Scope reads those terms and does not re-ask them.
- **Clear solo build** (you know the product and features) → `/ux-new` alone is enough. Grilling rounds are already inside Round 1 / Round 2; grill-with-docs is not required.

```text
/ux-new Design the assignment flow from this app's requirements.
```

**Audit** — name `ux-audit` for an existing app. Folder → **ask audit docs style** (`ux-audit/layouts/` + typography + custom, then font pairing) → understand → walkthrough → evaluate → prioritize → redesign. All HTML under `design/audit/`.

```text
/ux-audit Audit the checkout experience in this app.
```

## Catalog

### Create pipeline

`ux-new` runs Round 1 + Round 2, then pilot-first kit and screens. `look.json` tracks `status` and `pilotFeature`.

| Need | Skill |
| --- | --- |
| Full create run with progress | `ux-new` |
| Round 2 Scope + brief + handbook shell | `ux-discover` |
| Write `system.html` (brand, foundations, pilot components, tokens) | `ux-build-kit` |
| Write `screens.html` artboard (pilot first) | `ux-design-ui` |

### Audit pipeline

`ux-audit` runs all five after Folder and Docs template. Artifacts under `design/audit/` (including `audit/docs.json` / `audit/docs.css`).

| Need | Skill |
| --- | --- |
| Full audit run with progress | `ux-audit` |
| Product, users, flows, vocabulary (as-is) | `ux-understand` |
| Current screens/states along flows | `ux-walkthrough` |
| Problems + opportunities backlog | `ux-evaluate` |
| Focused improvement backlog | `ux-prioritize` |
| Hi-fi for approved opportunities | `ux-redesign` |

### Assist

| Need | Skill |
| --- | --- |
| Which skill / how this suite works | `ux-ask` |
| Progress report, no writes | `ux-show-status` |
| Continue from last unfinished state | `ux-resume` |
| Critique a create system or screens slice (no edits) | `ux-critique` |
| Engineering handoff page | `ux-handoff` |

### Single commands (create only)

| Need | Skill |
| --- | --- |
| Run one system or screens substep | `ux-step` |
| Fix whatever is wrong — describe the problem; no menus | `ux-repair` |

## Name clarity

- `ux-understand` (audit as-is) ≠ `ux-discover` (create scope + brief + handbook)
- `ux-redesign` (audit improvements) ≠ `ux-design-ui` (create `screens.html`)
- `ux-evaluate` (product UX audit) ≠ `ux-critique` (create design-folder critique)

## Where the files go

The folder is always named `design`. Ask where it should live; do not assume the repo root.

Create: `look.json`, `handbook.css`, `handbook.js`, `favicon.svg`, `index.html`, `brief.html`, `system.html`, `screens.html` (plus `logo/` when the mark is custom).  
Audit: everything under `design/audit/`. Audit docs catalog: `ux-audit/layouts/` + `ux-audit/typography.html`.  
Create handbook chrome (fixed): [handbook.md](../ux-new/handbook.md) — General Sans / Geist Mono 12px; zinc-only (no accent); minified custom CSS/JS (no Tailwind); CSS-first; Lucide nav; ⌘K; **ON THIS PAGE** on every page; favicon + meta; home Overview/Start here/How to use/Status; compact titles; clickable site name; three links only (no DS subnav).

## Answer

1. Answer in a few sentences.
2. Name the one skill to run, when a skill is the next move.
3. Give one prompt they can paste.

```text
/ux-audit Audit the main teacher workflows in this app.
```
