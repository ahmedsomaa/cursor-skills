---
name: ux-edit
description: Ask whether a change is in the design system or the screens, then edit only that.
disable-model-invocation: true
---

# UX — Edit

Change work that already exists. Ask which surface before editing.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, use that one.

## Ask

Ask what they want to change, and which surface:

1. **Design system.** Follow [ux-system](../ux-system/SKILL.md) for the sections they name. Update `system.json` and those HTML pages. Leave the screens as they are.
2. **Screens.** Follow [ux-screens](../ux-screens/SKILL.md) for the screens they name. Update the storyboard when the journey changes. Leave the design system as it is.

When the answer names both, edit each surface only for the part they named.

## Done

The named pages match the change. The other surface is unchanged. `docs.css` is rebuilt the way [ux](../ux/SKILL.md) builds it when the docs chrome classes change.
