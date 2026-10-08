# Gallery (audit) — page jobs

**Id:** `gallery` · **Fit:** Walkthrough frames and redesign packages — card grids over long report pages. Example: Mantine UI gallery.

**How to use:** Read this file once when building the audit handbook. **Do not** read all of [gallery.html](gallery.html). Open a single `#wf-*` only if needed. Ship a finished unique audit site — wireframes are IA/placement only.

## Chrome

- **No navbar / main-nav strip.**
- Header: product title + “Audit handbook” ‖ theme toggle.
- Home (`audit/index.html`): five **page sections** — Understand, Walkthrough, Evaluate, Prioritize, Redesign — each with heading + **card grid**.
- Nested pages: optional crumb + page title; still no navbar.
- Docs chrome: text labels only. `audit/docs.json` `style` on cards/theme.
- Theme control; persist `localStorage`.

Deep reference: [gallery.html#details](gallery.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Home | `audit/index.html` | [#wf-home](gallery.html#wf-home) | Header then five sections; cards open nested pages. |
| Understand | `audit/understand.html` | [#wf-understand](gallery.html#wf-understand) | Product sheet — users, goals, flows, vocabulary. No evaluation. |
| Walkthrough · flow | `audit/walkthrough/<flow-id>.html` | [#wf-walkthrough](gallery.html#wf-walkthrough) | Ordered screens/states for one flow. |
| Evaluate | `audit/evaluate.html` | [#wf-evaluate](gallery.html#wf-evaluate) | Findings + opportunity backlog. |
| Prioritize | `audit/prioritize.html` | [#wf-prioritize](gallery.html#wf-prioritize) | Ranked backlog for redesign. |
| Redesign · opportunity | `audit/redesign/<id>/index.html` | [#wf-redesign](gallery.html#wf-redesign) | Before → problem → after + hi-fi links. |
| Redesign · screen | `audit/redesign/<id>/<screen>.html` | [#wf-redesign-screen](gallery.html#wf-redesign-screen) | Hi-fi + states. |
