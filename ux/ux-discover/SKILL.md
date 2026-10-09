---
name: ux-discover
description: Discover project context, write look.json scope, brief.html, and the handbook shell.
disable-model-invocation: true
---

# UX — Discover

Confirm platform and the features → screens list (Round 2). Write the brief page and finish the Design Handbook shell. Do not style the product UI.

This is the Scope state. Say "Scope." / "Round 2." before asking.

## Designs directory

The folder is always named `design`. Path should already be chosen in Round 1 ([ux-new](../ux-new/SKILL.md)). If unknown, ask once. Do not assume the repo root.

Read `<design>/look.json`. If it is missing `description` or `logo`, finish Round 1 in [ux-new](../ux-new/SKILL.md) first.

## Inventory (facts — do not ask)

Prefer the repo and existing domain docs over assumptions. Read:

- Requirements and existing product (routes, roles, flows)
- **`GLOSSARY.md`** and **`docs/adr/`** when present — use those terms; never re-ask settled vocabulary
- Features and screens in scope; what is out of scope
- Constraints (brand, tech, a11y)

Leave unrelated parts of the repo alone. If Round 1’s parallel inventory already ran, reuse it; refresh only if stale.

If the handbook shell is not yet scaffolded, create `handbook.css` / `handbook.js` / stub `index.html` per [handbook.md](../ux-new/handbook.md) before or right after Round 2 writes.

## Round 2 — one grilling message

Ask the **whole frontier in one message** ([grilling](../grilling/SKILL.md) format). Prefill recommendations from inventory + GLOSSARY. Wait once.

```
❓ **Q1** - **Name / product / who**: Confirm the short system name, one-line purpose, and primary role(s).

➡️ <prefilled from repo + GLOSSARY>

---

❓ **Q2** - **Platform**: Mobile first, website first, or both?

➡️ <recommend from the app>

---

❓ **Q3** - **Features → Screens**: Confirm or trim this table (and the pilot feature).

➡️ <proposed table; pilot = first high-traffic feature id>

---

❓ **Q4** - **Out of scope**: What should this run not design?

➡️ <proposed list>
```

## Write look.json

After answers, merge into `<design>/look.json` (keep `source`, `description`, `logo`):

```json
{
  "source": "custom",
  "description": "…",
  "logo": { "mode": "user | cook", "notes": "…" },
  "name": "Short product name",
  "platform": "mobile-first | website-first | both",
  "product": "one-line purpose",
  "who": "primary role(s)",
  "features": [
    {
      "id": "kebab-id",
      "name": "Feature name",
      "screens": [
        { "id": "kebab-id", "name": "Screen name" }
      ]
    }
  ],
  "pilotFeature": "kebab-id",
  "outOfScope": ["…"],
  "status": "scope"
}
```

`pilotFeature` defaults to the first high-traffic feature in the confirmed table unless they overrode it in Q3. Do not write a handbook `accent` field.

## Handbook shell

Follow [handbook.md](../ux-new/handbook.md). Create or refresh:

- `handbook.css` — **minified** custom CSS (no Tailwind); static zinc-only light/dark (no accent); **General Sans** / **Geist Mono**; φ radius; ⌘K command palette styles — never from Look or product
- `handbook.js` — **minified** tiny kernel: theme persist + ⌘K command palette open/focus/filter only (CSS-first for nav, TOC, Preview/Code)
- `favicon.svg` — handbook favicon per [handbook.md](../ux-new/handbook.md)
- `index.html` — home with Overview / Start here / How to use / Status + **ON THIS PAGE**; document head meta; site name links home
- Sidebar brand uses `look.json` `name` (clickable → `index.html`)

Stub Design system / Screens until those pages exist. Every HTML page gets the document head + favicon from [handbook.md](../ux-new/handbook.md).

## Brief page

Write `<design>/brief.html` as a denser **spec sheet** in the handbook main column (handbook fonts). Include sticky **ON THIS PAGE** (all uppercase) with top-padded rail. Use `h2` ids. Use GLOSSARY terms when present. Blocks in order:

1. **Meta** — key/value grid or definition list (Product / Platform / Purpose), not three equal-weight gray lines
2. **Problem** — 2–3 sentences; problem, not UI solution
3. **Who** — primary role(s) as a compact list (no tinted icon tiles)
4. **Goals** — user goal, product goal, success in plain language
5. **Scope** — **In | Out** true two-column layout
6. **Features → Screens** — table matching `look.json` `features` (mark the pilot)
7. **Constraints** — short list (brand, tech, a11y, terms to keep)
8. **Open questions** — omit when empty

Between Brief `h2` sections, use the same **dashed or dotted** horizontal rule (handbook Border token) as Design system / Screens. Keep the page short. No product mockups. No design-system specimens. No screen frames.

This step is done when `look.json` has `name`, `platform`, `features`, `pilotFeature`, and `status`: `scope`; handbook assets and `brief.html` match [handbook.md](../ux-new/handbook.md). Say "Scope finished. Next is the design system."
