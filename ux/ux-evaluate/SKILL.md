---
name: ux-evaluate
description: Evaluate current UX/UI — usability problems, friction, opportunities — without redesigning.
disable-model-invocation: true
---

# UX — Evaluate

Evaluate the current experience from a **product/UX** perspective. Produce a structured audit and opportunity backlog. **Do not redesign.**

This is the Evaluate state in [ux-audit](../ux-audit/SKILL.md). Say "Evaluate." before starting.

Not [ux-critique](../ux-critique/SKILL.md) (that gates create kit/ui substeps in `design/`).

## Designs directory

Ask for the `design` path if unknown. All outputs go under `<design>/audit/`. Read `audit/understand.html` and `audit/walkthrough/`. If either is missing, follow the earlier audit skills first. Use audit docs chrome from `audit/docs.json` / `audit/docs.css`; if missing, follow Docs template in [ux-audit](../ux-audit/SKILL.md). Structure from the Evaluate row in `layouts/<id>.jobs.md`; open `#wf-evaluate` only if needed — **do not** read the full layout HTML.

## Evaluate

Read [dimensions.md](../ux-audit/dimensions.md) and apply every dimension.

Identify usability problems, friction, inconsistencies, and opportunities. For every finding document: where, what, why, who, impact, opportunity, type, severity (fields in dimensions.md).

Distinguish:

- Actual usability problems
- Minor visual polish
- Product/UX opportunities
- Personal design preferences (do not treat as required fixes)

Do not criticize something only because it differs from a preferred style. Justify with established UX principles and this product’s context.

## Write

Write `<design>/audit/evaluate.html` with findings grouped by flow or dimension, plus a flat opportunity backlog. Link from `audit/index.html`.

No hi-fi. No solution specs (those belong in prioritize/design).

This step is done when findings are structured and typed. Say "Evaluate finished. Next is prioritize."
