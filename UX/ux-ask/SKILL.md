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

**Create** — name `ux-new` and say what to design. Folder → docs template → brief → kit → screens.

```text
/ux-new Design the assignment flow from this app's requirements.
```

**Audit** — name `ux-audit` for an existing app. Folder → **ask audit docs style** (same catalog templates as create + custom, then font pairing) → understand → walkthrough → evaluate → prioritize → redesign. All HTML under `design/audit/`.

```text
/ux-audit Audit the checkout experience in this app.
```

## Catalog

### Create pipeline

`ux-new` runs the three create steps after Folder and Docs template.

| Need | Skill |
| --- | --- |
| Full create run with progress | `ux-new` |
| Forward brief from requirements | `ux-discover` |
| Invent design system (kit) | `ux-build-kit` |
| Storyboards + high-fidelity screens | `ux-design-ui` |

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
| Critique a create kit/ui substep (no edits) | `ux-critique` |
| Engineering handoff page | `ux-handoff` |

### Single commands (create only)

Ask **step → substep** from [menus.json](../ux-new/menus.json) before any context.

| Need | Skill |
| --- | --- |
| Run one kit or ui substep | `ux-step` |
| Evaluate and auto-repair one substep | `ux-repair` |

## Name clarity

- `ux-understand` (audit as-is) ≠ `ux-discover` (create brief)
- `ux-redesign` (audit improvements) ≠ `ux-design-ui` (create screens)
- `ux-evaluate` (product UX audit) ≠ `ux-critique` (create design-folder substep)

## Where the files go

The folder is always named `design`. Ask where it should live; do not assume the repo root.

Create: `brief.html`, `design-system/`, feature storyboards and screens.  
Audit: everything under `design/audit/` — `docs.json`, `docs.css`, `understand.html`, `walkthrough/`, `evaluate.html`, `prioritize.html`, `redesign/`.  
Create chrome stays at `design/docs.json` when present. Docs template catalog lives in `ux-new/docs-templates/` (audit asks the same options + custom).

## Answer

1. Answer in a few sentences.
2. Name the one skill to run, when a skill is the next move.
3. Give one prompt they can paste.

```text
/ux-audit Audit the main teacher workflows in this app.
```
