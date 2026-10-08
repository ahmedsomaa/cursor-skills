---
name: ux-walkthrough
description: Walk existing key flows and document current screens and states without proposing solutions.
disable-model-invocation: true
---

# UX — Walkthrough

Systematically use the application as its intended users would. Document the **current** UX/UI. **Do not propose solutions.**

This is the Walkthrough state in [ux-audit](../ux-audit/SKILL.md). Say "Walkthrough." before starting.

## Designs directory

The folder is always named `design`. Ask for the path if unknown. All outputs go under `<design>/audit/`. Read `<design>/audit/understand.html` first. If it is missing, follow [ux-understand](../ux-understand/SKILL.md). Use audit docs chrome from `audit/docs.json` / `audit/docs.css`; if missing, follow Docs template in [ux-audit](../ux-audit/SKILL.md). Structure from the Walkthrough row in `layouts/<id>.jobs.md`; open `#wf-walkthrough` only if needed — **do not** read the full layout HTML.

## Walk

Use the key flows from understand. Follow complete workflows, not isolated screens.

For each screen along a flow, capture:

- Purpose
- User goal
- Entry point
- Primary action
- Secondary actions
- Information hierarchy
- Available interactions
- Expected next step

Pay attention to: navigation, forms, search/filtering, empty, loading, error, success/confirmation, permissions, edge cases.

## Write

Create `<design>/audit/walkthrough/`:

- `index.html` — list of flows with links
- `<flow-id>.html` — screens and states in order for that flow

Describe the current product faithfully. No evaluation language (“bad”, “should”). No redesign.

Link walkthrough from `audit/index.html`.

This step is done when the important workflows have a reliable current-state map. Say "Walkthrough finished. Next is evaluate."
