# Patterns

## Produce

Reusable solutions to recurring UX problems from the brief — not feature one-offs.

- Pattern = scenario + structure + behavior + states. Distinct from a component (“Dialog” vs “how to confirm a destructive action”).
- Include loading / empty / error / success and mobile behavior when real.
- `system.json` `patterns` names the patterns and when to use them.

## Represent

`patterns.html` — for each pattern:

1. When to use (user problem)
2. Structure (diagram or layout skeleton)
3. Behavior and decision points
4. States (loading → empty → populated → error)
5. Mini storyboard when multi-step
6. Alternatives when legitimate
7. Do / Don't

## Do / Don't

**Do:** Start from the user problem; complete interaction; edge cases; mobile; a11y pointers.

**Don't:** Glue components and call it a pattern; one-feature-only patterns; implementation dumps; ignore empty/error; force one solution when several are valid.
