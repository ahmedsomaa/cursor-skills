# Components

## Produce

Only components the brief’s screens need. Each consumes foundation roles — no one-off values.

- For each: purpose, anatomy, variants, sizes, states, behavior, content rules, accessibility (link to Accessibility layer for shared rules).
- Keep the variant API small. `system.json` `components` lists inventory + key rules.

## Represent

Interactive HTML specimens (not screenshots). Per component:

```text
Purpose → Anatomy → Variants → Sizes → States → Behavior → Content → Accessibility → Do/Don't
```

Show variants and states together with realistic labels. Light/dark via page theme or paired specimens.

Page opens with What / Why / When / How / When not for the component set, then each component block.

## Do / Don't

**Do:** Start from purpose; show meaningful states; explain when not to use; realistic content; small API.

**Don't:** Variant per visual tweak; one-off “components”; default-only docs; appearance-based names; let screens redefine behavior.
