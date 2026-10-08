# Sidebar — page jobs

**Id:** `sidebar` · **Fit:** Written system + long-form reading (sidebar + column). Examples: Mintlify, Fumadocs.

**How to use:** Read this file once when building the handbook. **Do not** read all of [sidebar.html](sidebar.html). Open a single `#wf-*` in that HTML only if a checklist line is ambiguous. Ship a finished unique site — wireframes are IA/placement only.

## Chrome

- Left **sidebar** + narrow reading column.
- Header: system name + “Design handbook” (left), theme toggle (right), separator under header.
- Nav groups (uppercase labels): **Brief** · **Design system** · **Screens**.
- Design system: **category buttons only** (Foundations, Components, Patterns, Content, Accessibility). Subcategories open from the category page / main column — not as required sidebar leaves.
- Screens: nest each feature → **Storyboard** | **Designs** only (no per-screen nav buttons).
- Docs chrome: text labels only (no Lucide in nav). `docs.json` `style` radii on nav/chips/cards/theme. Docs fonts = handbook default; product type only in UI samples, typography specimens, storyboards, screens.
- Theme control on every page; persist `localStorage`.

Deep reference: [sidebar.html#details](sidebar.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Brief · Overview | `brief.html` | [#wf-brief](sidebar.html#wf-brief) | Spec sheet one scroll: Meta (name, platform, purpose) → Problem → Who → Goals → Scope In‖Out → Features→Screens table → Constraints → Open questions (omit if empty). No cards, tabs, mockups. |
| Foundations · Category | category hub | [#wf-category](sidebar.html#wf-category) | Sidebar marks Foundations. Main: subcategory tiles → section pages. |
| Principles | `design-system/principles.html` | [#wf-f-principles](sidebar.html#wf-f-principles) | What/Why · Looks like / Refuses · 4–7 principles. Docs fonts for prose. No token tables. |
| Color | `design-system/color.html` | [#wf-f-color](sidebar.html#wf-f-color) | Semantic swatches → usage → light/dark → token table. Not hue ladders. |
| Typography | `design-system/typography.html` | [#wf-f-typography](sidebar.html#wf-f-typography) | Per family: name+role, **weight variants with labels**, semantic roles with size·weight·lh·tracking → responsive / content / a11y → tokens. Specimens = product type; prose = docs fonts. |
| Spacing | `design-system/spacing.html` | [#wf-f-spacing](sidebar.html#wf-f-spacing) | Scale bars → inset/stack/row/section → tokens. |
| Layout | `design-system/layout.html` | [#wf-f-layout](sidebar.html#wf-f-layout) | Viewport stance → widths/breakpoints → regions → phone‖desktop skeletons. |
| Shape | `design-system/shape.html` | [#wf-f-shape](sidebar.html#wf-f-shape) | Radius ramp → controls/surfaces → borders → tokens. |
| Elevation | `design-system/elevation.html` | [#wf-f-elevation](sidebar.html#wf-f-elevation) | Role cards L‖D → stack + fragments → tokens. One model (shadow or tonal). |
| Icons | `design-system/icons.html` | [#wf-f-icons](sidebar.html#wf-f-icons) | Style rules → detail → inventory → sizes → downloads. Prose = docs fonts. |
| Motion | `design-system/motion.html` | [#wf-f-motion](sidebar.html#wf-f-motion) | Duration/easing → tiny demos → reduced-motion → Do/Don't. |
| Logo | `design-system/logo.html` | [#wf-f-logo](sidebar.html#wf-f-logo) | Idea → source → in action → L/D variants → clear space → min sizes → don'ts → color swatches → downloads. |
| Themes | `design-system/themes.html` | [#wf-f-themes](sidebar.html#wf-f-themes) | Same UI L‖D → stress cases → Do/Don't. Prose = docs fonts; samples may use product UI. |
| Components · Category | hub / `components.html` | [#wf-c-category](sidebar.html#wf-c-category) | Inventory tiles of components this product needs. |
| Components · Specimen | blocks on `components.html` | [#wf-c-button](sidebar.html#wf-c-button) | Purpose → Anatomy → Variants → Sizes → States → Behavior → Content → A11y → Do/Don't. Live specimens (product type inside samples). |
| Patterns · Category | hub / `patterns.html` | [#wf-p-category](sidebar.html#wf-p-category) | Patterns named by user problem. |
| Patterns · Specimen | blocks on `patterns.html` | [#wf-p-destructive](sidebar.html#wf-p-destructive) | When → Structure → Behavior → States → Mini storyboard → Alternatives → Do/Don't. Prose = docs fonts. |
| Content | `design-system/content.html` | [#wf-content](sidebar.html#wf-content) | Voice → terminology Preferred‖Avoid → labels → errors → formatting → Do/Don't. |
| Accessibility | `design-system/accessibility.html` | [#wf-a11y](sidebar.html#wf-a11y) | Per topic: Rule → good → bad. |
| Storyboard | `<feature>/storyboard.html` | [#wf-storyboard](sidebar.html#wf-storyboard) | Header (feature·who·goal). Film panels **always 16:9** (≤3/row). Mobile\|Web toggle. Captions: name·action·outcome. → / ↓. Notes for edges only. |
| Designs hub | `<feature>/designs.html` | [#wf-designs](sidebar.html#wf-designs) | List every hi-fi screen (thumb·name·states). Mobile\|Web. Nav = Storyboard + Designs only. |
| Design screen | `<feature>/<screen>.html` | [#wf-design-screen](sidebar.html#wf-design-screen) | Hi-fi + Mobile\|Web (Web 16:9 · Mobile 9:16) + state strip for real critical states. |

## Index

`index.html` links Brief → Overview; Design system categories; Screens → each feature → Storyboard, Designs. Keep current page marked.
