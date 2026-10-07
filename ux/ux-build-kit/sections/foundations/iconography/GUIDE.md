# Iconography

## Produce

One icon language: a set (Lucide, Hugeicons, etc.) or a small custom set.

- Inventory only icons the app uses. Optical sizes (16 / 20 / 24). Color via icon color roles.
- Custom: local SVG/PNG. Set: name set + each icon; downloads are outbound links.
- `system.json` `icons`: style, sizes, inventory, source.

## Represent

Lucide-style documentation ([example](https://lucide.dev/icons/plus)):

1. What / Why / When
2. Style rules (stroke/fill, default size, color roles)
3. **Detail** — large preview, icon name, usage tags
4. **Inventory grid** — every product icon labeled
5. Sizes row
6. **Downloads**
   - **Set icons:** link to the icon’s page on the set site (no local download).
   - **Custom icons only:** controller for **color**, **size** (and stroke when stroke-based), then **Download SVG** and **Download PNG**; live preview updates with the controls. Combobox of icons + All when exporting many.

## Do / Don't

**Do:** Match Lucide’s clarity (big preview, name, tags); limit inventory to real use; customizer only for custom assets.

**Don't:** Local download for unmodified set icons; one-off icon colors; invent icons the screens never need.
