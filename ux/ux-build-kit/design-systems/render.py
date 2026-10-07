#!/usr/bin/env python3
"""Generate design-system catalog HTML. Run: python3 render.py"""
from __future__ import annotations

import html
import re
from pathlib import Path

from _catalog import SYSTEMS

OUT = Path(__file__).resolve().parent

# Same four SaaS wireframes for every design system — only `.t` CSS changes the look.
WF_SLOTS = (
    ("shell", "App shell", "Nav + primary region — how the product greets you."),
    ("data", "Data view", "List/table — density and scanning."),
    ("form", "Form / settings", "Inputs + primary action — control language."),
    ("moment", "Focal moment", "Confirm / empty — the signature beat."),
)

SHARED_WFS = {
    "shell": """
<div class="stage">
  <div class="top">
    <span class="brand">Harbor</span>
    <nav class="nav"><span class="on">Projects</span><span>Team</span><span>Settings</span></nav>
    <span class="meta">Alex</span>
  </div>
  <div class="body">
    <aside class="side">
      <div class="nav-item on">All projects</div>
      <div class="nav-item">Starred</div>
      <div class="nav-item">Archive</div>
    </aside>
    <main class="main">
      <div class="title-row"><h3>Projects</h3><span class="btn">New</span></div>
      <p class="muted">3 active · Updated today</p>
      <div class="chips"><span class="chip">Design</span><span class="chip">Ops</span><span class="chip on">All</span></div>
    </main>
  </div>
</div>""".strip(),
    "data": """
<div class="stage">
  <div class="top">
    <span class="brand">Harbor</span>
    <span class="meta">128 records</span>
  </div>
  <table class="grid">
    <thead><tr><th>Name</th><th>Owner</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Atlas</td><td>Alex</td><td><span class="tag">Live</span></td></tr>
      <tr><td>Northwind</td><td>Sam</td><td><span class="tag">Live</span></td></tr>
      <tr><td>Beacon</td><td>Riley</td><td><span class="tag muted">Draft</span></td></tr>
      <tr><td>Cedar</td><td>Jordan</td><td><span class="tag">Live</span></td></tr>
    </tbody>
  </table>
</div>""".strip(),
    "form": """
<div class="stage pad">
  <div class="panel">
    <h3>New project</h3>
    <label>Name</label>
    <input value="Atlas" readonly/>
    <label>Visibility</label>
    <input value="Private" readonly/>
    <div class="actions"><span class="btn">Create project</span></div>
  </div>
</div>""".strip(),
    "moment": """
<div class="stage pad center">
  <div class="modal">
    <h3>Delete project?</h3>
    <p class="muted">Atlas will be removed. This can’t be undone.</p>
    <div class="actions">
      <span class="btn ghost">Cancel</span>
      <span class="btn danger">Delete</span>
    </div>
  </div>
</div>""".strip(),
}

# sid, num, title, short tab label, lead
SECTION_META = (
    ("philosophy", "1", "Core Philosophy", "Philosophy", "Purpose, maker context, and when this system fits."),
    ("layout", "2", "Layout & Spatial Architecture", "Layout", "Grid, spacing, and how screens are organized."),
    ("type", "3", "Typography Rules", "Type", "Type roles plus the fonts this system suggests."),
    ("anatomy", "4", "Component Anatomy", "Anatomy", "Shape, elevation, components, and icon libraries."),
    ("color", "5", "Intentional Color Systems", "Color", "Roles, themes, and how color carries meaning."),
    ("dodont", "6", "Do vs Don’t Matrix", "Do / Don’t", "What to keep when adapting — and what to refuse."),
    ("specimens", "7", "Specimen gallery", "Specimens", "The same four Harbor SaaS wireframes, skinned for this system."),
)

WF_BASE_CSS = """
.t{
  --bg:#fff;--fg:#111;--muted:#737373;--line:#d4d4d4;--soft:#f5f5f5;
  --accent:#111;--accent-fg:#fff;--danger:#b91c1c;--danger-fg:#fff;
  --radius:0;--radius-sm:0;--shadow:none;--font:Inter,ui-sans-serif,system-ui,sans-serif;
  --weight:600;--tracking:0;--stage-border:1px solid var(--line);
  --blur:none;--saturate:100%;
  font-family:var(--font);color:var(--fg);font-size:11px;line-height:1.4;display:block;
}
.t .stage{
  background:var(--bg);border:var(--stage-border);border-radius:var(--radius);
  box-shadow:var(--shadow);overflow:hidden;min-height:168px;
  backdrop-filter:var(--blur) saturate(var(--saturate));
  -webkit-backdrop-filter:var(--blur) saturate(var(--saturate));
}
.t .stage.pad{padding:16px}.t .stage.center{display:flex;align-items:center;justify-content:center}
.t .top{display:flex;align-items:center;gap:12px;padding:8px 12px;border-bottom:1px solid var(--line);background:var(--soft)}
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
.t .chip{border:1px solid var(--line);padding:3px 8px;border-radius:var(--radius-sm);color:var(--muted);background:var(--bg)}
.t .chip.on{background:var(--accent);color:var(--accent-fg);border-color:var(--accent)}
.t .btn{display:inline-block;background:var(--accent);color:var(--accent-fg);border:1px solid var(--accent);padding:6px 12px;border-radius:var(--radius-sm);font-size:11px;font-weight:var(--weight);box-shadow:var(--shadow);cursor:default}
.t .btn.ghost{background:var(--bg);color:var(--fg);border-color:var(--line);box-shadow:none}
.t .btn.danger{background:var(--danger);border-color:var(--danger);color:var(--danger-fg)}
.t .grid{width:100%;border-collapse:collapse}
.t .grid th,.t .grid td{padding:8px 12px;border-bottom:1px solid var(--line);text-align:left}
.t .grid th{font-size:10px;color:var(--muted);font-weight:500;background:var(--soft)}
.t .tag{display:inline-block;padding:1px 6px;border:1px solid var(--line);border-radius:var(--radius-sm);font-size:10px;background:var(--bg)}
.t .tag.muted{color:var(--muted)}
.t .panel,.t .modal{background:var(--bg);border:1px solid var(--line);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow);max-width:280px;width:100%}
.t label{display:block;font-size:10px;color:var(--muted);margin:10px 0 4px}
.t input{width:100%;box-sizing:border-box;border:1px solid var(--line);background:var(--bg);color:var(--fg);padding:7px 8px;border-radius:var(--radius-sm);font:inherit}
.t .actions{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.t .modal p{margin:6px 0 0}
"""

BASE_CSS = """
:root { color-scheme: light; --ink:#0a0a0a; --muted:#525252; --line:#e5e5e5; --paper:#fff; --wash:#fafafa; --blue:#1d4ed8; }
* { box-sizing: border-box; }
body { margin:0; font-family:Inter,ui-sans-serif,system-ui,sans-serif; background:var(--wash); color:var(--ink); line-height:1.5; }
.page { max-width:960px; margin:0 auto; padding:28px 20px 80px; }
a { color:var(--blue); text-decoration:none; }
a:hover { text-decoration:underline; }
code { font-family:ui-monospace,Menlo,monospace; font-size:0.85em; background:#eee; padding:1px 5px; border-radius:0; }
.back { display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:0; border:1px solid #111; background:var(--paper); color:var(--ink); margin-bottom:20px; }
.back:hover { text-decoration:none; background:#fff; }
.back svg { display:block; }
.hero-title { font-size:clamp(1.75rem,3vw,2.25rem); font-weight:650; letter-spacing:-0.035em; line-height:1.15; margin:0 0 4px; }
.hero-sub { font-size:0.95rem; font-weight:500; color:var(--muted); letter-spacing:0.04em; text-transform:uppercase; margin:0 0 14px; }
.fit { font-size:1.05rem; color:#262626; margin:0 0 10px; max-width:40rem; }
.meta-row { display:flex; flex-wrap:wrap; gap:8px; margin:0 0 20px; font-size:0.8rem; color:var(--muted); }
.toc {
  display:flex; align-items:stretch; gap:0; margin:0 0 36px; padding:0;
  border:1px solid #111; background:#fff;
  overflow-x:auto; -webkit-overflow-scrolling:touch; scrollbar-width:thin;
}
.toc a {
  flex:1 1 0; min-width:5.5rem;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  gap:2px; padding:12px 10px;
  font-size:0.8rem; font-weight:550; letter-spacing:-0.01em;
  color:#525252; text-decoration:none; text-align:center;
  border-right:1px solid #e5e5e5; white-space:nowrap;
  transition:background .12s ease, color .12s ease;
}
.toc a:last-child { border-right:0; }
.toc a .n {
  font-size:0.65rem; font-weight:700; letter-spacing:0.08em;
  color:#a3a3a3; line-height:1;
}
.toc a:hover { background:#f5f5f5; color:#111; text-decoration:none; }
.toc a:hover .n { color:#737373; }
.toc a:focus-visible { outline:2px solid #111; outline-offset:-2px; z-index:1; }
.section { padding:8px 0 36px; border-bottom:1px solid var(--line); scroll-margin-top:24px; }
.section:last-of-type { border-bottom:0; }
.section h2 {
  font-size:1.25rem; font-weight:650; letter-spacing:-0.025em;
  margin:0 0 8px; border:0; padding:0;
  display:flex; align-items:baseline; gap:10px;
}
.section h2 .n {
  font-size:0.75rem; font-weight:700; letter-spacing:0.06em;
  color:#a3a3a3; font-variant-numeric:tabular-nums;
}
.section .lead { font-size:0.9rem; color:var(--muted); margin:0 0 16px; max-width:40rem; }
.two-col { display:grid; grid-template-columns:1.2fr 1fr; gap:20px 28px; }
@media (max-width:720px){ .two-col{ grid-template-columns:1fr; } }
ul.bullets { margin:0; padding-left:1.15rem; }
ul.bullets li { margin:5px 0; font-size:0.92rem; }
h3.block-title { font-size:0.72rem; font-weight:650; letter-spacing:0.07em; text-transform:uppercase; color:var(--muted); margin:0 0 8px; }
.field { background:var(--paper); border:1px solid #111; border-radius:0; padding:12px 14px; margin:0 0 10px; }
.field .k { font-size:0.68rem; font-weight:700; letter-spacing:0.07em; text-transform:uppercase; color:var(--muted); margin:0 0 4px; }
.field .v { font-size:0.9rem; margin:0; }
.field.dim .v { color:#737373; font-style:italic; }
.resource-list { list-style:none; margin:0 0 12px; padding:0; display:grid; gap:8px; }
.resource-list li { background:var(--paper); border:1px solid #111; border-radius:0; padding:10px 12px; font-size:0.88rem; }
.resource-list .role { display:block; font-size:0.68rem; font-weight:650; letter-spacing:0.06em; text-transform:uppercase; color:var(--muted); margin-bottom:2px; }
.resource-list a { font-weight:600; color:var(--ink); }
.resource-list a:hover { color:var(--blue); }
.resource-list .note { color:var(--muted); font-size:0.8rem; }
.do-dont { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:4px; }
.do-dont > div { background:var(--paper); border:1px solid #111; border-radius:0; padding:14px 16px; font-size:0.9rem; }
.do-dont .label { font-size:0.68rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:6px; }
.do-dont .do .label { color:#15803d; }
.do-dont .dont .label { color:#b91c1c; }
@media (max-width:640px){ .do-dont{ grid-template-columns:1fr; } }
.wf-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:4px; }
@media (max-width:720px){ .wf-grid{ grid-template-columns:1fr; } }
.wf-card { background:var(--paper); border:1px solid #111; border-radius:0; overflow:hidden; display:flex; flex-direction:column; }
.wf-card .wf-head { padding:10px 12px 8px; border-bottom:1px solid #111; background:#fff; }
.wf-card .wf-head h3 { margin:0 0 2px; font-size:0.92rem; font-weight:650; }
.wf-card .wf-head .desc { margin:0; font-size:0.78rem; color:var(--muted); }
.wf-card .specimen { padding:12px; background:#f0f0f0; flex:1; }
.index-board { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:28px 20px; margin-top:28px; }
.wf-link { display:block; color:inherit; text-decoration:none; }
.wf-link:hover { text-decoration:none; }
.wf-link:hover .wf-frame { outline:2px solid #111; outline-offset:2px; }
.wf-frame { border:1px dashed #111; background:#f0f0f0; padding:10px; border-radius:0; }
.wf-frame .t { display:block; pointer-events:none; }
.wf-caption { margin-top:10px; border-top:1px solid #111; padding-top:8px; }
.wf-caption .name { font-size:0.95rem; font-weight:650; letter-spacing:-0.02em; margin:0 0 2px; }
.wf-caption .tid { font-size:11px; font-family:ui-monospace,Menlo,monospace; color:#525252; margin:0 0 6px; }
.wf-caption .fit { font-size:0.8rem; color:#404040; margin:0 0 6px; line-height:1.4; }
.wf-caption .meta { font-size:0.72rem; color:#737373; font-family:ui-monospace,Menlo,monospace; display:flex; align-items:center; gap:6px; flex-wrap:wrap; }
.swatch { width:10px; height:10px; border:1px solid #111; display:inline-block; flex:0 0 auto; }
.agent-note { font-size:0.8rem; color:var(--muted); margin:18px 0 0; }
.tone-pills { display:flex; flex-wrap:wrap; gap:6px; margin:0; padding:0; list-style:none; }
.tone-pills a { display:inline-block; border:1px solid #111; padding:4px 8px; font-size:0.78rem; color:var(--ink); background:#fff; }
.tone-pills a:hover { background:#111; color:#fff; text-decoration:none; }
"""

HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;600&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet"/>
"""

BACK_ICON = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>"""


def field_block(key: str, value: str) -> str:
    dim = value.strip() == "Unconfirmed."
    cls = "field dim" if dim else "field"
    shown = "Unconfirmed — fill when adapting for this product." if dim else value
    return (
        f'<div class="{cls}"><div class="k">{html.escape(key)}</div>'
        f'<p class="v">{html.escape(shown)}</p></div>'
    )


def resource_list(items: list[dict]) -> str:
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


def section(sid: str, num: str, title: str, lead: str, body: str) -> str:
    return (
        f'<section class="section" id="{html.escape(sid)}">'
        f'<h2><span class="n">{html.escape(num)}</span>{html.escape(title)}</h2>'
        f'<p class="lead">{html.escape(lead)}</p>'
        f"{body}</section>"
    )


def render_toc() -> str:
    links = "".join(
        f'<a href="#{sid}"><span class="n">{html.escape(num)}</span>{html.escape(tab)}</a>'
        for sid, num, _title, tab, _lead in SECTION_META
    )
    return f'<nav class="toc" aria-label="On this page">{links}</nav>'


def scope_css(system_id: str, css: str) -> str:
    tid = re.sub(r"[^a-z0-9-]", "", system_id)
    return re.sub(r"\.t(?=[\s.{:#\[\],]|$)", f".skin-{tid}.t", css)


def render_wireframes() -> str:
    cards = []
    for key, title, desc in WF_SLOTS:
        cards.append(
            f'<article class="wf-card"><div class="wf-head"><h3>{html.escape(title)}</h3>'
            f'<p class="desc">{html.escape(desc)}</p></div>'
            f'<div class="specimen"><div class="t">{SHARED_WFS[key]}</div></div></article>'
        )
    return f'<div class="wf-grid">{"".join(cards)}</div>'


def render_system(s: dict) -> str:
    tones = s["tones"]
    tone_links = "".join(
        f'<li><a href="../tones/{html.escape(t)}.html">{html.escape(t)}</a></li>' for t in tones
    )
    philosophy = (
        '<div class="two-col"><div>'
        + field_block("principles", s["principles"])
        + field_block("fit", s["fit"])
        + "</div><div>"
        + f'<h3 class="block-title">Source</h3><p class="fit" style="font-size:0.9rem;margin-bottom:12px">'
        f'<a href="{html.escape(s["source"])}" rel="noopener noreferrer">{html.escape(s["source"])}</a>'
        f'<br/>Maker: {html.escape(s["maker"])}</p>'
        f'<h3 class="block-title">Closest catalog tones</h3><ul class="tone-pills">{tone_links}</ul>'
        + "</div></div>"
    )

    layout = field_block("layout", s["layout"]) + field_block("spacing", s["spacing"])

    typography = (
        '<div class="two-col"><div>'
        + field_block("typography", s["typography"])
        + "</div><div>"
        + '<h3 class="block-title">Suggested fonts</h3>'
        + resource_list(s["fonts"])
        + "</div></div>"
    )

    anatomy = (
        '<div class="two-col"><div>'
        + field_block("shape", s["shape"])
        + field_block("elevation", s["elevation"])
        + field_block("components", s["components"])
        + field_block("logo", s["logo"])
        + "</div><div>"
        + field_block("icons", s["icons"])
        + '<h3 class="block-title">Icon libraries</h3>'
        + resource_list(s["icon_libs"])
        + "</div></div>"
    )

    color = field_block("color", s["color"]) + field_block("themes", s["themes"])

    layers = (
        '<h3 class="block-title" style="margin-top:16px">Also fill when adapting</h3>'
        + field_block("motion", s["motion"])
        + field_block("patterns", s["patterns"])
        + field_block("content", s["content"])
        + field_block("accessibility", s["accessibility"])
    )
    dodont = (
        f'<div class="do-dont"><div class="do"><div class="label">Do (adapt)</div>'
        f'{html.escape(s["adapt"])}</div>'
        f'<div class="dont"><div class="label">Don’t</div>{html.escape(s["dont"])}</div></div>'
        + layers
    )

    bodies = {
        "philosophy": philosophy,
        "layout": layout,
        "type": typography,
        "anatomy": anatomy,
        "color": color,
        "dodont": dodont,
        "specimens": render_wireframes(),
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
<title>{html.escape(s["name"])} — Guidelines</title>
{HEAD}
<style>
{BASE_CSS}
{WF_BASE_CSS}
{s["css"]}
</style>
</head>
<body>
<div class="page">
<a class="back" href="index.html" aria-label="Back to design system catalog">{BACK_ICON}</a>
<h1 class="hero-title">{html.escape(s["name"])}</h1>
<p class="hero-sub">Guidelines</p>
<p class="fit">{html.escape(s["fit"])}</p>
<p class="meta-row"><span>System id <code>{html.escape(s["id"])}</code></span><span>·</span><span>{html.escape(s["maker"])}</span><span>·</span><span>Primary <code>{html.escape(s.get("primary", "—"))}</code></span><span>·</span><span>Write fields into <code>system.json</code></span></p>
{render_toc()}
{sections_html}
<p class="agent-note">Carry Philosophy → Layout → Type (incl. suggested fonts) → Anatomy (incl. icon libraries) → Color into Foundations. Specimens are the shared Harbor set — match this system’s skin and the chosen tone. Skip any field marked Unconfirmed when adapting.</p>
</div>
</body>
</html>
"""


def render_index(systems: list[dict]) -> str:
    skins_css = []
    tiles = []
    shell = SHARED_WFS["shell"]
    for s in systems:
        sid = s["id"]
        skins_css.append(scope_css(sid, s["css"]))
        tones = ", ".join(s["tones"])
        primary = s.get("primary", "#111")
        tiles.append(
            f'<a class="wf-link" href="{html.escape(sid)}.html">'
            f'<div class="wf-frame"><div class="t skin-{html.escape(sid)}">{shell}</div></div>'
            f'<div class="wf-caption">'
            f'<div class="name">{html.escape(s["name"])}</div>'
            f'<div class="tid">{html.escape(sid)}</div>'
            f'<p class="fit">{html.escape(s["fit"])}</p>'
            f'<div class="meta">'
            f'<span class="swatch" style="background:{html.escape(primary)}"></span>'
            f'{html.escape(primary)} · {html.escape(s["maker"])} · tones:{html.escape(tones)}'
            f"</div></div></a>"
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Design system catalog — UX build kit</title>
{HEAD}
<style>
{BASE_CSS}
{WF_BASE_CSS}
{"".join(skins_css)}
</style>
</head>
<body>
<div class="page">
<h1 class="hero-title">Design system catalog</h1>
<p class="hero-sub">SaaS wireframes</p>
<p class="fit">Same Harbor shell for every system — compare skins, then open a guide. Specimens stay identical; each system’s primary brand color drives buttons, active nav, chips, and tags.</p>
<p class="agent-note" style="margin-top:0">Dashed frames are wireframe chrome (0 radius). Fonts, icon libraries, and the primary swatch are on each tile / guidelines page.</p>
<div class="index-board">
{chr(10).join(tiles)}
</div>
</div>
</body>
</html>
"""


def main() -> list[str]:
    for s in SYSTEMS:
        for key in ("fonts", "icon_libs", "css", "tones", "dont", "adapt", "primary"):
            if key not in s:
                raise SystemExit(f"{s['id']} missing {key}")
        if not re.fullmatch(r"#[0-9a-fA-F]{3,8}", s["primary"]):
            raise SystemExit(f"{s['id']} primary must be a hex color, got {s['primary']!r}")

    for path in OUT.glob("*.html"):
        path.unlink()

    written = []
    for s in SYSTEMS:
        (OUT / f"{s['id']}.html").write_text(render_system(s), encoding="utf-8")
        written.append(s["id"])

    (OUT / "index.html").write_text(render_index(SYSTEMS), encoding="utf-8")
    return written


if __name__ == "__main__":
    ids = main()
    print(f"Wrote index.html + {len(ids)} system guides")
    for i in ids:
        print(f"  {i}.html")
