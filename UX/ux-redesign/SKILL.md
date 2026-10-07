---
name: ux-redesign
description: Design high-fidelity HTML improvements for prioritized UX audit opportunities.
disable-model-invocation: true
---

# UX — Redesign

Design solutions for **approved** audit opportunities. High-fidelity HTML under `design/audit/redesign/`.

This is the Redesign state in [ux-audit](../ux-audit/SKILL.md). Say "Redesign." before starting.

Not [ux-design-ui](../ux-design-ui/SKILL.md) (that creates greenfield feature screens from a brief).

## Designs directory

Ask for the `design` path if unknown. All audit HTML lives under `<design>/audit/`. Read `audit/prioritize.html` and the related walkthrough/evaluate pages. If prioritize is missing, follow [ux-prioritize](../ux-prioritize/SKILL.md). Use audit docs chrome from `audit/docs.json` and link `audit/docs.css`. If those are missing, follow the Docs template step in [ux-audit](../ux-audit/SKILL.md). Rebuild `audit/docs.css` the way ux-audit builds it when chrome classes change.

## Redesign

For each approved opportunity:

1. Revisit the existing workflow (walkthrough)
2. Define the desired improved experience
3. Explore possible solutions
4. Choose the simplest effective solution
5. Update the affected user flow
6. Design the affected screens and states

Rules:

- Preserve the product’s established visual language unless changing it is necessary to solve the UX problem
- Do not redesign unrelated screens
- Do not redesign the entire design system
- Reuse existing components and patterns when appropriate
- Include needed states: default, loading, empty, error, success, disabled, validation
- Communicate **before → problem → after** for each improvement
- Ensure the design resolves the problem named in prioritize
- Review the redesigned flow for consistency and usability

**Inspiration:** not a separate skill. When stuck on a pattern, search once (e.g. Mobbin MCP) for comparable products — as a check, not a copy.

For hi-fi craft quality (tokens in frames, production-like labels, theme switch), lean on patterns from [ux-design-ui](../ux-design-ui/SKILL.md) without inventing a new product kit unless required.

## Write

For each opportunity id:

```text
<design>/audit/redesign/<opportunity-id>/index.html
<design>/audit/redesign/<opportunity-id>/<screen>.html
```

`index.html` carries before → problem → after and links to frames. Link each package from `audit/index.html` and from the opportunity on `prioritize.html` when practical. Every page uses the audit docs chrome.

This step is done when approved opportunities have redesign packages that address their success criteria. Say "Redesign finished."
