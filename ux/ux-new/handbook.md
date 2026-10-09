# Design handbook chrome

Fixed shell for every create HTML page. **Do not ask** for layout, fonts, or corner style. No catalog. **No Tailwind** — minified custom CSS only.

Look and feel: **minimal** Mintlify / Fumadocs density with Lime [anti-slop](https://design.how/systems/lime/foundations/anti-slop) restraint — dense left sidebar, zinc-only light/dark (no accent hue), hairline borders, wide content column, Lucide nav icons, sticky **ON THIS PAGE** TOC, raised-pill active states, ⌘K command palette. No gradients, blobs, glass, decorative glow, emoji, or tinted icon tiles in the shell. Finished product documentation, not a wireframe. Shell layout stays as specified below — do not regroup nav, add Design system subnav, or adopt a product layout. Never copy product branding into the shell.

## Fonts (fixed)

| Role | Family | Weight | Use |
| --- | --- | --- | --- |
| Body / UI | **General Sans** | `400` | Prose, nav labels, command trigger, TOC, muted chrome |
| Controls | **General Sans** | `500` | Preview/Code labels, interactive UI chrome |
| Titles | **General Sans** | `600` | Page `h1`, section `h2`/`h3`, sidebar system name |
| Mono | **Geist Mono** | `400` at **12px** (`0.75rem`) | Tokens, hex, CSS variables, code blocks |

Load General Sans from [Fontshare](https://www.fontshare.com/fonts/general-sans) (`400`, `500`, `600` only; `display=swap`). Load Geist Mono from Google Fonts, or the official Geist CDN if GF is unavailable. Do **not** load Extralight / Light / Bold. Drop Source Sans 3, Open Sans, Inter, Clash Grotesque, DM Sans, Inconsolata, and Tailwind from the shell.

Product UI inside design-system specimens and screen frames uses product fonts from `system.html` tokens — not the handbook pair — unless the product type is one of those families.

## Shared files (minified)

```text
<design>/handbook.css   — minified custom CSS (shell, palette, Preview/Code, theme)
<design>/handbook.js    — minified tiny kernel (theme persist + ⌘K palette only)
<design>/favicon.svg    — handbook favicon (see Document head)
```

Every create HTML page links both CSS/JS and the favicon. **Deliver minified** `handbook.css` and `handbook.js` in `design/` (author readable source in the session if needed, then write the minified artifacts pages link to). No separate unminified copies required. No Tailwind CDN or build.

## Document head (every HTML page)

In `<head>` on `index.html`, `brief.html`, `system.html`, and `screens.html`:

- `charset="utf-8"`
- `viewport` meta (`width=device-width, initial-scale=1`)
- `<title>` — `{Page} · {name} Design Handbook` (home: `{name} Design Handbook`)
- `meta name="description"` — one line from `look.json` `product` (or page-specific one-liner)
- `meta name="theme-color"` — `#ffffff` light default (optional second for dark not required)
- `link rel="icon"` → `favicon.svg` (and `apple-touch-icon` only if a PNG is also written)
- Fonts: General Sans (Fontshare) + Geist Mono as specified
- `link` to `handbook.css`; script `handbook.js` at end of `body` is fine
- `html` `lang` attribute (e.g. `en`)

**Favicon:** write `<design>/favicon.svg` — simple mark derived from the product logo when available, otherwise a geometric monogram from `look.json` `name` (1–2 letters) on zinc. Keep it readable at 16px. Same file for all pages.

**CSS-first.** Prefer HTML + CSS for almost everything. `handbook.js` only: open/close the command palette on ⌘K / Ctrl+K and trigger click, focus the palette input, filter palette results by query, sync theme to `localStorage` (key `design-handbook-theme`). Theme toggle switches handbook chrome and product frames together when a page has product UI — chrome colors stay the static handbook palette either way.

### CSS-first mechanisms

| Behavior | Mechanism |
| --- | --- |
| Theme visuals | CSS variables on `:root` / `[data-theme="dark"]` |
| Theme toggle | Checkbox or button + CSS sun/moon |
| Current nav | Static `aria-current="page"` in each HTML file — no JS |
| ON THIS PAGE | Static HTML links authored from that page’s headings — no JS builder |
| TOC in-view highlight | CSS scroll-driven (`animation-timeline: view()`) if practical; otherwise skip — no IntersectionObserver |
| Preview / Code | Radio inputs + CSS `:checked` siblings — **no JS** |
| Raised pills, layout, focus rings | Pure CSS |
| Palette open / filter + theme persist | Tiny JS only, then minify |

## Shell layout

Inner pages (Brief / Design system / Screens):

```text
┌──────────────────────────────────────────────────────────────────────┐
│  SIDEBAR (~260px)              │  MAIN (padded)     │  ON THIS PAGE  │
│  ┌──────────────────────────┐  │                    │  (sticky)      │
│  │ SystemName→home   [☀/☾]  │  │  <main>            │  padded top    │
│  │ Design Handbook          │  │                    │  h2 / h3 list  │
│  ├──────────────────────────┤  │                    │                │
│  │ [ Search handbook…  ⌘K ] │  │  ← opens command palette            │
│  │ ───────────────────────  │  │  ← hairline under trigger           │
│  │ 📄 Brief                 │  │                    │                │
│  │ 🎨 Design system         │  │                    │                │
│  │ ▦  Screens               │  │                    │                │
│  └──────────────────────────┘  │                    │                │
└──────────────────────────────────────────────────────────────────────┘
```

Home uses the same three-column shell (sidebar + main + **ON THIS PAGE**).

### Sidebar header

**Top left**

1. **System name** — from `look.json` `name`. General Sans `600`, ~15–16px. **Link to `index.html`** (home). Hover/focus zinc only.
2. Directly beneath: the words **Design Handbook** — muted, General Sans `400`, ~12px. Plain text; do not rename; not a link.

**Top right of the sidebar** (same row as the system name): icon-only **theme toggle**. Sun when dark is active (click → light), moon when light is active (click → dark). Lucide-style SVG. Accessible `aria-label`. Hover and focus-visible ring (zinc text/border — no colored accent). Do **not** put the theme toggle in the main column.

No logo required in the sidebar brand block (product logo lives in `system.html` / Brand).

### Command search (⌘K)

Not a sidebar filter field. A **command palette**.

1. **Sidebar trigger** — A button under the brand block that looks like a search field: label `Search handbook…` plus a quiet `⌘K` / `Ctrl K` hint. Click opens the palette. **Separator:** hairline under the trigger, before the nav links.
2. **Palette** — `<dialog class="handbook-cmd">` (or equivalent): centered, Elevated surface, Border, φ radius, soft shadow, scrim. Input at top; results below grouped as **Pages** then **On this page** (group label). Each result is a link (`brief.html` / `system.html` / `screens.html`, or `#heading-id` on the current page). Quiet empty state.
3. **Static results** — Author page links + current-page heading anchors into the dialog when generating each HTML file. No runtime heading scrape.
4. **Keyboard:** `⌘K` (macOS) / `Ctrl+K` (Windows/Linux) opens the palette and focuses the input. Escape / backdrop closes. Do not steal the shortcut when the user is typing in a content `input` / `textarea` other than the palette input.

### Navigation

Exactly **three** sidebar links. **No group labels, no children, no sub-nav** (including no Design system Foundations/Components children).

Each row is Lucide icon + label (inline SVG, same stroke weight). Active and inactive states use the **same raised-pill language** as Preview / Code (no colored tint):

- **Active:** Elevated surface, hairline border, soft drop shadow, φ radius, high-contrast Text icon + label — mark with `aria-current="page"` in the HTML for that page
- **Inactive:** muted zinc icon + label, transparent, no border or fill
- Do **not** tint the active nav item with any hue

| Link | Lucide icon | Target |
| --- | --- | --- |
| Brief | `file-text` | `brief.html` |
| Design system | `palette` | `system.html` |
| Screens | `panels-top-left` | `screens.html` |

Section headings and feature rows live only in the main column (and ON THIS PAGE / ⌘K). No Design system or Screens sidebar children.

### Home (`index.html`)

Real home page (not a redirect). **Includes ON THIS PAGE** — earn it with real sections (not a one-link rail).

Compact `h1`: `{name} Design Handbook`. Short lead under the title. Then these `h2` sections (ids for TOC):

| Section | id | Content |
| --- | --- | --- |
| Overview | `overview` | 2–3 sentences: what this handbook is for this product (from `look.json` `product` / brief). |
| Start here | `start-here` | Vertical stack of three **horizontal** icon+text cards (Brief / Design system / Screens). Max-width ~520–560px, **left-aligned** in main (TOC is on the right — do not center the whole main). Icons: `file-text` / `palette` / `panels-top-left`. Hairline Border at rest; raised-pill hover. Gap ~8–12px. |
| How to use | `how-to-use` | Numbered 3 steps: confirm Brief → confirm Design system → review Screens. One line each. |
| Status | `status` | One short line from `look.json` `status` + `pilotFeature` when present (e.g. “Current: kit · pilot inbox”). If status missing: “Current: not started — open Brief.” |

No filler widgets, stats strips, or promo cards. Prefer spacing between sections over extra dashed rules on home.

### ON THIS PAGE

**Every** handbook page (`index.html`, `brief.html`, `system.html`, `screens.html`) includes a sticky right **ON THIS PAGE** aside.

- Label (exact, **all uppercase**): **ON THIS PAGE** — muted, small size; letter-spacing OK
- **Static** links to that page’s `main` `h2` / `h3` (ids required) — written into the HTML; not built by JS
- Home TOC: Overview, Start here, How to use, Status
- Optional CSS scroll-driven “in view” highlight; otherwise leave unhighlighted
- **Top padding** on the rail (and its vertical separator) matches main title padding (`--handbook-pad`) — the rule must **not** start flush at the top of the content shell
- Same presence and width rhythm on all four pages

### Main content layout

- Same padding on every page: use a fixed token (e.g. `--handbook-pad: 2rem`) for main horizontal and vertical rhythm
- Content max-width **1000px** inside main (between ~960–1040px). Home Start-here cards stay ~520–560px wide inside that. Screens artboard may use the full width of that padded main region
- One `h1` per page in main
- **Compact titles** (General Sans `600`) — smallest fit; hierarchy from weight/spacing, not display sizes:
  - Page `h1` ≈ **22–24px**
  - Section `h2` ≈ **16–18px**
  - Subsection `h3` ≈ **14–15px**
  - Body ≈ **15–16px** / `400`
- **Category separators** (Design system major `h2` blocks; Screens feature rows): dashed or dotted horizontal rule using Border token — see step skills

## Segmented control (Preview / Code)

Shared pattern for Tokens, component Examples, and any other Preview vs Code surface. Implement with **radio inputs + CSS `:checked`** in `handbook.css` — **no JS**.

- **Track:** quiet muted background (Track token), φ radius
- **Active item:** raised pill — Elevated surface, hairline border, soft drop shadow, Text icon + label at weight `500`
- **Inactive:** muted icon + label, no fill
- Lucide icons beside labels (e.g. `eye` for Preview, `code-2` for Code)
- Accessible labeling on the radios; default to **Preview**; Code shows the CSS variables or markup snippet

## Semantic HTML

Every page uses landmarks — not a div-only outline:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>…</title>
  <meta name="description" content="…" />
  <meta name="theme-color" content="#ffffff" />
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <!-- fonts + handbook.css -->
</head>
<body>
  <div class="handbook"> <!-- layout shell only -->
    <aside class="handbook-sidebar">
      <header>…<a href="index.html">system name</a>, Design Handbook, theme toggle…</header>
      <!-- command trigger + separator -->
      <nav aria-label="Handbook">…three links with aria-current on this page…</nav>
    </aside>
    <main>…one h1, sections with h2/h3…</main>
    <aside aria-label="On this page">…ON THIS PAGE heading + static links…</aside>
    <dialog class="handbook-cmd">…Pages + on-this-page links…</dialog>
  </div>
  <script src="handbook.js"></script>
</body>
</html>
```

Use `<section>` for major blocks with heading ids. Tables for brief scope. Prefer lists and headings over unlabeled div stacks.

## Theme coloring (static — never from product)

Hardcode in minified `handbook.css`. Do **not** seed from Look, product primary, or `system.html`. **No accent color** — no blue, lime, or brand hue in the shell.

| Token | Light | Dark |
| --- | --- | --- |
| Sidebar | `#fafafa` | `#09090b` |
| Content | `#ffffff` | `#0c0c0e` |
| Elevated (active pills / dialog) | `#ffffff` | `#18181b` |
| Track (segmented) | `#f4f4f5` | `#27272a` |
| Border | `#e4e4e7` | `#27272a` |
| Text | `#09090b` | `#fafafa` |
| Muted text | `#71717a` | `#a1a1aa` |
| Focus ring | Text at ~2px outline (or Border + Text) | same idea on dark |
| Scrim (palette) | `rgb(9 9 11 / 0.4)` | `rgb(0 0 0 / 0.6)` |

In-content links: Text color + underline; hover may use weight `500`. Never introduce a hue token for chrome. Active sidebar nav and Preview / Code pills stay **neutral raised-pill**. Product specimens use product tokens inside frames only.

## Radius (golden ratio)

Shell controls use φ (`≈ 1.618`), distinct from product `--radius`:

```css
--handbook-radius: 10px;
--handbook-radius-sm: calc(var(--handbook-radius) / 1.618);
--handbook-radius-lg: calc(var(--handbook-radius) * 1.618);
```

Apply to command trigger, palette, nav pills, segmented control, theme toggle, TOC chrome.

## Premium bar

- General Sans `400` / `500` / `600`; Geist Mono 12px for code
- Minified custom CSS/JS; CSS-first; no Tailwind
- ⌘K command palette; **ON THIS PAGE** (uppercase) on every page
- Favicon + document meta on every page
- Hairline borders; soft elevation on sticky sidebar / TOC / active raised pills (neutral)
- Clear zinc focus rings; links underlined — no colored accent
- Home: Overview / Start here / How to use / Status; clickable site name; compact titles
- Anti-slop: space over nested cards; sentence case; Lucide in nav only; no DS sidebar subnav

## Pages that use the shell

| File | Content |
| --- | --- |
| `index.html` | Home — Overview, Start here, How to use, Status + ON THIS PAGE |
| `brief.html` | Spec sheet (Scope) + ON THIS PAGE |
| `system.html` | Design system (Brand, Foundations, Components, Tokens) — one page, no subnav |
| `screens.html` | Figma-style artboard |

Do not invent extra handbook pages. Product look stays inside specimens and frames; the shell stays General Sans / Geist Mono with the static zinc-only theme (no accent).
