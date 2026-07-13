import io
f='/home/konerleonard/.openclaw/workspace/kdp-j/docs/index.html'
h=open(f).read()
old=(
'  <div class="side">\n'
'    <div class="stat"><div class="k">Score</div><div class="v" id="score">0</div></div>\n'
'    <div class="stat"><div class="k">Lines</div><div class="v" id="lines">0</div></div>\n'
'    <div class="stat"><div class="k">Level</div><div class="v" id="level">1</div></div>\n'
'    <div class="stat"><div class="k">Next</div><canvas id="next" width="100" height="80"></canvas></div>\n'
'    <div class="btns">\n'
'      <button id="pauseBtn">\u23f8 Pause</button>\n'
'      <button id="restartBtn">\u21bb New</button>\n'
'    </div>\n'
'  </div>\n'
'  </div>\n'
'  <div class="btns" style="width:100%;max-width:280px">\n'
'    <button id="pauseBtn2">\u23f8 Pause</button>\n'
'    <button id="restartBtn2">\u21bb New</button>\n'
'  </div>\n'
'  <div class="pad">'
)
new=(
'  <div class="side">\n'
'    <div class="stat"><div class="k">Score</div><div class="v" id="score">0</div></div>\n'
'    <div class="stat"><div class="k">Lines</div><div class="v" id="lines">0</div></div>\n'
'    <div class="stat"><div class="k">Level</div><div class="v" id="level">1</div></div>\n'
'    <div class="stat"><div class="k">Next</div><canvas id="next" width="100" height="80"></canvas></div>\n'
'  </div>\n'
'  <div class="btns">\n'
'    <button id="pauseBtn">\u23f8 Pause</button>\n'
'    <button id="restartBtn">\u21bb New</button>\n'
'  </div>\n'
'  <div class="pad">'
)
if old in h:\n    h=h.replace(old,new)\n    open(f,'w').write(h)\n    print("replaced OK")
else:
    print("OLD NOT FOUND")
    i=h.find('<div class="side">')
    print(repr(h[i:i+650]))
