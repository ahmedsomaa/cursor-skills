---
name: ux-design-ui
description: Create design/screens.html — one Figma-style artboard of high-fidelity screens and critical states.
disable-model-invocation: true
---

# UX — Design UI

These are the Figma files, in one handbook page. Every screen for every feature, using the design system — the same discipline as [figma-generate-design](https://www.figma.com/): **compose from the system**, do not draw primitives with hardcoded values.

This is the Screens state. Say "Screens." before writing. Set `look.json` `status` to `screens` when you start; set `done` when finished.

## Designs directory

The folder is always named `design`. If this session has not chosen where it lives, ask where in the current project to put it. Do not assume the repo root. If a `design` directory already exists, confirm that one instead of creating a second.

Read `<design>/look.json` and `<design>/system.html` first.

- If `look.json` is missing `description` or `logo`, follow Round 1 in [ux-new](../ux-new/SKILL.md).
- If scope or handbook / `brief.html` is missing, follow [ux-discover](../ux-discover/SKILL.md).
- If `system.html` is missing, follow [ux-build-kit](../ux-build-kit/SKILL.md) and wait for confirm before writing screens.

## Before writing frames (Step 1 — understand)

For each screen you will ship (start with `pilotFeature`):

1. List **major sections** of the view (e.g. Header / Nav, Content, Form, Action bar, Footer; for a modal: Title, Body, Actions).
2. For each section, list **controls** that `system.html` Components already documents (button, input, …). Prefer those patterns — same tokens, same visual language — over inventing new chrome.
3. Note **images** (avatars, product photos, empty-state art). Use real or believable assets; do not leave blank image boxes. Prefer inline SVG from the **Foundations Icons** library chosen in `system.html` (must be one from [Icon libraries](https://design.how/directory/icon-libraries)) over reconstructing icons from rotated divs.
4. Read Look + Tokens from `system.html` — you will bind every fill, type, space, radius, and shadow to those CSS variables.

**Never hardcode** hex colors, ad-hoc px spacing, or one-off radii when a system variable exists. Copy the product `<style>` custom properties from `system.html` into `screens.html` (keep them in sync).

## Write — pilot first, then the rest

Create `<design>/screens.html` as a **handbook page** using [handbook.md](../ux-new/handbook.md). Link minified `handbook.css` and `handbook.js`. Include sticky **ON THIS PAGE** (uppercase, static links, top-padded rail), document head meta + favicon, and a ⌘K palette entry list for this page’s feature headings. Main may use the full padded content width for the artboard (~1000px content max, or full main pane inside the same padding).

Sidebar stays three Lucide links only: Brief, Design system, Screens → `screens.html`. No per-feature sidebar items. Refresh `index.html` if needed.

No per-feature folders, no separate storyboard pages.

### Order (section-by-section, like Figma generate-design)

1. **Scaffold the artboard** — feature row headings + empty frame shells (name + state labels) for `pilotFeature` first. Placeholders are fine for one pass.
2. **Fill one screen at a time** — build that frame’s sections in order (header → content → actions). Land finished HTML in the file before starting the next screen.
3. **Validate that screen** (see Done checks) before moving on — especially the pilot.
4. Then remaining features (same file). Use a subagent per feature **only** when 3+ features remain and the host supports it.
5. Light rendered checks on the rest: regressions only.

### What to build vs reuse from the system

| Build in the frame | Reuse from `system.html` |
| --- | --- |
| Frame chrome (device/desktop shell, artboard label) | Color / type / radius / spacing / elevation **variables** |
| Section layout structure (rows, columns, stacks) | Pilot **component** look (button, input, …) — same sizes, radii, states |
| Page composition unique to this screen | Logo treatments from Brand |
| | Icon library named in Foundations |

Manual one-off styles are the exception. If a control is missing from Components, either use Tokens only and keep it minimal, or note it in the kit coverage gap — do not invent a second visual language.

### Artboard

Neutral artboard background inside the main column (distinct from product UI). Product frames use the **same CSS custom properties** as `system.html`. Handbook theme toggle switches chrome and product frames together.

**Features as rows.** For each feature in `look.json` `features` (pilot first):

1. A row heading (`h2` or `h3`) with `id="<feature-id>"` for ON THIS PAGE / ⌘K — not sidebar.
2. A horizontal strip of frames for that feature’s screens (and their states).
3. Between feature blocks: a **dashed or dotted** horizontal rule (handbook Border token) — same language as Design system `h2` separators.

**Frames.** Above each frame: screen name and state (e.g. `Inbox · Default`). Size the wrapper from platform (like Figma wrapper widths):

- **Default** is always shown.
- **Loading, empty, error, success** (or disabled) are sibling frames only when that screen really has that state.
- **Platform** from `look.json`:
  - `mobile-first` — phone frames (≈9:16)
  - `website-first` — desktop frames (≈16:9; ~1280–1440 CSS px wide content when it fits the artboard)
  - `both` — show phone and desktop for each default (states may match the primary platform if space is tight; prefer both for the default state)

Inside: finished product UI — real labels, density, Look from `look.json`, tokens from `system.html`, logo where nav/branding appears. Prefer **auto-layout-like** CSS (flex/grid + gap/padding from spacing tokens), not absolute-positioned stacks.

Every color, space, type, radius, and shadow on a frame is one of the system variables. A generic admin layout or “Title / Button” placeholder copy is not a finished screen.

### What each screen shows

Only what this screen actually has:

- Navigation, header, content structure, primary and secondary actions (one clear primary per view when Anti-slop applies)
- Production-like labels, data, names, dates, and statuses — override any lorem / “Title” / “Button” placeholders
- The interactions this screen uses (forms, tabs, filters, modal, drawer, menu) — use the correct **variant** (e.g. primary vs secondary) matching Look and kit Examples
- Critical states as separate frames when they differ
- Focus, labels, and error identification visible in the frame when relevant
- Icons: inline SVG from the kit-chosen [directory](https://design.how/directory/icon-libraries) library at the slot size (16/20/24) — not emoji, not hand-drawn geometry

A note under a frame appears only when the behavior cannot be seen in the UI.

## Done — validate like Figma screenshots

Before finishing, spot-check **each pilot frame** (and spot-check the rest) for:

- Clear hierarchy; no overlapping or clipped text (line-height / overflow)
- Readable contrast on real token pairs
- No leftover placeholder strings (“Title”, “Heading”, “Button”, “Lorem”)
- Correct control variants (primary vs muted, etc.)
- Critical states shown when real; adequate tap/click targets
- Images/avatars not blank; icons sized to their slots
- Variables still match `system.html` (no drift)

Fix obvious misses — thoroughly on the pilot, lightly on the rest. Prefer opening the page / taking a visual pass over trusting markup alone.

This step is done when `screens.html` uses the handbook shell (including ON THIS PAGE + ⌘K entries + favicon/meta), includes every feature and screen from `look.json` (pilot first), dashed/dotted separators between feature rows, default frames for each, critical-state frames where real, platform framing matches `look.json`, frames are composed from system tokens/components (not hardcoded chrome), logo appears where branding belongs, and the sidebar still has only the three top-level links. Say "Screens finished." Set `look.json` `status` to `done`.
