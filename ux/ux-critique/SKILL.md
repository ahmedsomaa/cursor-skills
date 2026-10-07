---
name: ux-critique
description: Critique a kit or UI substep against skill rules without auto-repairing.
disable-model-invocation: true
---

# UX — Critique

Evaluate a chosen surface against the skill rules. Report findings only. Do not edit files (use [ux-repair](../ux-repair/SKILL.md) to fix).

## Gate (before any context)

Do not evaluate until both selections exist. Read [menus.json](../ux-new/menus.json) and ask in this order:

```text
Step:
1. kit   (design system)
2. ui    (screens)
```

Wait. Then list substeps for that step:

```text
Substep:
1. …
```

Wait. Then ask for path / feature / screen as needed.

## After the gate

1. Confirm where `design` lives.
2. Load the parent skill and the substep’s guide / process / rules.
3. Compare existing files to the rules.
4. Report: what passes, what fails, and a short recommended fix list — without applying it.

## Done

The user has a clear critique. No files changed.
