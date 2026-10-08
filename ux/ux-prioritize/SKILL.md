---
name: ux-prioritize
description: Consolidate audit findings into a focused high-value UX improvement backlog.
disable-model-invocation: true
---

# UX — Prioritize

Decide what is actually worth improving. Turn evaluate findings into a concise backlog for redesign.

This is the Prioritize state in [ux-audit](../ux-audit/SKILL.md). Say "Prioritize." before starting.

## Designs directory

Ask for the `design` path if unknown. All outputs go under `<design>/audit/`. Read `audit/evaluate.html` (and understand/walkthrough as needed). If evaluate is missing, follow [ux-evaluate](../ux-evaluate/SKILL.md). Use audit docs chrome from `audit/docs.json` / `audit/docs.css`; if missing, follow Docs template in [ux-audit](../ux-audit/SKILL.md). Structure from the Prioritize row in `layouts/<id>.jobs.md`; open `#wf-prioritize` only if needed — **do not** read the full layout HTML.

## Prioritize

- Consolidate duplicate or related findings
- Separate symptoms from root problems
- Drop personal preferences and low-value polish unless the user asks to keep them
- Rank by: user impact, frequency, severity, business importance, confidence, implementation/design effort

Avoid turning every observation into a redesign task.

Each **selected** opportunity must include:

- Problem
- Evidence / observation
- Desired outcome
- Priority
- Scope
- Success criteria

## Write

Write `<design>/audit/prioritize.html` as the focused improvement backlog. Link from `audit/index.html`.

Ask whether to redesign all selected items or a subset. Wait if they want to trim. Do not start [ux-redesign](../ux-redesign/SKILL.md) until the backlog (or subset) is confirmed when they asked to choose.

This step is done when `prioritize.html` is a clear input for redesign. Say "Prioritize finished. Next is redesign."
