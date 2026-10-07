# Logo process

Create the product mark. Draw an SVG, or pick one icon from Lucide, Hugeicons, Remix Icon, Font Awesome, or Devicon. Do not jump from the brief to a finished logo.

Used when `ux-build-kit` writes the logo section, or when `ux-step` / `ux-repair` runs kit → logo.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/brief.html` first. If it is missing, follow [ux-discover](../../../../ux-discover/SKILL.md). Read `<design>/docs.json` and `<design>/design-system/system.json` when they exist. Create `<design>/design-system/` if it is missing.

## Process

1. **Understand.** Product, audience, positioning, and where the mark appears: app icon, nav, favicon, docs, marketing.
2. **Research.** One pass at competitor marks and industry clichés to avoid.
3. **Explore.** Several different concepts: symbol, lettermark, wordmark, metaphor. Not twenty tweaks of one idea.
4. **Select.** Pick one direction for relevance, distinctiveness, simplicity, and scale at small sizes.
5. **Design.** Build the SVG, or choose the icon and adapt its fills and strokes to this product's logo colors (the same roles on `color.html`), never default black or unset `currentColor`. If the mark includes text, name the font.
6. **Validate.** Check large, small (16–24px), app-icon size, black and white, light background, and dark background.
7. **Systemize.** Colored (product colors), monochrome, and duotone variants.
8. **Deliver.** Write the assets and `logo.html`. Update `system.json` `logo` when that file exists.

## Deliver

```text
<design>/design-system/logo.html
<design>/design-system/logo/primary.svg
<design>/design-system/logo/primary.png
<design>/design-system/logo/monochrome.svg
<design>/design-system/logo/monochrome.png
<design>/design-system/logo/duotone.svg
<design>/design-system/logo/duotone.png
```

No PDF. For a custom mark, write the SVG and PNG files and offer downloads. For a library mark with no custom wordmark assets, show it on the page and link the set — no local download row. Library mark plus custom typography: local assets for the wordmark lockup may use the download controller.

## logo.html

Use the docs chrome from `docs.json` when it exists. Follow [GUIDE.md](GUIDE.md) for Produce / Represent / Do-Don't. The page answers What / Why / When / How / When not, then shows:

- Idea and inspiration in plain language
- Source: Custom, or library name + icon name + outbound link
- In action: nav, favicon, app-icon size
- Variants (primary / mono / reverse or duotone) on fixed light and dark surfaces; product colors, never default black
- Clear space diagram and minimum sizes
- Incorrect usage grid
- Colors with role name and hex; fonts when the mark includes text
- Downloads only when local assets exist: Theme (Light / Dark / Both), Variant, Size (16–512, SVG, All), live preview, **Download**

The `logo` string in `system.json` names source, idea, colors (with names and hex), fonts when relevant, and the set link when from a library.

Link `logo.html` from `<design>/design-system/index.html` when that index exists.

This step is done when `logo.html` and the assets exist, and someone can see the mark in action and download or open the set link.
