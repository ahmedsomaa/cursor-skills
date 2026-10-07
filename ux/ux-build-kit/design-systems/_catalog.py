# Design system catalog — source for render.py.

SYSTEMS: list[dict] = [
{'id': 'ant-design',
 'name': 'Ant Design',
 'source': 'https://ant.design/',
 'maker': 'Ant Group',
 'fit': 'Enterprise forms and dashboards driven by one seed color.',
 'tone': 'Unconfirmed.',
 'principles': 'Natural, certain, meaningful, growing. A seed color derives the palette, so there '
               'is one color source.',
 'color': 'Seed roles: primary, success, warning, and error. The published defaults are primary '
          '#1677ff, success #52c41a, warning #faad14, and error #ff4d4f. Those seeds map to '
          'semantic roles.',
 'typography': 'A system sans stack, with a numeric scale for titles and body.',
 'spacing': 'An 8px base with component padding tokens.',
 'shape': 'A border-radius token on controls.',
 'elevation': 'Shadow levels for cards and overlays.',
 'layout': 'A 24-column grid and a side-plus-header layout.',
 'logo': 'Unconfirmed.',
 'icons': 'A large outlined and filled icon set.',
 'motion': 'Unconfirmed.',
 'components': 'A very large set. Use only what this app needs: form, table, menu, modal, message.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark algorithm themes from the same seed.',
 'adapt': 'Keep the seed-to-role model and the form density. Do not import the whole component '
          'catalog. Change the seed and the font.',
 'fonts': [{'role': 'UI',
            'name': 'Chinese Quote / system sans stack',
            'note': '-apple-system, Segoe UI, PingFang SC…'},
           {'role': 'Web alt',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'common substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': '@ant-design/icons',
                'url': 'https://ant.design/components/icon',
                'note': 'outlined / filled / two-tone'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#d9d9d9;\n'
        '  --soft:#f5f5f5;\n'
        '  --accent:#1677ff;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'swiss', 'soft'],
 'dont': "Don't ignore the seed-color model, or mix dense form layouts with sparse consumer "
         'marketing density.',
 'primary': '#1677ff'},
{'id': 'astryx',
 'name': 'Astryx (Meta)',
 'source': 'https://astryx.atmeta.com/',
 'maker': 'Meta (Facebook)',
 'fit': 'Meta’s open, themeable React design system for product and agent-ready SaaS UIs.',
 'tone': 'Unconfirmed.',
 'principles': 'Grown inside Meta for thousands of apps. Accessible components, brand-level '
               'theming, dark mode, and agent-ready docs/CLI.',
 'color': 'Theme packages (neutral and others) expose CSS custom properties for surfaces, text, '
          'and action.',
 'typography': 'Theme-driven sans for UI; swap via theme packages.',
 'spacing': 'Built-in spacing on components plus theme tokens.',
 'shape': 'Themeable radii; product-friendly rounding by default.',
 'elevation': 'Theme shadows for overlays and panels.',
 'layout': 'AppShell / TopNav / SideNav plus page templates for dashboards and settings.',
 'logo': 'Unconfirmed.',
 'icons': 'Use with Meta/product icon sets or Lucide when adapting outside Meta.',
 'motion': 'Unconfirmed.',
 'components': '150+ React components in @astryxdesign/core — buttons, forms, nav, overlays, data '
               'display.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Accessibility is a stated core goal of the open system.',
 'themes': 'Multiple ready themes (neutral, and others) plus dark mode.',
 'adapt': 'Keep the theme-token model and accessible primitives. Replace Meta brand marks; pick a '
          'theme that matches the chosen tone.',
 'fonts': [{'role': 'UI', 'name': 'Optimistic / system sans', 'note': 'Meta product type adjacent'},
           {'role': 'Web',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'practical substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Lucide',
                'url': 'https://lucide.dev/',
                'note': 'when adapting outside Meta'},
               {'role': 'Alt',
                'name': 'Astryx / Meta icons',
                'url': 'https://astryx.atmeta.com/',
                'note': 'in-package where available'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#ced0d4;\n'
        '  --soft:#f0f2f5;\n'
        '  --accent:#0866FF;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:8px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'liquid-glass'],
 'dont': "Don't ship Meta wordmarks or Facebook-only chrome on an unrelated product.",
 'primary': '#0866FF'},
{'id': 'atlassian',
 'name': 'Atlassian Design System',
 'source': 'https://atlassian.design/',
 'maker': 'Atlassian',
 'fit': 'Collaboration and work-management products.',
 'tone': 'Unconfirmed.',
 'principles': 'Bold, optimistic, and practical. Tokens are named so a picker can choose a role '
               'instead of a raw value.',
 'color': 'Tokens for background, text, border, and icon, including inverse roles for bold '
          'surfaces. Alpha and transparent colors are part of the set.',
 'typography': 'A product sans with a short heading and body scale.',
 'spacing': 'A space scale used by stack and inline layouts.',
 'shape': 'A radius scale. Many surfaces use a medium radius.',
 'elevation': 'A small set of elevation tokens, including one below the surface (sunken). Each '
              'elevation color token is paired with a shadow token. Light mode builds depth with '
              'shadow. Dark mode uses shadow and color together.',
 'layout': 'Page layouts with navigation, banners, and a main column.',
 'logo': 'Unconfirmed.',
 'icons': 'A dual icon set for 16px UI and larger spot illustrations.',
 'motion': 'Unconfirmed.',
 'components': 'Button, lozenge, flag, modal, dynamic table, and inline edit.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark token sets. The same elevation roles resolve differently in each.',
 'adapt': 'Keep the named elevation pairs and the token roles. Replace the Atlassian palette and '
          'illustration style.',
 'fonts': [{'role': 'UI', 'name': 'Charlie Sans / Atlassian Sans', 'note': 'product UI'},
           {'role': 'Web fallback',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'open substitute'}],
 'icon_libs': [{'role': 'UI',
                'name': 'Atlassian Design Icons',
                'url': 'https://atlassian.design/components/icon',
                'note': '16px UI'},
               {'role': 'Spot', 'name': 'Atlassian spot illustrations', 'note': 'larger moments'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#dfe1e6;\n'
        '  --soft:#f7f8f9;\n'
        '  --accent:#0c66e4;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'soft', 'swiss'],
 'dont': "Don't turn collaboration chrome into a marketing landing, or ignore the issue/board "
         'metaphors the system is built around.',
 'primary': '#0c66e4'},
{'id': 'blueprint',
 'name': 'Blueprint',
 'source': 'https://blueprintjs.com/',
 'maker': 'Palantir',
 'fit': 'Dense desktop-class data and ops interfaces in the browser.',
 'tone': 'Unconfirmed.',
 'principles': 'Complex UIs stay keyboardable and compact. Opinionated components for serious '
               'tools.',
 'color': 'Dark and light themes with intent colors for danger/warning/success.',
 'typography': 'System fonts with compact UI sizing; monospace for code.',
 'spacing': 'Tight control spacing for toolbars and tables.',
 'shape': 'Small radii; utilitarian.',
 'elevation': 'Elevated overlays; dark UI common for tools.',
 'layout': 'Toolbars, left nav, and multi-pane editors.',
 'logo': 'Unconfirmed.',
 'icons': 'Blueprint icons (16/20px).',
 'motion': 'Unconfirmed.',
 'components': 'Table, Tree, Dialog, Toast, DateTime, and form controls.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Focus management in overlays.',
 'themes': 'Light and dark (often dark-default for tools).',
 'adapt': 'Keep density and toolbar patterns. Soften Palantir-dark defaults only if the product '
          'tone needs it.',
 'fonts': [{'role': 'UI', 'name': 'Segoe UI / system sans', 'note': 'Blueprint default stack'},
           {'role': 'Mono', 'name': 'Menlo / Consolas', 'note': 'code'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Blueprint icons',
                'url': 'https://blueprintjs.com/docs/#icons',
                'note': '16/20px'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#d3d8de;\n'
        '  --soft:#f6f7f9;\n'
        '  --accent:#2d72d2;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'calm-density', 'terminal'],
 'dont': "Don't restyle Blueprint into large-radius consumer cards.",
 'primary': '#2d72d2'},
{'id': 'canvas',
 'name': 'Canvas',
 'source': 'https://canvas.workday.com/',
 'maker': 'Workday',
 'fit': 'Enterprise HR and finance SaaS — dense forms, records, and admin workflows.',
 'tone': 'Unconfirmed.',
 'principles': 'Accessible enterprise patterns. Predictable forms and data density for daily work '
               'apps.',
 'color': 'Workday canvas tokens for background, text, and action; themes for contrast.',
 'typography': 'Product sans with a documented hierarchy for page and section titles.',
 'spacing': 'Form and page spacing tokens for dense enterprise layouts.',
 'shape': 'Slight rounding; enterprise, not playful.',
 'elevation': 'Panels and dialogs with restrained elevation.',
 'layout': 'Record pages, lists, and multi-step flows.',
 'logo': 'Unconfirmed.',
 'icons': 'Canvas kit icons.',
 'motion': 'Unconfirmed.',
 'components': 'Inputs, selects, tables, prompts, and navigation from canvas-kit.',
 'patterns': 'Unconfirmed.',
 'content': 'Voice & tone present in Canvas.',
 'accessibility': 'Strong enterprise a11y expectations.',
 'themes': 'Default and high-contrast oriented themes.',
 'adapt': 'Keep form density and accessibility. Replace Workday brand colors and wordmarks.',
 'fonts': [{'role': 'UI',
            'name': 'Roboto / system sans',
            'url': 'https://fonts.google.com/specimen/Roboto',
            'note': 'common enterprise'},
           {'role': 'Alt',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'web substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Canvas kit icons',
                'url': 'https://canvas.workday.com/',
                'note': 'Workday set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#ced3d9;\n'
        '  --soft:#f0f1f2;\n'
        '  --accent:#0875e1;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'swiss', 'soft'],
 'dont': "Don't sparsify enterprise record pages into marketing heroes.",
 'primary': '#0875e1'},
{'id': 'carbon',
 'name': 'Carbon',
 'source': 'https://carbondesignsystem.com/',
 'maker': 'IBM',
 'fit': 'Dense product UI for tools and data.',
 'tone': 'Unconfirmed.',
 'principles': 'Neutral gray does the organizing. Color is for action and status. Productive '
               'screens stay compact. Expressive marketing type is a separate set.',
 'color': 'Role tokens: background, layer, field, border, text, link, icon, support, focus, and '
          'skeleton. Light themes are White and Gray 10. Dark themes are Gray 90 and Gray 100.',
 'typography': 'IBM Plex. Productive type is fixed, with a 14px body for dense UI. Expressive '
               'headings are fluid. Product weights are Light, Regular, and SemiBold.',
 'spacing': 'Multiples of 2, 4, and 8, inside components and between them. A stack utility owns '
            'gaps so components do not carry margin.',
 'shape': 'Unconfirmed.',
 'elevation': 'Layer tokens do the stacking. In dark themes, surfaces lighten as they rise. In '
              'light themes, white and gray alternate. Shadow is secondary.',
 'layout': 'The 2x Grid. The mini unit is 8px.',
 'logo': 'Unconfirmed.',
 'icons': 'IBM icon and pictogram sets, aligned to the icon color tokens.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, forms, data table, tabs, modal, notification, and structured list, '
               'including skeleton states. Patterns cover login, forms, and filtering.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Four named themes. Changing the theme swaps the universal tokens. Components are not '
           'restyled one by one.',
 'adapt': 'Keep the role tokens, the productive type scale, and the spacing tokens. Replace IBM '
          'Plex and IBM blue unless this product is that formal.',
 'fonts': [{'role': 'UI / productive',
            'name': 'IBM Plex Sans',
            'url': 'https://fonts.google.com/specimen/IBM+Plex+Sans',
            'note': '14px body'},
           {'role': 'Mono',
            'name': 'IBM Plex Mono',
            'url': 'https://fonts.google.com/specimen/IBM+Plex+Mono',
            'note': 'code / data'},
           {'role': 'Expressive',
            'name': 'IBM Plex Serif',
            'url': 'https://fonts.google.com/specimen/IBM+Plex+Serif',
            'note': 'marketing set'}],
 'icon_libs': [{'role': 'UI',
                'name': 'Carbon icons',
                'url': 'https://carbondesignsystem.com/elements/icons/library/',
                'note': '16/20/24/32'},
               {'role': 'Pictograms',
                'name': 'IBM pictograms',
                'url': 'https://carbondesignsystem.com/elements/pictograms/library/',
                'note': 'illustrative'}],
 'css': '.t{\n'
        '  --bg:#f4f4f4;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#8d8d8d;\n'
        '  --soft:#e0e0e0;\n'
        '  --accent:#0f62fe;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'calm-density', 'swiss'],
 'dont': "Don't restyle each component ad hoc, or swap IBM Plex/blue without a product reason "
         "while keeping Carbon's density.",
 'primary': '#0f62fe'},
{'id': 'chakra',
 'name': 'Chakra UI',
 'source': 'https://chakra-ui.com/',
 'maker': 'Chakra UI / Segun Adebayo',
 'fit': 'Composable React SaaS UI with accessible primitives and a themeable token model.',
 'tone': 'Unconfirmed.',
 'principles': 'Simple, modular, and accessible. Style props and a theme object keep product UI '
               'consistent without a mega component dump.',
 'color': 'Semantic tokens for background, foreground, muted, border, and brand. Light and dark '
          'color modes from the same roles.',
 'typography': 'A sans scale for heading and body; theme fonts are swappable.',
 'spacing': 'Theme space scale (commonly 4px rhythm) via style props.',
 'shape': 'Radii tokens from none to full; controls often use md/lg radii.',
 'elevation': 'Shadow tokens for cards, popovers, and modals.',
 'layout': 'Stack, Flex, Grid, and Container patterns for product layouts.',
 'logo': 'Unconfirmed.',
 'icons': 'Works with any React icon set; docs commonly pair with React Icons / Lucide.',
 'motion': 'Unconfirmed.',
 'components': 'Button, Input, Modal, Menu, Table, Toast, and form controls — use only what the '
               'app needs.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'WAI-ARIA patterns on primitives; focus rings are first-class.',
 'themes': 'Light and dark color modes; theme overrides per product.',
 'adapt': 'Keep the semantic token + accessible primitive model. Replace default purple brand and '
          'default fonts with this product’s tone.',
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'common Chakra default'},
           {'role': 'Alt', 'name': 'System UI stack', 'note': 'theme.fonts.body'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Lucide / React Icons',
                'url': 'https://lucide.dev/',
                'note': 'pair with Chakra Icon'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e2e8f0;\n'
        '  --soft:#f7fafc;\n'
        '  --accent:#319795;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'minimalism'],
 'dont': "Don't treat Chakra as a free-for-all style-prop soup with no token source of truth.",
 'primary': '#319795'},
{'id': 'cloudscape',
 'name': 'Cloudscape (Amazon / AWS)',
 'source': 'https://cloudscape.design/',
 'maker': 'Amazon Web Services',
 'fit': 'Amazon / AWS console and cloud-admin SaaS — dense resources, wizards, and ops tables.',
 'tone': 'Unconfirmed.',
 'principles': 'Content first. One primary action per view. Density is high and consistent. Help '
               'text sits next to the decision.',
 'color': 'A cool neutral canvas with a single action blue. Status colors for error, warning, '
          'success, and info.',
 'typography': 'A compact product scale. Page headers are larger than section headers. Body stays '
               'small.',
 'spacing': 'A tight spacing scale for forms, tables, and wizards.',
 'shape': 'Small radii on containers and controls.',
 'elevation': 'Flash, modal, and dropdown are the elevated layers. The page itself is flat.',
 'layout': 'App layout with side navigation, content, split panel, and a wizard or form layout.',
 'logo': 'Unconfirmed.',
 'icons': 'A small functional icon set sized for 16px controls.',
 'motion': 'Unconfirmed.',
 'components': 'App layout, table, form, form field, wizard, flashbar, modal, and side navigation.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the app layout, the form density, and the one-primary-action rule. Replace the AWS '
          'blue and any console chrome that is not this product.',
 'fonts': [{'role': 'UI', 'name': 'Amazon Ember', 'note': 'Cloudscape default'},
           {'role': 'Fallback', 'name': 'Helvetica Neue / Arial', 'note': 'system'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Cloudscape icons',
                'url': 'https://cloudscape.design/foundation/visual-foundation/iconography/',
                'note': '16px functional'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#7d8998;\n'
        '  --soft:#f2f3f3;\n'
        '  --accent:#0972d3;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'calm-density', 'terminal'],
 'dont': "Don't flatten wizards and resource tables into cards-only marketing UI, or hide "
         'region/resource identity.',
 'primary': '#0972d3'},
{'id': 'eui',
 'name': 'Elastic UI (EUI)',
 'source': 'https://eui.elastic.co/',
 'maker': 'Elastic',
 'fit': 'Dense observability, search, and data-tool SaaS with strong table and chart patterns.',
 'tone': 'Unconfirmed.',
 'principles': 'Productivity over decoration. Compact controls, clear empty states, and data-first '
               'layouts.',
 'color': 'Light and dark themes with semantic status colors for severity.',
 'typography': 'Inter-based product type with compact sizes for dense UI.',
 'spacing': 'Strict size scale for padding and control heights.',
 'shape': 'Slight radii on controls; panels stay structured.',
 'elevation': 'Panels and flyouts with restrained shadows.',
 'layout': 'Page, side nav, and kibana-like app frames.',
 'logo': 'Unconfirmed.',
 'icons': 'EUI icon set for UI and logos for Elastic products.',
 'motion': 'Unconfirmed.',
 'components': 'Data grid, tables, filters, forms, charts wrappers, and flyouts.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Keyboard and contrast guidance for dense tools.',
 'themes': 'Light, dark, and Amsterdam theme variants.',
 'adapt': 'Keep density and data-grid patterns. Replace Elastic brand accents and marketing logos.',
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'EUI default'},
           {'role': 'Code',
            'name': 'Roboto Mono',
            'url': 'https://fonts.google.com/specimen/Roboto+Mono',
            'note': 'code samples'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'EUI icons',
                'url': 'https://eui.elastic.co/#/display/icons',
                'note': 'product icons'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#d3dae6;\n'
        '  --soft:#f5f7fa;\n'
        '  --accent:#0077cc;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'calm-density', 'terminal'],
 'dont': "Don't flatten EUI into sparse consumer cards — density is the point.",
 'primary': '#0077cc'},
{'id': 'evergreen',
 'name': 'Evergreen',
 'source': 'https://evergreen.segment.com/',
 'maker': 'Segment (Twilio)',
 'fit': 'B2B SaaS consoles — practical React components with a calm enterprise feel.',
 'tone': 'Unconfirmed.',
 'principles': 'Opinionated building blocks for product teams. Less theme theater, more usable '
               'defaults.',
 'color': 'Neutral grays with blue action; semantic intents.',
 'typography': 'UI sans (often system / Inter-like) with a small scale.',
 'spacing': 'Consistent paddings inside Panes and major layouts.',
 'shape': 'Small radii on inputs and buttons.',
 'elevation': 'Layers for side sheets and dialogs.',
 'layout': 'Pane, sidebar, and toolbar patterns for B2B apps.',
 'logo': 'Unconfirmed.',
 'icons': 'Evergreen icons.',
 'motion': 'Unconfirmed.',
 'components': 'Button, TextInput, Table, Dialog, CornerDialog, and navigation helpers.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Primarily light enterprise UI.',
 'adapt': 'Keep Pane/layout patterns and calm neutrals. Retint blues for brand.',
 'fonts': [{'role': 'UI',
            'name': 'Inter / system UI',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'typical Evergreen apps'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Evergreen icons',
                'url': 'https://evergreen.segment.com/components/icons',
                'note': 'Segment set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e6e8f0;\n'
        '  --soft:#f9f9fb;\n'
        '  --accent:#3366ff;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'soft', 'swiss'],
 'dont': "Don't explode Evergreen into a custom theme system that fights its defaults without "
         'tokens.',
 'primary': '#3366ff'},
{'id': 'fluent-2',
 'name': 'Fluent 2',
 'source': 'https://fluent2.microsoft.design/',
 'maker': 'Microsoft',
 'fit': 'Productivity apps that share a neutral, shared, and brand palette.',
 'tone': 'Unconfirmed.',
 'principles': 'Motion explains hierarchy. It is not decoration. Color is not the only signal: '
               'pair status color with text or an icon. Guidance is split by platform.',
 'color': 'Three palettes. Neutral is black, white, and gray for surfaces, text, and layout. '
          'Shared is for reusable pieces such as avatars, calendars, and badges, including '
          'semantic status colors. Brand marks the product on buttons, calls to action, and '
          'selected states. Global tokens hold the palette values. Alias tokens name the role, so '
          'a screen does not pick a hex. In dark mode the shared palette shifts in saturation and '
          'brightness.',
 'typography': 'Web roles, set in Segoe UI: Caption 2, Caption 1, Body 1, Subtitle 2, Subtitle 1, '
               'Title 3, Title 2, Title 1, Large Title, and Display, with Regular, Semibold, and '
               'Bold weights. Windows, Mac, iOS, and Android each have their own ramp and native '
               'family. Sentence case. Left aligned for left-to-right languages.',
 'spacing': 'Unconfirmed.',
 'shape': 'Unconfirmed.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Unconfirmed.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark. Interaction darkens a control from rest to hover to selected, except '
           'on Windows, where interaction lightens it. Focus keeps the control color and adds a '
           'thicker stroke. People can personalize the scheme.',
 'adapt': 'Keep the three palettes and the alias roles. Replace Segoe and the Microsoft brand '
          "colors. Use the ramp for this product's platform.",
 'fonts': [{'role': 'UI', 'name': 'Segoe UI', 'note': 'Windows / Fluent default'},
           {'role': 'Web / Mac',
            'name': 'Segoe UI Variable / system-ui',
            'note': 'optical sizing'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Fluent UI System Icons',
                'url': 'https://github.com/microsoft/fluentui-system-icons',
                'note': 'regular / filled'}],
 'css': '.t{\n'
        '  --bg:#faf9f8;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e1dfdd;\n'
        '  --soft:#f3f2f1;\n'
        '  --accent:#0f6cbd;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'liquid-glass', 'calm-density'],
 'dont': "Don't drop the neutral/shared/brand split, or force a loud single accent across every "
         'surface.',
 'primary': '#0f6cbd'},
{'id': 'forma-36',
 'name': 'Forma 36',
 'source': 'https://f36.contentful.com/',
 'maker': 'Contentful',
 'fit': 'Content and editorial tools.',
 'tone': 'Unconfirmed.',
 'principles': 'Clarity for people who work in the tool all day. Tokens are public and components '
               'consume them.',
 'color': 'Semantic roles: colorPrimary #0059C8, colorPositive #006D23, colorNegative #BD002A, '
          'colorWarning #CC4500, and colorTextDark #111. Base colors, plus gray and black and '
          'white, use shades 100 through 900.',
 'typography': 'Tokens exist for typography. A sans scale for UI, with a monospace for tokens and '
               'code. Exact steps are Unconfirmed.',
 'spacing': 'Tokens exist for spacing, used by stack and flex helpers. Exact steps are '
            'Unconfirmed.',
 'shape': 'Tokens exist for border radius. Exact steps are Unconfirmed.',
 'elevation': 'Tokens exist for shadows and z-index, used by popovers and modals. Exact steps are '
              'Unconfirmed.',
 'layout': 'Workbench layouts: nav, main canvas, sidebar.',
 'logo': 'Unconfirmed.',
 'icons': 'A small UI icon set.',
 'motion': 'Unconfirmed.',
 'components': 'Button, form controls, modal, note, and entity list.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the workbench layout and the rule that components consume tokens. Replace '
          "Contentful's blue.",
 'fonts': [{'role': 'UI', 'name': 'Geist / system sans', 'note': 'Forma 36 tokens'},
           {'role': 'Mono',
            'name': 'Geist Mono',
            'url': 'https://vercel.com/font',
            'note': 'code in CMS'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Forma 36 icons',
                'url': 'https://f36.contentful.com/components/icon',
                'note': 'small UI set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#cfd9e0;\n'
        '  --soft:#f7f9fa;\n'
        '  --accent:#036fe3;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['editorial', 'soft', 'calm-density'],
 'dont': "Don't treat editorial tools like ops consoles, or bury content-type structure under "
         'generic dashboard widgets.',
 'primary': '#036fe3'},
{'id': 'garden',
 'name': 'Garden',
 'source': 'https://garden.zendesk.com/',
 'maker': 'Zendesk',
 'fit': 'Support, messaging, and agent-workspace SaaS with calm, usable chrome.',
 'tone': 'Unconfirmed.',
 'principles': 'Practical components for agent productivity. Clear forms, tables, and conversation '
               'UI.',
 'color': 'Neutrals with Zendesk brand accents for action; themes for product surfaces.',
 'typography': 'System/product sans with a compact UI scale.',
 'spacing': 'Consistent control heights and form spacing.',
 'shape': 'Modest radii on inputs and buttons.',
 'elevation': 'Menus and modals elevate; lists stay flat.',
 'layout': 'Workspace layouts: list + detail, ticket views.',
 'logo': 'Unconfirmed.',
 'icons': 'Garden icon set.',
 'motion': 'Unconfirmed.',
 'components': 'Forms, tables, chrome, and notification patterns for support tools.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Product themes including dark where supported.',
 'adapt': 'Keep agent-workspace density and form clarity. Replace Zendesk brand green/mark.',
 'fonts': [{'role': 'UI',
            'name': 'System sans / Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'product UI'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Garden icons',
                'url': 'https://garden.zendesk.com/components/icons',
                'note': 'Zendesk set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#d8dcde;\n'
        '  --soft:#f8f9f9;\n'
        '  --accent:#1f73b7;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'swiss'],
 'dont': "Don't style support workspaces like consumer social feeds.",
 'primary': '#1f73b7'},
{'id': 'geist',
 'name': 'Geist',
 'source': 'https://vercel.com/geist',
 'maker': 'Vercel',
 'fit': 'Developer and AI-product SaaS — sharp, minimal, high-contrast product chrome.',
 'tone': 'Unconfirmed.',
 'principles': 'Clarity and speed. Quiet surfaces, strong type, and sparse chrome so content and '
               'code lead.',
 'color': 'Neutral gray scale with a single accent (often black/blue). Light and dark themes.',
 'typography': 'Geist Sans and Geist Mono as the system faces.',
 'spacing': 'Tight, consistent product spacing; dashboard density.',
 'shape': 'Small to medium radii; not pill-heavy.',
 'elevation': 'Hairline borders; soft shadows sparingly.',
 'layout': 'App frames for dashboards, docs, and marketing that share the same tokens.',
 'logo': 'Unconfirmed.',
 'icons': 'Simple stroke icons aligned to Geist weight.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, inputs, menus, and layout primitives suited to developer tools.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark.',
 'adapt': 'Keep Geist Sans/Mono pairing and quiet neutrals. Retint accent for brand without adding '
          'loud marketing clutter in app chrome.',
 'fonts': [{'role': 'UI',
            'name': 'Geist Sans',
            'url': 'https://vercel.com/font',
            'note': 'primary'},
           {'role': 'Mono',
            'name': 'Geist Mono',
            'url': 'https://vercel.com/font',
            'note': 'code'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Geist icons / Lucide',
                'url': 'https://lucide.dev/',
                'note': 'stroke UI'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#eaeaea;\n'
        '  --soft:#fafafa;\n'
        '  --accent:#0070f3;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['minimalism', 'calm-density', 'aurora'],
 'dont': "Don't turn Geist into a colorful maximal marketing kit inside the product shell.",
 'primary': '#0070f3'},
{'id': 'gestalt',
 'name': 'Gestalt',
 'source': 'https://github.com/pinterest/gestalt',
 'maker': 'Pinterest',
 'fit': "Creation and content products in Pinterest's design language.",
 'tone': 'Unconfirmed.',
 'principles': "A React component set that carries Pinterest's design language. The public docs "
               'require a sign-in, so token roles are not confirmed here.',
 'color': 'Unconfirmed.',
 'typography': 'Unconfirmed.',
 'spacing': 'Unconfirmed.',
 'shape': 'Unconfirmed.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Unconfirmed.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Open the source before using a color, type size, space, or shadow. Keep only the roles '
          "the source names. Replace Pinterest's brand.",
 'fonts': [{'role': 'UI', 'name': 'Helvetica Neue', 'note': 'Pinterest product'},
           {'role': 'Web', 'name': 'Helvetica / Arial', 'note': 'fallback stack'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Gestalt Icon',
                'url': 'https://gestalt.pinterest.systems/web/icon',
                'note': 'Pinterest icon component'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#111;\n'
        '  --soft:#efefef;\n'
        '  --accent:#e60023;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:16px;\n'
        '  --radius-sm:24px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['maximalism', 'neo-brutalism', 'soft'],
 'dont': "Don't mute Gestalt into a gray enterprise admin, or ignore creation/content-first flows.",
 'primary': '#e60023'},
{'id': 'govuk',
 'name': 'GOV.UK Design System',
 'source': 'https://design-system.service.gov.uk/',
 'maker': 'Government Digital Service',
 'fit': 'Public services that need a small, tested, accessible set.',
 'tone': 'Unconfirmed.',
 'principles': 'Simplicity, evidence from user research, and accessibility. Text and interactive '
               'elements meet WCAG 2.2 AA contrast. A component can be experimental until the '
               'source marks it stable.',
 'color': 'Use functional roles, not copied hex: text, secondary-text, inverse-text, link, '
          'link-hover, link-visited, link-active, border, input-border, body-background, '
          'template-background, focus, focus-text, error, success, hover, brand, '
          'surface-background, surface-text, and surface-border. Focus yellow is only for keyboard '
          'focus. A palette of named groups (blue, green, teal, purple, magenta, red, orange, '
          'yellow, brown, black, white) with tint and shade variants is for illustration and '
          'custom components, through the colour function.',
 'typography': 'Unconfirmed.',
 'spacing': 'Two scales, units 0 through 9. Static spacing is the same on every screen. Responsive '
            'spacing matches it above the 640px tablet breakpoint and is tighter below that, '
            'except units 0 through 3, which never change. Use the spacing helpers.',
 'shape': 'Unconfirmed.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Service patterns that have been tested with users. Prefer a published component '
               'over a custom one.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the functional colour roles, the spacing units, and the tested-pattern habit. '
          'Replace GOV.UK blue, the focus yellow, and the Transport type unless this product is a '
          'public service.',
 'fonts': [{'role': 'UI',
            'name': 'GDS Transport',
            'url': 'https://www.gov.uk/government/publications/govuk-design-system-fonts',
            'note': 'GOV.UK only'},
           {'role': 'Fallback', 'name': 'Arial / Helvetica', 'note': 'public services fallback'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'GOV.UK Frontend icons / SVG',
                'url': 'https://design-system.service.gov.uk/styles/images/',
                'note': 'minimal set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#0b0c0c;\n'
        '  --soft:#f3f2f1;\n'
        '  --accent:#00703c;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:0;\n'
        '  --radius-sm:0;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n'
        '.t .btn{background:#00703c;border-bottom:2px solid #002d18}\n',
 'tones': ['swiss', 'minimalism', 'editorial'],
 'dont': "Don't invent decorative chrome, or use GOV.UK crown/branding outside UK public services.",
 'primary': '#00703c'},
{'id': 'helios',
 'name': 'Helios',
 'source': 'https://helios.hashicorp.design/',
 'maker': 'HashiCorp',
 'fit': 'Infrastructure and platform SaaS — technical, structured, calm product UI.',
 'tone': 'Unconfirmed.',
 'principles': 'Clarity for complex systems. Consistent tokens across HashiCorp products.',
 'color': 'Neutral surfaces with HashiCorp brand accents used sparingly for action/status.',
 'typography': 'System/product sans with a compact scale for consoles.',
 'spacing': 'Tokenized spacing for forms and page sections.',
 'shape': 'Small radii; technical feel.',
 'elevation': 'Border + light elevation for panels.',
 'layout': 'Console layouts: side nav, main content, and detail drawers.',
 'logo': 'Unconfirmed.',
 'icons': 'Helios / HashiCorp iconography.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, forms, tables, alerts, and navigation for cloud consoles.',
 'patterns': 'Unconfirmed.',
 'content': 'Voice & tone present in Helios.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark product themes.',
 'adapt': 'Keep console structure and restrained accent use. Replace HashiCorp black/brand marks.',
 'fonts': [{'role': 'UI',
            'name': 'System sans / Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'product UI'},
           {'role': 'Mono', 'name': 'IBM Plex Mono / Geist Mono', 'note': 'CLI-adjacent strings'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Helios icons',
                'url': 'https://helios.hashicorp.design/icons/library',
                'note': 'HashiCorp set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#c2c5cb;\n'
        '  --soft:#f5f5f6;\n'
        '  --accent:#000000;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'swiss', 'terminal'],
 'dont': "Don't decorate infra consoles with playful consumer chrome.",
 'primary': '#000000'},
{'id': 'leafygreen',
 'name': 'LeafyGreen',
 'source': 'https://www.mongodb.design/',
 'maker': 'MongoDB',
 'fit': 'Developer-data and cloud console SaaS with approachable green brand accents.',
 'tone': 'Unconfirmed.',
 'principles': 'Friendly but technical. Consistent LeafyGreen components across MongoDB products.',
 'color': 'MongoDB green as brand/action with neutrals for structure; dark theme available.',
 'typography': 'Euclid / Akzidenz-adjacent product type — often system sans on web docs.',
 'spacing': 'Component spacing tokens for forms and pages.',
 'shape': 'Rounded controls; approachable radii.',
 'elevation': 'Cards and menus with soft elevation.',
 'layout': 'Marketing + product patterns; app shells for cloud.',
 'logo': 'Unconfirmed.',
 'icons': 'LeafyGreen glyphs.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, inputs, tables, modals, and navigation from leafygreen-ui.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark.',
 'adapt': 'Keep the approachable console patterns. Replace MongoDB green if the product brand '
          "isn't Mongo.",
 'fonts': [{'role': 'UI', 'name': 'Akzidenz-Grotesk / Euclid', 'note': 'MongoDB brand type'},
           {'role': 'Web',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'practical substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'LeafyGreen icons',
                'url': 'https://www.mongodb.design/foundation/icons',
                'note': 'glyphs'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e7eeec;\n'
        '  --soft:#f9fbfa;\n'
        '  --accent:#00684a;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'swiss'],
 'dont': "Don't keep Mongo green as the primary if the product isn't MongoDB.",
 'primary': '#00684a'},
{'id': 'lightning',
 'name': 'Lightning Design System',
 'source': 'https://www.lightningdesignsystem.com/',
 'maker': 'Salesforce',
 'fit': 'Record-heavy CRM and admin apps.',
 'tone': 'Unconfirmed.',
 'principles': 'Density, scannable records, and one clear path through a form. Motion is named '
               'kinetics.',
 'color': 'A blue brand on a gray page, with semantic colors for success, warning, and error.',
 'typography': 'A sans scale from page header to small meta text.',
 'spacing': 'A spacing scale tied to component padding.',
 'shape': 'Slightly rounded controls.',
 'elevation': 'Modals and menus are elevated. Record pages are flat.',
 'layout': 'Templates for record home, list view, and related lists.',
 'logo': 'Unconfirmed.',
 'icons': 'A large utility and standard icon set.',
 'motion': 'Unconfirmed.',
 'components': 'Button, input, data table, path, modal, and global header.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep record and list patterns only if the product is record-shaped. Replace Salesforce '
          'blue and the global header.',
 'fonts': [{'role': 'UI', 'name': 'Salesforce Sans', 'note': 'Lightning default'},
           {'role': 'Fallback',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'web substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Salesforce Lightning Design System icons',
                'url': 'https://www.lightningdesignsystem.com/icons/',
                'note': 'utility / standard / action'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#c9c7c5;\n'
        '  --soft:#f3f3f3;\n'
        '  --accent:#0176d3;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'dark-industrial', 'soft'],
 'dont': "Don't hide record identity, or build sparse marketing pages where list/detail density is "
         'the product.',
 'primary': '#0176d3'},
{'id': 'mantine',
 'name': 'Mantine',
 'source': 'https://mantine.dev/',
 'maker': 'Mantine',
 'fit': 'Full-featured React component library for dense SaaS dashboards and forms.',
 'tone': 'Unconfirmed.',
 'principles': 'Batteries included: forms, dates, overlays, and hooks under one theme. Consistent '
               'radius and spacing across a large set.',
 'color': 'Primary and gray scales plus semantic colors; CSS variables in v7+.',
 'typography': 'Theme font family with heading/body sizes; often Inter or system sans.',
 'spacing': 'Numeric spacing scale used by layout and components.',
 'shape': 'Global radius (xs–xl) applied across controls.',
 'elevation': 'Shadow scale for papers, modals, and menus.',
 'layout': 'AppShell, Grid, Stack, Group for admin layouts.',
 'logo': 'Unconfirmed.',
 'icons': 'Tabler Icons are the first-party companion set.',
 'motion': 'Unconfirmed.',
 'components': 'AppShell, DataTable patterns, Forms, DatePickers, Modals, Notifications.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Focus and keyboard behavior on overlays and menus.',
 'themes': 'Light and dark via CSS variables.',
 'adapt': 'Keep AppShell density and CSS-variable theming. Swap primary blue and fonts to match '
          'the tone.',
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'typical Mantine apps'},
           {'role': 'Mono', 'name': 'JetBrains Mono / IBM Plex Mono', 'note': 'code blocks'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Tabler Icons',
                'url': 'https://tabler.io/icons',
                'note': 'official pairing'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#dee2e6;\n'
        '  --soft:#f8f9fa;\n'
        '  --accent:#228be6;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'soft', 'swiss'],
 'dont': "Don't import every Mantine package into a minimal product, or ignore the global "
         'radius/spacing theme.',
 'primary': '#228be6'},
{'id': 'material-3',
 'name': 'Material 3',
 'source': 'https://m3.material.io/',
 'maker': 'Google',
 'fit': 'Cross-platform apps that generate color, type, and elevation from one source color.',
 'tone': 'Unconfirmed.',
 'principles': "One visual language across platforms, with room for a product's own brand. Color "
               'roles come from a source color. Surfaces stack by elevation. Motion explains where '
               'an element came from.',
 'color': 'Dynamic roles: primary, secondary, tertiary, surface, outline, and error, each with a '
          'container and an on-color. Light and dark schemes are generated from the same roles.',
 'typography': 'A type scale from display through headline, title, body, and label, in large, '
               'medium, and small.',
 'spacing': 'Padding and gap follow a 4px rhythm. Window margins change by window-size class.',
 'shape': 'A shape scale from none to full, applied per component corner.',
 'elevation': 'Tonal elevation. Higher surfaces are a lighter tint in the light scheme and a '
              'lighter overlay in the dark scheme, not only a drop shadow.',
 'layout': 'Canonical layouts and window-size classes for compact, medium, and expanded.',
 'logo': 'Unconfirmed.',
 'icons': 'Material Symbols, with weight, grade, and optical size.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, FAB, navigation bar and rail, top app bar, sheets, dialogs, lists, chips, '
               'and text fields, with pressed and dragged states.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark, plus contrast variants. A single source color retints the scheme.',
 'adapt': 'Keep the role model, the type scale, and tonal elevation. Choose a source color and '
          'type that belong to this product. Drop Android-only patterns on the web.',
 'fonts': [{'role': 'UI / all',
            'name': 'Roboto',
            'url': 'https://fonts.google.com/specimen/Roboto',
            'note': 'Material default'},
           {'role': 'Alt web', 'name': 'Google Sans / Roboto Flex', 'note': 'brand / variable'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Material Symbols',
                'url': 'https://fonts.google.com/icons',
                'note': 'weight / grade / opsz'}],
 'css': '.t{\n'
        '  --bg:#fef7ff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#cac4d0;\n'
        '  --soft:#e8def8;\n'
        '  --accent:#6750a4;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:16px;\n'
        '  --radius-sm:20px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n'
        '.t .btn{border-radius:20px}.t .chip.on{border-radius:8px}\n',
 'tones': ['soft', 'aurora', 'liquid-glass'],
 'dont': "Don't hard-code Android-only patterns on the web, or skip tonal roles for flat one-off "
         'hexes.',
 'primary': '#6750a4'},
{'id': 'netflix',
 'name': 'Netflix (public brand)',
 'source': 'https://netflixtechblog.com/hawkins-diving-into-the-reasoning-behind-our-design-system-964a7357547',
 'maker': 'Netflix',
 'fit': 'Dark cinematic SaaS / media product language — red CTA, charcoal surfaces. Hawkins '
        '(internal) is not fully public.',
 'tone': 'Unconfirmed.',
 'principles': 'Hawkins powers Studio tools internally; the public Netflix product language is '
               'high-contrast, content-first, and CTA-clear. Use public brand cues when adapting — '
               'do not invent private Hawkins APIs.',
 'color': 'Black / charcoal surfaces (`#141414`), white text, Netflix red `#E50914` for primary '
          'action.',
 'typography': 'Netflix Sans for brand; geometric sans substitute on the web (Inter / Bebas for '
               'display sparingly).',
 'spacing': 'Comfortable media grids; denser in tool UIs.',
 'shape': 'Small-to-medium radii (~4–8px); pill CTAs on consumer surfaces.',
 'elevation': 'Overlays and dimming over drop shadows.',
 'layout': 'Poster rails and hero for consumer; denser tool chrome when building Studio-like SaaS.',
 'logo': 'Unconfirmed.',
 'icons': 'Simple light icons on dark; avoid colorful icon grids.',
 'motion': 'Unconfirmed.',
 'components': 'Unconfirmed. — no public component library; adapt buttons, lists, and modals to '
               'the brand language.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed. — verify contrast on red CTAs and dark charcoal panels.',
 'themes': 'Dark-first product language; light is uncommon for Netflix brand UI.',
 'adapt': 'Keep red action + dark charcoal climate only if the product tone wants cinematic media '
          'energy. Never claim full Hawkins access — fill Unconfirmed fields for this product.',
 'fonts': [{'role': 'UI', 'name': 'Netflix Sans', 'note': 'brand face (licensed)'},
           {'role': 'Web',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Lucide',
                'url': 'https://lucide.dev/',
                'note': 'light stroke on dark'}],
 'css': '.t{\n'
        '  --bg:#141414;\n'
        '  --fg:#fff;\n'
        '  --muted:#b3b3b3;\n'
        '  --line:#333;\n'
        '  --soft:#181818;\n'
        '  --accent:#E50914;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#E50914;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:4px;\n'
        '  --radius-sm:4px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid #333;\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['dark-industrial', 'maximalism', 'cyberpunk'],
 'dont': "Don't use Netflix wordmarks, or pretend Hawkins is an open npm library.",
 'primary': '#E50914'},
{'id': 'pajamas',
 'name': 'Pajamas',
 'source': 'https://design.gitlab.com/',
 'maker': 'GitLab',
 'fit': 'Developer-tool and DevOps SaaS — content-heavy product UI with clear hierarchy.',
 'tone': 'Unconfirmed.',
 'principles': 'Progressive, inclusive, and intentional. Product UI stays readable in dense '
               'workflows.',
 'color': 'UI gray scale plus blue action and status colors; dark mode support.',
 'typography': 'GitLab Sans / system sans with a documented type scale.',
 'spacing': '4px-based spacing scale.',
 'shape': 'Modest border radii on controls and cards.',
 'elevation': 'Borders first; shadows for overlays.',
 'layout': 'Contextual navigation, content, and sidebar patterns for product sections.',
 'logo': 'Unconfirmed.',
 'icons': 'GitLab SVG icon set.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, forms, navigation, data display, and feedback components.',
 'patterns': 'Unconfirmed.',
 'content': 'Voice and tone guidance in Pajamas.',
 'accessibility': 'Documented contrast and interaction guidance.',
 'themes': 'Light and dark.',
 'adapt': 'Keep the productive gray UI and status colors. Replace GitLab brand orange/purple where '
          'it would read as GitLab.',
 'fonts': [{'role': 'UI', 'name': 'GitLab Sans', 'note': 'Pajamas product type'},
           {'role': 'Fallback',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'web substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'GitLab SVGs',
                'url': 'https://gitlab-org.gitlab.io/gitlab-svgs/',
                'note': 'UI icons'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#6b6680;\n'
        '  --line:#dcdcde;\n'
        '  --soft:#fbfafd;\n'
        '  --accent:#fc6d26;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['calm-density', 'swiss', 'terminal'],
 'dont': "Don't style DevOps workflows like a lifestyle marketing site.",
 'primary': '#fc6d26'},
{'id': 'paste',
 'name': 'Paste',
 'source': 'https://paste.twilio.design/',
 'maker': 'Twilio',
 'fit': 'Messaging, account, and support products built from a theme of tokens.',
 'tone': 'Unconfirmed.',
 'principles': 'Compose with primitives and tokens. A theme package and a theme provider supply '
               'every value. Accessibility belongs to the component.',
 'color': 'Background, text, border, and data-visualization tokens, plus error, warning, success, '
          'and neutral.',
 'typography': 'A sans family with heading, text, and display styles.',
 'spacing': 'A space scale consumed by stack and box primitives.',
 'shape': 'Radii for controls and cards. Shadows are tokens.',
 'elevation': 'Shadow tokens for card and overlay.',
 'layout': 'Page composition from stack, grid, and column primitives.',
 'logo': 'Unconfirmed.',
 'icons': 'A product icon set plus illustrative icons.',
 'motion': 'Unconfirmed.',
 'components': 'Button, input, modal, alert, table, and tabs. Patterns combine those components. '
               'Each one reads tokens only.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the rule that components only use tokens from the theme. Retheme color and type '
          'for this product.',
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'Paste default sans'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Paste icons',
                'url': 'https://paste.twilio.design/components/icons',
                'note': 'product + illustrative'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e1e3ea;\n'
        '  --soft:#f4f4f6;\n'
        '  --accent:#001489;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'swiss'],
 'dont': "Don't hard-code Twilio brand blue into a non-Twilio product without retokenizing, or "
         'ignore theme-driven roles.',
 'primary': '#001489'},
{'id': 'polaris',
 'name': 'Polaris',
 'source': 'https://polaris.shopify.com/',
 'maker': 'Shopify',
 'fit': 'Commerce admin, checkout, and point of sale.',
 'tone': 'Unconfirmed.',
 'principles': 'One UI framework, built on web components, shared by Shopify admin, checkout, '
               'customer accounts, and Point of Sale. Each surface exposes its own subset of '
               'components.',
 'color': 'Unconfirmed.',
 'typography': 'Unconfirmed.',
 'spacing': 'Unconfirmed.',
 'shape': 'Unconfirmed.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Web components for admin, checkout, customer accounts, and Point of Sale. A '
               'surface does not get the full set.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the idea of one commerce framework with a smaller set per surface. Open the source '
          "before using a color, type size, space, or shadow. Replace Shopify's brand.",
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'Polaris web'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Polaris icons',
                'url': 'https://polaris.shopify.com/icons',
                'note': 'commerce admin'}],
 'css': '.t{\n'
        '  --bg:#f6f6f7;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e1e3e5;\n'
        '  --soft:#fff;\n'
        '  --accent:#2c6ecb;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:8px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'minimalism', 'calm-density'],
 'dont': "Don't style merchant admin like a consumer storefront, or drop the commerce nouns "
         '(orders, products, customers).',
 'primary': '#2c6ecb'},
{'id': 'primer',
 'name': 'Primer',
 'source': 'https://primer.style/',
 'maker': 'GitHub',
 'fit': 'Developer tools and content-heavy product UI.',
 'tone': 'Unconfirmed.',
 'principles': 'Functional, accessible, and restrained. Color carries meaning. Interface chrome '
               'stays quiet so content leads.',
 'color': 'Functional roles for foreground, background, border, accent, success, attention, '
          'danger, and done. Light, dark, and high-contrast themes share those names.',
 'typography': 'System and monospace stacks for product and code. Roles for title, body, and '
               'caption.',
 'spacing': 'A numeric space scale for padding, gap, and control height.',
 'shape': 'Small radii. Many controls are lightly rounded or square.',
 'elevation': 'Overlays use a shadow plus a border. Most surfaces are flat.',
 'layout': 'Page, pane, and split layouts for tools. Responsive breakpoints for narrow viewports.',
 'logo': 'Unconfirmed.',
 'icons': 'Octicons, a 16px-first UI icon set.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, forms, navigation, dialogs, and data lists, with a strong focus state.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light, dark, and high-contrast modes share the same role names.',
 'adapt': 'Keep the functional color roles, the quiet chrome, and the focus treatment. Change the '
          'accent and type so it is not GitHub.',
 'fonts': [{'role': 'UI',
            'name': 'System stack (−apple-system, Segoe UI, …)',
            'note': 'Primer product'},
           {'role': 'Mono', 'name': 'SFMono / Consolas / Liberation Mono', 'note': 'code'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Octicons',
                'url': 'https://primer.style/foundations/icons',
                'note': '16px-first'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#656d76;\n'
        '  --line:#d0d7de;\n'
        '  --soft:#f6f8fa;\n'
        '  --accent:#1f883d;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['swiss', 'calm-density', 'terminal'],
 'dont': "Don't loud-up the chrome, or abandon functional color roles for decorative gradients.",
 'primary': '#1f883d'},
{'id': 'shadcn',
 'name': 'shadcn/ui',
 'source': 'https://ui.shadcn.com/',
 'maker': 'shadcn',
 'fit': 'Copy-paste Radix + Tailwind components for modern product and AI SaaS UIs.',
 'tone': 'Unconfirmed.',
 'principles': 'You own the code. Accessible primitives (Radix) styled with tokens (CSS variables) '
               'and Tailwind utilities.',
 'color': 'CSS variables for background, foreground, primary, muted, border, destructive — '
          'light/dark.',
 'typography': 'Utility-driven type; Inter or Geist are common defaults.',
 'spacing': 'Tailwind spacing scale; consistent gap/padding utilities.',
 'shape': 'Radius CSS variable (often ~0.5rem); rounded controls.',
 'elevation': 'Subtle borders and shadows; cards over heavy skeuomorphism.',
 'layout': 'Flexible — sidebar + main patterns appear in blocks/examples.',
 'logo': 'Unconfirmed.',
 'icons': 'Lucide is the default icon set in examples.',
 'motion': 'Unconfirmed.',
 'components': 'Button, Dialog, Form, Table, Sheet, Dropdown — copied into the repo, not an npm '
               'megabrundle.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Inherited from Radix primitives.',
 'themes': 'Light and dark via class/CSS variables.',
 'adapt': 'Keep the token CSS variables and Radix accessibility. Restyle primary/radius/fonts for '
          "the chosen tone — don't stay locked to the demo zinc look.",
 'fonts': [{'role': 'UI',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'docs default'},
           {'role': 'Alt',
            'name': 'Geist',
            'url': 'https://vercel.com/font',
            'note': 'common in Next apps'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Lucide',
                'url': 'https://lucide.dev/',
                'note': 'default in shadcn examples'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#71717a;\n'
        '  --line:#e4e4e7;\n'
        '  --soft:#f4f4f5;\n'
        '  --accent:#18181b;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['minimalism', 'calm-density', 'aurora'],
 'dont': "Don't treat shadcn as an untouchable library — the point is owned, adapted code.",
 'primary': '#18181b'},
{'id': 'spark',
 'name': 'Spark UI (Netlify)',
 'source': 'https://spark-ui-docs.netlify.com/',
 'maker': 'Netlify',
 'fit': 'Netlify product and marketing foundations — tokens, components, and light/dark theming '
        'for web SaaS.',
 'tone': 'Unconfirmed.',
 'principles': 'Token-first (`--ntl-*`) foundations with composable Astro components. Semantic '
               'colors flip for light/dark.',
 'color': 'Semantic tokens for bg/text/border/state; Netlify teal/cyan as brand action.',
 'typography': 'Product sans from Netlify tokens; Inter-like web feel.',
 'spacing': 'Tokenized spacing scale via Spark foundations.',
 'shape': 'Rounded controls; modern web radii.',
 'elevation': 'Soft cards and sections over heavy skeuomorphism.',
 'layout': 'PageSection and content blocks for product/marketing hybrid pages.',
 'logo': 'Unconfirmed.',
 'icons': 'SVG slots; pair with Lucide or Netlify marks.',
 'motion': 'Unconfirmed.',
 'components': 'Button, Card, PageSection, HeadingBlock, and related Spark UI pieces.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light and dark via `data-theme` / prefers-color-scheme.',
 'adapt': 'Keep `--ntl` semantic roles and theme flipping. Replace Netlify teal if the brand isn’t '
          'Netlify.',
 'fonts': [{'role': 'UI',
            'name': 'Inter / Netlify sans',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'web default'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Lucide',
                'url': 'https://lucide.dev/',
                'note': 'common pairing'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#cceceb;\n'
        '  --soft:#f5fffe;\n'
        '  --accent:#05BDBA;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:8px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'aurora', 'minimalism'],
 'dont': "Don't keep Netlify wordmarks on a non-Netlify product.",
 'primary': '#05BDBA'},
{'id': 'spectrum',
 'name': 'Spectrum',
 'source': 'https://spectrum.adobe.com/',
 'maker': 'Adobe',
 'fit': 'Creative tools with separate mobile and desktop scales.',
 'tone': 'Unconfirmed.',
 'principles': 'Writing is part of the system: voice, grammar, inclusivity, and error messages.',
 'color': 'Unconfirmed.',
 'typography': 'Separate type scales for mobile and desktop. Mobile components are 25% larger than '
               'desktop, a 1:1.25 ratio.',
 'spacing': 'Unconfirmed.',
 'shape': 'Border widths stay consistent across components.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Unconfirmed.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the mobile and desktop scales and the consistent border width. Open the source '
          "before using a color, space, or shadow. Replace Adobe's brand.",
 'fonts': [{'role': 'UI', 'name': 'Adobe Clean', 'note': 'Spectrum product type'},
           {'role': 'Fallback',
            'name': 'Source Sans 3',
            'url': 'https://fonts.google.com/specimen/Source+Sans+3',
            'note': 'open adjacent'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Spectrum icons / Workflow icons',
                'url': 'https://spectrum.adobe.com/page/iconography/',
                'note': 'Adobe'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e1e1e1;\n'
        '  --soft:#f5f5f5;\n'
        '  --accent:#0265dc;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:4px;\n'
        '  --radius-sm:16px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'bauhaus', 'editorial'],
 'dont': "Don't collapse mobile and desktop scales into one cramped density, or style creative "
         'tools like a CRM table farm.',
 'primary': '#0265dc'},
{'id': 'stripe',
 'name': 'Stripe Apps UI',
 'source': 'https://docs.stripe.com/stripe-apps/components',
 'maker': 'Stripe',
 'fit': 'Stripe Dashboard–aligned SaaS chrome — calm finance UI, purple action, dense tables and '
        'drawers.',
 'tone': 'Unconfirmed.',
 'principles': 'Match Stripe Dashboard quality. Components and tokens keep apps consistent with '
               'Stripe’s product language.',
 'color': 'Neutrals with Stripe purple (`#635BFF`) for primary action; semantic intents for '
          'danger/success.',
 'typography': 'Camera Plain / Söhne-adjacent product type; Inter is a common public substitute.',
 'spacing': 'Stripe layout tokens via Box/Inline in the Apps SDK.',
 'shape': 'Soft small radii; refined, not playful.',
 'elevation': 'Drawers and overlays; flat lists/tables in the main pane.',
 'layout': 'ContextView drawer beside Dashboard content; FocusView for deep flows; SettingsView '
           'for config.',
 'logo': 'Unconfirmed.',
 'icons': 'Stripe Apps icon set in the UI extension SDK.',
 'motion': 'Unconfirmed.',
 'components': 'Button, DataTable, Banner, Tabs, Accordion, forms — from '
               '`@stripe/ui-extension-sdk/ui`.',
 'patterns': 'Documented Stripe Apps patterns for Dashboard extensions.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Aligned to Stripe Dashboard light product UI.',
 'adapt': 'Keep purple action + calm finance density when the tone fits. Outside Stripe Apps, '
          'reimplement tokens — don’t assume the SDK ships for any host.',
 'fonts': [{'role': 'UI', 'name': 'Camera Plain / Söhne', 'note': 'Stripe product type'},
           {'role': 'Web',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'common substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Stripe Apps icons',
                'url': 'https://docs.stripe.com/stripe-apps/components',
                'note': 'SDK set'},
               {'role': 'Alt',
                'name': 'Lucide',
                'url': 'https://lucide.dev/',
                'note': 'outside the SDK'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e3e8ee;\n'
        '  --soft:#f6f9fc;\n'
        '  --accent:#635BFF;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:6px;\n'
        '  --radius-sm:6px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'calm-density', 'minimalism'],
 'dont': "Don't paste Stripe’s marketing gradient mesh into ops tables, or use Stripe wordmarks "
         'off-brand.',
 'primary': '#635BFF'},
{'id': 'uber-base',
 'name': 'Base',
 'source': 'https://base.uber.com/',
 'maker': 'Uber',
 'fit': 'One foundation shared across many Uber products.',
 'tone': 'Unconfirmed.',
 'principles': "One foundation for Uber's products: system principles, a design language, "
               'components, patterns, and extensions for product verticals.',
 'color': 'Unconfirmed.',
 'typography': 'Unconfirmed.',
 'spacing': 'Unconfirmed.',
 'shape': 'Unconfirmed.',
 'elevation': 'Unconfirmed.',
 'layout': 'Unconfirmed.',
 'logo': 'Unconfirmed.',
 'icons': 'Unconfirmed.',
 'motion': 'Unconfirmed.',
 'components': 'Shared components, plus extension patterns for product verticals. Exact names are '
               'Unconfirmed.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Unconfirmed.',
 'adapt': 'Keep the idea of one foundation shared by many products. Open the source before using a '
          "color, type size, space, or shadow. Replace Uber's brand.",
 'fonts': [{'role': 'UI', 'name': 'Uber Move / Inter', 'note': 'Base foundation'},
           {'role': 'Web',
            'name': 'Inter',
            'url': 'https://fonts.google.com/specimen/Inter',
            'note': 'common'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Base icons / Uber icon set',
                'url': 'https://baseweb.design/components/icon/',
                'note': 'Base Web'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#e2e2e2;\n'
        '  --soft:#f6f6f6;\n'
        '  --accent:#000000;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:8px;\n'
        '  --shadow:none;\n'
        '  --font:Inter, ui-sans-serif, system-ui, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['minimalism', 'swiss', 'calm-density'],
 'dont': "Don't fork a separate visual language per product if Base is the shared foundation, or "
         'overload the UI with decorative brand noise.',
 'primary': '#000000'},
{'id': 'uswds',
 'name': 'U.S. Web Design System',
 'source': 'https://designsystem.digital.gov/',
 'maker': 'U.S. Government (TTS / GSA)',
 'fit': 'Public-sector services and accessible government SaaS-style portals.',
 'tone': 'Unconfirmed.',
 'principles': 'Trustworthy, accessible, and consistent across agencies. Proven components over '
               'novelty.',
 'color': 'USWDS theme tokens; Americana blues/reds used carefully; strong focus styles.',
 'typography': 'Source Sans Pro / Public Sans and Merriweather for content.',
 'spacing': 'USWDS spacing units for forms and pages.',
 'shape': 'Mostly rectangular; modest rounding.',
 'elevation': 'Minimal; clarity over depth.',
 'layout': 'Government site patterns: header, footer, forms, step indicators.',
 'logo': 'Unconfirmed.',
 'icons': 'USWDS icon sprite / Material-derived set in docs.',
 'motion': 'Unconfirmed.',
 'components': 'Accordion, alert, form controls, identifier, step indicator, table.',
 'patterns': 'Unconfirmed.',
 'content': 'Plain language expectations.',
 'accessibility': 'Section 508 / WCAG-oriented guidance.',
 'themes': 'Themeable tokens per agency.',
 'adapt': 'Keep accessibility and plain-language forms. Do not use USWDS branding on '
          'non-government products without adaptation.',
 'fonts': [{'role': 'UI / body',
            'name': 'Public Sans',
            'url': 'https://public-sans.digital.gov/',
            'note': 'USWDS sans'},
           {'role': 'Content',
            'name': 'Merriweather',
            'url': 'https://fonts.google.com/specimen/Merriweather',
            'note': 'serif content'},
           {'role': 'Alt',
            'name': 'Source Sans 3',
            'url': 'https://fonts.google.com/specimen/Source+Sans+3',
            'note': 'legacy adjacent'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'USWDS icons',
                'url': 'https://designsystem.digital.gov/components/icon/',
                'note': 'sprite / SVG'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#1b1b1b;\n'
        '  --soft:#f0f0f0;\n'
        '  --accent:#005ea2;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:0;\n'
        '  --radius-sm:2px;\n'
        '  --shadow:none;\n'
        "  --font:'Public Sans', Source Sans 3, sans-serif;\n"
        '  --weight:700;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['swiss', 'minimalism', 'editorial'],
 'dont': "Don't use US flag/gov identifiers on private commercial products.",
 'primary': '#005ea2'},
{'id': 'vibe',
 'name': 'Vibe',
 'source': 'https://vibe.monday.com/',
 'maker': 'monday.com',
 'fit': 'Work-management and board-based SaaS with colorful, friendly product UI.',
 'tone': 'Unconfirmed.',
 'principles': 'Energetic but structured. Boards, statuses, and people-centric components stay '
               'consistent.',
 'color': 'Bright status colors on neutral chrome; brand blue for primary actions.',
 'typography': 'Poppins / product sans for UI (monday.com language).',
 'spacing': 'Comfortable board and table spacing — denser than marketing, friendlier than ops.',
 'shape': 'Rounded controls and chips for statuses.',
 'elevation': 'Soft elevation for menus and dialogs.',
 'layout': 'Board, table, and item-detail layouts.',
 'logo': 'Unconfirmed.',
 'icons': 'Vibe / monday.com icons.',
 'motion': 'Unconfirmed.',
 'components': 'Buttons, inputs, boards UI, dialogs, and avatars from @vibe/core.',
 'patterns': 'Unconfirmed.',
 'content': 'Unconfirmed.',
 'accessibility': 'Unconfirmed.',
 'themes': 'Light primary; dark where supported.',
 'adapt': 'Keep status-color clarity and board metaphors. Replace monday.com brand blue/wordmark.',
 'fonts': [{'role': 'UI',
            'name': 'Poppins',
            'url': 'https://fonts.google.com/specimen/Poppins',
            'note': 'monday.com UI feel'},
           {'role': 'Alt', 'name': 'Figtree / Inter', 'note': 'substitute'}],
 'icon_libs': [{'role': 'Primary',
                'name': 'Vibe icons',
                'url': 'https://vibe.monday.com/',
                'note': 'monday.com set'}],
 'css': '.t{\n'
        '  --bg:#fff;\n'
        '  --fg:#111;\n'
        '  --muted:#737373;\n'
        '  --line:#d0d4e4;\n'
        '  --soft:#f6f7fb;\n'
        '  --accent:#6161ff;\n'
        '  --accent-fg:#fff;\n'
        '  --danger:#b91c1c;\n'
        '  --danger-fg:#fff;\n'
        '  --radius:8px;\n'
        '  --radius-sm:20px;\n'
        '  --shadow:none;\n'
        '  --font:Poppins, Inter, sans-serif;\n'
        '  --weight:600;\n'
        '  --tracking:0;\n'
        '  --stage-border:1px solid var(--line);\n'
        '  --blur:none;\n'
        '  --saturate:100%;\n'
        '}\n'
        '\n'
        '.t .btn{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .chip.on{background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}\n'
        '.t .nav-item.on,.t .nav .on{color:var(--accent)}\n'
        '.t .tag:not(.muted){border-color:var(--accent);color:var(--accent)}\n',
 'tones': ['soft', 'clay', 'calm-density'],
 'dont': "Don't mute all status color into gray — boards need scannable state.",
 'primary': '#6161ff'},
]
