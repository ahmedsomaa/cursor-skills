---
name: ux-build-kit
description: Write design/system.html from look.json — brand, foundations, components, tokens.
disable-model-invocation: true
---

# UX — Build kit

Design a visual system that fits this app and would look wrong on a different product. Deliver it as one handbook page. Make system-level decisions — do not only document tokens.

Document the **product** system in a Lime-like way ([Lime](https://design.how/systems/lime)): purpose-named foundations, live specimens first, short Don’t/Do — not Lime’s warm chrome or multi-route sidebar.

This is the Design system state. Say "Design system." before writing (or before Look if `look.json` is missing). Set `look.json` `status` to `kit` when you start writing.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/look.json` first.

- If `look.json` is missing `description` or `logo`, run Round 1 in [ux-new](../ux-new/SKILL.md) and finish those fields before continuing.
- If `name`, `platform`, `features`, or `pilotFeature` is missing, or the handbook shell / `brief.html` is missing, follow [ux-discover](../ux-discover/SKILL.md) before designing.

## Look

Visual system and logo intent were decided in Round 1. If `description` and `logo` are present, **skip re-asking** — use them and go to Write.

If they chose Remake, re-run Round 1 in [ux-new](../ux-new/SKILL.md) (visual system + logo), then Write.

Execute Brand / logo from `look.json` `logo` (`user` notes/assets vs `cook` concept). Search once for UI inspiration when cooking or remaking if `description` needs a fresh check.

**Do not invent** colors, typefaces, or shadows that Look’s `description` does not imply. Token roles are named by purpose. A copied screen, and a system that could ship on any other app, are both unfinished.

## Write

Create `<design>/system.html` as a **handbook page** using [handbook.md](../ux-new/handbook.md). Link minified `handbook.css` and `handbook.js`.

**No Design system sidebar subnav.** Sidebar **Design system** is a single link to this page. Foundations and components are reached via **ON THIS PAGE** + the ⌘K palette only — do not add Foundations/Components children under Design system.

Major sections use `h2`; subsections use `h3` with ids so **ON THIS PAGE** and the command palette list them. Author static ON THIS PAGE links and palette heading entries for this page. TOC rail top padding matches main title padding. Include document head meta + `favicon.svg` per [handbook.md](../ux-new/handbook.md).

Do **not** recolor `handbook.css` from product primary — the shell stays the static zinc theme. No Tailwind. No multi-page foundations site. No `system.json`.

**Fonts:** Handbook General Sans / Geist Mono for page chrome and all explanatory copy (`h1`/`h2`/`h3`, prose, Usage Don’t/Do). **Product fonts** only inside Brand logo wordmarks (when type is part of the mark), Foundations Typography specimens, component Examples Preview, and Tokens Preview specimens — never restyle the whole `system.html` page in product type. Product color/space/radius/elevation tokens apply inside specimen frames only.

**Separators:** Between major categories (**Brand / Foundations / Components / Tokens**), a **dashed or dotted** horizontal rule (handbook Border token). Prefer rules between `h2` categories — do not line every Foundations `h3`.

Write **Brand + Foundations + Tokens** in one pass — no mid-write asks. Do not block Confirm on polishing every foundation specimen twice.

### Major sections (main column), in order

#### 1. Brand (`h2`)

- **Guidelines** — short brand rules: idea of the mark, where it appears, a few do / don’t lines.
- **Logo** — variants **colored**, **monochrome**, and **duotone**, each on light and dark surfaces, plus once in nav or app-icon context.
- **Downloads / source**
  - **Custom mark:** write assets under `design/logo/` (SVG and PNG for each variant as needed) and expose download controls on the page.
  - **Library mark:** adapt fills/strokes to product colors; link the public icon set / icon page — no fake local download set.

#### 2. Foundations (`h2`)

Each Foundations item is an `h3` with an id. Pattern: short purpose line, then **live specimens** (not a prose essay). Order:

##### Color

- Purpose-named roles (product tokens), e.g. `background`, `foreground`, `card`, `primary`, `secondary`, `muted`, `accent`, `destructive`, `border`, `ring` — same names in light and dark.
- Each role: **large swatch**, role name, hex, CSS variable, **one-line job** (“where it goes”).
- Show light‖dark pair (or theme-switch specimens). No flat hex dump. Contrast must hold for text-on-surface pairs the product uses.

##### Typography

- Section title is **Typography** (not Type). Roles: display/heading, body, caption, mono.
- **Source:** fuse families from **[Google Fonts](https://fonts.google.com)** and/or **[Fontshare](https://www.fontshare.com)** only. Same source or mixed (e.g. Fontshare display + Google body). No Adobe Fonts, no system-only stack as the named product face, no random CDN orphans.
- Per role: family name, weight (prefer `400` / `500` / `600` when the face supports it), size, line-height, live specimen string.
- Load with `display=swap` via Fontshare CSS and/or Google Fonts `<link>` in `system.html` specimens.
- Note tracking only when the Look needs it. No fake marketing headlines.

##### Spacing

- Compact or comfortable scale the screens actually use.
- Show steps as a **visual ladder** (bars or inset blocks) with token names + px/rem — not a bullet list alone.

##### Radius

- One base `--radius`; smaller / larger steps. Prefer φ-related steps from the base when Look allows (`/ 1.618` and `* 1.618`).
- Specimen: same box at each step.

##### Elevation

- `rest`, `raised`, `overlay` with distinct light and dark shadows (never naive invert).
- Specimens on a card and an overlay surface. `sunken` only if the product uses it.

##### Icons

- Recommend **exactly one** library from [Icon libraries](https://design.how/directory/icon-libraries): Bootstrap Icons, Carbon, Fluent UI System Icons, Font Awesome Free, Heroicons, Hugeicons, Iconify, Iconoir, Ionicons, Lucide, Material Symbols, MingCute, Octicons, Phosphor, Radix Icons, Simple Icons, Tabler Icons.
- **Default: Lucide** unless Look clearly implies another set on that list. One-line rationale + outbound link to the set.
- Small specimen row in product colors — icons as UI, not tinted decorative tiles ([anti-slop](https://design.how/systems/lime/foundations/anti-slop)).

##### Anti-slop

- Short Don’t / Do table for **this product** (Look + [Lime anti-slop](https://design.how/systems/lime/foundations/anti-slop) habits): no nested cards, no emoji, sentence case, one primary action per view, believable copy/data, space over chrome.
- Not a paste of Lime’s warm/glow rules into the product.

#### 3. Components (`h2`) — pilot first

Inventory only controls the **`pilotFeature`** needs (button, input, …). Keep the set small. Do **not** invent a full component catalog for every feature.

At the top of Components, add a one-line **coverage gap**: which components are deferred until screens prove the need (e.g. “Later: date picker, data table”). Optional later pass: `ux-step` → components expands after screens.

For **each** pilot component, **examples first** (Lime bias — show the real control before long prose):

1. **Description** — one line: what it is for
2. **Examples** — live specimen with handbook **Preview | Code** (CSS radios per [handbook.md](../ux-new/handbook.md)); Preview default; Code shows markup or token usage
3. **Variants / States** — named variants and default/hover/focus/disabled (and real error/loading) shown in the example row when possible
4. **Anatomy** — parts only if needed
5. **Usage rules** — Don’t / Do pairs; mark gaps instead of inventing behavior Look does not imply

#### 4. Tokens (`h2`)

Use **Preview | Code** (CSS radios):

- **Preview** — compact specimen of the token set (color chips, type, radius, shadows)
- **Code** — copy-paste CSS variables block (light + dark) for engineering: color roles, type, radius, spacing steps used, elevation shadows, font families (real GF/Fontshare names) plus the `@import` / `<link>` sources used

List one-off exceptions under Tokens when a value is not a shared role.

Inline a product `<style>` (or scoped block) with CSS custom properties for light and dark used by specimens. The handbook theme toggle switches handbook chrome and product specimen themes together; chrome palette stays static.

### Logo process

Follow `look.json` `logo` — do not re-open the user-vs-cook ask unless Remake.

- **`mode: user`:** Honor their notes, file paths, or library + icon. Adapt to product colors; if they pointed at a library icon, treat as library mark (link the set). If they provided or described a custom mark, produce variants and downloads.
- **`mode: cook`:** Invent from `logo.notes` + product + visual system. Draw an SVG, or pick one icon from the [Icon libraries](https://design.how/directory/icon-libraries) list (prefer the Foundations Icons choice) and adapt fills/strokes — never default black or unset `currentColor`.

Then:

1. **Avoid the cliché.** One pass at competitor marks to refuse.
2. **Design.** Colored, monochrome, and duotone treatments. If the mark includes text, name the font.
3. **Validate.** Readable large and at ~24px; works on light and dark.
4. **Deliver.**
   - Custom: `design/logo/` assets + downloads on Brand; inline previews on the page.
   - Library: inline preview + link to the set / icon; no pretend download zip.

## Confirm

When `system.html` exists, say "Design system ready." Point them at `<design>/system.html`. Ask **once**:

1. **Confirm.** Keep this system. Say "Design system finished. Next is the screens."
2. **Remake.** Re-run Round 1 (rewrite `look.json` `description` + `logo`), then Write again, then ask again.
3. **Change parts.** Ask which: Brand, Foundations (which subsection), Components, or Tokens. Update only those parts. Ask again until they confirm.

**Gates with defaults:** unanswered Change parts **defaults to keep** the current section — do not stall waiting on naming. Do not block Confirm on polishing every foundation specimen twice.

Do not start [ux-design-ui](../ux-design-ui/SKILL.md) until they confirm.

This step is done when they confirm; `system.html` uses the handbook shell with Brand, Foundations (including Anti-slop), pilot Components (examples-first, plus coverage-gap line), and Tokens; dashed/dotted separators between `h2` categories; handbook fonts on chrome/copy and product fonts only in specimens; no DS sidebar subnav; color cards and Typography specimens are complete; Preview/Code uses CSS radios; logo has three variants with downloads or a library link; an icon library is named; both product themes feel like this product; and the system would look wrong on a different app.
