# UX

I made this set because I am a developer and I do not design in Figma. Matt Pocock's skills cover how the software gets specified and built. Nothing in that flow produces the look of the product: the type, the color, the screens, and the cases a person actually moves through.

These skills are that missing step. They act as a product designer. A run asks where a `design` folder should live, then writes a brief, a design system that belongs to this app, and high-fidelity HTML screens. The result is unique to the product. A generic kit, or a copy of a reference, is not finished.

The screens stay HTML so I can open them, and so a later implementation can follow them. Storybook is a later version, once the product has components to preview.

## How a run goes

`ux` runs three steps and says which one is current.

| Skill | What it does |
| --- | --- |
| `ux-understand` | Reads the app and writes `brief.html`. |
| `ux-system` | Lists the catalog of design systems, or cooks a custom one, and writes the system as HTML plus `system.json`. |
| `ux-screens` | Writes one HTML page per screen, grouped by feature, plus a storyboard of at most three screens per row. |

`ux-edit` is for a change after that. It asks whether the change is in the design system or in the screens, then edits only that. `ux-polish` fixes navigation, type, and light and dark when the folder is rough. `ux-ask` answers how to start and which skill to run.

## What the files are

The design system catalog is fifteen token-first systems in `ux-system/design-systems/`. A run writes `system.json` in the project's `design` folder using that same shape, so a system made for one product can be added to the catalog later.

Docs chrome is separate from the product. `ux/docs-templates/` has four layouts: sidebar, cards, grid, and top bar. Each names its type scale, Google Fonts, and Lucide icons. Custom is always a choice: describe color, type, and radius, or let the agent decide the look from the brief and then look for inspiration.
