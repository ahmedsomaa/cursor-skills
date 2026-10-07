# Best-fit SaaS wireframes per tone (same 4 slots; product context changes).
# Markup uses shared `.t` classes from render.py WF_BASE_CSS.

def _shell(brand, nav, side, title, muted, chips, cta="New"):
    nav_html = "".join(
        f'<span class="on">{n}</span>' if i == 0 else f"<span>{n}</span>" for i, n in enumerate(nav)
    )
    side_html = "".join(
        f'<div class="nav-item{" on" if i == 0 else ""}">{s}</div>' for i, s in enumerate(side)
    )
    chips_html = "".join(
        f'<span class="chip{" on" if c.get("on") else ""}">{c["label"]}</span>' for c in chips
    )
    return f"""
<div class="stage">
  <div class="top">
    <span class="brand">{brand}</span>
    <nav class="nav">{nav_html}</nav>
    <span class="meta">Alex</span>
  </div>
  <div class="body">
    <aside class="side">{side_html}</aside>
    <main class="main">
      <div class="title-row"><h3>{title}</h3><span class="btn">{cta}</span></div>
      <p class="muted">{muted}</p>
      <div class="chips">{chips_html}</div>
    </main>
  </div>
</div>""".strip()


def _data(brand, meta, headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for row in rows:
        cells = ""
        for cell in row:
            if isinstance(cell, dict) and cell.get("tag"):
                muted = " muted" if cell.get("muted") else ""
                cells += f'<td><span class="tag{muted}">{cell["tag"]}</span></td>'
            else:
                cells += f"<td>{cell}</td>"
        body += f"<tr>{cells}</tr>"
    return f"""
<div class="stage">
  <div class="top">
    <span class="brand">{brand}</span>
    <span class="meta">{meta}</span>
  </div>
  <table class="grid">
    <thead><tr>{th}</tr></thead>
    <tbody>{body}</tbody>
  </table>
</div>""".strip()


def _form(title, fields, cta):
    fields_html = ""
    for label, value in fields:
        fields_html += f"<label>{label}</label><input value=\"{value}\" readonly/>"
    return f"""
<div class="stage pad">
  <div class="panel">
    <h3>{title}</h3>
    {fields_html}
    <div class="actions"><span class="btn">{cta}</span></div>
  </div>
</div>""".strip()


def _moment(title, body, ghost, primary, *, destructive=False):
    cls = "btn danger" if destructive else "btn"
    return f"""
<div class="stage pad center">
  <div class="modal">
    <h3>{title}</h3>
    <p class="muted">{body}</p>
    <div class="actions">
      <span class="btn ghost">{ghost}</span>
      <span class="{cls}">{primary}</span>
    </div>
  </div>
</div>""".strip()


# Tone → four SaaS specimens
WFS: dict[str, dict[str, str]] = {
    "swiss": {
        "shell": _shell(
            "Ledger",
            ["Workspace", "Billing", "Members"],
            ["Overview", "Invoices", "Audit"],
            "Workspace",
            "Plan · Growth · Renews Apr 12",
            [{"label": "Usage"}, {"label": "Seats", "on": True}, {"label": "Limits"}],
            "Invite",
        ),
        "data": _data(
            "Ledger",
            "24 invoices",
            ["Invoice", "Customer", "Status"],
            [
                ["INV-1042", "Northwind", {"tag": "Paid"}],
                ["INV-1041", "Atlas Co", {"tag": "Paid"}],
                ["INV-1040", "Beacon", {"tag": "Open", "muted": True}],
                ["INV-1039", "Cedar", {"tag": "Paid"}],
            ],
        ),
        "form": _form("Workspace settings", [("Name", "Ledger Inc"), ("Billing email", "ops@ledger.app")], "Save"),
        "moment": _moment("Archive workspace?", "Members lose access immediately.", "Cancel", "Archive", destructive=True),
    },
    "minimalism": {
        "shell": _shell(
            "Focus",
            ["Today", "Later"],
            ["Inbox", "Done"],
            "Today",
            "One clear next step",
            [{"label": "Now", "on": True}, {"label": "Soon"}],
            "Continue",
        ),
        "data": _data(
            "Focus",
            "3 tasks",
            ["Task", "When", ""],
            [
                ["Ship pricing page", "Today", {"tag": "Now"}],
                ["Reply to Sam", "Today", {"tag": "Now"}],
                ["Review contract", "Later", {"tag": "Soon", "muted": True}],
            ],
        ),
        "form": _form("Rename task", [("Title", "Ship pricing page")], "Save"),
        "moment": _moment("Nothing here yet", "Create the first task when you’re ready.", "Not now", "New task"),
    },
    "maximalism": {
        "shell": _shell(
            "Studio",
            ["Store", "Audience", "Payouts"],
            ["Products", "Posts", "Tips"],
            "Storefront",
            "12 products · $4.2k this week",
            [{"label": "Live", "on": True}, {"label": "Drafts"}, {"label": "Bundles"}],
            "Add product",
        ),
        "data": _data(
            "Studio",
            "18 sales today",
            ["Product", "Buyer", "Status"],
            [
                ["Neon kit", "Maya", {"tag": "Paid"}],
                ["Poster pack", "Omar", {"tag": "Paid"}],
                ["LUT bundle", "Rae", {"tag": "Pending", "muted": True}],
                ["Icon set", "Jin", {"tag": "Paid"}],
            ],
        ),
        "form": _form("New product", [("Title", "Neon starter kit"), ("Price", "$29")], "Publish"),
        "moment": _moment("Launch to storefront?", "Buyers can purchase immediately.", "Keep draft", "Launch"),
    },
    "neo-brutalism": {
        "shell": _shell(
            "Punch",
            ["Dashboard", "Customers", "$$"],
            ["Today", "Queue", "Spam"],
            "Dashboard",
            "Cash out Friday · 3 alerts",
            [{"label": "Sales", "on": True}, {"label": "Traffic"}, {"label": "Fees"}],
            "Do it",
        ),
        "data": _data(
            "Punch",
            "Queue · 4",
            ["Job", "Who", "State"],
            [
                ["Payout run", "You", {"tag": "RUN"}],
                ["Tax export", "Bot", {"tag": "WAIT", "muted": True}],
                ["Webhook retry", "Sys", {"tag": "RUN"}],
                ["Refund batch", "You", {"tag": "DONE"}],
            ],
        ),
        "form": _form("Sign up", [("Email", "you@company.com"), ("Password", "••••••••")], "Create account"),
        "moment": _moment("Delete this product?", "Gone forever. No undo.", "Nope", "Yes delete", destructive=True),
    },
    "soft": {
        "shell": _shell(
            "Calmly",
            ["Home", "Sessions", "Care"],
            ["Today", "Library", "Coach"],
            "Home",
            "Good evening · 12 min left in streak",
            [{"label": "Breathe", "on": True}, {"label": "Sleep"}, {"label": "Focus"}],
            "Start",
        ),
        "data": _data(
            "Calmly",
            "This week",
            ["Session", "Length", "Feel"],
            [
                ["Evening wind-down", "12m", {"tag": "Done"}],
                ["Focus block", "25m", {"tag": "Done"}],
                ["Morning stretch", "8m", {"tag": "Skip", "muted": True}],
                ["Gratitude", "5m", {"tag": "Done"}],
            ],
        ),
        "form": _form("Preferences", [("Display name", "Alex"), ("Reminders", "Evenings")], "Save"),
        "moment": _moment("Take a pause?", "We’ll save your place.", "Keep going", "Pause"),
    },
    "editorial": {
        "shell": _shell(
            "Gazette",
            ["Drafts", "Published", "Extras"],
            ["All stories", "Features", "Notes"],
            "Drafts",
            "3 ready · 1 needs edit",
            [{"label": "Mine", "on": True}, {"label": "Desk"}, {"label": "Scheduled"}],
            "New story",
        ),
        "data": _data(
            "Gazette",
            "12 stories",
            ["Headline", "Author", "Status"],
            [
                ["Grid before ornament", "Alex", {"tag": "Draft", "muted": True}],
                ["Type leads color", "Sam", {"tag": "Live"}],
                ["Signal red", "Riley", {"tag": "Review"}],
                ["Quiet margins", "Jordan", {"tag": "Live"}],
            ],
        ),
        "form": _form("Publish settings", [("Headline", "Grid before ornament"), ("Section", "Design")], "Schedule"),
        "moment": _moment("Publish now?", "Story goes live on the homepage.", "Keep editing", "Publish"),
    },
    "liquid-glass": {
        "shell": _shell(
            "Orb",
            ["Workspace", "Files", "Share"],
            ["Recents", "Starred", "Trash"],
            "Workspace",
            "Synced · 2 devices",
            [{"label": "Boards", "on": True}, {"label": "Docs"}, {"label": "Media"}],
            "New",
        ),
        "data": _data(
            "Orb",
            "Recents",
            ["Name", "Kind", "Updated"],
            [
                ["Q2 narrative", "Doc", {"tag": "Live"}],
                ["Launch board", "Board", {"tag": "Live"}],
                ["Brand kit", "File", {"tag": "Shared"}],
                ["Offsite notes", "Doc", {"tag": "Private", "muted": True}],
            ],
        ),
        "form": _form("New board", [("Name", "Launch plan"), ("Visibility", "Team")], "Create"),
        "moment": _moment("Move to Trash?", "You can restore within 30 days.", "Cancel", "Move", destructive=True),
    },
    "dark-industrial": {
        "shell": _shell(
            "Signal",
            ["Ops", "Services", "Deploys"],
            ["Incidents", "SLOs", "Logs"],
            "Incidents",
            "2 open · p95 182ms",
            [{"label": "Open", "on": True}, {"label": "Resolved"}, {"label": "Muted"}],
            "Declare",
        ),
        "data": _data(
            "Signal",
            "Live feed",
            ["Incident", "Service", "Sev"],
            [
                ["Checkout latency", "payments", {"tag": "SEV-2"}],
                ["Auth spike", "identity", {"tag": "SEV-3", "muted": True}],
                ["Queue lag", "workers", {"tag": "SEV-2"}],
                ["CDN miss storm", "edge", {"tag": "SEV-4", "muted": True}],
            ],
        ),
        "form": _form("Alert rule", [("Metric", "checkout.p95"), ("Threshold", "> 400ms")], "Save rule"),
        "moment": _moment("Page on-call?", "Pages the primary for payments.", "Cancel", "Page now", destructive=True),
    },
    "bauhaus": {
        "shell": _shell(
            "Forma",
            ["Canvas", "Assets", "Share"],
            ["Files", "Components", "Tokens"],
            "Files",
            "8 files · 2 shared",
            [{"label": "Recent", "on": True}, {"label": "Team"}, {"label": "Archive"}],
            "New file",
        ),
        "data": _data(
            "Forma",
            "Assets",
            ["Name", "Type", "Status"],
            [
                ["Primary mark", "SVG", {"tag": "Live"}],
                ["Type scale", "Token", {"tag": "Live"}],
                ["Poster A1", "Frame", {"tag": "Draft", "muted": True}],
                ["Icon grid", "Comp", {"tag": "Live"}],
            ],
        ),
        "form": _form("New file", [("Name", "Campaign poster"), ("Format", "Frame")], "Create"),
        "moment": _moment("Export PNG?", "2x and 3x will download.", "Cancel", "Export"),
    },
    "calm-density": {
        "shell": _shell(
            "Linearish",
            ["Inbox", "My issues", "Projects"],
            ["Active", "Backlog", "Triage"],
            "Active",
            "14 issues · Updated 2m ago",
            [{"label": "All", "on": True}, {"label": "Mine"}, {"label": "Bugs"}],
            "New issue",
        ),
        "data": _data(
            "Linearish",
            "14 issues",
            ["ID", "Title", "Status"],
            [
                ["HAR-182", "Fix billing webhook", {"tag": "In progress"}],
                ["HAR-179", "Empty state copy", {"tag": "Todo", "muted": True}],
                ["HAR-176", "SAML timeout", {"tag": "In progress"}],
                ["HAR-170", "CSV export", {"tag": "Done"}],
            ],
        ),
        "form": _form("New issue", [("Title", "Fix billing webhook"), ("Priority", "High")], "Create issue"),
        "moment": _moment("Mark as Done?", "HAR-182 moves to Done.", "Keep open", "Done"),
    },
    "japandi": {
        "shell": _shell(
            "Ma",
            ["Space", "Rituals", "Notes"],
            ["Today", "Week", "Later"],
            "Today",
            "Three things · leave room",
            [{"label": "Focus", "on": True}, {"label": "Rest"}, {"label": "Home"}],
            "Add",
        ),
        "data": _data(
            "Ma",
            "This week",
            ["Ritual", "When", "State"],
            [
                ["Morning pages", "Daily", {"tag": "On"}],
                ["Desk clear", "Fri", {"tag": "On"}],
                ["Deep work", "Tue/Thu", {"tag": "Pause", "muted": True}],
                ["Walk", "Daily", {"tag": "On"}],
            ],
        ),
        "form": _form("Quiet settings", [("Name", "Ma"), ("Theme", "Warm paper")], "Save"),
        "moment": _moment("Clear the desk?", "Archive finished rituals for this week.", "Not yet", "Clear"),
    },
    "terminal": {
        "shell": _shell(
            "shipctl",
            ["apps", "deploys", "logs"],
            ["prod", "staging", "preview"],
            "deploys",
            "prod · healthy · v2.14.3",
            [{"label": "running", "on": True}, {"label": "failed"}, {"label": "queued"}],
            "deploy",
        ),
        "data": _data(
            "shipctl",
            "last 4 deploys",
            ["id", "target", "status"],
            [
                ["dpl_9f2a", "prod", {"tag": "ok"}],
                ["dpl_9f19", "staging", {"tag": "ok"}],
                ["dpl_9f08", "prod", {"tag": "failed", "muted": True}],
                ["dpl_9ef1", "preview", {"tag": "ok"}],
            ],
        ),
        "form": _form("set env", [("KEY", "DATABASE_URL"), ("VALUE", "postgres://•••")], "apply"),
        "moment": _moment("deploy to prod?", "ships commit 9f2a to production.", "abort", "deploy", destructive=True),
    },
    "clay": {
        "shell": _shell(
            "Buddy",
            ["People", "Pipelines", "Hugs"],
            ["All", "Warm", "Cold"],
            "People",
            "128 contacts · 6 due today",
            [{"label": "Customers", "on": True}, {"label": "Leads"}, {"label": "Friends"}],
            "Add",
        ),
        "data": _data(
            "Buddy",
            "Due today",
            ["Name", "Company", "Stage"],
            [
                ["Sam Lee", "Northwind", {"tag": "Warm"}],
                ["Riley Chen", "Beacon", {"tag": "Lead"}],
                ["Jordan Park", "Cedar", {"tag": "Customer"}],
                ["Alex Kim", "Atlas", {"tag": "Cold", "muted": True}],
            ],
        ),
        "form": _form("Add contact", [("Name", "Sam Lee"), ("Email", "sam@northwind.co")], "Save contact"),
        "moment": _moment("Nice work!", "Sam moved to Customer.", "Close", "Next"),
    },
    "aurora": {
        "shell": _shell(
            "Lumen",
            ["Chat", "Projects", "Usage"],
            ["Home", "Agents", "Library"],
            "Projects",
            "4 agents · 82% monthly budget",
            [{"label": "Active", "on": True}, {"label": "Sleeping"}, {"label": "Shared"}],
            "New agent",
        ),
        "data": _data(
            "Lumen",
            "Generations today",
            ["Run", "Model", "State"],
            [
                ["Brief rewrite", "lumen-2", {"tag": "Done"}],
                ["UI variants", "lumen-2", {"tag": "Running"}],
                ["SQL helper", "lumen-mini", {"tag": "Done"}],
                ["Image board", "lumen-vision", {"tag": "Queued", "muted": True}],
            ],
        ),
        "form": _form("Agent settings", [("Name", "Brief rewrite"), ("Model", "lumen-2")], "Save"),
        "moment": _moment("Stop generation?", "Partial output will be kept.", "Keep going", "Stop", destructive=True),
    },
    "cyberpunk": {
        "shell": _shell(
            "NIGHTWATCH",
            ["SOC", "Assets", "Playbooks"],
            ["Alerts", "Hunt", "Intel"],
            "Alerts",
            "7 open · 1 critical",
            [{"label": "Critical", "on": True}, {"label": "High"}, {"label": "Noise"}],
            "Declare",
        ),
        "data": _data(
            "NIGHTWATCH",
            "live alerts",
            ["Signal", "Asset", "Sev"],
            [
                ["Credential stuffing", "auth-gw", {"tag": "CRIT"}],
                ["Lateral scan", "vpc-east", {"tag": "HIGH"}],
                ["Beaconing host", "laptop-92", {"tag": "HIGH"}],
                ["Port sweep", "edge-3", {"tag": "LOW", "muted": True}],
            ],
        ),
        "form": _form("Detection rule", [("Name", "Credential stuffing"), ("Severity", "Critical")], "Deploy rule"),
        "moment": _moment("Escalate to IR?", "Pages incident response now.", "Hold", "Escalate", destructive=True),
    },
}
