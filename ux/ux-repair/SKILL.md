---
name: ux-repair
description: Evaluate a kit or UI substep against skill rules and auto-repair it.
disable-model-invocation: true
---

# UX — Repair

Evaluate the current state of a chosen surface against the skill rules, then fix it automatically. Absorbs former edit and polish work.

## Gate (before any context)

Do not evaluate, read the user’s freeform design dump as the task, or write until both selections exist. Read [menus.json](../ux-new/menus.json) and ask in this order:

```text
Step:
1. kit   (design system)
2. ui    (screens)
```

Wait for their choice. Then list every substep for that step from `menus.json` (id + label):

```text
Substep:
1. …
```

Wait for their choice. Only then ask for path, feature, screen, or other context needed to locate the files. If they already pasted context in the first message, ignore it for work until the gate is complete, then use it.

## After the gate

1. Confirm where `design` lives (ask if unknown).
2. Load the parent skill: [ux-build-kit](../ux-build-kit/SKILL.md) or [ux-design-ui](../ux-design-ui/SKILL.md).
3. Load the substep’s `guide`, `process`, or `rules` from `menus.json`.
4. Compare the existing files to those rules. List gaps briefly, then apply repairs.
5. Re-run any ask-gates the original step would require when a decision is missing (overall tone, catalog pick, mobile vs website, feature name, etc.).
6. Rebuild `docs.css` the way [ux-new](../ux-new/SKILL.md) builds it when docs chrome classes change.

### Kit

- Section pages: fix `system.json` and HTML to match the GUIDE.
- **logo:** repair via [PROCESS.md](../ux-build-kit/sections/foundations/logo/PROCESS.md).
- **chrome:** repair via [chrome.md](../ux-new/chrome.md) (nav, docs type, light/dark shell).

### UI

- **storyboard / screen / states:** repair to match [ux-design-ui](../ux-design-ui/SKILL.md) for that slice only.

## Done

The named surface passes the rules. Other surfaces stay unchanged except required shared fixes (broken index links, missing theme tokens used by that page).
