# Docs chrome rules

Former polish rules. Used when step is `kit` and substep is `chrome`, or when `ux-repair` / `ux-critique` targets chrome.

Bring the `design` folder up to a finished docs-shell standard. Do not redesign the product.

## Prerequisites

Read `<design>/brief.html`, `<design>/docs.json`, `<design>/design-system/system.json`, and `<design>/design-system/index.html`. If `docs.json` is missing, ask using [docs-templates/index.json](docs-templates/index.json) the way [ux-new](SKILL.md) does, including custom, and write it before editing pages. Keep the product's visual language. If the design system has no dark theme, add one that still belongs to this product. `docs.json`, `docs.css`, and `system.json` stay. Fold any other non-HTML file into the HTML pages. Color, spacing, type size, and shadow inside product frames are the roles named in `system.json`.

## Navigation

Every HTML page uses the layout and nav from `docs.json`. The index navigation always includes every feature. The current page is marked. A page deep in a feature can get back to the index and to its feature.

## Typography

Docs type follows the `typography` and `fonts` fields in `docs.json`. Load those families from Google Fonts. Hierarchy is visible from size and weight. Code, token names, and file paths use the monospace named there. Docs icons are the Lucide names in `icons`. Product frames keep the type from the design system's `<style>` block.

## Themes

The docs chrome is Tailwind classes and links `docs.css`. Rebuild `docs.css` the way [ux-new](SKILL.md) builds it when the classes change. Product themes stay in each page's `<style>` block. Light and dark values match the design system page.

- One theme control on every page switches the docs chrome and the product frames together. Persist the choice in `localStorage` so every page opens on the same theme.
- `design-system/index.html` links every section page. Components and themes show both light and dark.
- Every screen case is visible in both themes.
- Both themes look like this product.

## Done

The folder reads as one site. Index, system, storyboards, and screens share navigation, typography, and light and dark themes. The product designs are unchanged except where a missing theme or a broken link had to be fixed.
