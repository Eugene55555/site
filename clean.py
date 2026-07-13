import re
f='/home/konerleonard/.openclaw/workspace/kdp-j/docs/index.html'
h=open(f).read()
pattern = r'@media\(min-width:561px\)\{[^}]*\}\s*</style>'
h2 = re.sub(pattern, '</style>', h, flags=re.S)
changed = h2 != h
if changed:
    h = h2
    open(f, 'w').write(h)
    print("media query removed")
else:
    print("not found / no change")
print('style close:', h.count('</style>'), 'head close:', h.count('</head>'))
print('side refs left:', h.count('class="side"'))
print('hud refs:', h.count('class="hud"'))
