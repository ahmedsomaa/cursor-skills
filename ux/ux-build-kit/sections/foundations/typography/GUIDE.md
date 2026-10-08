# Typography

## Produce

A small semantic type scale, not a pixel ladder. Docs chrome fonts stay in `docs.json`. Page chrome and handbook prose on this page use docs fonts; **product type specimens** use `system.json` roles.

- **Families:** 1 primary UI font; optional mono; second family only for brand/editorial or a second script.
- **Weights:** only those used; default 400 / 500 / 600 / 700.
- **Roles (~8–10):** `display`, `heading-1`…`heading-3`, `body-l`, `body`, `body-s`, `label`, `caption`, `code`.
- Each role defines family, size, weight, line height, letter spacing together.
- Brand decorative face stays under Brand/logo; Product UI stays on the primary sans.
- `system.json` `typography` must be enough to rebuild the page.

## Represent

`typography.html`:

1. What / Why / When
2. **Per family** — for **each** family in the system (UI, mono, optional brand):
   - Family name + role (UI / mono / brand)
   - **Weight variants** actually used — live specimen line per weight with the numeric label (e.g. Regular 400 · Medium 500 · Semibold 600 · Bold 700). Do not list unused file weights.
   - Usage note (where this face appears in product UI)
3. **Semantic styles** — for each role: live specimen in product copy **plus** size, weight, line-height, letter-spacing (and family). Show the metrics as readable details next to or under the specimen, not only in a token dump.
4. Responsive shifts when sizes change with the brief’s viewport stance
5. Content rules (hierarchy, line length, truncation, capitalization)
6. Accessibility (min sizes, contrast, zoom)
7. Token table + Do / Don't

## Do / Don't

**Do:** Semantic roles; five properties per style; weight + size specimens per family; realistic copy; brand vs UI split.

**Don't:** `font-12` ladders; every weight the file offers; tokens for one-off screens; product type on the whole page chrome/prose (docs fonts for handbook text).
