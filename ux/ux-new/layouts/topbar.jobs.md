# Topbar — page jobs

**Id:** `topbar` · **Fit:** Chakra-style docs: top navbar + horizontal category tabs + vertical subsection tabs. Example: Chakra UI docs.

**How to use:** Read this file once when building the handbook. **Do not** read all of [topbar.html](topbar.html). Open a single `#wf-*` in that HTML only if a checklist line is ambiguous. Ship a finished unique site — wireframes are IA/placement only.

## Chrome

- **Navbar:** name + “Design handbook” (left); centered Brief / Design system / feature names; theme (right).
- **Horizontal tabs** under the bar for the current main’s top-level children:
  - Design system → Foundations · Components · Patterns · Content · Accessibility
  - Feature → Storyboard · Designs
  - Brief → Overview
- **Vertical tabs** (left column) for the open category’s subsections (Foundations → Principles · Color · …; Components → Button · …; Designs → screen names). Right column = page title + body/specimen.
- Horizontal tabs stay on Design system **categories** — do not replace them with Foundations items.
- Docs chrome: text labels only. `docs.json` `style` on nav; tab underline 2px solid. Docs fonts = handbook default; product type only in UI samples, typography specimens, storyboards, screens.
- Theme control; persist `localStorage`.

Deep reference: [topbar.html#details](topbar.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Brief · Overview | `brief.html` | [#wf-brief](topbar.html#wf-brief) | Nav marks Brief; tab Overview; body = spec sheet (Meta → Problem → Who → Goals → Scope → Features→Screens → Constraints → Open questions). |
| Principles | `design-system/principles.html` | [#wf-f-principles](topbar.html#wf-f-principles) | H-tabs Foundations; V-tab Principles; looks like / refuses. Docs fonts. |
| Color | `design-system/color.html` | [#wf-f-color](topbar.html#wf-f-color) | Semantic swatches → usage → L/D → tokens. |
| Typography | `design-system/typography.html` | [#wf-f-typography](topbar.html#wf-f-typography) | Per family: weight variants with labels; roles with size·weight·lh·tracking → responsive / content / a11y → tokens. Specimens = product type; prose = docs fonts. |
| Spacing | `design-system/spacing.html` | [#wf-f-spacing](topbar.html#wf-f-spacing) | Scale bars → specimens → tokens. |
| Layout | `design-system/layout.html` | [#wf-f-layout](topbar.html#wf-f-layout) | Stance → widths/breakpoints → regions → skeletons. |
| Shape | `design-system/shape.html` | [#wf-f-shape](topbar.html#wf-f-shape) | Radius ramp → surfaces → borders → tokens. |
| Elevation | `design-system/elevation.html` | [#wf-f-elevation](topbar.html#wf-f-elevation) | Role cards L‖D → stack → tokens. |
| Icons | `design-system/icons.html` | [#wf-f-icons](topbar.html#wf-f-icons) | Style → inventory → sizes → downloads. Docs fonts for prose. |
| Motion | `design-system/motion.html` | [#wf-f-motion](topbar.html#wf-f-motion) | Duration/easing → demos → reduced-motion → Do/Don't. |
| Logo | `design-system/logo.html` | [#wf-f-logo](topbar.html#wf-f-logo) | Full logo page jobs (idea → downloads). |
| Themes | `design-system/themes.html` | [#wf-f-themes](topbar.html#wf-f-themes) | Same UI L‖D → stress → Do/Don't. Docs fonts for prose. |
| Components · Specimen | `components.html` | [#wf-c-button](topbar.html#wf-c-button) | H-tab Components; V-tabs per component; panel = specimen. |
| Patterns · Specimen | `patterns.html` | [#wf-p-destructive](topbar.html#wf-p-destructive) | V-list of patterns · panel specimen. Docs fonts for prose. |
| Content | `design-system/content.html` | [#wf-content](topbar.html#wf-content) | Terminology and labels. |
| Accessibility | `design-system/accessibility.html` | [#wf-a11y](topbar.html#wf-a11y) | Rule · good · bad. |
| Storyboard | `<feature>/storyboard.html` | [#wf-storyboard](topbar.html#wf-storyboard) | Nav marks feature; tabs Storyboard \| Designs; panels **16:9**; Mobile\|Web. |
| Designs hub | `<feature>/designs.html` | [#wf-designs](topbar.html#wf-designs) | Lists every hi-fi; Mobile\|Web. |
| Design screen | `<feature>/<screen>.html` | [#wf-design-screen](topbar.html#wf-design-screen) | V-tabs for screens under Designs; hi-fi + Mobile\|Web + state strip. |

## Index

Navbar always lists Brief, Design system, and every feature. Current main + tab + vertical tab marked.
