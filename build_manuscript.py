#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for Pregnancy Journal manuscript (7x10 in) v4 - Foxglen Press.
Fixes vs v3: bigger photo/ultrasound boxes, aligned checkboxes, no bottom
clipping, balanced vertical rhythm (space-between), added weekly plan&review,
doctor visit form, baby-name 2 cols, letter to baby, nursery vision board,
footprint frame."""

OUT = "Pregnancy Journal/P/manuscript.html"

HEAD = """<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>Pregnancy Journal - Foxglen Press</title><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Cormorant+Garamond:ital@0;1&family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}
@page{size:7in 10in;margin:0}
body{font-family:'Nunito',sans-serif;color:#4a3f35;-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#dfe3e6}
.page{height:10in;width:7in;page-break-after:always;position:relative;display:flex;flex-direction:column;padding:.72in .8in;margin:0 auto;box-sizing:border-box}
.page.center{justify-content:center;align-items:center;text-align:center}
.page.between{justify-content:space-between}
.decoframe{position:absolute;top:.34in;left:.34in;right:.34in;bottom:.34in;border:1px solid #e3d8ca;pointer-events:none}
.ic{width:1em;height:1em;vertical-align:middle}
.bigic{width:1.7em;height:1.7em;display:block;margin:0 auto .15in}
.topdec{text-align:center;margin-bottom:.12in;opacity:.9}
.botdec{text-align:center;margin-top:.12in;opacity:.9}
.wk{font-family:'Playfair Display',serif;font-weight:700;font-size:22pt;text-align:center;color:#4a3f35;margin-bottom:.05in}
.wk.small{font-size:15pt}
.wk-sub{font-style:italic;font-size:12.5pt;text-align:center;color:#8a7a6a;margin-bottom:.12in}
.t1{font-family:'Playfair Display',serif;font-weight:700;font-size:32pt;color:#4a3f35;line-height:1.1}
.t2{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:18pt;color:#8a7a6a;margin-top:.14in}
.t3{font-size:11pt;color:#c9a86a;letter-spacing:1.5px;margin-top:.4in;text-transform:uppercase}
.goldline{width:2in;height:2px;background:#c9a86a;margin:.3in auto}
.prompt{font-size:11.5pt;color:#4a3f35;margin:.08in 0 0;display:flex;gap:.12in;align-items:baseline;line-height:1.4;font-weight:600}
.qmark{flex:0 0 auto;position:relative;top:.02in}
.write{border-bottom:1px solid #d9cebc;height:1.5em;margin:.15in 0}
.write.big{height:2.3em}
.body{font-size:11.5pt;line-height:1.75;color:#7a6c5c;margin:.18in 0;text-align:center}
.quote{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:13.5pt;text-align:center;color:#a8896a;margin:.16in auto;max-width:5in;line-height:1.4}
.chkgrid{display:grid;grid-template-columns:1fr 1fr;gap:.16in .4in;margin:.18in 0}
.chk{font-size:11pt;color:#4a3f35;display:flex;align-items:center;gap:.14in}
.chk .box{flex:0 0 auto;width:.2in;height:.2in;border:1.4px solid #c9a86a;border-radius:3px}
.photobox{border:1.5px dashed #c9a86a;border-radius:8px;display:flex;align-items:flex-end;justify-content:center;color:#a8967c;font-size:8.5pt;text-transform:uppercase;letter-spacing:1px;padding:.12in}
.usbox{border:2px solid #c9a86a;border-radius:10px;display:flex;align-items:flex-end;justify-content:center;color:#a8967c;font-size:8.5pt;background:#fffdf8;position:relative;padding:.12in;text-transform:uppercase;letter-spacing:1px}
.usbox:before{content:'ULTRASOUND';position:absolute;top:.14in;left:0;right:0;text-align:center;font-size:7pt;letter-spacing:1.5px;color:#c9a86a;font-weight:700}
.fullphoto{flex:1;margin:.16in 0}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:.25in;margin:.16in 0}
.fruitwrap{text-align:center;margin:.1in 0}
.fruitsize{font-size:11pt;color:#7a6c5c;background:#f3efe6;padding:.1in .22in;border-radius:20px;display:inline-block}
.fruitsize b{color:#4a3f35}
.snapshot{margin:.14in 0;padding:.16in .2in;border:1px solid #e3d8ca;border-radius:8px;background:#fffdf8}
.snaprow{display:flex;align-items:center;gap:.2in;font-size:10.5pt;color:#4a3f35;margin:.1in 0}
.snaprow .lbl{flex:0 0 1.1in}
.snaprow .dots{display:flex;gap:.14in}
.snaprow .dot{width:.16in;height:.16in;border:1.3px solid #c9a86a;border-radius:50%}
.win{font-size:10.5pt;color:#7a6c5c;margin-top:.06in}
.winline{display:inline-block;border-bottom:1px solid #d9cebc;width:2.6in}
.info{width:100%;border-collapse:collapse;margin:.1in 0}
.info td{padding:.15in .05in;font-size:11.5pt;border-bottom:1px dotted #bbaa90}
.info td.lbl{color:#4a3f35;font-weight:600;width:45%}
.track{width:100%;border-collapse:collapse;margin:.14in 0}
.track th,.track td{border:1px solid #e3d8ca;padding:.13in .06in;font-size:9.5pt;text-align:center}
.track th{font-style:italic;color:#8a7a6a;background:#f7f3ec}
.tabpage{height:10in;width:7in;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;page-break-after:always;padding:1in .9in;box-sizing:border-box}
.tabt{font-family:'Playfair Display',serif;font-weight:700;font-size:30pt;color:#4a3f35}
.tabsub{font-style:italic;color:#8a7a6a;margin-top:.14in;font-size:15pt}
.tabdesc{font-size:11.5pt;color:#7a6c5c;max-width:4.4in;margin:.3in auto;line-height:1.65}
.tablist{font-size:11pt;color:#4a3f35;margin:.2in auto;line-height:2}
.tg1{background:#f3efe6}.tg2{background:#eef3ea}.tg3{background:#f7eef0}.tg4{background:#fbf3e6}
.colh{font-style:italic;color:#a8896a;font-size:11pt;margin-bottom:.1in;text-align:center;font-weight:600}
.envwrap{text-align:center;margin:.2in 0}
.env{width:3.4in;height:2.4in}
.envlabel{font-style:italic;color:#8a7a6a;font-size:10.5pt;margin-top:.14in}
.stickers{display:flex;flex-wrap:wrap;gap:.16in;justify-content:center;margin:.2in auto;max-width:5.2in}
.stk{padding:.12in .22in;border:1px dashed #c9a86a;border-radius:20px;font-size:9.5pt;color:#8a7a6a}
.secttitle{font-family:'Playfair Display',serif;font-weight:700;font-size:19pt;text-align:center;color:#4a3f35;margin-bottom:.05in}
@media print{.no-print{display:none!important}}
</style></head><body>"""

SVG_DEFS = """<svg width="0" height="0" style="position:absolute"><defs>
<symbol id="leaf" viewBox="0 0 40 40"><path d="M20 4C10 12 10 28 20 36 30 28 30 12 20 4Z" fill="none" stroke="#a8c4a2" stroke-width="1.4"/><path d="M20 8 20 34" stroke="#a8c4a2" stroke-width=".8"/></symbol>
<symbol id="sprig" viewBox="0 0 120 22"><path d="M2 11H118" stroke="#a8c4a2" stroke-width="1.2" fill="none"/><path d="M30 11C24 4 24 18 30 11" stroke="#a8c4a2" stroke-width="1.2" fill="none"/><path d="M60 11C54 3 54 19 60 11" stroke="#a8c4a2" stroke-width="1.2" fill="none"/><path d="M90 11C84 4 84 18 90 11" stroke="#a8c4a2" stroke-width="1.2" fill="none"/></symbol>
<symbol id="foot" viewBox="0 0 34 22"><ellipse cx="16" cy="11" rx="9" ry="7" fill="#e8b4b8" opacity=".9"/><circle cx="27" cy="6" r="2.4" fill="#e8b4b8" opacity=".9"/><circle cx="29" cy="11" r="2" fill="#e8b4b8" opacity=".9"/><circle cx="29" cy="16" r="1.7" fill="#e8b4b8" opacity=".9"/></symbol>
<symbol id="heart" viewBox="0 0 18 18"><path d="M9 16C2 10 2 4 9 6 16 4 16 10 9 16Z" fill="#e8b4b8"/></symbol>
<symbol id="star" viewBox="0 0 16 16"><path d="M8 1 10 6 15 6 11 9 13 14 8 11 3 14 5 9 1 6 6 6Z" fill="#c9a86a"/></symbol>
<symbol id="fruit" viewBox="0 0 24 24"><path d="M12 21C5 21 3 13 8 8 9 6 12 6 12 6 12 6 15 6 16 8 21 13 19 21 12 21Z" fill="none" stroke="#c9a86a" stroke-width="1.3"/><path d="M12 6 13 3" stroke="#a8c4a2" stroke-width="1.2"/></symbol>
<symbol id="flower" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3" fill="#e8b4b8"/><g fill="none" stroke="#a8c4a2" stroke-width="1.1"><path d="M12 12C12 5 12 5 12 4"/><path d="M12 12C19 12 19 12 20 12"/><path d="M12 12C12 19 12 19 12 20"/><path d="M12 12C5 12 5 12 4 12"/></g></symbol>
<symbol id="envelope" viewBox="0 0 80 60"><rect x="2" y="2" width="76" height="56" rx="4" fill="none" stroke="#c9a86a" stroke-width="1.4"/><path d="M2 2 40 32 78 2" fill="none" stroke="#c9a86a" stroke-width="1.4"/></symbol>
</defs></svg>"""

def sprig_top():
    return '<div class="topdec"><svg class="ic" style="width:1.4em"><use href="#sprig"/></svg></div>'
def leaf_bot():
    return '<div class="botdec"><svg class="ic"><use href="#leaf"/></svg></div>'

def snapshot():
    rows = ""
    for lbl in ("Energy", "Physical", "Mood"):
        rows += ('<div class="snaprow"><span class="lbl">%s</span><span class="dots">'
                 '<span class="dot"></span><span class="dot"></span><span class="dot"></span>'
                 '<span class="dot"></span><span class="dot"></span></span></div>') % lbl
    return ('<div class="snapshot">%s<div class="win">Weekly win: '
            '<span class="winline"></span></div></div>') % rows

def chkgrid(items):
    cells = "".join('<div class="chk"><span class="box"></span>%s</div>' % i for i in items)
    return '<div class="chkgrid">%s</div>' % cells

FRUITS = ["poppy seed","sesame seed","lentil","sweet pea","apple seed","blueberry","raspberry",
    "kidney bean","grape","kumquat","fig","lime","lemon","peach","apple","avocado","onion",
    "bell pepper","tomato","banana","carrot","papaya","mango","ear of corn","cauliflower",
    "scallion","broccoli","eggplant","cabbage","lettuce","coconut","squash","pineapple",
    "cantaloupe","romaine lettuce","butternut squash","honeydew melon","swiss chard",
    "leek","mini watermelon","small pumpkin","winter melon"]

PROMPTS = ["How are you feeling today? Any new symptoms?","What made you smile this week?",
    "A craving or aversion you noticed?","One thing you are grateful for right now?",
    "Write a note to your baby this week.","How did you care for yourself today?",
    "A song, book, or show you loved?","How is sleep treating you?",
    "Something you are looking forward to?","A small win or milestone you celebrated?",
    "What surprised you about pregnancy this week?","A moment you want to remember?"]

QUOTES = ["A baby is a wish your heart makes.","Every kick is a hello.",
    "The smallest feet make the biggest footprints on the heart.","Trust your body. It knows the way.",
    "You are already the mother your baby needs.","You are growing a whole human. Be gentle with yourself.",
    "Soon enough, you will hold them in your arms.","Love grows the moment it begins."]

def trimester_of(week):
    if week <= 13: return "First Trimester"
    if week <= 27: return "Second Trimester"
    return "Third Trimester"

print("assets loaded")


def page(inner, cls=""):
    return '<div class="page between %s"><div class="decoframe"></div>%s</div>' % (cls, inner)

def title_page():
    inner = ('<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">'
        '<svg class="ic bigic"><use href="#flower"/></svg>'
        '<div class="t1">Pregnancy Journal</div>'
        '<div class="t2">for the First-Time Mom</div>'
        '<div class="goldline"></div>'
        '<div class="t3">A guided 9-month keepsake &middot; Foxglen Press</div>'
        '<div style="margin-top:.4in"><svg class="ic" style="width:1.6em"><use href="#foot"/></svg></div>'
        '</div>')
    return '<div class="page center"><div class="decoframe"></div>%s</div>' % inner

def howto_page():
    inner = (sprig_top()
        + '<div style="flex:1;display:flex;flex-direction:column;justify-content:center">'
        + '<div class="wk">How to Use This Journal</div>'
        + '<div class="body">Your quiet space for the next nine months &mdash; and the first year with your baby. '
          'Each week has gentle prompts, a fruit-size fact, a mood snapshot, and room for a photo and an ultrasound. '
          'There is no wrong answer. Keep a pen close, breathe, and let the memory build itself.</div>'
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#heart"/></svg></span>My hope as I begin:</div>'
        + '<div class="write big"></div><div class="write big"></div>'
        + '<div class="quote">A baby is a wish your heart makes.</div></div>'
        + leaf_bot())
    return page(inner)

def ataglance_page():
    rows = ["Due date","Baby's name idea","Clinic / doctor","First appointment",
            "Birth partner","How we found out","Expected size at birth"]
    body = "".join('<tr><td class="lbl">%s</td><td></td></tr>' % r for r in rows)
    inner = (sprig_top()
        + '<div style="flex:1;display:flex;flex-direction:column;justify-content:center">'
        + '<div class="wk">At a Glance</div>'
        + '<table class="info">%s</table></div>' % body
        + leaf_bot())
    return page(inner)

def tab_page(title, sub, desc, inside, cls):
    return ('<div class="tabpage %s"><svg class="ic bigic"><use href="#leaf"/></svg>'
        '<div class="tabt">%s</div><div class="tabsub">%s</div>'
        '<div class="tabdesc">%s</div><div class="tablist">%s</div></div>'
        % (cls, title, sub, desc, inside))

def month_page(n):
    q = QUOTES[(n-1) % len(QUOTES)]
    inner = (sprig_top()
        + '<div class="wk">Month %d</div><div class="wk-sub">Overview &amp; highlights</div>' % n
        + chkgrid(["Doctor visit done","Took prenatal vitamins","Drank enough water","Rest & gentle movement"])
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#heart"/></svg></span>This month in one sentence:</div>'
        + '<div class="write big"></div>'
        + '<div class="twocol" style="flex:1"><div class="usbox fullphoto"><span>ultrasound snapshot</span></div>'
          '<div class="photobox fullphoto"><span>bump photo</span></div></div>'
        + '<div class="quote">%s</div>' % q
        + leaf_bot())
    return page(inner)

def week_page(w):
    fruit = FRUITS[(w-1) % len(FRUITS)]
    p1 = PROMPTS[(w-1) % len(PROMPTS)]
    p2 = PROMPTS[w % len(PROMPTS)]
    inner = (sprig_top()
        + '<div class="wk">Week %d</div><div class="wk-sub">%s</div>' % (w, trimester_of(w))
        + '<div class="fruitwrap"><span class="fruitsize"><svg class="ic"><use href="#fruit"/></svg> Size of a <b>%s</b></span></div>' % fruit
        + snapshot()
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#heart"/></svg></span>%s</div><div class="write"></div>' % p1
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#star"/></svg></span>%s</div><div class="write"></div>' % p2
        + '<div class="twocol" style="flex:1"><div class="usbox fullphoto"><span>ultrasound</span></div>'
          '<div class="photobox fullphoto"><span>photo</span></div></div>'
        + leaf_bot())
    return page(inner)

def doctor_visit_page(idx):
    rows = ["Date","Weeks along","Weight","Blood pressure","Baby's heartbeat",
            "Questions I asked","Doctor's notes","Next appointment"]
    body = "".join('<tr><td class="lbl">%s</td><td></td></tr>' % r for r in rows)
    inner = (sprig_top()
        + '<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-start">'
        + '<div class="wk small">Prenatal Visit #%d</div>' % idx
        + '<table class="info">%s</table>' % body
        + '<div class="colh" style="margin-top:.2in">Ultrasound from this visit</div>'
        + '<div class="usbox" style="height:2.4in"><span>tape photo here</span></div></div>'
        + leaf_bot())
    return page(inner)

def weight_tracker_page():
    rows = ""
    for _ in range(10):
        rows += '<tr><td></td><td></td><td></td><td></td></tr>'
    inner = (sprig_top()
        + '<div class="wk small">Weight &amp; Belly Tracker</div>'
        + '<table class="track"><tr><th>Date</th><th>Weeks</th><th>Weight</th><th>Belly (in)</th></tr>%s</table>' % rows
        + '<div class="colh" style="margin-top:.2in">Notes on how my body is changing</div>'
        + '<div class="write"></div><div class="write"></div><div class="write"></div>'
        + leaf_bot())
    return page(inner)

print("part2 loaded")


def photo_fullpage(label, sub):
    inner = (sprig_top()
        + '<div class="wk small">%s</div><div class="wk-sub">%s</div>' % (label, sub)
        + '<div class="photobox" style="flex:1"><span>photo</span></div>'
        + '<div class="write" style="margin-top:.2in"></div>'
        + leaf_bot())
    return page(inner)

def babyname_page():
    def col(title):
        lines = "".join('<div class="write"></div>' for _ in range(7))
        return '<div><div class="colh">%s</div>%s</div>' % (title, lines)
    inner = (sprig_top()
        + '<div class="wk">Baby Name Ideas</div><div class="wk-sub">Our favourites &amp; why we love them</div>'
        + '<div class="twocol" style="flex:1">%s%s</div>' % (col("For a girl"), col("For a boy"))
        + leaf_bot())
    return page(inner)

def letter_page():
    inner = (sprig_top()
        + '<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-start">'
        + '<div class="wk">A Letter to Our Baby</div>'
        + '<div class="quote">Before we even met you, we loved you.</div>'
        + "".join('<div class="write"></div>' for _ in range(11))
        + '<div style="text-align:right;margin-top:.2in;font-style:italic;color:#8a7a6a">With all our love, ______________</div></div>'
        + leaf_bot())
    return page(inner)

def nursery_board_page():
    inner = (sprig_top()
        + '<div class="wk small">Nursery Vision Board</div><div class="wk-sub">Colours, themes &amp; little dreams</div>'
        + '<div class="twocol" style="flex:1">'
          '<div class="photobox"><span>inspiration</span></div>'
          '<div class="photobox"><span>inspiration</span></div></div>'
        + '<div class="twocol" style="flex:1">'
          '<div class="photobox"><span>colours &amp; fabrics</span></div>'
          '<div class="photobox"><span>furniture ideas</span></div></div>'
        + leaf_bot())
    return page(inner)

def hospital_bag_page():
    left = chkgrid(["Comfy robe","Toiletries","Phone charger","Snacks","Going-home outfit","Nursing bra"])
    inner = (sprig_top()
        + '<div class="wk small">Hospital Bag Checklist</div>'
        + '<div class="colh">For me</div>' + left
        + '<div class="colh" style="margin-top:.1in">For baby</div>'
        + chkgrid(["Coming-home outfit","Swaddle blanket","Newborn hat","Mittens","Car seat","Extra onesies"])
        + '<div class="colh" style="margin-top:.1in">For partner</div>'
        + chkgrid(["Change of clothes","Snacks & water","Camera","Important documents"])
        + leaf_bot())
    return page(inner)

def birth_plan_page():
    rows = ["Where I want to give birth","Who will be with me","Pain relief preferences",
            "Atmosphere (music, lights)","After birth wishes","Feeding plan"]
    body = "".join('<tr><td class="lbl">%s</td><td></td></tr>' % r for r in rows)
    inner = (sprig_top()
        + '<div style="flex:1;display:flex;flex-direction:column;justify-content:center">'
        + '<div class="wk small">My Birth Preferences</div>'
        + '<div class="body" style="margin:.1in 0">A gentle guide, not a set of rules &mdash; stay flexible and kind to yourself.</div>'
        + '<table class="info">%s</table></div>' % body
        + leaf_bot())
    return page(inner)

def birth_details_page():
    rows = ["Date & time of birth","Weight","Length","Hair & eyes","Where born","Who was there","The first thing we said"]
    body = "".join('<tr><td class="lbl">%s</td><td></td></tr>' % r for r in rows)
    inner = (sprig_top()
        + '<div class="wk">Birth Day</div><div class="wk-sub">The day we finally met you</div>'
        + '<table class="info">%s</table>' % body
        + '<div class="photobox" style="flex:1;margin-top:.15in"><span>our first photo together</span></div>'
        + leaf_bot())
    return page(inner)

def footprint_page():
    inner = (sprig_top()
        + '<div class="wk small">Tiny Hands &amp; Feet</div><div class="wk-sub">Press an inked print inside each frame</div>'
        + '<div class="twocol" style="flex:1">'
          '<div class="photobox"><span>left footprint</span></div>'
          '<div class="photobox"><span>right footprint</span></div></div>'
        + '<div class="twocol" style="flex:1">'
          '<div class="photobox"><span>left handprint</span></div>'
          '<div class="photobox"><span>right handprint</span></div></div>'
        + leaf_bot())
    return page(inner)

def firsts_page():
    rows = ["First smile","First laugh","First tooth","First word","First crawl","First steps",
            "First food","First night through","First haircut","First birthday"]
    body = "".join('<tr><td class="lbl">%s</td><td></td></tr>' % r for r in rows)
    inner = (sprig_top()
        + '<div class="wk small">Memorable Firsts</div>'
        + '<table class="info">%s</table>' % body
        + leaf_bot())
    return page(inner)

def firstyear_month_page(m):
    inner = (sprig_top()
        + '<div class="wk">Month %d</div><div class="wk-sub">Baby&rsquo;s first year</div>' % m
        + '<div class="photobox" style="flex:1"><span>this month\'s photo</span></div>'
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#star"/></svg></span>What you love doing now:</div><div class="write"></div>'
        + '<div class="prompt"><span class="qmark"><svg class="ic"><use href="#heart"/></svg></span>A moment we never want to forget:</div><div class="write"></div>'
        + leaf_bot())
    return page(inner)

def pocket_page():
    inner = ('<div class="page center"><div class="decoframe"></div>'
        '<svg class="ic bigic"><use href="#envelope"/></svg>'
        '<div class="wk">My Keepsakes</div>'
        '<div class="body" style="max-width:4.5in">A place for the little things &mdash; the hospital bracelet, '
        'the first scan, a lock of hair, a note from someone you love.</div>'
        '<div class="envwrap"><svg class="env"><use href="#envelope"/></svg>'
        '<div class="envlabel">tuck your treasures here</div></div></div>')
    return inner

def sticker_ideas_page():
    tags = ["First kick","Baby shower","Heard heartbeat","Found out the sex","Nursery done",
            "Due date","Hospital bag ready","Name chosen","Maternity photos","Baby has arrived"]
    chips = "".join('<span class="stk">%s</span>' % t for t in tags)
    inner = (sprig_top()
        + '<div class="wk small">Milestone Markers</div>'
        + '<div class="body" style="margin:.1in 0">Colour or circle each moment as it happens &mdash; your own little milestones.</div>'
        + '<div class="stickers">%s</div>' % chips
        + leaf_bot())
    return page(inner)

def closing_page():
    inner = ('<div class="page center"><div class="decoframe"></div>'
        '<svg class="ic bigic"><use href="#flower"/></svg>'
        '<div class="wk">With Love</div>'
        '<div class="quote" style="max-width:4.5in">However these pages were filled &mdash; in tidy lines or hurried notes '
        '&mdash; they hold a story only you could tell. Thank you for letting us be part of it.</div>'
        '<div class="t3" style="margin-top:.5in">Foxglen Press</div></div>')
    return inner

print("part3 loaded")


def build():
    P = []
    P.append(title_page())
    P.append(howto_page())
    P.append(ataglance_page())

    # ---- First Trimester ----
    P.append(tab_page("First Trimester", "Weeks 1&ndash;13",
        "The early weeks &mdash; big changes happen quietly. Take it slow, rest often, and let the prompts hold your story.",
        "Month 1&ndash;3 overviews &middot; Weekly pages &middot; Ultrasound &amp; fruit-size facts &middot; First prenatal visits", "tg1"))
    P.append(month_page(1)); P.append(month_page(2)); P.append(month_page(3))
    P.append(doctor_visit_page(1))
    for w in range(1, 14):
        P.append(week_page(w))

    # ---- Second Trimester ----
    P.append(tab_page("Second Trimester", "Weeks 14&ndash;27",
        "The golden months &mdash; more energy, first kicks, and the anatomy scan. Capture every new feeling.",
        "Month 4&ndash;6 overviews &middot; Weekly pages &middot; Anatomy scan &middot; Baby names &middot; Nursery board", "tg2"))
    P.append(month_page(4)); P.append(month_page(5)); P.append(month_page(6))
    P.append(doctor_visit_page(2))
    P.append(babyname_page())
    P.append(photo_fullpage("The Big Reveal", "Gender reveal / anatomy scan keepsake"))
    for w in range(14, 28):
        P.append(week_page(w))

    # ---- Third Trimester ----
    P.append(tab_page("Third Trimester", "Weeks 28&ndash;40",
        "The final stretch &mdash; nesting, counting down, and getting ready to meet your little one.",
        "Month 7&ndash;9 overviews &middot; Weekly pages &middot; Nursery board &middot; Hospital bag &middot; Birth plan", "tg3"))
    P.append(month_page(7)); P.append(month_page(8)); P.append(month_page(9))
    P.append(doctor_visit_page(3))
    P.append(nursery_board_page())
    for w in range(28, 41):
        P.append(week_page(w))
    P.append(weight_tracker_page())
    P.append(letter_page())
    P.append(hospital_bag_page())
    P.append(birth_plan_page())

    # ---- Baby's Arrival & First Year ----
    P.append(tab_page("Welcome, Baby", "Your arrival &amp; first year",
        "You are finally here. These pages hold your very first days &mdash; and the year of firsts that follow.",
        "Birth day &middot; Footprints &middot; Memorable firsts &middot; Month-by-month first year &middot; Keepsakes", "tg4"))
    P.append(birth_details_page())
    P.append(footprint_page())
    P.append(firsts_page())
    for m in range(1, 13):
        P.append(firstyear_month_page(m))
    P.append(sticker_ideas_page())
    P.append(pocket_page())
    P.append(closing_page())

    html = HEAD + SVG_DEFS + "".join(P) + "</body></html>"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT)
    print("bytes:", len(html))
    print("page divs (page):", html.count('class="page'))
    print("tab pages:", html.count('class="tabpage'))

if __name__ == "__main__":
    build()
