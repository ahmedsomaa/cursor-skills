# Color

## Produce

Build semantic color roles screens and components depend on. Light and dark are both this product.

- Roles: background, text, border, icon; plus action, success, caution, danger, focus as needed.
- Name by job (`bg-canvas`, `text-primary`, `action`), never by hue (`blue-500`).
- Every role has light and dark hex. Contrast must hold for text and interactive labels on paired backgrounds.
- Write roles + hex into `system.json` `color`.

Foundations stay stable: components never bind to raw palette steps.

## Represent

`color.html`: visual specimens + usage + token table + Do/Don't.

1. What / Why / When
2. Semantic swatches (large) with role name and hex per theme
3. Usage lines (Primary → primary actions)
4. Pairings (button, input, alert) in light and dark
5. Token table: name · light · dark · when
6. Do / Don't

## Do / Don't

**Do:** Semantic roles; small vocabulary; show light/dark; explain when; realistic pairings.

**Don't:** Dozens of near-duplicate tokens; semantic names after colors; document values with no purpose; mix component-only colors into foundations.
