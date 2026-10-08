# Sidebar (audit) — page jobs

**Id:** `sidebar` · **Fit:** Written audit reports — Understand, Evaluate, Prioritize with long reading columns. Examples: Mintlify, Fumadocs.

**How to use:** Read this file once when building the audit handbook. **Do not** read all of [sidebar.html](sidebar.html). Open a single `#wf-*` only if a checklist line is ambiguous. Ship a finished unique audit site — wireframes are IA/placement only.

## Chrome

- Left **sidebar** + reading column.
- Header: product name + “Audit handbook” (left), theme toggle (right).
- Five uppercase groups: **Understand** · **Walkthrough** · **Evaluate** · **Prioritize** · **Redesign**.
- Walkthrough nests **flow** buttons. Redesign nests **opportunity** ids (index + screen pages).
- Docs chrome: text labels only. `audit/docs.json` `style` on nav/chips/theme. Docs fonts on report pages; product type in walkthrough/redesign frames when a create kit exists.
- Theme control; persist `localStorage`.

Deep reference: [sidebar.html#details](sidebar.html#details).

## Page inventory

| Page | File | Anchor | Required blocks |
| --- | --- | --- | --- |
| Understand | `audit/understand.html` | [#wf-understand](sidebar.html#wf-understand) | Product, users, goals, key flows, vocabulary. No evaluation. |
| Walkthrough · flow | `audit/walkthrough/<flow-id>.html` | [#wf-walkthrough](sidebar.html#wf-walkthrough) | Ordered screens and states for one flow. |
| Evaluate | `audit/evaluate.html` | [#wf-evaluate](sidebar.html#wf-evaluate) | Structured findings + flat opportunity backlog. |
| Prioritize | `audit/prioritize.html` | [#wf-prioritize](sidebar.html#wf-prioritize) | Ranked opportunities ready for redesign. |
| Redesign · opportunity | `audit/redesign/<id>/index.html` | [#wf-redesign](sidebar.html#wf-redesign) | Before → problem → after + links to hi-fi screens. |
| Redesign · screen | `audit/redesign/<id>/<screen>.html` | [#wf-redesign-screen](sidebar.html#wf-redesign-screen) | Hi-fi with critical states. |

## Index

`audit/index.html` links all five steps; nest flows and redesign opportunities. Current page marked.
