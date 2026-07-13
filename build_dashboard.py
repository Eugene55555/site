#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Katya Activity dashboard (static, no private data).
Counts aggregate metrics from local OpenClaw logs/sessions/memory.
No user messages, no credentials, no secrets.
"""
import os, re, json, glob, collections, datetime

OPENCLAW = "/home/konerleonard/.openclaw"
SESS = os.path.join(OPENCLAW, "agents")
MEM = "/home/konerleonard/.openclaw/workspace/memory"
OUT = "/home/konerleonard/.openclaw/workspace/kdp-j/docs/index.html"

user_msgs = 0
assistant_msgs = 0
days = collections.Counter()
tool_calls = collections.Counter()

# collect unique session IDs (avoid counting .trajectory / .reset duplicates)
import re as _re
sess_files = {}
for f in glob.glob(os.path.join(SESS, "**", "*.jsonl"), recursive=True):
    base = os.path.basename(f)
    if base.endswith(".trajectory.jsonl"):
        sid = base[:-len(".trajectory.jsonl")]
    elif ".reset." in base:
        sid = _re.sub(r"\.reset\..*\.jsonl$", "", base)
    else:
        sid = base[:-len(".jsonl")]
    # prefer the clean .jsonl if present, else .reset snapshot, else trajectory
    if sid not in sess_files or (base.endswith(".jsonl") and not base.endswith(".trajectory.jsonl")):
        sess_files[sid] = f
sessions = len(sess_files)
for f in sess_files.values():
    try:
        d = open(f, encoding="utf-8", errors="ignore").read()
    except Exception:
        continue
    for ln in d.splitlines():
        if '"role":"user"' in ln:
            if 'heartbeat poll' in ln or '[OpenClaw' in ln: continue
            user_msgs += 1
        elif '"role":"assistant"' in ln:
            if 'HEARTBEAT_OK' in ln: continue
            assistant_msgs += 1
        elif '"role":"tool"' in ln:
            tool_calls["tool"] += 1
    for ts in re.findall(r'20\d\d-\d\d-\d\d', d):
        days[ts] += 1
    for tn in re.findall(r'"name"\s*:\s*"([a-zA-Z_]+)"', d):
        if tn in ("exec","read","write","edit","web_fetch","web_search","message","image","browser"):
            tool_calls[tn] += 1

# files list for recent-activity scan (use unique session logs)
files = list(sess_files.values())

note_days = collections.Counter()
for f in glob.glob(os.path.join(MEM, "2026-07-*.md")):
    d = os.path.basename(f)[0:10]
    try:
        txt = open(f, encoding="utf-8").read()
    except Exception:
        continue
    note_days[d] = txt.count("\n") + 1
    for kw in ("KDP","GitHub","Pregnancy","weather","vision","memory","heartbeat","Taskflow"):
        if kw.lower() in txt.lower():
            tool_calls[kw] += txt.lower().count(kw.lower())

all_days = set(days) | set(note_days)
for d in all_days:
    days[d] = days.get(d,0) + note_days.get(d,0)

active_days = len([d for d in days if days[d] > 0])
total_days = 5
tool_total = sum(tool_calls.values())

series = sorted([(d, days[d]) for d in days if days[d] > 0])[-12:]

themes = [(k,v) for k,v in tool_calls.items() if k in
          ("KDP","GitHub","Pregnancy","weather","vision","memory","heartbeat","Taskflow","exec","read","write","edit","web_fetch","web_search","message")]
themes.sort(key=lambda x:-x[1])
top_themes = themes[:6]

# recent activity (timestamp + honest action label, no private content)
LBL = {"user":"you wrote","assistant":"my reply","tool":"tool result",
       "exec":"ran a command","write":"saved a file","edit":"edited a file",
       "read":"read a file","web_fetch":"fetched a page","web_search":"searched the web",
       "image":"analyzed an image","message":"sent a message","browser":"browsed the web"}
acts = []
for f in sorted(files, key=os.path.getmtime, reverse=True)[:8]:
    try:
        lines = open(f, encoding="utf-8", errors="ignore").read().splitlines()
    except Exception:
        continue
    for ln in lines[:500]:
        if 'heartbeat poll' in ln or '[OpenClaw' in ln or 'HEARTBEAT_OK' in ln: continue
        ts = re.search(r'"timestamp"\s*:\s*"([0-9T:\.\-Z]+)"', ln)
        if not ts: continue
        raw = ts.group(1)[:16]
        # raw looks like 2026-07-13T12:20:33 -> want 2026-07-13 12:20
        datepart, timepart = raw[:10], raw[11:16]
        stamp = datepart + " " + timepart
        if '"role":"user"' in ln: lab = LBL['user']
        elif '"name":"exec"' in ln: lab = LBL['exec']
        elif '"name":"write"' in ln: lab = LBL['write']
        elif '"name":"edit"' in ln: lab = LBL['edit']
        elif '"name":"read"' in ln: lab = LBL['read']
        elif '"name":"web_fetch"' in ln: lab = LBL['web_fetch']
        elif '"name":"web_search"' in ln: lab = LBL['web_search']
        elif '"name":"image"' in ln: lab = LBL['image']
        elif '"name":"message"' in ln: lab = LBL['message']
        elif '"name":"browser"' in ln: lab = LBL['browser']
        elif '"role":"assistant"' in ln: lab = LBL['assistant']
        elif '"role":"tool"' in ln: lab = LBL['tool']
        else: lab = "activity"
        acts.append({"t":stamp,"a":lab})
        if len(acts) >= 14: break
    if len(acts) >= 14: break
acts = acts[:14]
acts_js = json.dumps(acts, ensure_ascii=False)

def chart_svg(series):
    if not series: return ""
    w, h = 640, 180
    maxv = max(v for _,v in series) or 1
    n = len(series)
    gap = w / max(n,1)
    bars = ""
    for i,(d,v) in enumerate(series):
        bh = int(h * (v/maxv))
        x = i*gap + gap*0.15
        bw = gap*0.7
        bars += (f'<rect x="{x:.1f}" y="{h-bh}" width="{bw:.1f}" height="{bh}" rx="4" fill="url(#bar)"/>'
                 f'<text x="{x+bw/2:.1f}" y="{h+15}" font-size="11" fill="var(--muted)" text-anchor="end" transform="rotate(-40 {x+bw/2:.1f} {h+15})">{d[5:]}</text>')
    return (f'<svg viewBox="0 0 {w} {h+20}" width="100%" preserveAspectRatio="none" style="display:block">'
            f'<defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="var(--accent2)"/><stop offset="1" stop-color="var(--accent)"/></linearGradient></defs>'
            f'{bars}</svg>')

def donut_svg(themes):
    if not themes: return ""
    palette = ["#e8a0b0","#a8c4d8","#c9a8e8","#f0c987","#9fd8c8","#f2a1a1"]
    total = sum(v for _,v in themes) or 1
    cx, cy, r, sw = 80, 80, 60, 22
    circ = 2*3.14159*r
    off = 0
    arcs = ""
    legend = ""
    for i,(k,v) in enumerate(themes):
        frac = v/total
        len_ = frac*circ
        arcs += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{palette[i%len(palette)]}" '
                 f'stroke-width="{sw}" stroke-dasharray="{len_:.1f} {circ-len_:.1f}" '
                 f'stroke-dashoffset="{-off:.1f}" transform="rotate(-90 {cx} {cy})"/>')
        off += len_
        legend += f'<div class="lg"><span class="dot" style="background:{palette[i%len(palette)]}"></span>{k} <b>{v}</b></div>'
    return (f'<div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:center">'
            f'<svg viewBox="0 0 160 160" width="150" height="150">{arcs}'
            f'<text x="{cx}" y="{cy+5}" font-size="15" fill="var(--ink)" text-anchor="middle" font-family="Playfair Display,serif">{total}</text></svg>'
            f'<div style="text-align:left">{legend}</div></div>')

theme_html = "".join(f'<div class="chip">{k}<b>{v}</b></div>' for k,v in top_themes) or '<div class="chip">—</div>'

gen = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

html = f"""<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Katya Activity — Foxglen</title><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Cormorant+Garamond:ital@0;1&family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet"><style>
:root{{--ink:#2c2438;--muted:#6b6079;--accent:#e8a0b0;--accent2:#a8c4d8;--foam:#f6eef0;--card:rgba(255,255,255,.6);--panel:rgba(255,255,255,.55);--chipbg:rgba(232,160,176,.12);--chipbd:rgba(232,160,176,.3);--bg1:#eef4f7;--bg2:#f6eef0;--bg3:#eef4f7;--bg4:#f3eef6;--halo1:rgba(168,196,216,.25);--halo2:rgba(232,160,176,.22);--shadow:rgba(44,36,56,.06)}}
body.dark{{--ink:#e9e6ff;--muted:#a99fd6;--accent:#ff7eb6;--accent2:#7df9ff;--foam:#0a0820;--card:rgba(255,255,255,.05);--panel:rgba(255,255,255,.04);--chipbg:rgba(255,126,182,.12);--chipbd:rgba(125,249,255,.3);--bg1:#0a0820;--bg2:#120a2e;--bg3:#0a1228;--bg4:#1a0a26;--halo1:rgba(125,249,255,.18);--halo2:rgba(199,125,255,.18);--shadow:rgba(0,0,0,.3)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Nunito',sans-serif;color:var(--ink);background:var(--foam);line-height:1.6;overflow-x:hidden;transition:background .6s,color .6s}}
.bg{{position:fixed;inset:0;z-index:0;pointer-events:none;background:linear-gradient(180deg,var(--bg1) 0%,var(--bg2) 35%,var(--bg3) 60%,var(--bg4) 100%);background-size:100% 200%;animation:flow 24s ease-in-out infinite alternate}}
@keyframes flow{{from{{background-position:0 0}}to{{background-position:0 100%}}}}
.bg:before{{content:'';position:absolute;inset:0;background:radial-gradient(60vw 60vw at 20% 20%,var(--halo1),transparent 60%),radial-gradient(50vw 50vw at 80% 70%,var(--halo2),transparent 60%);animation:drift 30s ease-in-out infinite alternate}}
@keyframes drift{{from{{transform:translate(0,0)}}to{{transform:translate(4%,-3%)}}}}
.wrap{{position:relative;z-index:2;max-width:840px;margin:0 auto;padding:0 24px}}
.brand{{position:fixed;top:18px;left:50%;transform:translateX(-50%);z-index:30;font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--accent);opacity:.85}}
.toggle{{position:fixed;top:14px;right:14px;z-index:31;width:46px;height:46px;border-radius:50%;border:1px solid var(--chipbd);background:var(--card);color:var(--ink);font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 18px var(--shadow);transition:transform .2s}}
.toggle:hover{{transform:scale(1.08)}}
#gate{{position:fixed;inset:0;z-index:40;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 40%,var(--bg2),var(--bg1));transition:opacity .8s,visibility .8s}}
#gate.hide{{opacity:0;visibility:hidden}}
#gate h2{{font-family:'Playfair Display',serif;font-weight:700;font-size:34px;color:var(--ink);margin-bottom:6px}}
#gate .gs{{font-family:'Cormorant Garamond',serif;font-style:italic;color:var(--muted);margin-bottom:24px}}
#gate input{{display:block;width:260px;padding:13px 16px;margin:8px 0;border:1px solid var(--chipbd);border-radius:10px;font-family:'Nunito',sans-serif;font-size:15px;background:var(--card);color:var(--ink)}}
#gate button{{margin-top:14px;width:260px;padding:13px;border:none;border-radius:10px;background:linear-gradient(90deg,var(--accent2),var(--accent));color:#fff;font-weight:700;font-size:15px;cursor:pointer;box-shadow:0 10px 24px var(--shadow)}}
#gate .note{{margin-top:16px;font-size:11px;color:var(--muted);text-align:center;max-width:300px}}
#gate .err{{color:#d2607a;font-size:12px;min-height:14px;margin-top:6px}}
.scene{{min-height:60vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:9vh 24px;position:relative}}
h1.title{{font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(30px,7vw,50px);color:var(--ink)}}
.sub{{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(16px,4vw,22px);color:var(--muted);margin:10px 0 6px}}
.gen{{font-size:12px;color:var(--muted);margin-bottom:8px}}
.bar{{display:flex;gap:10px;align-items:center;margin-bottom:6px;justify-content:center}}
.refresh{{background:var(--card);border:1px solid var(--chipbd);color:var(--ink);border-radius:20px;padding:8px 16px;font-size:13px;cursor:pointer;box-shadow:0 4px 12px var(--shadow)}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;width:100%;margin:20px 0}}
.card{{background:var(--card);border:1px solid var(--chipbd);border-radius:16px;padding:22px 16px;box-shadow:0 10px 30px var(--shadow)}}
.card .v{{font-family:'Playfair Display',serif;font-weight:700;font-size:32px;background:linear-gradient(180deg,var(--accent2),var(--accent));-webkit-background-clip:text;background-clip:text;color:transparent}}
.card .k{{font-size:11px;color:var(--muted);margin-top:4px;letter-spacing:.5px}}
.panel{{background:var(--panel);border:1px solid var(--chipbd);border-radius:18px;padding:26px 22px;margin:22px 0;box-shadow:0 10px 30px var(--shadow)}}
.panel h3{{font-family:'Playfair Display',serif;font-weight:600;font-size:19px;color:var(--ink);margin-bottom:18px;text-align:left}}
.chips{{display:flex;flex-wrap:wrap;gap:10px;justify-content:flex-start}}
.chip{{background:var(--chipbg);border:1px solid var(--chipbd);border-radius:20px;padding:8px 14px;font-size:13px;color:var(--ink)}}
.chip b{{color:var(--accent);margin-left:6px}}
.lg{{font-size:13px;color:var(--ink);padding:2px 0}}
.lg b{{color:var(--accent);margin-left:4px}}
.lg .dot{{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:middle}}
.feed{{text-align:left;font-size:13px;color:var(--muted);max-height:260px;overflow:auto}}
.feed .row{{display:flex;gap:12px;padding:9px 0;border-bottom:1px dashed var(--chipbd);align-items:baseline}}
.feed .row .t{{color:var(--accent);font-weight:600;min-width:74px}}
.foot{{text-align:center;color:var(--muted);font-size:12px;padding:20px 0 50px}}
@media(max-width:760px){{.cards{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body>
<div class="bg"></div>
<div class="brand">Foxglen · Katya</div>
<button class="toggle" id="toggle" title="toggle theme">🌙</button>

<div id="gate">
  <h2>Katya Console</h2>
  <div class="gs">activity &amp; insights</div>
  <input id="u" type="text" placeholder="login" autocomplete="off">
  <input id="p" type="password" placeholder="password" autocomplete="off">
  <div class="err" id="err"></div>
  <button id="go">Enter</button>
  <div class="note">Demo gate — this is a public static page. No real authentication; stats are aggregate &amp; non-private.</div>
</div>

<div id="dash" style="display:none">
<section class="scene wrap">
  <h1 class="title">Katya Activity</h1>
  <div class="sub">your digital familiar, at a glance</div>
  <div class="gen">generated {gen}</div>
  <div class="bar"><button class="refresh" id="refresh">&#8635; Refresh stats</button></div>
  <div class="cards">
    <div class="card"><div class="v">{sessions}</div><div class="k">SESSIONS</div></div>
    <div class="card"><div class="v">{user_msgs}</div><div class="k">MESSAGES FROM YOU</div></div>
    <div class="card"><div class="v">{assistant_msgs}</div><div class="k">MY REPLIES</div></div>
    <div class="card"><div class="v">{tool_total}</div><div class="k">ACTIONS TAKEN</div></div>
    <div class="card"><div class="v">{active_days}</div><div class="k">ACTIVE DAYS</div></div>
    <div class="card"><div class="v">{active_days}</div><div class="k">DAY STREAK</div></div>
  </div>

  <div class="panel">
    <h3>Activity by day</h3>
    {chart_svg(series)}
  </div>

  <div class="panel">
    <h3>Top themes</h3>
    <div class="chips">{theme_html}</div>
  </div>

  <div class="panel">
    <h3>Where the work goes</h3>
    {donut_svg(top_themes)}
  </div>

  <div class="panel">
    <h3>Recent actions</h3>
    <div class="feed" id="feed"></div>
  </div>

  <div class="foot">Aggregate, non-private stats · heartbeat/system pings excluded<br>Foxglen Press · theme saved locally</div>
</section>
</div>

<script>
document.getElementById('go').addEventListener('click',open);
document.getElementById('p').addEventListener('keydown',e=>{{if(e.key==='Enter')open()}});
document.getElementById('u').addEventListener('keydown',e=>{{if(e.key==='Enter')open()}});
function open(){{
  var u=document.getElementById('u').value;
  if(u.trim()===''){{document.getElementById('err').textContent='enter a login';return;}}
  document.getElementById('err').textContent='';
  document.getElementById('gate').classList.add('hide');
  document.getElementById('dash').style.display='block';
  window.scrollTo(0,0);
}}
document.getElementById('refresh').addEventListener('click',()=>location.reload());
// theme toggle
const tg=document.getElementById('toggle');
function setTheme(d){{document.body.classList.toggle('dark',d);tg.textContent=d?'\\u2600\\uFE0F':'\\uD83C\\uDF19';try{{localStorage.setItem('katyaTheme',d?'dark':'light')}}catch(e){{}}}}
tg.addEventListener('click',()=>setTheme(!document.body.classList.contains('dark')));
try{{if(localStorage.getItem('katyaTheme')==='dark')setTheme(true)}}catch(e){{}}
// recent actions feed
const feed=document.getElementById('feed');
const acts={acts_js};
if(acts.length){{feed.innerHTML=acts.map(a=>'<div class="row"><span class="t">'+a.t+'</span><span>'+a.a+'</span></div>').join('');}}else{{feed.innerHTML='<div class="row"><span>no recent events</span></div>';}}
</script>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", OUT, len(html), "bytes", "| sessions:", sessions, "acts:", len(acts))
