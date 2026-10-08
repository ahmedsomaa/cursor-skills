# Topbar (audit) — page jobs

**Id:** `topbar` · **Fit:** Horizontal browsing across audit steps with tabbed flows and redesign packages. Example: Chakra UI docs.

**How to use:** Read this file once when building the audit handbook. **Do not** read all of [topbar.html](topbar.html). Open a single `#wf-*` only if needed. Ship a finished unique audit site — wireframes are IA/placement only.

## Chrome

- **Navbar:** name + “Audit handbook” (left); centered Understand / Walkthrough / Evaluate / Prioritize / Redesign; theme (right).
- **Horizontal tabs** for the current main’s children (Walkthrough → flow ids; Redesign → opportunity ids; Understand/Evaluate/Prioritize → Overview / Findings / Backlog).
- **Vertical tabs** when a redesign opportunity is open — screen names; right panel = specimen.
- Docs chrome: text labels only. `audit/docs.json` `style` on nav; tab underline 2px solid.
- Theme control; persist `localStorage`.

Deep reference: [topbar.html#details](topbar.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Understand | `audit/understand.html` | [#wf-understand](topbar.html#wf-understand) | Nav marks Understand; tab Overview; product sheet. |
| Walkthrough · flow | `audit/walkthrough/<flow-id>.html` | [#wf-walkthrough](topbar.html#wf-walkthrough) | Nav Walkthrough; H-tab = flow; ordered screens/states. |
| Evaluate | `audit/evaluate.html` | [#wf-evaluate](topbar.html#wf-evaluate) | Findings + backlog. |
| Prioritize | `audit/prioritize.html` | [#wf-prioritize](topbar.html#wf-prioritize) | Ranked backlog. |
| Redesign · opportunity | `audit/redesign/<id>/index.html` | [#wf-redesign](topbar.html#wf-redesign) | H-tab = opportunity; before → problem → after. |
| Redesign · screen | `audit/redesign/<id>/<screen>.html` | [#wf-redesign-screen](topbar.html#wf-redesign-screen) | V-tabs = screens; hi-fi + states. |
