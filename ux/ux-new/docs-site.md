# Documentation site rules

Used when repairing or stepping the main documentation site (`ux-repair` from context, or `ux-critique` / `ux-step` docs substeps).

Bring the site shell up to a **finished handbook that looks and feels like Look** (`docs.json.look` / `look.json`) — not a clone of the agent-guide wireframes and not a generic docs skin. Use `layouts/<id>.jobs.md` for chrome and page jobs; open a single `#wf-*` only when needed — **do not** dump the full layout HTML. Wireframes are guidelines for IA and element placement only; ship real Tailwind chrome, docs fonts, and style radii. When the shell looks generic, wireframe-like, or clashes with Look, restyle to match Look and search once for docs-site inspiration that fits Look + layout. Do not redesign product Foundations specimens or feature screens except for shared chrome (nav, theme control, docs fonts, links).

## Prerequisites

Read `<design>/look.json`, `<design>/docs.json`, `<design>/brief.html`, and `<design>/index.html` when they exist. Read `layouts/<id>.jobs.md` for the layout id in `docs.json`. If `docs.json` is missing, follow Docs template in [SKILL.md](SKILL.md) (layout, then fonts + style, including custom) and write it before editing pages. Rebuild `docs.css` the way [SKILL.md](SKILL.md) builds it when docs chrome classes change. `docs.json`, `docs.css`, and `look.json` stay. Fold any other non-HTML file into the HTML pages except `design-system/system.json`.

## Template (`template`)

`docs.json` must include layout id (or custom fields), `fonts` (heading / body / mono), `style` (`square` | `squircle` | `pill`), and **`look`** copied from `look.json` (`source` + `id`/`name` for catalog; `description` required when `source` is `custom`). Every HTML page uses that layout and style, links `docs.css`, and loads the Google Fonts families named in `fonts` with `display=swap`. Apply `style` radii to docs chrome (nav buttons, chips, cards, theme control). Docs chrome is **text labels only** — no Lucide or other icons in nav, tabs, or section heads. Handbook atmosphere must match `look`.

## Brief (`brief`)

`<design>/brief.html` matches [ux-discover](../ux-discover/SKILL.md): finished docs page (not a wireframe clone), blocks in order (meta + platform, problem, who, goals, scope, features→screens, constraints). Uses docs fonts and chrome from `docs.json`.

## Index (`index`)

`<design>/index.html` is the navigation for every design file. Three main groups:

- Brief → Overview
- Design system → category pages (subcategories on the category page, not duplicated as required sidebar leaves unless the chosen layout says so)
- Screens → each feature → Storyboard, Designs

The index always lists every feature from the brief. Current page is marked. Deep pages can reach the index and their feature. Keep links current whenever files are added.

## Chrome (`chrome`)

Site-wide shell: layout, nav, docs type, light/dark theme control. Follow [chrome.md](chrome.md) in full. Chrome feels like `docs.json.look`. Docs fonts are the handbook default (including principles, patterns, icons, themes prose). Design-system typography only inside UI samples, typography specimens, storyboards, and screens. One theme control on every page; persist in `localStorage`.

## Done

The documentation site reads as one polished shell that matches Look. Index, brief, design-system entry, storyboards, and screens share navigation, docs typography, style radii, and themes. Product designs are unchanged except where a missing theme, broken link, or shared chrome fix was required.
