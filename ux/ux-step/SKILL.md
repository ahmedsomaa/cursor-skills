---
name: ux-step
description: Run one system or screens substep after the user picks step and substep.
disable-model-invocation: true
---

# UX — Step

Run a single substep under the design system (system) or screens. Create or refresh only that slice.

## Gate (before any context)

Do not read design intent, open product files for the task, or write until both selections exist. Ask in this order:

```text
Step:
1. system  (design system — brand, foundations, components, tokens)
2. screens (screens artboard)
```

Wait for their choice. Then list every substep for that step:

```text
System substeps:
1. brand          (guidelines, logo variants, downloads / library link)
2. color
3. typography
4. radius
5. spacing
6. elevation
7. icons          (public icon library pick)
8. components
9. tokens
10. all           (full system.html rewrite)

Screens substeps:
1. all     (full screens.html)
2. feature (one feature’s frames — ask which)
```

Wait for their choice. Only then ask for path / feature / other context as needed.

## After the gate

1. Confirm where `design` lives (ask if unknown). Do not assume the repo root.
2. Load the parent skill: [ux-build-kit](../ux-build-kit/SKILL.md) (system) or [ux-design-ui](../ux-design-ui/SKILL.md) (screens). For handbook chrome issues, also follow [handbook.md](../ux-new/handbook.md).
3. Re-run any ask-gates that substep originally required (Look when remaking the whole system; Scope when features or shell are missing; feature name for screens → feature).
4. Write only the files for that substep. Keep the handbook shell consistent across pages (General Sans / Geist Mono, zinc-only no accent, minified custom CSS/JS, CSS-first, Lucide nav, ⌘K, ON THIS PAGE, favicon/meta, separator, Preview/Code radios, padding; no DS subnav). Do **not** recolor handbook chrome from product tokens. For a single system section, update that section and the Tokens Preview/Code block in `system.html`; refresh `design/logo/` downloads when brand/logo changes. For screens → feature, refresh that feature’s row only. Keep product variables in sync with `system.html` when screens change.

## Done

The chosen substep’s output matches the parent skill’s rules for that slice. Other surfaces are unchanged unless the substep requires a shared update (sidebar, variables block, feature row, logo assets).
