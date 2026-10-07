# Typography

## Produce

A small semantic type scale, not a pixel ladder. Docs chrome fonts stay in `docs.json`.

- **Families:** 1 primary UI font; optional mono; second family only for brand/editorial or a second script.
- **Weights:** only those used; default 400 / 500 / 600 / 700.
- **Roles (~8–10):** `display`, `heading-1`…`heading-3`, `body-l`, `body`, `body-s`, `label`, `caption`, `code`.
- Each role defines family, size, weight, line height, letter spacing together.
- Brand decorative face stays under Brand/logo; Product UI stays on the primary sans.
- `system.json` `typography` must be enough to rebuild the page.

## Represent

`typography.html`:

1. What / Why / When
2. Font families (usage)
3. Weights
4. Semantic styles — specimen in product copy + five properties + usage
5. Responsive shifts when sizes change with the brief’s viewport stance
6. Content rules (hierarchy, line length, truncation, capitalization)
7. Accessibility (min sizes, contrast, zoom)
8. Token table + Do / Don't

## Do / Don't

**Do:** Semantic roles; five properties per style; realistic copy; brand vs UI split.

**Don't:** `font-12` ladders; every weight the file offers; tokens for one-off screens.
