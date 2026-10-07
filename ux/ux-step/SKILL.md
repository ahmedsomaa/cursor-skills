---
name: ux-step
description: Run one kit or UI substep after the user picks step and substep.
disable-model-invocation: true
---

# UX — Step

Run a single substep under the design system (kit) or screens (ui). Create or refresh only that slice.

## Gate (before any context)

Do not read design intent, open product files for the task, or write until both selections exist. Read [menus.json](../ux-new/menus.json) and ask in this order:

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

Wait for their choice. Only then ask for path / feature / screen / other context as the substep’s `ask` field or rules require.

## After the gate

1. Confirm where `design` lives (ask if unknown). Do not assume the repo root.
2. Load the parent skill for the step: [ux-build-kit](../ux-build-kit/SKILL.md) or [ux-design-ui](../ux-design-ui/SKILL.md).
3. Load the substep’s `guide`, `process`, or `rules` path from `menus.json`.
4. Re-run any ask-gates that substep originally required (e.g. atmosphere only when the full kit ask applies; for logo follow PROCESS; for ui ask feature and/or screen).
5. Write only the files for that substep. Update `system.json` when a kit section changes. Update the storyboard when a ui journey changes. Rebuild `docs.css` the way [ux-new](../ux-new/SKILL.md) builds it when docs chrome classes change. Keep index links current.

### Kit

- Section pages: follow the section GUIDE; update `system.json` and that HTML page.
- **logo:** follow [PROCESS.md](../ux-build-kit/sections/foundations/logo/PROCESS.md) and the logo GUIDE.
- **chrome:** follow [chrome.md](../ux-new/chrome.md).

### UI

- **storyboard:** one feature’s `storyboard.html` per [ux-design-ui](../ux-design-ui/SKILL.md).
- **screen:** one high-fidelity screen page for the named feature + screen.
- **states:** critical states for that screen only.

## Done

The chosen substep’s pages match the parent skill’s rules for that slice. Other surfaces are unchanged unless the substep requires a shared update (index link, `system.json` field, storyboard caption).
