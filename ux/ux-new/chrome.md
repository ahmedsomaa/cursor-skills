# Docs chrome rules

Former polish rules. Used when repairing or stepping the docs site chrome (`ux-repair` from context, or `ux-step` / `ux-critique` docs → chrome). Site-wide shell only — see also [docs-site.md](docs-site.md) for template, brief, and index.

Bring the `design` folder up to a finished docs-shell that **looks and feels like Look** (`docs.json.look` / `look.json`) — surfaces, density, and climate from the chosen tone, design system, or custom description. Read `layouts/<id>.jobs.md` (from `docs.json`) for chrome rules — **do not** read the full layout HTML. Wireframes guide placement and page jobs only — do not ship dashed Inter wireframe chrome. If the shell is bland, wireframe-like, or clashes with Look, restyle to match Look; search once for docs-site inspiration that fits Look if needed. Do not redesign the product UI inside frames.

## Prerequisites

Read `<design>/look.json`, `<design>/brief.html`, `<design>/docs.json`, `<design>/design-system/system.json`, and `<design>/design-system/index.html`. Ensure `docs.json.look` matches `look.json` (copy if missing; custom requires `description`). If `docs.json` is missing, ask using [layouts/](layouts/) the way [ux-new](SKILL.md) does, including custom, and write it before editing pages. Keep the product's visual language. If the design system has no dark theme, add one that still belongs to this product. `docs.json`, `docs.css`, and `system.json` stay. Fold any other non-HTML file into the HTML pages. Color, spacing, type size, and shadow inside product frames are the roles named in `system.json`.

## Navigation

Every HTML page uses the layout and nav from `docs.json`. The index navigation always includes every feature. The current page is marked. A page deep in a feature can get back to the index and to its feature.

## Typography

Selected docs fonts (`docs.json` `fonts`) are the **handbook default** — chrome and body on every page, including principles, patterns, icons, themes, and other written guidance. Load those families from Google Fonts. Hierarchy is visible from size and weight. Code, token names, and file paths in docs areas use the monospace named there. Docs chrome is text labels only — no nav icons.

Design-system typography from `system.json` is used **only inside** UI samples / product frames, typography foundation specimens, storyboards, and screens. Do not apply product type to whole principles / patterns / icons / themes bodies.

## Themes

The docs chrome is Tailwind classes and links `docs.css`. Rebuild `docs.css` the way [ux-new](SKILL.md) builds it when the classes change. Product themes stay in each page's `<style>` block. Light and dark values match the design system page.

- One theme control on every page switches the docs chrome and the product frames together. Persist the choice in `localStorage` so every page opens on the same theme.
- `design-system/index.html` links every section page. Components and themes show both light and dark.
- Every screen case is visible in both themes.
- Both themes look like this product.

## Done

The folder reads as one site. Index, system, storyboards, and screens share navigation, typography, and light and dark themes. The product designs are unchanged except where a missing theme or a broken link had to be fixed.
