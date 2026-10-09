---
name: ux-critique
description: Critique a system or screens substep against skill rules without auto-repairing.
disable-model-invocation: true
---

# UX — Critique

Evaluate a chosen surface against the skill rules. Report findings only. Do not edit files (use [ux-repair](../ux-repair/SKILL.md) to fix).

## Gate (before any context)

Do not evaluate until both selections exist. Ask in this order:

```text
Step:
1. system  (design system)
2. screens (screens artboard)
```

Wait. Then list substeps:

```text
System: brand · color · typography · radius · spacing · elevation · icons · components · tokens · all
Screens: all · feature
```

Wait. Then ask for path / feature as needed.

## After the gate

1. Confirm where `design` lives.
2. Load the parent skill ([ux-build-kit](../ux-build-kit/SKILL.md) or [ux-design-ui](../ux-design-ui/SKILL.md)) and [handbook.md](../ux-new/handbook.md) for shell rules.
3. Compare existing files to the rules (handbook chrome, `system.html` / `screens.html`, `look.json`, logo assets when Brand).
4. For screens (and product frames on system specimens), also check rendered-evidence criteria: **hierarchy**, **contrast**, **critical states shown**, **touch/click targets**. Findings need a concrete location in the HTML/frames — not taste alone.
5. Report: what passes, what fails, and a short recommended fix list — without applying it.

## Done

The user has a clear critique. No files changed.
