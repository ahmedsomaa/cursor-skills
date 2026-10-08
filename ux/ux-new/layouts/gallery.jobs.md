# Gallery — page jobs

**Id:** `gallery` · **Fit:** Screen-heavy work; card/tile home (no navbar). Example: Mantine UI gallery.

**How to use:** Read this file once when building the handbook. **Do not** read all of [gallery.html](gallery.html). Open a single `#wf-*` in that HTML only if a checklist line is ambiguous. Ship a finished unique site — wireframes are IA/placement only.

## Chrome

- **No navbar / main-nav strip.**
- Header: one row — title + “Design handbook” (long column) ‖ theme toggle (small column).
- Home (`index.html`): three **page sections** — Brief, Design system, Screens — each with heading + **card grid** for subsections.
- Nested pages: optional crumb + page title; still no navbar.
- Path: Design system cards → Foundations subcategory cards → specimen; Screens cards → feature → Storyboard / Designs → screen + states.
- Docs chrome: text labels only. `docs.json` `style` on cards/theme. Docs fonts = handbook default; product type only in UI samples, typography specimens, storyboards, screens.
- Theme control; persist `localStorage`.

Deep reference: [gallery.html#details](gallery.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Home · index | `index.html` | [#wf-home](gallery.html#wf-home) | Header then Brief / Design system / Screens sections; cards = subsections. |
| Brief · Overview | `brief.html` | [#wf-brief](gallery.html#wf-brief) | Spec sheet: Meta → Problem → Who → Goals → Scope In‖Out → Features→Screens → Constraints → Open questions (optional). No navbar; crumb optional. |
| Foundations · Category | hub | [#wf-f-category](gallery.html#wf-f-category) | Section heading + card grid of Foundations subsections. |
| Principles | `design-system/principles.html` | [#wf-f-principles](gallery.html#wf-f-principles) | Looks like / Refuses · 4–7 principles. Docs fonts. No token tables. |
| Color | `design-system/color.html` | [#wf-f-color](gallery.html#wf-f-color) | Semantic swatches → usage → L/D → tokens. |
| Typography | `design-system/typography.html` | [#wf-f-typography](gallery.html#wf-f-typography) | Per family: weights with labels; roles with size·weight·lh·tracking → responsive / content / a11y → tokens. Specimens = product type; prose = docs fonts. |
| Spacing | `design-system/spacing.html` | [#wf-f-spacing](gallery.html#wf-f-spacing) | Scale bars → specimens → tokens. |
| Layout | `design-system/layout.html` | [#wf-f-layout](gallery.html#wf-f-layout) | Stance → widths/breakpoints → regions → phone‖desktop skeletons. |
| Shape | `design-system/shape.html` | [#wf-f-shape](gallery.html#wf-f-shape) | Radius ramp → surfaces → borders → tokens. |
| Elevation | `design-system/elevation.html` | [#wf-f-elevation](gallery.html#wf-f-elevation) | Role cards L‖D → stack → tokens. |
| Icons | `design-system/icons.html` | [#wf-f-icons](gallery.html#wf-f-icons) | Style → detail → inventory → sizes → downloads. Docs fonts for prose. |
| Motion | `design-system/motion.html` | [#wf-f-motion](gallery.html#wf-f-motion) | Duration/easing → demos → reduced-motion → Do/Don't. |
| Logo | `design-system/logo.html` | [#wf-f-logo](gallery.html#wf-f-logo) | Idea → source → action → L/D → clear space → mins → don'ts → swatches → downloads. |
| Themes | `design-system/themes.html` | [#wf-f-themes](gallery.html#wf-f-themes) | Same UI L‖D → stress → Do/Don't. Docs fonts for prose. |
| Components · Category | hub | [#wf-c-category](gallery.html#wf-c-category) | Cards per component → specimen. |
| Components · Specimen | `components.html` | [#wf-c-button](gallery.html#wf-c-button) | Purpose → anatomy → variants → states (live samples). |
| Patterns · Category | hub | [#wf-p-category](gallery.html#wf-p-category) | Cards named by user problem. |
| Patterns · Specimen | `patterns.html` | [#wf-p-destructive](gallery.html#wf-p-destructive) | When → structure → mini storyboard. Docs fonts for prose. |
| Content | `design-system/content.html` | [#wf-content](gallery.html#wf-content) | Terminology · labels · errors. |
| Accessibility | `design-system/accessibility.html` | [#wf-a11y](gallery.html#wf-a11y) | Shared rules; Rule · good · bad. |
| Feature hub | under Screens | [#wf-feature](gallery.html#wf-feature) | Cards: Storyboard + Designs only. |
| Storyboard | `<feature>/storyboard.html` | [#wf-storyboard](gallery.html#wf-storyboard) | Film **16:9**; Mobile\|Web; captions; Designs lists hi-fi. |
| Designs hub | `<feature>/designs.html` | [#wf-designs](gallery.html#wf-designs) | Every hi-fi listed (thumb·name·states); Mobile\|Web. |
| Design screen | `<feature>/<screen>.html` | [#wf-design-screen](gallery.html#wf-design-screen) | Hi-fi + Mobile\|Web (16:9 / 9:16) + state strip. |
