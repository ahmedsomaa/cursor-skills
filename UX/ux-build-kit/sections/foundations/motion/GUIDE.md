# Motion

## Produce

A tiny motion language: durations, easings, and when motion is used.

- Roles such as `motion-fast`, `motion-base`, `motion-slow` + easing names.
- Respect `prefers-reduced-motion`: reduce or cut decorative motion.
- Write into `system.json` `motion`. Skip motion theater the product never uses.

## Represent

`motion.html`:

1. What / Why / When / When not
2. Duration and easing chips (name · value · when)
3. Tiny loop demos: fade, move, scale — using the tokens
4. Reduced-motion note
5. Do / Don't

## Do / Don't

**Do:** Short token set; purposeful motion; reduced-motion path.

**Don't:** Unique timings per screen; motion that blocks understanding; ignore reduced motion.
