---
name: ux-audit
description: Run the full existing-product UX audit pipeline with step progress.
disable-model-invocation: true
---

# UX — Audit

Audit an **existing** product: understand it, walk the experience, evaluate, prioritize, then redesign improvements. **All audit artifacts are HTML under `design/audit/`.** This is not the create pipeline ([ux-new](../ux-new/SKILL.md)).

Run the five steps in order. Read each step skill when you reach it, then follow it. Do not add steps. Do not write a document for a step beyond the files that step names.

1. [ux-understand](../ux-understand/SKILL.md)
2. [ux-walkthrough](../ux-walkthrough/SKILL.md)
3. [ux-evaluate](../ux-evaluate/SKILL.md)
4. [ux-prioritize](../ux-prioritize/SKILL.md)
5. [ux-redesign](../ux-redesign/SKILL.md)

Evaluation dimensions: [dimensions.md](dimensions.md). Inspiration/research is **not** a pipeline step — use it inside `ux-redesign` when needed.

## Status

Say the current state in the reply before starting it. When that work is done, say it is finished and name the next state. A question that waits on the user stays the current state until they answer.

1. Folder. Where `design` lives. Finished when the path is chosen.
2. Docs template. Audit docs style chosen; `audit/docs.json` written.
3. Understand. Finished when `audit/understand.html` covers product, users, flows, and vocabulary.
4. Walkthrough. Finished when `audit/walkthrough/` maps the current experience for the key flows.
5. Evaluate. Finished when `audit/evaluate.html` holds structured findings.
6. Prioritize. Finished when `audit/prioritize.html` is a focused improvement backlog (user may trim).
7. Redesign. Finished when selected opportunities have before → problem → after hi-fi under `audit/redesign/`.

## Designs directory

The folder is always named `design`. This is the Folder state. Say "Folder." before asking.

Before creating it, ask where in the current project it should live. Do not assume the repo root. Use the path they give for the rest of the run. If a `design` directory already exists, confirm that one instead of creating a second. Create `<design>/audit/` for every audit artifact — do not put audit HTML next to create screens at the `design/` root (except linking from the main index).

Say "Folder finished. Next is the docs template." when the path is chosen.

## Docs chrome (audit style)

This is the Docs template state. Say "Docs template." before asking.

**Always ask** which style they want for the **audit** documentation — even if create already has `<design>/docs.json`. Audit chrome is separate: write `<design>/audit/docs.json` and `<design>/audit/docs.css`. Every audit HTML page uses that chrome and links `docs.css` relative to `audit/` (or an equivalent path that resolves to `audit/docs.css`).

Ask using this skill’s catalog with **staged reads** (same idea as create):

1. For the pick, read only **Id / Fit** from each [layouts/*.jobs.md](layouts/) — **do not** open the full wireframe HTML. Show name + fit. Recommend gallery when the work is mostly walkthrough/redesign frames, and sidebar when it is mostly written reports. **Always offer custom.**
2. Catalog layout: after they choose, read **once** `layouts/<id>.jobs.md` (chrome + page inventory). That file is the build bible. **Do not** read the full [sidebar.html](layouts/sidebar.html) / [gallery.html](layouts/gallery.html) / [topbar.html](layouts/topbar.html). Open a **single** `#wf-*` only when a jobs line is ambiguous. Build a **finished** audit docs site — real Tailwind chrome, fonts, and style — not dashed wireframe clones.
   - Sidebar — left groups Understand / Walkthrough / Evaluate / Prioritize / Redesign; nest flows and redesign opportunities.
   - Gallery — **no navbar**; home stacks the five steps as sections with card grids.
   - Topbar — **navbar** for the five steps + **horizontal tabs** for flows / opportunity children + **vertical tabs** for redesign screens.
3. Custom: ask whether they will describe the settings or the agent should cook them — same format as ux-new (color, typography, radius, monospace).
4. After layout choice, ask **font pairing and Style in the same turn** from [typography.html](typography.html) and [layouts/style.html](layouts/style.html) (recommend a pairing whose Best for includes the chosen layout id; custom last for fonts). Write `fonts` and `style` (`square` | `squircle` | `pill`) into `audit/docs.json`.

If `audit/docs.json` already exists, show the current choice and ask whether to **keep** it or **pick a new** style before continuing.

Write `<design>/audit/docs.json`. Load fonts from Google Fonts with `display=swap`.

**Docs fonts** apply to audit chrome and written report pages (index, understand, evaluate, prioritize, walkthrough indexes). **Product-like frames** on walkthrough flow pages and redesign hi-fi use the product’s type when a create kit exists; otherwise keep readable docs type in chrome and frame labels — do not force a second random pairing on frames only. Docs chrome is **text labels only** — no Lucide (or other) icons in nav, tabs, or section heads. Docs chrome is Tailwind utility classes.

Build `<design>/audit/docs.css` with the Tailwind CLI, minified, scanning the HTML under `audit`. From the `audit` folder: write a temporary `.tailwind-input.css` with `@import "tailwindcss" source(".");`, run `npx @tailwindcss/cli -i .tailwind-input.css -o docs.css --minify`, then delete the input file.

Theme control on every audit page switches light/dark and persists in `localStorage` (same key as create is fine so the site stays consistent, or an audit-specific key if create chrome differs).

Say "Docs template finished. Next is understand." when `audit/docs.json` is written.

## Index

Keep `<design>/index.html` and `<design>/audit/index.html` updated. The main index links Create artifacts (when present) and Audit. Audit index links understand, walkthrough, evaluate, prioritize, and redesign opportunities.

```text
<chosen-path>/design/index.html
<chosen-path>/design/audit/docs.json
<chosen-path>/design/audit/docs.css
<chosen-path>/design/audit/index.html
<chosen-path>/design/audit/understand.html
<chosen-path>/design/audit/walkthrough/index.html
<chosen-path>/design/audit/walkthrough/<flow-id>.html
<chosen-path>/design/audit/evaluate.html
<chosen-path>/design/audit/prioritize.html
<chosen-path>/design/audit/redesign/<opportunity-id>/index.html
<chosen-path>/design/audit/redesign/<opportunity-id>/<screen>.html
```

The run is done when prioritize exists and approved opportunities have redesign packages (or the user stops after prioritize). Say "Redesign finished." or "Prioritize finished." when stopping early.
