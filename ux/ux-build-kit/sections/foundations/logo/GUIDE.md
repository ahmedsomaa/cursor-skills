# Logo

## Produce

Follow [PROCESS.md](PROCESS.md) to create the mark and assets. Decide source: **custom** or **icon library**.

- Explain the idea in plain language (metaphor, why it fits).
- Library mark: name the set and icon; link to the set page; no local download unless you added custom typography/wordmark assets.
- Custom (or library + custom wordmark): write SVG/PNG variants; product colors, never default black/`currentColor`.
- `system.json` `logo`: source, idea, colors (name + hex), fonts if text, link if library.

## Represent

Brand-guideline page (`logo.html`):

1. What / Why — idea and inspiration in simple terms
2. Source — Custom, or Library name + icon + outbound link
3. In action — nav, favicon, app icon
4. Variants — primary / mono / reverse (or duotone), each on **fixed** light and dark surfaces
5. Clear space — diagram with exclusion zone
6. Minimum sizes — digital floors; icon-only fallback when needed
7. Incorrect usage — small don't grid (stretch, recolor, rotate, low contrast, busy bg)
8. Colors — same treatment as [color/GUIDE.md](../color/GUIDE.md): **semantic swatches** filled with the actual hex, labeled with role name + hex (logo ink roles from `system.json` `logo` colors). Not a text-only list.
9. **Downloads** — only when local assets exist: Theme (Light / Dark / Both), Variant, Size (16–512, SVG, All), live preview, **Download**. Library-only: set link, no download row.

## Do / Don't

**Do:** Plain-language idea; clear space; min sizes; fixed light/dark specimens; contrast-safe variants; logo colors as filled swatches (role + hex), like `color.html`.

**Don't:** Download UI for pure library links; black marks on dark; skip incorrect-usage examples; colors as a text-only hex list with no swatches.
