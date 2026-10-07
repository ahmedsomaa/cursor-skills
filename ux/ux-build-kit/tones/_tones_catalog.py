# Tone data for render.py — imported at generation time.
# Wireframe HTML is shared (Harbor set in render.py); only `.t` CSS variables change the look.

def _t_css(**kw: str) -> str:
    """Build a `.t { --vars }` block. Unknown keys ignored."""
    defaults = {
        "bg": "#fff",
        "fg": "#111",
        "muted": "#737373",
        "line": "#d4d4d4",
        "soft": "#f5f5f5",
        "accent": "#111",
        "accent_fg": "#fff",
        "danger": "#b91c1c",
        "danger_fg": "#fff",
        "radius": "0",
        "radius_sm": "0",
        "shadow": "none",
        "font": "Inter, ui-sans-serif, system-ui, sans-serif",
        "weight": "600",
        "tracking": "0",
        "stage_border": "1px solid var(--line)",
    }
    defaults.update(kw)
    lines = [f"  --{k.replace('_', '-')}:{v};" for k, v in defaults.items()]
    return ".t{\n" + "\n".join(lines) + "\n}\n"


TONES: list[dict] = [
{
        "id": "swiss",
        "name": "Swiss",
        "fit": "Grid-led modernist clarity — objective, typographic, little ornament.",
        "principles": [
            "Structure is the beauty; alignment beats decoration.",
            "One signal accent; neutrals do the rest.",
            "Hierarchy from type scale and rules, not shadow theater.",
        ],
        "layout": [
            "Modular or asymmetric grid with visible columns/margins.",
            "Hairline separators instead of soft card stacks.",
            "Reading column or split content ‖ meta sidebar.",
        ],
        "colors": [
            "Black / white / gray base.",
            "One sharp signal (often red or brand primary).",
            "No gradients; flat semantic status only when needed.",
        ],
        "radius": "square",
        "anatomy": [
            "Hairline 1px borders; no soft elevation.",
            "Flush-left type blocks; sharp rectangular chrome.",
        ],
        "type": [
            "Neo-grotesk / grotesque sans throughout.",
            "Strong modular type scale; asymmetric headlines OK.",
            "Avoid display serif and playful rounded faces.",
        ],
        "fonts": [
            {"role": "UI / body", "name": "Inter", "url": "https://fonts.google.com/specimen/Inter", "note": "neutral grotesque"},
            {"role": "UI alt", "name": "Helvetica Neue / Arial", "note": "system fallback stack"},
            {"role": "Display", "name": "Neue Haas Grotesk", "note": "or Akzidenz-Grotesk"},
        ],
        "icons": [
            "Thin geometric stroke icons.",
            "Optical square alignment to the grid.",
            "No filled candy icons or skeuomorphic glyphs.",
        ],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "24px stroke"},
            {"role": "Alt", "name": "Phosphor (thin/light)", "url": "https://phosphoricons.com/", "note": "geometric"},
        ],
        "systems_ours": ["govuk", "primer", "atlassian"],
        "systems_other": ["IBM Carbon (restrained)", "Helvetica-era brand systems"],
        "examples": [
            ("GOV.UK Design System", "https://design-system.service.gov.uk/"),
            ("Braun", "https://www.braun.com/"),
            ("The Guardian", "https://www.theguardian.com/"),
            ("International Typographic Style", "https://en.wikipedia.org/wiki/International_Typographic_Style"),
            ("IBM Plex", "https://www.ibm.com/plex/"),
        ],
        "do": "Strict grid, grotesque sans, hairline rules, one signal color.",
        "dont": "Soft blobs, clay shapes, or multi-accent rainbows.",
        "css": _t_css(accent="#e11", accent_fg="#fff", line="#111", soft="#f5f5f5", radius="0", radius_sm="0", tracking="0.02em"),
    },
{
        "id": "minimalism",
        "name": "Minimalism",
        "fit": "Zen reduction — one clear action, intentional empty space.",
        "principles": ["Every element must earn its place.", "One primary action per view.", "Silence (space) is a material."],
        "layout": ["Centered or single-column hero for key tasks.", "Progressive disclosure for secondary actions.", "Huge margins; avoid multi-panel dashboards as default."],
        "colors": ["Near-monochrome fields.", "Single CTA color.", "No decorative gradients."],
        "radius": "pill",
        "anatomy": ["Almost no borders; separate with space.", "Pill CTAs; ghost secondary actions."],
        "type": ["Few sizes (3–4). Medium UI weights.", "Neutral grotesque or humanist sans.", "No mixed display circus."],
        "fonts": [
            {"role": "UI / body", "name": "Inter", "url": "https://fonts.google.com/specimen/Inter", "note": "or SF Pro"},
            {"role": "Reading", "name": "iA Writer Quattro", "url": "https://ia.net/topics/in-search-of-the-perfect-writing-font", "note": "calm proportional"},
            {"role": "Alt", "name": "Söhne / Neue Montreal", "note": "premium neutral"},
        ],
        "icons": ["Sparse outline icons only when needed.", "Prefer text labels over icon grids.", "Same stroke weight as type hairlines."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "use sparingly"},
            {"role": "Alt", "name": "Heroicons (outline)", "url": "https://heroicons.com/", "note": "thin"},
        ],
        "systems_ours": ["primer", "polaris", "paste"],
        "systems_other": ["Apple HIG (restraint)", "iA-inspired reading UIs"],
        "examples": [
            ("iA Writer", "https://ia.net/writer"),
            ("Things 3", "https://culturedcode.com/things/"),
            ("Apple", "https://www.apple.com/"),
            ("Stripe Press", "https://press.stripe.com/"),
            ("Notion (blank canvas)", "https://www.notion.com/"),
        ],
        "do": "One CTA, quiet fields, progressive disclosure.",
        "dont": "Competing actions or dense chrome.",
        "css": _t_css(bg="#fafafa", soft="#fafafa", line="#eee", muted="#a3a3a3", accent="#111", radius="16px", radius_sm="999px", stage_border="1px solid #eee", weight="500"),
    },
{
        "id": "maximalism",
        "name": "Maximalism",
        "fit": "More is more — layered color, mixed type, dense visual rhythm.",
        "principles": ["Controlled excess; personality on every surface.", "Clash is allowed if a reading path remains.", "Ornament is content."],
        "layout": ["Overlapping modules and tilted accents.", "Dense stacks; unequal tile sizes.", "Pattern backgrounds behind content."],
        "colors": ["Saturated multi-hue.", "Patterns and gradients welcome.", "Keep CTA still legible."],
        "radius": "square",
        "anatomy": ["Hard borders + loud fills.", "Mixed decorative frames OK if hierarchy holds."],
        "type": ["Mix display + UI sans (even serif+sans).", "Huge weight contrast.", "Short punchy labels."],
        "fonts": [
            {"role": "Display", "name": "Syne", "url": "https://fonts.google.com/specimen/Syne", "note": "loud geometric"},
            {"role": "UI", "name": "Space Grotesk", "url": "https://fonts.google.com/specimen/Space+Grotesk", "note": "quirky grotesque"},
            {"role": "Accent", "name": "Playfair Display", "url": "https://fonts.google.com/specimen/Playfair+Display", "note": "serif clash"},
        ],
        "icons": ["Filled or mixed styles OK.", "Can be illustrative.", "Avoid timid monochrome-only sets."],
        "icon_libs": [
            {"role": "Primary", "name": "Phosphor (fill/duotone)", "url": "https://phosphoricons.com/", "note": "expressive"},
            {"role": "Alt", "name": "Noun Project custom", "url": "https://thenounproject.com/", "note": "illustrative"},
        ],
        "systems_ours": ["gestalt", "ant-design", "material-3"],
        "systems_other": ["Custom brand illustration systems", "Agency portfolio kits"],
        "examples": [("Gumroad", "https://gumroad.com/"), ("Figma Config", "https://config.figma.com/"), ("It's Nice That", "https://www.itsnicethat.com/"), ("Adult Swim", "https://www.adultswim.com/"), ("Memphis Group", "https://en.wikipedia.org/wiki/Memphis_Group")],
        "do": "Layered color and type with a clear reading path.",
        "dont": "Chaos without hierarchy or unreadable CTAs.",
        "css": _t_css(bg="#fff7ed", soft="#ffedd5", line="#ea580c", accent="#db2777", accent_fg="#fff", radius="0", radius_sm="0", shadow="4px 4px 0 #111", font="'Space Grotesk', Inter, sans-serif", weight="700"),
    },
{
        "id": "neo-brutalism",
        "name": "Neo-brutalism",
        "fit": "Raw, loud, high-contrast — thick borders and hard shadows.",
        "principles": ["Visible structure over polish.", "High contrast always.", "Personality over corporate smoothness."],
        "layout": ["Packed sections; little empty luxury.", "Chunky blocks snap to a coarse grid.", "Overlapping hard shadows for depth."],
        "colors": ["Flat saturated fills.", "Black structural borders.", "One or two loud accents max."],
        "radius": "square",
        "anatomy": ["3px solid black borders.", "Hard offset shadow (e.g. 4px 4px 0 #000).", "0px radius everywhere."],
        "type": ["Bold grotesque / display.", "Uppercase CTAs OK.", "High weight contrast."],
        "fonts": [
            {"role": "UI / display", "name": "Space Grotesk", "url": "https://fonts.google.com/specimen/Space+Grotesk", "note": "bold weights"},
            {"role": "Alt", "name": "Archivo Black", "url": "https://fonts.google.com/specimen/Archivo+Black", "note": "impact headlines"},
            {"role": "Body", "name": "IBM Plex Sans", "url": "https://fonts.google.com/specimen/IBM+Plex+Sans", "note": "sturdy grotesque"},
        ],
        "icons": ["Chunky stroke or filled mono.", "Can be slightly crude on purpose.", "No soft duotone illustrations."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide (bold stroke)", "url": "https://lucide.dev/", "note": "stroke-width 2.5"},
            {"role": "Alt", "name": "Phosphor (bold/fill)", "url": "https://phosphoricons.com/", "note": "chunky"},
        ],
        "systems_ours": ["gestalt", "chakra", "mantine"],
        "systems_other": ["Gumroad-era marketing kits", "Indie hacker landing systems"],
        "examples": [("Gumroad", "https://gumroad.com/"), ("Figma marketing", "https://www.figma.com/"), ("Unitap", "https://unitap.app/"), ("Brutalist Websites", "https://brutalistwebsites.com/"), ("Creep Exotics", "https://www.creepexotics.com/")],
        "do": "Thick borders, hard shadows, usable navigation.",
        "dont": "Soft blur, glass, or delicate hairlines as the main language.",
        "css": _t_css(bg="#fef08a", soft="#fde047", line="#000", accent="#000", accent_fg="#fef08a", danger="#000", danger_fg="#fff", radius="0", radius_sm="0", shadow="4px 4px 0 #000", stage_border="3px solid #000", font="'Space Grotesk', Inter, sans-serif", weight="700", tracking="0.02em"),
    },
{
        "id": "soft",
        "name": "Soft",
        "fit": "Friendly cushioned UI — rounded, airy, low-contrast comfort.",
        "principles": ["Comfort over edge.", "Soft elevation, never harsh.", "Approachable language and scale."],
        "layout": ["Generous padding inside cards.", "Stacked single columns on mobile-first.", "Floating panels with soft shadow."],
        "colors": ["Pastel surfaces.", "Low-contrast borders.", "Warm accent for primary actions."],
        "radius": "squircle",
        "anatomy": ["Large continuous corner radii.", "Diffuse shadows; no hard offsets.", "Pill or squircle controls."],
        "type": ["Rounded humanist sans.", "Medium weights; avoid ultra-black.", "Friendly sentence case labels."],
        "fonts": [
            {"role": "UI", "name": "Nunito", "url": "https://fonts.google.com/specimen/Nunito", "note": "rounded humanist"},
            {"role": "Alt", "name": "Plus Jakarta Sans", "url": "https://fonts.google.com/specimen/Plus+Jakarta+Sans", "note": "soft modern"},
            {"role": "System", "name": "SF Pro Rounded", "note": "Apple-like warmth"},
        ],
        "icons": ["Rounded stroke icons.", "Soft duotone or pastel fills OK.", "Match corner language of UI."],
        "icon_libs": [
            {"role": "Primary", "name": "Phosphor (regular/duotone)", "url": "https://phosphoricons.com/", "note": "rounded"},
            {"role": "Alt", "name": "Hugeicons", "url": "https://hugeicons.com/", "note": "friendly stroke"},
        ],
        "systems_ours": ["polaris", "chakra", "fluent-2"],
        "systems_other": ["Consumer wellness apps", "Fintech ‘friendly bank’ kits"],
        "examples": [("Headspace", "https://www.headspace.com/"), ("Notion", "https://www.notion.com/"), ("Calm", "https://www.calm.com/"), ("Linear (soft surfaces)", "https://linear.app/"), ("Stripe Dashboard", "https://stripe.com/")],
        "do": "Rounded panels, soft shadow, warm CTA.",
        "dont": "Harsh black borders or industrial density.",
        "css": _t_css(bg="#fff", soft="#fdf2f8", line="#fbcfe8", muted="#9d174d", accent="#db2777", accent_fg="#fff", radius="20px", radius_sm="14px", shadow="0 8px 24px rgba(219,39,119,.12)", font="Nunito, Inter, sans-serif", weight="600"),
    },
{
        "id": "editorial",
        "name": "Editorial",
        "fit": "Magazine discipline — type-led hierarchy and long-form calm.",
        "principles": ["Typography is the interface.", "Story first; chrome second.", "Whitespace frames reading."],
        "layout": ["Strong column grid for body.", "Pull quotes / rules as structure.", "Sparse chrome; content width locked."],
        "colors": ["Ink on paper neutrals.", "One ink accent for links/CTA.", "Photography can carry color."],
        "radius": "square",
        "anatomy": ["Thin rules under titles.", "Minimal button chrome; text links preferred."],
        "type": ["Display serif + neutral sans.", "Large headline sizes; tight leading on display.", "Small caps / labels for meta."],
        "fonts": [
            {"role": "Display", "name": "Fraunces", "url": "https://fonts.google.com/specimen/Fraunces", "note": "editorial serif"},
            {"role": "Body", "name": "Source Serif 4", "url": "https://fonts.google.com/specimen/Source+Serif+4", "note": "reading"},
            {"role": "UI / meta", "name": "Inter", "url": "https://fonts.google.com/specimen/Inter", "note": "labels"},
        ],
        "icons": ["Minimal; prefer typographic marks.", "Thin stroke when needed.", "No chunky app-icon aesthetic."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "thin, rare"},
            {"role": "Alt", "name": "Typographic only", "note": "rules, bullets, small caps"},
        ],
        "systems_ours": ["primer", "govuk", "carbon"],
        "systems_other": ["News org design systems", "Publisher CMS themes"],
        "examples": [("The New York Times", "https://www.nytimes.com/"), ("Medium", "https://medium.com/"), ("Are.na", "https://www.are.na/"), ("Pitchfork", "https://pitchfork.com/"), ("The Verge", "https://www.theverge.com/")],
        "do": "Serif headlines, calm columns, ink accent links.",
        "dont": "App-dense dashboards as the default reading surface.",
        "css": _t_css(bg="#faf8f5", soft="#f3efe8", line="#d6d3d1", accent="#1c1917", accent_fg="#faf8f5", radius="0", radius_sm="2px", font="Georgia, 'Source Serif 4', serif", weight="600", tracking="-0.01em"),
    },
{
        "id": "liquid-glass",
        "name": "Liquid glass",
        "fit": "Translucent layered panels — light, blur, and specular depth.",
        "principles": [
            "Glass needs something rich behind it — never frost over flat gray.",
            "Depth through translucency and specular edges, not heavy borders.",
            "Keep text contrast; tint glass, don’t wash type out.",
        ],
        "layout": [
            "Floating frosted sheets over vivid or photographic grounds.",
            "Stacked translucent toolbars and panels.",
            "Soft separation; let blur do the hierarchy work.",
        ],
        "colors": [
            "Vivid mesh or photo underlay (always).",
            "White/ice glass with cool blue tint.",
            "Accents that survive blur (saturated blue / system blue).",
        ],
        "radius": "squircle",
        "anatomy": [
            "Large continuous radii; 1px luminous rim.",
            "backdrop-filter blur + saturate; inset specular highlight.",
            "Semi-transparent fills — never opaque white cards.",
        ],
        "type": ["System sans with optical sizing.", "Medium weight UI; light large titles.", "Avoid heavy serif clash."],
        "fonts": [
            {"role": "UI", "name": "SF Pro / Inter", "url": "https://fonts.google.com/specimen/Inter", "note": "system clarity"},
            {"role": "Alt", "name": "Geist", "url": "https://vercel.com/font", "note": "modern UI"},
        ],
        "icons": ["SF-style thin stroke on glass.", "Subtle fill for selected state.", "Match blur panel contrast."],
        "icon_libs": [
            {"role": "Primary", "name": "SF Symbols", "url": "https://developer.apple.com/sf-symbols/", "note": "best match"},
            {"role": "Web alt", "name": "Lucide", "url": "https://lucide.dev/", "note": "thin stroke"},
        ],
        "systems_ours": ["fluent-2", "material-3", "polaris"],
        "systems_other": ["visionOS / iOS materials", "Windows Acrylic patterns"],
        "examples": [
            ("Apple.com", "https://www.apple.com/"),
            ("visionOS materials", "https://developer.apple.com/design/human-interface-guidelines/materials"),
            ("Microsoft Fluent", "https://fluent2.microsoft.design/"),
            ("Arc Browser", "https://arc.net/"),
            ("iOS Control Center", "https://www.apple.com/ios/"),
        ],
        "do": "Frosted panels over color, soft radii, luminous rims.",
        "dont": "Opaque flat cards or glass over empty gray (nothing to refract).",
        "css": _t_css(
            bg="rgba(255,255,255,0.38)",
            soft="rgba(255,255,255,0.28)",
            line="rgba(255,255,255,0.62)",
            muted="#334155",
            accent="rgba(37,99,235,0.92)",
            accent_fg="#fff",
            danger="rgba(225,29,72,0.9)",
            danger_fg="#fff",
            radius="22px",
            radius_sm="14px",
            shadow="0 16px 48px rgba(15,23,42,0.22), inset 0 1px 0 rgba(255,255,255,0.75)",
            stage_border="1px solid rgba(255,255,255,0.55)",
            weight="500",
            blur="blur(18px)",
            saturate="180%",
        )
        + """
.t{
  padding:12px;
  border-radius:24px;
  background:
    radial-gradient(120% 90% at 8% 0%, rgba(125,211,252,.95) 0%, transparent 42%),
    radial-gradient(90% 80% at 92% 12%, rgba(240,171,252,.9) 0%, transparent 40%),
    radial-gradient(80% 70% at 70% 100%, rgba(167,139,250,.85) 0%, transparent 45%),
    radial-gradient(70% 60% at 20% 85%, rgba(52,211,153,.55) 0%, transparent 40%),
    linear-gradient(145deg, #1d4ed8 0%, #7c3aed 42%, #db2777 78%, #f97316 100%);
}
.t .stage{
  background:linear-gradient(160deg, rgba(255,255,255,.52) 0%, rgba(255,255,255,.22) 100%);
  border:1px solid rgba(255,255,255,.58);
  box-shadow:0 18px 50px rgba(15,23,42,.28), inset 0 1px 0 rgba(255,255,255,.85), inset 0 -1px 0 rgba(255,255,255,.15);
}
.t .top,.t .side,.t .grid th{
  background:rgba(255,255,255,.32);
  border-color:rgba(255,255,255,.4);
}
.t .main{background:transparent}
.t .chip{
  background:rgba(255,255,255,.35);
  border-color:rgba(255,255,255,.55);
  color:#1e293b;
}
.t .chip.on{
  background:rgba(37,99,235,.88);
  border-color:rgba(255,255,255,.5);
  color:#fff;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.35);
}
.t .btn{
  background:linear-gradient(180deg, rgba(59,130,246,.95), rgba(37,99,235,.9));
  border-color:rgba(255,255,255,.45);
  box-shadow:0 6px 18px rgba(37,99,235,.35), inset 0 1px 0 rgba(255,255,255,.45);
}
.t .btn.ghost{
  background:rgba(255,255,255,.35);
  color:#0f172a;
  border-color:rgba(255,255,255,.55);
}
.t .panel,.t .modal{
  background:linear-gradient(165deg, rgba(255,255,255,.55), rgba(255,255,255,.28));
  border:1px solid rgba(255,255,255,.6);
  box-shadow:0 12px 36px rgba(15,23,42,.2), inset 0 1px 0 rgba(255,255,255,.8);
}
.t input{
  background:rgba(255,255,255,.45);
  border-color:rgba(255,255,255,.65);
}
""",
    },
{
        "id": "dark-industrial",
        "name": "Dark industrial",
        "fit": "Ops / infra night mode — dense, technical, status-first.",
        "principles": ["Data legibility over decoration.", "Status color is sacred.", "Compact, keyboard-friendly chrome."],
        "layout": ["Dense tables and side rails.", "Fixed utility bars.", "Minimal ornament between panels."],
        "colors": ["Near-black canvas.", "Muted zinc panels.", "Amber/green/red for status only."],
        "radius": "square",
        "anatomy": ["1px cool borders; tiny radii optional.", "Monospace for IDs and metrics."],
        "type": ["Neutral sans + mono for data.", "Compact sizes; tabular nums.", "Uppercase micro-labels."],
        "fonts": [
            {"role": "UI", "name": "IBM Plex Sans", "url": "https://fonts.google.com/specimen/IBM+Plex+Sans", "note": "technical"},
            {"role": "Data", "name": "IBM Plex Mono", "url": "https://fonts.google.com/specimen/IBM+Plex+Mono", "note": "IDs / logs"},
            {"role": "Alt", "name": "JetBrains Mono", "url": "https://www.jetbrains.com/lp/mono/", "note": "code"},
        ],
        "icons": ["Thin technical stroke.", "Monochrome on dark.", "Status dots over playful glyphs."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "mono stroke"},
            {"role": "Alt", "name": "Tabler Icons", "url": "https://tabler.io/icons", "note": "dense UI"},
        ],
        "systems_ours": ["carbon", "primer", "atlassian"],
        "systems_other": ["Grafana / Datadog UI patterns", "Cloud console systems"],
        "examples": [("Vercel Dashboard", "https://vercel.com/dashboard"), ("Linear", "https://linear.app/"), ("Datadog", "https://www.datadoghq.com/"), ("GitHub", "https://github.com/"), ("Stripe Dashboard dark", "https://stripe.com/")],
        "do": "Dark zinc panels, mono metrics, status color sparingly.",
        "dont": "Pastel wellness palettes or huge marketing heroes.",
        "css": _t_css(bg="#0a0a0a", fg="#e5e5e5", soft="#171717", line="#262626", muted="#a3a3a3", accent="#f59e0b", accent_fg="#0a0a0a", danger="#ef4444", danger_fg="#fff", radius="0", radius_sm="2px", font="'IBM Plex Sans', Inter, sans-serif", weight="500"),
    },
{
        "id": "bauhaus",
        "name": "Bauhaus",
        "fit": "Primary geometry — circle, triangle, square as the visual system.",
        "principles": ["Form follows function.", "Primary colors + black/white.", "Geometry is ornament enough."],
        "layout": ["Strong modular blocks.", "Asymmetric balance with primitives.", "Posters-as-UI energy OK."],
        "colors": ["Red / yellow / blue accents.", "Black structure on white.", "No muddy pastels."],
        "radius": "square",
        "anatomy": ["Geometric frames; circular badges.", "Flat fills; no skeuomorphism."],
        "type": ["Geometric sans (Futura-like).", "All caps labels acceptable.", "Circular counters or numerals as motif."],
        "fonts": [
            {"role": "UI / display", "name": "Futura", "note": "or Century Gothic"},
            {"role": "Web", "name": "Josefin Sans", "url": "https://fonts.google.com/specimen/Josefin+Sans", "note": "geometric"},
            {"role": "Alt", "name": "Bauhaus 93 / Archivo", "url": "https://fonts.google.com/specimen/Archivo", "note": "display"},
        ],
        "icons": ["Geometric primitives.", "Circle / triangle / square language.", "No skeuomorphic metaphors."],
        "icon_libs": [
            {"role": "Primary", "name": "Phosphor (regular)", "url": "https://phosphoricons.com/", "note": "geometric"},
            {"role": "Alt", "name": "Custom SVG primitives", "note": "circle/square/triangle"},
        ],
        "systems_ours": ["material-3", "ant-design", "gestalt"],
        "systems_other": ["Museum / education brand systems", "Poster-led campaigns"],
        "examples": [("Bauhaus Archiv", "https://www.bauhaus.de/"), ("Swiss Style posters", "https://en.wikipedia.org/wiki/International_Typographic_Style"), ("Airbnb Cereal (geometric era)", "https://airbnb.design/"), ("Lego", "https://www.lego.com/"), ("Braun design lineage", "https://www.braun.com/")],
        "do": "Primary color geometry, flat modules, geometric sans.",
        "dont": "Skeuomorphic textures or muddy tertiary palettes.",
        "css": _t_css(bg="#fff", soft="#fafafa", line="#111", accent="#e11", accent_fg="#fff", radius="0", radius_sm="0", font="Josefin Sans, Futura, Inter, sans-serif", weight="600", tracking="0.04em"),
    },
{
        "id": "calm-density",
        "name": "Calm density",
        "fit": "Lots of information, still quiet — Linear/Notion-like composure.",
        "principles": ["Density without noise.", "Muted chrome; sharp content.", "Keyboard and scan paths first."],
        "layout": ["Tight rows; consistent 8px rhythm.", "Side nav + dense main.", "Subtle dividers, not card spam."],
        "colors": ["Neutral gray scale.", "One quiet accent.", "Status tints desaturated."],
        "radius": "squircle",
        "anatomy": ["Small radii; hairline dividers.", "Compact controls; 28–32px rows."],
        "type": ["Neutral sans at 12–13px UI.", "Medium weight for labels.", "Tabular figures in tables."],
        "fonts": [
            {"role": "UI", "name": "Inter", "url": "https://fonts.google.com/specimen/Inter", "note": "optical sizing"},
            {"role": "Alt", "name": "Geist", "url": "https://vercel.com/font", "note": "product UI"},
            {"role": "Mono", "name": "Geist Mono / IBM Plex Mono", "note": "IDs"},
        ],
        "icons": ["Small 16px stroke icons.", "Aligned to text cap height.", "Muted until active."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "16–18px"},
            {"role": "Alt", "name": "Radix Icons", "url": "https://www.radix-ui.com/icons", "note": "dense UI"},
        ],
        "systems_ours": ["primer", "atlassian", "carbon"],
        "systems_other": ["Linear-like product kits", "Issue tracker patterns"],
        "examples": [("Linear", "https://linear.app/"), ("Notion", "https://www.notion.com/"), ("Height", "https://height.app/"), ("GitHub Issues", "https://github.com/"), ("Superhuman", "https://superhuman.com/")],
        "do": "Quiet density, muted chrome, sharp scan paths.",
        "dont": "Huge marketing cards or loud multi-accent dashboards.",
        "css": _t_css(bg="#fff", soft="#fafafa", line="#ececec", muted="#8a8a8a", accent="#5e6ad2", accent_fg="#fff", radius="10px", radius_sm="6px", font="Inter, sans-serif", weight="500"),
    },
{
        "id": "japandi",
        "name": "Japandi",
        "fit": "Japanese calm × Scandinavian warmth — sparse, natural, precise.",
        "principles": ["Empty space is intentional.", "Natural materials as metaphor.", "Quiet luxury, not flash."],
        "layout": ["Asymmetric but balanced voids.", "Low visual weight chrome.", "One focal object per view."],
        "colors": ["Warm off-white, charcoal, wood.", "Muted sage or clay accent.", "No neon."],
        "radius": "squircle",
        "anatomy": ["Soft but restrained radii.", "Hairline charcoal rules; matte surfaces."],
        "type": ["Humanist sans or restrained serif.", "Light weights for large type.", "Wide letterspacing on labels OK."],
        "fonts": [
            {"role": "UI", "name": "DM Sans", "url": "https://fonts.google.com/specimen/DM+Sans", "note": "humanist"},
            {"role": "Display", "name": "Newsreader", "url": "https://fonts.google.com/specimen/Newsreader", "note": "quiet serif"},
            {"role": "Alt", "name": "Satoshi / General Sans", "note": "soft geometric"},
        ],
        "icons": ["Minimal stroke; wabi-sabi simplicity.", "Earth-tone or charcoal.", "No glossy 3D."],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "light stroke"},
            {"role": "Alt", "name": "Phosphor (thin)", "url": "https://phosphoricons.com/", "note": "quiet"},
        ],
        "systems_ours": ["polaris", "primer", "fluent-2"],
        "systems_other": ["Lifestyle / interior brand systems", "Wellness product UI"],
        "examples": [("Muji", "https://www.muji.com/"), ("Aesop", "https://www.aesop.com/"), ("Kinfolk", "https://www.kinfolk.com/"), ("Notion", "https://www.notion.com/"), ("Airbnb (calm stays)", "https://www.airbnb.com/")],
        "do": "Warm neutrals, light type, generous void.",
        "dont": "Loud maximal color or dense industrial tables as the vibe.",
        "css": _t_css(bg="#f7f4ef", soft="#efeae3", line="#ddd5c8", muted="#78716c", accent="#44403c", accent_fg="#f7f4ef", radius="16px", radius_sm="10px", font="'DM Sans', Inter, sans-serif", weight="500", tracking="0.02em"),
    },
{
        "id": "terminal",
        "name": "Terminal",
        "fit": "CLI aesthetic — monospace, prompts, phosphor on black.",
        "principles": ["Text is the UI.", "Prompt → command → output rhythm.", "No ornamental chrome."],
        "layout": ["Full-bleed console panels.", "ASCII / box-drawing structure.", "Single column command streams."],
        "colors": ["Black / near-black.", "Phosphor green or amber.", "Red only for errors."],
        "radius": "square",
        "anatomy": ["0 radius; 1px phosphor borders.", "Block cursor / prompt glyphs."],
        "type": ["Monospace only.", "No proportional headlines in UI.", "ASCII box drawing welcome."],
        "fonts": [
            {"role": "UI / all", "name": "JetBrains Mono", "url": "https://www.jetbrains.com/lp/mono/", "note": "coding default"},
            {"role": "Alt", "name": "IBM Plex Mono", "url": "https://fonts.google.com/specimen/IBM+Plex+Mono", "note": "terminal"},
            {"role": "Retro", "name": "IBM VGA / Perfect DOS VGA", "note": "nostalgia"},
        ],
        "icons": ["No icons — use ASCII or omit.", "Chevrons as > prompts.", "Folder paths as navigation."],
        "icon_libs": [
            {"role": "Primary", "name": "ASCII / Unicode only", "note": "› ■ ▶ ─ │"},
            {"role": "Alt", "name": "Nerd Fonts glyphs", "url": "https://www.nerdfonts.com/", "note": "if needed"},
        ],
        "systems_ours": ["primer", "carbon", "atlassian"],
        "systems_other": ["CLI tool docs themes", "Hacker / devops dashboards"],
        "examples": [("GitHub CLI", "https://cli.github.com/"), ("Vercel CLI", "https://vercel.com/docs/cli"), ("Warp", "https://www.warp.dev/"), ("replit (console)", "https://replit.com/"), ("classic green-phosphor CRT UIs", "https://en.wikipedia.org/wiki/Phosphor")],
        "do": "Mono only, prompt rhythm, phosphor contrast.",
        "dont": "Rounded marketing cards or icon-grid navigation.",
        "css": _t_css(bg="#0b0f0b", fg="#39ff14", soft="#0f160f", line="#39ff14", muted="#2db812", accent="#39ff14", accent_fg="#0b0f0b", danger="#ff3333", danger_fg="#0b0f0b", radius="0", radius_sm="0", font="'JetBrains Mono', ui-monospace, monospace", weight="500", tracking="0"),
    },
{
        "id": "clay",
        "name": "Clay",
        "fit": "Claymorphism — soft extruded shapes, candy light, playful depth.",
        "principles": [
            "UI feels molded from soft clay, not printed flat.",
            "Light comes from above; shadows are colored and diffuse.",
            "Friendly and tactile without neumorphism mush.",
        ],
        "layout": [
            "Floating clay slabs with generous padding.",
            "Stacked soft modules; avoid hairline grids.",
            "Big touch targets; toy-like proportions.",
        ],
        "colors": [
            "Pastel clay bodies (mint, peach, lilac).",
            "Colored soft shadows (never pure black).",
            "Slightly richer accent “pressed clay”.",
        ],
        "radius": "squircle",
        "anatomy": [
            "Extra-large radii; thick soft rims.",
            "Inner highlight + outer pastel shadow (extrusion).",
            "No hard 1px black borders.",
        ],
        "type": [
            "Rounded sans; medium weights.",
            "Friendly sentence case.",
            "Avoid ultra-condensed display.",
        ],
        "fonts": [
            {"role": "UI", "name": "Nunito", "url": "https://fonts.google.com/specimen/Nunito", "note": "rounded"},
            {"role": "Alt", "name": "Rounded Mplus / Varela Round", "url": "https://fonts.google.com/specimen/Varela+Round", "note": "soft"},
            {"role": "Display", "name": "Baloo 2", "url": "https://fonts.google.com/specimen/Baloo+2", "note": "playful"},
        ],
        "icons": [
            "Filled soft icons with round terminals.",
            "Pastel duotone OK.",
            "No sharp technical stroke sets.",
        ],
        "icon_libs": [
            {"role": "Primary", "name": "Phosphor (duotone/fill)", "url": "https://phosphoricons.com/", "note": "soft fills"},
            {"role": "Alt", "name": "Solar Icons", "url": "https://www.svgrepo.com/collection/solar-icons/", "note": "rounded"},
        ],
        "systems_ours": ["chakra", "mantine", "polaris"],
        "systems_other": ["Kids / edtech kits", "Claymorphism UI kits"],
        "examples": [
            ("Claymorphism trend refs", "https://www.nngroup.com/"),
            ("Notion faces / soft 3D marketing", "https://www.notion.com/"),
            ("Figma community clay kits", "https://www.figma.com/community"),
            ("Duolingo (soft playful)", "https://www.duolingo.com/"),
            ("Headspace", "https://www.headspace.com/"),
        ],
        "do": "Extruded pastel slabs, soft colored shadows, big radii.",
        "dont": "Flat gray neumorphism or hard neo-brutal borders.",
        "css": _t_css(
            bg="#e8f0ff",
            fg="#1e293b",
            soft="#dbe7ff",
            line="#c7d7fe",
            muted="#64748b",
            accent="#7c6af7",
            accent_fg="#fff",
            danger="#f43f5e",
            danger_fg="#fff",
            radius="28px",
            radius_sm="18px",
            shadow="8px 10px 0 rgba(124,106,247,.18), 0 18px 40px rgba(100,116,139,.12)",
            font="Nunito, 'Varela Round', sans-serif",
            weight="700",
            stage_border="1px solid rgba(255,255,255,.85)",
        )
        + """
.t .stage{
  background:linear-gradient(180deg,#f4f7ff 0%,#e4ecff 100%);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.95), 10px 12px 0 rgba(148,163,184,.18), 0 22px 44px rgba(99,102,241,.12);
}
.t .top,.t .side{background:#dfe8ff;box-shadow:inset 0 1px 0 rgba(255,255,255,.8)}
.t .btn{
  box-shadow:inset 0 2px 0 rgba(255,255,255,.45), 0 8px 0 rgba(88,70,220,.25);
  border:0;
}
.t .panel,.t .modal{
  background:linear-gradient(180deg,#fff,#eef2ff);
  box-shadow:inset 0 2px 0 #fff, 8px 10px 0 rgba(148,163,184,.2);
}
""",
    },
{
        "id": "aurora",
        "name": "Aurora",
        "fit": "Mesh-gradient night sky — luminous color fields, soft glow UI.",
        "principles": [
            "Color fields are the brand; chrome stays quiet.",
            "Glow and bloom over hard lines.",
            "Trendy 2025–26 mesh energy without clutter.",
        ],
        "layout": [
            "Full-bleed aurora / mesh behind sparse content.",
            "Floating light panels; few hard dividers.",
            "Hero moments over dense tables as default.",
        ],
        "colors": [
            "Deep indigo night + shifting greens / magentas.",
            "Soft white type on dark fields.",
            "One luminous CTA (mint or violet).",
        ],
        "radius": "pill",
        "anatomy": [
            "Soft pills; translucent panels over mesh.",
            "Glow shadows; no hard black borders.",
            "Hairline light borders at most.",
        ],
        "type": [
            "Geometric sans; light large titles.",
            "Medium UI weights for contrast on mesh.",
            "Avoid heavy serif newspaper energy.",
        ],
        "fonts": [
            {"role": "UI", "name": "Space Grotesk", "url": "https://fonts.google.com/specimen/Space+Grotesk", "note": "modern geometric"},
            {"role": "Alt", "name": "Satoshi / General Sans", "note": "soft geometric"},
            {"role": "Display", "name": "Cabinet Grotesk", "note": "airy headlines"},
        ],
        "icons": [
            "Thin light strokes on dark.",
            "Soft glow on active icons OK.",
            "Avoid chunky pixel or clay fills.",
        ],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "thin light"},
            {"role": "Alt", "name": "Phosphor (thin)", "url": "https://phosphoricons.com/", "note": "airy"},
        ],
        "systems_ours": ["polaris", "material-3", "fluent-2"],
        "systems_other": ["AI product marketing kits", "Mesh-gradient design systems"],
        "examples": [
            ("Linear marketing", "https://linear.app/"),
            ("Vercel", "https://vercel.com/"),
            ("OpenAI site moments", "https://openai.com/"),
            ("Raycast", "https://www.raycast.com/"),
            ("Stripe ambient gradients", "https://stripe.com/"),
        ],
        "do": "Mesh night sky, glowing soft panels, quiet chrome.",
        "dont": "Flat gray dashboards or hard neo-brutal frames.",
        "css": _t_css(
            bg="rgba(15,23,42,0.55)",
            fg="#f8fafc",
            soft="rgba(30,41,59,0.55)",
            line="rgba(167,243,208,0.35)",
            muted="#cbd5e1",
            accent="#34d399",
            accent_fg="#022c22",
            danger="#f472b6",
            danger_fg="#fff",
            radius="20px",
            radius_sm="999px",
            shadow="0 0 40px rgba(52,211,153,.2)",
            font="'Space Grotesk', Inter, sans-serif",
            weight="500",
            tracking="-0.01em",
            stage_border="1px solid rgba(255,255,255,.14)",
            blur="blur(10px)",
            saturate="140%",
        )
        + """
.t{
  padding:10px;border-radius:22px;
  background:
    radial-gradient(80% 70% at 20% 20%, rgba(52,211,153,.55), transparent 50%),
    radial-gradient(70% 60% at 80% 30%, rgba(167,139,250,.55), transparent 45%),
    radial-gradient(60% 50% at 50% 90%, rgba(244,114,182,.4), transparent 45%),
    linear-gradient(160deg,#020617,#0f172a 50%,#1e1b4b);
}
.t .stage{
  background:rgba(15,23,42,.5);
  box-shadow:0 20px 50px rgba(2,6,23,.45), inset 0 1px 0 rgba(255,255,255,.12);
}
.t .top,.t .side{background:rgba(15,23,42,.45);border-color:rgba(255,255,255,.1)}
.t .btn{box-shadow:0 0 24px rgba(52,211,153,.45)}
.t .chip.on{background:#34d399;color:#022c22;border-color:transparent}
.t .panel,.t .modal{
  background:rgba(15,23,42,.62);
  border:1px solid rgba(255,255,255,.14);
  box-shadow:0 16px 40px rgba(2,6,23,.4);
}
""",
    },
{
        "id": "cyberpunk",
        "name": "Cyberpunk",
        "fit": "Neon noir — rain-soaked tech, glitch accents, high-contrast night.",
        "principles": [
            "Night city first; neon is signal, not wallpaper everywhere.",
            "Tech grit with cinematic contrast.",
            "Glitch and scanlines as accents, not noise soup.",
        ],
        "layout": [
            "Dense HUD overlays and slanted panels sparingly.",
            "Dark canvas; neon edges for focus.",
            "Data strips and status stacks feel like a cockpit.",
        ],
        "colors": [
            "Near-black / deep teal night.",
            "Magenta + acid lime + cyan neon triad (use 1–2 at a time).",
            "Warning amber for alerts.",
        ],
        "radius": "square",
        "anatomy": [
            "Hard clipped panels; thin neon rims.",
            "Optional clip-path slant on one chrome piece.",
            "No soft clay or glass blur as the main language.",
        ],
        "type": [
            "Wide techno display for titles.",
            "Condensed grotesque or mono for data.",
            "Uppercase micro-labels.",
        ],
        "fonts": [
            {"role": "Display", "name": "Oxanium", "url": "https://fonts.google.com/specimen/Oxanium", "note": "tech display"},
            {"role": "UI", "name": "Rajdhani", "url": "https://fonts.google.com/specimen/Rajdhani", "note": "condensed HUD"},
            {"role": "Data", "name": "Share Tech Mono", "url": "https://fonts.google.com/specimen/Share+Tech+Mono", "note": "mono readout"},
        ],
        "icons": [
            "Thin HUD strokes or filled danger glyphs.",
            "High contrast on black.",
            "Avoid cute rounded consumer icons.",
        ],
        "icon_libs": [
            {"role": "Primary", "name": "Lucide", "url": "https://lucide.dev/", "note": "thin HUD"},
            {"role": "Alt", "name": "Tabler Icons", "url": "https://tabler.io/icons", "note": "tech"},
        ],
        "systems_ours": ["carbon", "primer", "atlassian"],
        "systems_other": ["Game HUD systems", "Security / SOC dashboards"],
        "examples": [
            ("Cyberpunk 2077 UI language", "https://www.cyberpunk.net/"),
            ("Blade Runner visual refs", "https://en.wikipedia.org/wiki/Blade_Runner"),
            ("CD Projekt / night-city promos", "https://www.cdprojekt.com/"),
            ("Mr. Robot title design energy", "https://www.usanetwork.com/mr-robot"),
            ("Tesla UI night modes (partial)", "https://www.tesla.com/"),
        ],
        "do": "Dark night canvas, neon signal edges, HUD density.",
        "dont": "Pastel wellness or bright vaporwave clutter as the whole UI.",
        "css": _t_css(
            bg="#070b12",
            fg="#e2f6ff",
            soft="#0d1522",
            line="#00f0ff",
            muted="#7dd3fc",
            accent="#ff2bd6",
            accent_fg="#070b12",
            danger="#ffe600",
            danger_fg="#070b12",
            radius="0",
            radius_sm="0",
            shadow="0 0 0 1px #00f0ff, 0 0 18px rgba(0,240,255,.35)",
            font="Rajdhani, Oxanium, sans-serif",
            weight="700",
            tracking="0.08em",
            stage_border="1px solid #00f0ff",
        )
        + """
.t .stage{background:linear-gradient(180deg,#070b12,#101b2d 60%,#1a0b24)}
.t .top{background:#0d1522;border-bottom:1px solid #ff2bd6;box-shadow:0 0 12px rgba(255,43,214,.25)}
.t .side{background:#0a121c;border-right:1px solid #00f0ff}
.t .btn{box-shadow:0 0 16px rgba(255,43,214,.45)}
.t .chip.on{background:#00f0ff;color:#070b12;border-color:#00f0ff}
.t .grid th{color:#00f0ff;background:#0d1522}
""",
    },
]
