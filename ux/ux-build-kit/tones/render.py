#!/usr/bin/env python3
"""Generate tone catalog HTML (index + 20 guides). Run: python3 render.py"""
from __future__ import annotations

import html
import re
from pathlib import Path

from _saas_wfs import WFS
from _tones_catalog import TONES

OUT = Path(__file__).resolve().parent

# Four SaaS slots — markup is best-fit per tone in `_saas_wfs.py`.
WF_SLOTS = (
    ("shell", "App shell", "Nav + primary region — how this SaaS greets you."),
    ("data", "Data view", "List/table — density and scanning for this product."),
    ("form", "Form / settings", "Inputs + primary action — control language."),
    ("moment", "Focal moment", "Confirm / empty / escalate — the signature beat."),
)

RADIUS_META = {
    "square": ("square", "0", "Structural / technical corners."),
    "squircle": ("squircle", "16px (+ corner-shape: squircle when available)", "Premium continuous curves."),
    "pill": ("pill", "9999px / 50%", "Friendly actionable corners."),
}

# Shared wireframe layout — tones only override CSS variables on `.t`
WF_BASE_CSS = """
.t{
  --bg:#fff;--fg:#111;--muted:#737373;--line:#d4d4d4;--soft:#f5f5f5;
  --accent:#111;--accent-fg:#fff;--danger:#b91c1c;--danger-fg:#fff;
  --radius:0;--radius-sm:0;--shadow:none;--font:Inter,ui-sans-serif,system-ui,sans-serif;
  --weight:600;--tracking:0;--stage-border:1px solid var(--line);
  --blur:none;--saturate:100%;
  font-family:var(--font);color:var(--fg);font-size:11px;line-height:1.4;
  display:block;
}
.t .stage{
  background:var(--bg);border:var(--stage-border);border-radius:var(--radius);
  box-shadow:var(--shadow);overflow:hidden;min-height:168px;
  backdrop-filter:var(--blur) saturate(var(--saturate));
  -webkit-backdrop-filter:var(--blur) saturate(var(--saturate));
}
.t .stage.pad{padding:16px}.t .stage.center{display:flex;align-items:center;justify-content:center}
.t .top{
  display:flex;align-items:center;gap:12px;padding:8px 12px;
  border-bottom:1px solid var(--line);background:var(--soft);
}
.t .brand{font-weight:var(--weight);letter-spacing:var(--tracking)}
.t .nav{display:flex;gap:10px;flex:1;color:var(--muted)}
.t .nav .on,.t .nav-item.on{color:var(--fg);font-weight:var(--weight)}
.t .meta{margin-left:auto;color:var(--muted);font-size:10px}
.t .body{display:grid;grid-template-columns:118px 1fr;min-height:120px}
.t .side{border-right:1px solid var(--line);padding:8px;background:var(--soft)}
.t .nav-item{padding:6px 8px;border-radius:var(--radius-sm);margin-bottom:2px;color:var(--muted)}
.t .main{padding:12px 14px}
.t .title-row{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:4px}
.t h3{margin:0;font-size:14px;font-weight:var(--weight);letter-spacing:var(--tracking)}
.t .muted{margin:0;color:var(--muted);font-size:10px}
.t .chips{display:flex;gap:6px;margin-top:12px;flex-wrap:wrap}
.t .chip{
  border:1px solid var(--line);padding:3px 8px;border-radius:var(--radius-sm);
  color:var(--muted);background:var(--bg)
}
.t .chip.on{background:var(--accent);color:var(--accent-fg);border-color:var(--accent)}
.t .btn{
  display:inline-block;background:var(--accent);color:var(--accent-fg);
  border:1px solid var(--accent);padding:6px 12px;border-radius:var(--radius-sm);
  font-size:11px;font-weight:var(--weight);box-shadow:var(--shadow);cursor:default
}
.t .btn.ghost{background:var(--bg);color:var(--fg);border-color:var(--line);box-shadow:none}
.t .btn.danger{background:var(--danger);border-color:var(--danger);color:var(--danger-fg)}
.t .grid{width:100%;border-collapse:collapse}
.t .grid th,.t .grid td{padding:8px 12px;border-bottom:1px solid var(--line);text-align:left}
.t .grid th{font-size:10px;color:var(--muted);font-weight:500;background:var(--soft)}
.t .tag{
  display:inline-block;padding:1px 6px;border:1px solid var(--line);
  border-radius:var(--radius-sm);font-size:10px;background:var(--bg)
}
.t .tag.muted{color:var(--muted)}
.t .panel,.t .modal{
  background:var(--bg);border:1px solid var(--line);border-radius:var(--radius);
  padding:14px;box-shadow:var(--shadow);max-width:280px;width:100%;
  backdrop-filter:var(--blur) saturate(var(--saturate));
  -webkit-backdrop-filter:var(--blur) saturate(var(--saturate));
}
.t label{display:block;font-size:10px;color:var(--muted);margin:10px 0 4px}
.t input{
  width:100%;box-sizing:border-box;border:1px solid var(--line);background:var(--bg);
  color:var(--fg);padding:7px 8px;border-radius:var(--radius-sm);font:inherit
}
.t .actions{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.t .modal p{margin:6px 0 0}
"""

BASE_CSS = """
:root { color-scheme: light; --ink:#0a0a0a; --muted:#525252; --line:#e5e5e5; --paper:#fff; --wash:#fafafa; --blue:#1d4ed8; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  background: var(--wash);
  color: var(--ink);
  line-height: 1.5;
}
.page { max-width: 960px; margin: 0 auto; padding: 28px 20px 80px; }
a { color: var(--blue); text-decoration: none; }
a:hover { text-decoration: underline; }
code {
  font-family: ui-monospace, Menlo, monospace; font-size: 0.85em;
  background: #eee; padding: 1px 5px; border-radius: 0;
}

.back {
  display: inline-flex; align-items: center; justify-content: center;
  width: 36px; height: 36px; border-radius: 0; border: 1px solid #111;
  background: var(--paper); color: var(--ink); margin-bottom: 20px;
}
.back:hover { border-color: #a3a3a3; text-decoration: none; background: #fff; }
.back svg { display: block; }

.hero-title {
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  font-weight: 650; letter-spacing: -0.035em; line-height: 1.15;
  margin: 0 0 4px;
}
.hero-sub {
  font-size: 0.95rem; font-weight: 500; color: var(--muted);
  letter-spacing: 0.04em; text-transform: uppercase; margin: 0 0 14px;
}
.fit { font-size: 1.05rem; color: #262626; margin: 0 0 10px; max-width: 40rem; }
.meta-row {
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 20px;
  font-size: 0.8rem; color: var(--muted);
}
.meta-row code { background: #eee; }

.toc {
  display: flex; align-items: stretch;
  gap: 0; margin: 0 0 36px; padding: 0;
  border: 1px solid #111; background: #fff;
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
}
.toc a {
  flex: 1 1 0; min-width: 5.5rem;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 2px; padding: 12px 10px;
  font-size: 0.8rem; font-weight: 550; letter-spacing: -0.01em;
  color: #525252; text-decoration: none; text-align: center;
  border-right: 1px solid #e5e5e5; white-space: nowrap;
  transition: background .12s ease, color .12s ease;
}
.toc a:last-child { border-right: 0; }
.toc a .n {
  font-size: 0.65rem; font-weight: 700; letter-spacing: 0.08em;
  color: #a3a3a3; line-height: 1;
}
.toc a:hover { background: #f5f5f5; color: #111; text-decoration: none; }
.toc a:hover .n { color: #737373; }
.toc a:focus-visible { outline: 2px solid #111; outline-offset: -2px; z-index: 1; }

.section {
  padding: 8px 0 36px;
  border-bottom: 1px solid var(--line);
  scroll-margin-top: 24px;
}
.section:last-of-type { border-bottom: 0; }
.section h2 {
  font-size: 1.25rem; font-weight: 650; letter-spacing: -0.025em;
  margin: 0 0 8px; border: 0; padding: 0;
  display: flex; align-items: baseline; gap: 10px;
}
.section h2 .n {
  font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em;
  color: #a3a3a3; font-variant-numeric: tabular-nums;
}
.section .lead { font-size: 0.9rem; color: var(--muted); margin: 0 0 16px; max-width: 40rem; }

.two-col {
  display: grid; grid-template-columns: 1.2fr 1fr; gap: 20px 28px;
}
@media (max-width: 720px) { .two-col { grid-template-columns: 1fr; } }

ul.bullets { margin: 0; padding-left: 1.15rem; }
ul.bullets li { margin: 5px 0; font-size: 0.92rem; }
h3.block-title {
  font-size: 0.72rem; font-weight: 650; letter-spacing: 0.07em;
  text-transform: uppercase; color: var(--muted); margin: 0 0 8px;
}

.pick {
  display: inline-flex; align-items: baseline; gap: 8px; flex-wrap: wrap;
  background: var(--paper); border: 1px solid #111;
  border-radius: 0; padding: 10px 14px; font-size: 0.9rem;
}
.pick strong { font-weight: 650; }
.pick .cue { color: var(--muted); font-size: 0.85rem; }

.resource-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
.resource-list li {
  background: var(--paper); border: 1px solid #111;
  border-radius: 0; padding: 10px 12px; font-size: 0.88rem;
}
.resource-list .role {
  display: block; font-size: 0.68rem; font-weight: 650;
  letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); margin-bottom: 2px;
}
.resource-list a { font-weight: 600; color: var(--ink); }
.resource-list a:hover { color: var(--blue); }
.resource-list .note { color: var(--muted); font-size: 0.8rem; }

.examples { font-size: 0.9rem; line-height: 1.75; margin: 0; }
.examples a { margin-right: 2px; }

.do-dont {
  display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 4px;
}
.do-dont > div {
  background: var(--paper); border: 1px solid #111;
  border-radius: 0; padding: 14px 16px; font-size: 0.9rem;
}
.do-dont .label {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em;
  text-transform: uppercase; margin-bottom: 6px;
}
.do-dont .do .label { color: #15803d; }
.do-dont .dont .label { color: #b91c1c; }
@media (max-width: 640px) { .do-dont { grid-template-columns: 1fr; } }

.wf-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 4px;
}
@media (max-width: 720px) { .wf-grid { grid-template-columns: 1fr; } }
.wf-card {
  background: var(--paper); border: 1px solid #111;
  border-radius: 0; overflow: hidden; display: flex; flex-direction: column;
}
.wf-card .wf-head {
  padding: 10px 12px 8px; border-bottom: 1px solid #111;
  background: #fff;
}
.wf-card .wf-head h3 { margin: 0 0 2px; font-size: 0.92rem; font-weight: 650; }
.wf-card .wf-head .desc { margin: 0; font-size: 0.78rem; color: var(--muted); }
.wf-card .specimen { padding: 12px; background: #f0f0f0; flex: 1; }
.wf-card .specimen .t { display: block; }

/* Catalog index — wireframe board, never soft “cards” */
.index-board {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 28px 20px;
  margin-top: 28px;
}
.wf-link {
  display: block; color: inherit; text-decoration: none;
}
.wf-link:hover { text-decoration: none; }
.wf-link:hover .wf-frame { outline: 2px solid #111; outline-offset: 2px; }
.wf-frame {
  border: 1px dashed #111;
  background: #f0f0f0;
  padding: 10px;
  border-radius: 0;
}
.wf-frame .t { display: block; pointer-events: none; }
.wf-caption {
  margin-top: 10px;
  border-top: 1px solid #111;
  padding-top: 8px;
}
.wf-caption .name {
  font-size: 0.95rem; font-weight: 650; letter-spacing: -0.02em; margin: 0 0 2px;
}
.wf-caption .tid {
  font-size: 11px; font-family: ui-monospace, Menlo, monospace; color: #525252; margin: 0 0 6px;
}
.wf-caption .fit {
  font-size: 0.8rem; color: #404040; margin: 0 0 6px; line-height: 1.4;
}
.wf-caption .meta {
  font-size: 0.72rem; color: #737373; font-family: ui-monospace, Menlo, monospace;
}

.agent-note { font-size: 0.8rem; color: var(--muted); margin: 18px 0 0; }
"""

HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Press+Start+2P&family=VT323&family=Orbitron:wght@500;700&family=Nunito:wght@500;700&family=Space+Grotesk:wght@400;500;700&family=Quicksand:wght@500;700&family=Rajdhani:wght@500;700&family=Oxanium:wght@500;700&family=Josefin+Sans:wght@400;600&family=Fredoka:wght@500;700&display=swap" rel="stylesheet"/>
"""

BACK_ICON = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>"""

# sid, num, title, short tab label, lead
SECTION_META = (
    ("philosophy", "1", "Core Philosophy", "Philosophy", "Purpose, emotional boundaries, and when to use this aesthetic."),
    ("layout", "2", "Layout & Spatial Architecture", "Layout", "Canvas organization: grids, alignment, density — not arbitrary placement."),
    ("type", "3", "Typography Rules", "Type", "Typeface choices, weights, and scale limits that build hierarchy."),
    ("anatomy", "4", "Component Anatomy", "Anatomy", "Borders, corners, shapes, shadows, and icon language."),
    ("color", "5", "Intentional Color Systems", "Color", "Limited spectrum; how colors interact for utility and emphasis."),
    ("dodont", "6", "Do vs Don’t Matrix", "Do / Don’t", "Side-by-side guardrails — keep the Do, reject the Don’t."),
    ("specimens", "7", "Specimen gallery", "Specimens", "Four SaaS wireframes chosen for this tone — shell · data · form · moment."),
)


def links(pairs: list[tuple[str, str]]) -> str:
    return " · ".join(
        f'<a href="{html.escape(u)}" rel="noopener noreferrer">{html.escape(n)}</a>'
        for n, u in pairs
    )


def bullets(items: list[str]) -> str:
    return '<ul class="bullets">' + "".join(f"<li>{html.escape(i)}</li>" for i in items) + "</ul>"


def resource_list(items: list[dict]) -> str:
    """items: {role, name, url?, note?}"""
    rows = []
    for it in items:
        name = html.escape(it["name"])
        if it.get("url"):
            name = f'<a href="{html.escape(it["url"])}" rel="noopener noreferrer">{name}</a>'
        note = f'<span class="note"> — {html.escape(it["note"])}</span>' if it.get("note") else ""
        rows.append(
            f'<li><span class="role">{html.escape(it["role"])}</span>{name}{note}</li>'
        )
    return f'<ul class="resource-list">{"".join(rows)}</ul>'


def radius_pick(choice: str) -> str:
    oid, css, why = RADIUS_META[choice]
    return (
        f'<div class="pick"><strong><code>{html.escape(oid)}</code></strong>'
        f'<span class="cue">{html.escape(css)} · {html.escape(why)}</span></div>'
    )


def section(sid: str, num: str, title: str, lead: str, body: str) -> str:
    return (
        f'<section class="section" id="{html.escape(sid)}">'
        f'<h2><span class="n">{html.escape(num)}</span>{html.escape(title)}</h2>'
        f'<p class="lead">{html.escape(lead)}</p>'
        f"{body}"
        f"</section>"
    )


def render_toc() -> str:
    links = "".join(
        f'<a href="#{sid}"><span class="n">{html.escape(num)}</span>{html.escape(tab)}</a>'
        for sid, num, _title, tab, _lead in SECTION_META
    )
    return f'<nav class="toc" aria-label="On this page">{links}</nav>'


def tone_wfs(t: dict) -> dict[str, str]:
    wfs = WFS.get(t["id"])
    if not wfs:
        raise SystemExit(f"{t['id']} missing SaaS wireframes in _saas_wfs.py")
    for key, _, _ in WF_SLOTS:
        if key not in wfs:
            raise SystemExit(f"{t['id']} missing wfs.{key}")
    return wfs


def render_wireframes(t: dict) -> str:
    wfs = tone_wfs(t)
    cards = []
    for key, title, desc in WF_SLOTS:
        cards.append(
            f'<article class="wf-card">'
            f'<div class="wf-head"><h3>{html.escape(title)}</h3>'
            f'<p class="desc">{html.escape(desc)}</p></div>'
            f'<div class="specimen"><div class="t">{wfs[key].strip()}</div></div>'
            f"</article>"
        )
    return f'<div class="wf-grid">{"".join(cards)}</div>'


def render_tone(t: dict) -> str:
    philosophy = (
        '<div class="two-col">'
        f"<div>{bullets(t['principles'])}</div>"
        "<div>"
        '<h3 class="block-title">Real products</h3>'
        f'<p class="examples">{links(t["examples"])}</p>'
        '<h3 class="block-title" style="margin-top:16px">From our catalog</h3>'
        + bullets(
            [
                f"Closest systems: {', '.join(t['systems_ours'])}",
                f"Also fits: {', '.join(t['systems_other'])}",
            ]
        )
        + "</div></div>"
    )

    type_body = (
        '<div class="two-col">'
        f"<div>{bullets(t['type'])}</div>"
        "<div>"
        '<h3 class="block-title">Suggested fonts</h3>'
        f"{resource_list(t['fonts'])}"
        "</div></div>"
    )

    anatomy = (
        '<div class="two-col">'
        "<div>"
        '<h3 class="block-title">Border radius</h3>'
        f"{radius_pick(t['radius'])}"
        f'<div style="margin-top:16px">{bullets(t.get("anatomy", []))}</div>'
        "</div>"
        "<div>"
        '<h3 class="block-title">Icon rules</h3>'
        f"{bullets(t['icons'])}"
        '<h3 class="block-title" style="margin-top:16px">Icon libraries</h3>'
        f"{resource_list(t['icon_libs'])}"
        "</div></div>"
    )

    do_dont = (
        f'<div class="do-dont"><div class="do"><div class="label">Do</div>{html.escape(t["do"])}</div>'
        f'<div class="dont"><div class="label">Don’t</div>{html.escape(t["dont"])}</div></div>'
    )

    bodies = {
        "philosophy": philosophy,
        "layout": bullets(t["layout"]),
        "type": type_body,
        "anatomy": anatomy,
        "color": bullets(t["colors"]),
        "dodont": do_dont,
        "specimens": render_wireframes(t),
    }

    sections_html = "".join(
        section(sid, num, title, lead, bodies[sid])
        for sid, num, title, _tab, lead in SECTION_META
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(t["name"])} — Guidelines</title>
{HEAD}
<style>
{BASE_CSS}
{WF_BASE_CSS}
{t["css"]}
</style>
</head>
<body>
<div class="page">
<a class="back" href="index.html" aria-label="Back to tone catalog">{BACK_ICON}</a>
<h1 class="hero-title">{html.escape(t["name"])}</h1>
<p class="hero-sub">Guidelines</p>
<p class="fit">{html.escape(t["fit"])}</p>
<p class="meta-row"><span>Tone id <code>{html.escape(t["id"])}</code></span><span>·</span><span>Write into <code>system.json</code> <code>tone</code></span></p>
{render_toc()}
{sections_html}
<p class="agent-note">SaaS-fit tone. Carry Philosophy → Layout → Type → Anatomy → Color into Foundations. Match the four specimens and radius pick.</p>
</div>
</body>
</html>
"""


def scope_tone_css(tone_id: str, css: str) -> str:
    """Scope every `.t` class selector so many tones can share one catalog page."""
    tid = re.sub(r"[^a-z0-9-]", "", tone_id)
    return re.sub(r"\.t(?=[\s.{:#\[\],]|$)", f".skin-{tid}.t", css)


def render_index(tones: list[dict]) -> str:
    skins = []
    tiles = []
    for t in tones:
        tid = t["id"]
        shell = tone_wfs(t)["shell"].strip()
        skins.append(scope_tone_css(tid, t["css"]))
        sys = ", ".join(t["systems_ours"])
        tiles.append(
            f'<a class="wf-link" href="{html.escape(tid)}.html">'
            f'<div class="wf-frame">'
            f'<div class="t skin-{html.escape(tid)}">{shell}</div>'
            f"</div>"
            f'<div class="wf-caption">'
            f'<div class="name">{html.escape(t["name"])}</div>'
            f'<div class="tid">{html.escape(tid)}</div>'
            f'<p class="fit">{html.escape(t["fit"])}</p>'
            f'<div class="meta">radius:{html.escape(t["radius"])} · {html.escape(sys)}</div>'
            f"</div></a>"
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Tone catalog — UX build kit</title>
{HEAD}
<style>
{BASE_CSS}
{WF_BASE_CSS}
{"".join(skins)}
</style>
</head>
<body>
<div class="page">
<h1 class="hero-title">Tone catalog</h1>
<p class="hero-sub">SaaS wireframes</p>
<p class="fit">Only tones that fit a SaaS product. Each tile shows that tone’s best-fit app shell — open a guide for all four specimens. Write <code>id</code> + <code>name</code> into <code>system.json</code> <code>tone</code>.</p>
<p class="agent-note" style="margin-top:0">Dashed frames are wireframe chrome (0 radius). Interior corner language follows each tone’s radius pick.</p>
<div class="index-board">
{chr(10).join(tiles)}
</div>
</div>
</body>
</html>
"""


def main() -> list[str]:
    expected = set(WFS)
    ids = {t["id"] for t in TONES}
    if ids != expected:
        raise SystemExit(f"Tone set mismatch: missing={expected - ids} extra={ids - expected}")

    for t in TONES:
        for key in ("fonts", "icon_libs", "css", "radius"):
            if key not in t:
                raise SystemExit(f"{t['id']} missing {key}")
        tone_wfs(t)  # validate SaaS specimens

    for path in OUT.glob("*.html"):
        path.unlink()

    written: list[str] = []
    for t in TONES:
        tid = t["id"]
        written.append(tid)
        (OUT / f"{tid}.html").write_text(render_tone(t), encoding="utf-8")

    (OUT / "index.html").write_text(render_index(TONES), encoding="utf-8")
    return written


if __name__ == "__main__":
    tone_ids = main()
    print(f"Wrote index.html + {len(tone_ids)} tone guides")
    for tid in tone_ids:
        print(f"  {tid}.html")
