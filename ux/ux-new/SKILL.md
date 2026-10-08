---
name: ux-new
description: Create-pipeline orchestrator — discover, build kit, design UI — with step progress.
disable-model-invocation: true
---

# UX — New

You are the product designer for a developer who does not design in Figma. The work is HTML in a `design` directory.

The design system and the screens must be unique to this app. Color, type, shape, and layout come from this product and from inspiration gathered before the system is created. A default SaaS kit is not a finished design.

Layout guide wireframes under [layouts/](layouts/) define **IA, nav, and page jobs** — not the visual finish. Everything written into `design/` is a **real polished site**: typography, color, spacing, components, and the chosen Look applied. Do not ship dashed wireframe chrome, Inter wireframe scaffolding, or placeholder hatching.

Run the three steps in order. Read each step skill when you reach it, then follow it. Do not add steps. Do not write a document for a step beyond the files that step names.

1. [ux-discover](../ux-discover/SKILL.md)
2. [ux-build-kit](../ux-build-kit/SKILL.md)
3. [ux-design-ui](../ux-design-ui/SKILL.md)

## Status

Say the current state in the reply before starting it. When that work is done, say it is finished and name the next state. A question that waits on the user stays the current state until they answer.

1. Folder. Where `design` lives. Finished when the path is chosen.
2. Look. Tone, design system, or custom. Finished when `look.json` is written.
3. Docs template. Layout, then fonts + style. Finished when `docs.json` is written with fonts and style.
4. Brief. Finished when `brief.html` is the spec sheet (meta + platform, problem, who, goals, scope in/out, features→screens, constraints) per [ux-discover](../ux-discover/SKILL.md).
5. Design system. Finished when the user confirms the system. Waiting on confirm, remake, or change parts stays this state.
6. Screens. Finished when every feature has a storyboard and its screen pages, and the index links them.

## Designs directory

The folder is always named `design`. This is the Folder state. Say "Folder." before asking.

Before creating it, ask where in the current project it should live. Do not assume the repo root. Use the path they give for the rest of the run. If a `design` directory already exists, confirm that one instead of creating a second.

Say "Folder finished. Next is Look." when the path is chosen.

## Look

This is the Look state. Say "Look." before asking.

Product visual direction — **one** catalog path, not stacked asks. Tone and design system are mutually exclusive picks.

**Ask (three options only):** Tone, Design system, or Custom? Skim the product quickly (brief may not exist yet). Mark one recommendation in one line. Wait.

### Tone

1. Read [tones/catalog.md](../ux-build-kit/tones/catalog.md) and list **every** tone (id · name · fit). Do **not** read `tones/index.html` or every tone HTML for the pick.
2. Mark one recommendation again. Wait until they pick a tone id.
3. Open that tone’s HTML only (`tones/{id}.html`, 6+1 framework). Write `<design>/look.json` with `source`: `tone`, plus `id` and `name`.

When the kit is written later, invent machinery from the tone guide — **no** second catalog ask for a design system.

### Design system

1. Read [design-systems/catalog.md](../ux-build-kit/design-systems/catalog.md) and list **every** system (id · name · fit). Do **not** read `design-systems/index.html` or every system HTML for the pick.
2. Mark one recommendation again. Wait until they pick a system id.
3. Open that system’s HTML guide only (`design-systems/{id}.html`). Write `<design>/look.json` with `source`: `design-system`, plus `id` and `name`.

That system *is* the look. When writing the kit, derive climate into `system.json` `tone` from the guide’s philosophy / closest-tone pills.

### Custom

Ask whether **they will describe** the vibe or **the agent should cook** it. Wait.

- **They describe it.** Wait for one reply: overall feel, surfaces, density, ornament (and color/type/radius if they give them). Write `look.json` with `source`: `custom` and a **`description`** field holding those notes.
- **The agent cooks it.** Decide from the product skim in a few lines, optionally search once for references. Write `look.json` with `source`: `custom` and a **`description`** of the decision.

If `look.json` already exists, show the current choice and ask whether to **keep** it or **pick a new** Look before continuing.

Say "Look finished. Next is the docs template." when `look.json` is written.

## Docs chrome

This is the Docs template state. Say "Docs template." before asking.

After Look is finished, ask which docs layout. For the pick, read only the **Id / Fit** lines from each [layouts/*.jobs.md](layouts/) (or Name/Description in Details) — **do not** open the full wireframe HTML files. Show name + fit. Recommend gallery when the work is mostly screens, and sidebar when it is mostly the written system. Always offer custom.

- A catalog layout: after they choose, read **once** that layout’s `layouts/<id>.jobs.md` (chrome + page inventory). That file is the build bible. **Do not** read the full [sidebar.html](layouts/sidebar.html) / [gallery.html](layouts/gallery.html) / [topbar.html](layouts/topbar.html). Open a **single** `#wf-*` in the matching HTML only when a jobs checklist line is ambiguous. Wireframes are **structure only** (IA, placement, page jobs). **Do not implement the wireframes themselves** — no dashed borders, Inter wireframe scaffolding, or placeholder hatching in `design/`. Build a **finished handbook site** whose chrome **looks and feels like Look** (`look.json`): surfaces, density, radius character, and color climate from the chosen tone / design system / custom description — not a generic docs skin. Sidebar = left nav + column. Gallery = **no navbar**; home stacks Brief / Design system / Screens as card sections. Topbar = **navbar** + horizontal category tabs + vertical subsection tabs ([Chakra](https://chakra-ui.com/docs/get-started/installation)-style).
- After the layout is chosen (catalog or custom), drive handbook atmosphere from Look: open the one tone or design-system HTML named in `look.json`, or use `look.json` `description` when `source` is `custom`. Then **search once** for docs-site inspiration that fits that Look + layout id — Mobbin (Mobbin MCP), Figma Community, Dribbble, Behance, Pinterest, or a real design-system / docs site. Use what you find as a check, not as a copy. Carry that polish into index, brief, and design-system chrome.
- Custom docs chrome settings (only if they override fonts/colors beyond Look): ask whether they will describe the settings or the agent should cook them.
  - They describe it. Give this format and wait for one reply. Color: the vibe, or background, text, and action. Typography: the families, or how the type should feel. Radius: sharp, slight, or round. A monospace for code, token names, and file paths.
  - The agent cooks it. Decide docs chrome from Look first and write that decision in a few lines before any search. Then search once for references that match Look (same sources as above). Use what you find as a check, not as the design. Name the families and a monospace, and write the same flat fields.

After the layout is chosen (catalog or custom), ask **font pairing and Style in the same turn** (one reply covers both):

1. **Font pairing** for the documentation site. Open [typography.html](typography.html) and list every pairing (name, heading/body/mono, fit). Mark as recommendation a pairing that fits **both** the chosen layout id and Look (tone meta / DS suggested fonts when present). Custom is always last: user names Google Fonts for heading, body, and mono. Write the chosen families into `docs.json` `fonts`. For `geist-geist-mono`, if Geist cannot load from Google Fonts, use Inter and JetBrains Mono per that pairing’s Adapt.
2. **Style** for the docs chrome corners (not the product Foundations shape). Open [layouts/style.html](layouts/style.html) — Square / Squircle / Circle·Pill. Recommend the id that matches Look (tone radius meta / DS shape). Write the chosen id (`square` | `squircle` | `pill`) into `docs.json` `style`. Apply those radii to docs chrome (nav buttons, chips, cards, theme control).

Write `<design>/docs.json` with layout, `fonts`, `style`, and a **`look`** object copied from `look.json`:

- Catalog Look: `"look": { "source": "tone"|"design-system", "id": "…", "name": "…" }`
- Custom Look: `"look": { "source": "custom", "description": "…" }` — `description` required (from `look.json`); `id` / `name` optional

Every HTML page uses that layout and style, and links `docs.css`. Load the families named in `fonts` from [Google Fonts](https://fonts.google.com/) with a stylesheet link and `display=swap`.

**Selected docs fonts** (`docs.json` `fonts`) are the **handbook default** — chrome and body on every docs page, including design-system section prose (`principles.html`, `patterns.html`, `icons.html`, `themes.html`, and any other mostly-written guidance page). Monospace from `fonts` is for code, token names, and file paths in docs areas.

**Design-system typography** (`system.json` type roles) is used **only inside**:

- UI samples, component/pattern examples, and product frames embedded on handbook pages
- Typography foundation specimens on `typography.html` (the scale itself)
- Feature **storyboards** and **screens** (bodies, film panels, frames)

Site chrome (nav, tabs, crumbs, theme) always stays on docs fonts. Do not wrap whole principles / patterns / icons / themes bodies in product type.

Say "Docs template finished. Next is the brief." when `docs.json` includes template fields, `fonts`, `style`, and `look` (with `description` when `source` is `custom`).

Docs chrome is **text labels only** — no Lucide (or other) icons in nav, tabs, or section heads. Do not mix icon-nav with text-only nav. Product Foundations / screens may use Lucide when the kit defines icons.

Docs chrome is Tailwind utility classes. Product color, spacing, type, and elevation inside frames and subcategory specimens stay the custom properties from `system.json`.

Build `<design>/docs.css` with the Tailwind CLI, minified, scanning the HTML in `design`. Use that compressed file, not the Tailwind browser CDN. Write a temporary `<design>/.tailwind-input.css` that contains `@import "tailwindcss" source(".");`, run `npx @tailwindcss/cli -i .tailwind-input.css -o docs.css --minify` from the `design` folder, then delete the input file.

## Index

`<design>/index.html` is the navigation for every design file. Keep it updated whenever a file is added. The navigation itself always includes each feature from the brief, with that feature's storyboard and screens under it.

It links three main groups:

- Brief → Overview
- Design system → category pages (subcategories on the category page, not in the sidebar)
- Screens → each feature → Storyboard, Designs

The folder is HTML, plus `docs.css`, `docs.json`, `look.json`, and `system.json` in `design-system/`.

```text
<chosen-path>/design/index.html
<chosen-path>/design/look.json
<chosen-path>/design/docs.json
<chosen-path>/design/docs.css
<chosen-path>/design/brief.html
<chosen-path>/design/design-system/system.json
<chosen-path>/design/design-system/index.html
<chosen-path>/design/design-system/principles.html
<chosen-path>/design/design-system/color.html
<chosen-path>/design/design-system/typography.html
<chosen-path>/design/design-system/spacing.html
<chosen-path>/design/design-system/layout.html
<chosen-path>/design/design-system/shape.html
<chosen-path>/design/design-system/elevation.html
<chosen-path>/design/design-system/icons.html
<chosen-path>/design/design-system/motion.html
<chosen-path>/design/design-system/logo.html
<chosen-path>/design/design-system/logo/primary.svg
<chosen-path>/design/design-system/themes.html
<chosen-path>/design/design-system/components.html
<chosen-path>/design/design-system/patterns.html
<chosen-path>/design/design-system/content.html
<chosen-path>/design/design-system/accessibility.html
<chosen-path>/design/<feature>/storyboard.html
<chosen-path>/design/<feature>/<screen>.html
```

## Folder

The `design` folder is a polished site, not a dump of files. The chrome comes from `docs.json`. Product UI comes from Look + `system.json`.

- Navigation, layout, and docs chrome type match `docs.json`. Handbook chrome **matches Look** (`docs.json.look` / `look.json`). The current page is marked. The index navigation always lists every feature.
- Docs fonts are the handbook default (including principles, patterns, icons, themes prose). Design-system typography only inside UI samples, typography specimens, storyboards, and screens.
- Light and dark cover the docs chrome and the product. Product themes live in `design-system/color.html` as custom properties, and every other page repeats that block. One theme control on every page switches both the Tailwind docs shell and the product frames together. Persist the choice in `localStorage` so every page opens on the same theme.
- `design-system/index.html` links every design-system section, grouped by layer (Foundations, Components, Patterns, Content, Accessibility). Every screen case is shown in both themes.
- Every page links `docs.css`.
- Specimens and screens are finished UI with the chosen tone/system — not wireframe clones of the agent guides. The handbook shell itself is a unique inspired site following layout wireframes for placement only.

If navigation, type, or themes are still rough when the screens exist, use [ux-repair](../ux-repair/SKILL.md) and describe the problem (rules in [chrome.md](chrome.md) and [docs-site.md](docs-site.md)).

The run is done when the index links the brief, the design system, and every feature's storyboard and screens, `look.json` and `docs.json.look` match, handbook chrome feels like Look, `docs.css` is the minified Tailwind build, `system.json` is this product's filled record, and the folder is HTML except for `look.json`, `docs.json`, `docs.css`, and `design-system/system.json`. Say "Screens finished."

Shared substep menus for single commands live in [menus.json](menus.json). Planned skills: [ROADMAP.md](ROADMAP.md).
